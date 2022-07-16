import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import re

# library for the E-test (doesn't work on Windows)
# pip install poisson-etest
from poisson_etest import poisson_etest

# library for forest plot
# pip install zepid
from zepid.graphics import EffectMeasurePlot

# for making tables pretty
# pip install sigfig
from sigfig import round

# turns off warnings that arise with the sigfig formatting routine
import warnings
warnings.filterwarnings("ignore")

# US counts from VARES
# (ae label, ae abbreviation, COVID count, flu count)
us_data = [
    ('Abnormal uterine bleeding (menstrual irregularity)', 'AUB', 6352, 54),
    ('Miscarriage', 'M', 1232, 259),
    ('Fetal chromosomal abnormalities', 'FCM', 7, 0),
    ('Fetal malformation', 'FM', 2, 1),
    ('Fetal cystic hygroma', 'FCM', 5, 0),
    ('Fetal cardiac disorders', 'FCD', 10, 2),
    ('Fetal arrhythmia', 'FA', 3, 0),
    ('Fetal cardiac arrest', 'FCA', 3, 0),
    ('Fetal vascular mal-perfusion', 'FVMP', 5, 0),
    ('Fetal growth abnormalities', 'FGA', 59, 20),
    ('Fetal abnormal surveillance', 'FAS', 125, 36),
    ('Fetal placental thrombosis', 'FPT', 5, 0),
    ('Fetal death (stillbirth)', 'FD', 168, 42)
]

# global counts from VARES
# (ae label, ae abbreviation, COVID count, flu count)
global_data = [
    ('Abnormal uterine bleeding (menstrual irregularity)', 'AUB', 12843, 65),
    ('Miscarriage', 'M', 3338, 325),
    ('Fetal chromosomal abnormalities', 'FCM', 10, 0),
    ('Fetal malformation', 'FM', 22, 2),
    ('Fetal cystic hygroma', 'FCM', 8, 0),
    ('Fetal cardiac disorders', 'FCD', 18, 2),
    ('Fetal arrhythmia', 'FA', 5, 0),
    ('Fetal cardiac arrest', 'FCA', 20, 0),
    ('Fetal vascular mal-perfusion', 'FVMP', 12, 0),
    ('Fetal growth abnormalities', 'FGA', 188, 24),
    ('Fetal abnormal surveillance', 'FAS', 178, 45),
    ('Fetal placental thrombosis', 'FPT', 6, 0),
    ('Fetal death (stillbirth)', 'FD', 402, 64)
]


def compare_rates(ae_data, cperiod, fperiod, period_label):
    table_data = {}

    print('******************************')
    print('***** '+period_label+" *****")
    print(ae_data)
    print('cperiod=', cperiod)
    print('cperiod=', fperiod)
    print('******************************\n')

    print('*** RATES ***')
    for (ae, abb, c, f) in ae_data:
        # for each ae, just print the rates for this period post COVID and post flu
        print('{:55s} {:6d} {:10.4f} {:6d} {:10.4f}'.format(ae, c, c/cperiod, f, f/fperiod))
    print('******************************\n')

    print('*** P VALUES ***')
    sig = set()
    for (ae, abb, c, f) in ae_data:
        # for each ae, do the E-test, get the p-Value
        p = poisson_etest(c, f*cperiod/fperiod, 1, 1)
        table_data[ae] = {'p': re.sub('e(.+)', r'x10^\1^', '{:#.2}'.format(p))}

        # if it's significant, add it to our set of significant AE for plotting later
        # the "or True" is there because later we decided to report everything
        if p < 0.05 or True:
            sig.add(ae)

        print('{:55s} {:.3e}'.format(ae, p))
    print('******************************\n')

    print('*** RELATIVE RATES ***')
    # data for the forest plot later
    labs = []
    measure = []
    lower = []
    upper = []

    # reset the seed here so we're repeatable
    np.random.seed(1)

    for (ae, abb, c, f) in ae_data:
        # pull a bunch of samples of post COVID events from the Poisson distribution
        crate = c/cperiod
        nc = np.random.poisson(crate*cperiod, 1000000)

        # pull a bunch of samples of post flu events from the Poisson distribution
        frate = f/fperiod
        nf = np.random.poisson(frate*cperiod, 1000000)

        # filter out zero-count flu events (zero-truncated Poisson) and compute rate
        w = np.where(nf > 0)
        r = nc[w]/nf[w]

        # get stats from r
        mean = 0
        low = 0
        hi = 0
        if len(r) > 0:
            mean = np.mean(r)
            low = np.percentile(r, 2.5)
            hi = np.percentile(r, 97.5)

        print('{:55s} {:10.4f} {:10.4f} {:10.4f}'.format(ae, mean, low, hi))

        # if we we're signifiant and we have counts (mean >0) save off data for forest plot
        table_data[ae]['rr'] = ''
        if (ae in sig and mean > 0):
            smean = '{:.0f}'.format(mean)
            slow = round(low, sigfigs=len(smean)+1, output_type=str)
            shi = round(hi, sigfigs=len(smean)+1, output_type=str)
            table_data[ae]['rr'] = '{:s} [{:s}-{:s}]'.format(smean, slow, shi)
            labs.append(abb)
            measure.append(smean)
            lower.append(slow)
            upper.append(shi)

        # draw the distribution (for debugging)
        xc = np.arange(stats.poisson.ppf(0.001, crate), stats.poisson.ppf(0.999, crate))
        xf = np.arange(stats.poisson.ppf(0.00001, frate), stats.poisson.ppf(0.99999, frate))
        plt.clf()
        plt.cla()
        plt.figure(figsize=(8, 5))
        plt.title(ae)
        plt.xlabel('Events/'+period_label)
        plt.ylabel('Probability')
        plt.plot(xc, stats.poisson.pmf(xc, crate))
        plt.plot(xf, stats.poisson.pmf(xf, frate))
        plt.legend(['COVID', 'Flu'])
        plt.savefig(ae+'-'+period_label+'.png')
        # plt.show()
        plt.close()
    print('******************************\n')

    # draw the forest plot
    plt.clf()
    plt.cla()
    p = EffectMeasurePlot(label=labs, effect_measure=measure, lcl=lower, ucl=upper)
    p.labels(effectmeasure='RR', scale='log')
    p.colors(pointshape="D")
    ax = p.plot(figsize=(8, 4), t_adjuster=0.06, max_value=15000, min_value=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(False)
    plt.title('Relative Rate By '+period_label, loc='center', y=1.045)
    plt.savefig('forest-'+period_label+'.png')
    # plt.show()
    plt.close()
    return table_data

###################
# MAIN STARTS HERE
###################


###################
# US ONLY DATA
###################

# run the stats by dose
# number of doses of COVID and flu vaccine
cdose = .59623
fdose = 3.3
us_dose = compare_rates(us_data, cdose, fdose, 'Dose (US)')

# run the stats by month
# amount of time COVID and flu have been tracked in VAERS
ctime = 18
ftime = 294
us_time = compare_rates(us_data, ctime, ftime, 'Month (US)')

# run the stats by people
# number of vaccinated people
cpeople = .25996
fpeople = .38861  # estimated
us_people = compare_rates(us_data, cpeople, fpeople, 'People (US)')

with open('table1.md', 'w') as md:
    print('| Adverse Event | US Count of AE reports post Vaccine | US Rate of reported AE<br/>(count/Month) | US Rate of reported AE<br/>(count/billion doses) | US Rate of reported AE<br/>(count/billion people vaccinated) |', file=md)
    print('| --- | --: | --: | --: | --: |', file=md)
    for (ae, abb, c, f) in us_data:
        print('| {:s} | {:d}<br/>{:d} | {:s}<br/>{:s} | {:s}<br/>{:s} | {:s}<br/>{:s} |'.format(
            ae,
            c, f,
            round(c/ctime, sigfigs=3, output_type=str), round(f/ftime, sigfigs=3, output_type=str),
            round(c/cdose, sigfigs=3, output_type=str), round(f/fdose, sigfigs=3, output_type=str),
            round(c/cpeople, sigfigs=3, output_type=str), round(f/fpeople, sigfigs=3, output_type=str)
        ), file=md)

###################
# GLOBAL DATA
###################

# run the stats by dose
# number of doses of COVID and flu vaccine
cdose = 12.07
fdose = 66  # estimated
global_dose = compare_rates(global_data, cdose, fdose, 'Dose (Global)')

# run the stats by month
# amount of time COVID and flu have been tracked in VAERS
ctime = 18
ftime = 294
global_time = compare_rates(global_data, ctime, ftime, 'Month (Global)')

# run the stats by people
# number of vaccinated people
cpeople = 5.23
fpeople = 9.23  # estimated
global_people = compare_rates(global_data, cpeople, fpeople, 'People (Global)')

with open('table2.md', 'w') as md:
    print('| Adverse Event | Global Count of AE reports post Vaccine | Global Rate of reported AE<br/>(count/Month) | Global Rate of reported AE<br/>(count/billion doses) | Global Rate of reported AE<br/>(count/billion people vaccinated) |', file=md)
    print('| --- | --: | --: | --: | --: |', file=md)
    for (ae, abb, c, f) in global_data:
        print('| {:s} | {:d}<br/>{:d} | {:s}<br/>{:s} | {:s}<br/>{:s} | {:s}<br/>{:s} |'.format(
            ae,
            c, f,
            round(c/ctime, sigfigs=3, output_type=str), round(f/ftime, sigfigs=3, output_type=str),
            round(c/cdose, sigfigs=3, output_type=str), round(f/fdose, sigfigs=3, output_type=str),
            round(c/cpeople, sigfigs=3, output_type=str), round(f/fpeople, sigfigs=3, output_type=str)
        ), file=md)

with open('table3.md', 'w') as md:
    print('| Adverse Event | Relative Rate<br/>(by time) | Relative Rate<br/>(by dose) | Relative Rate<br/>(by person vaccinated) |', file=md)
    print('| --- | --: | --: | --: |', file=md)
    for (ae, abb, c, f) in global_data:
        print('| {:s} | {:s} p={:s} <br/>{:s} p={:s}| {:s} p={:s}<br/>{:s} p={:s}| {:s} p={:s}<br/>{:s} p={:s}|'.format(
            ae,
            global_time[ae]['rr'], global_time[ae]['p'], us_time[ae]['rr'], us_time[ae]['p'],
            global_dose[ae]['rr'], global_dose[ae]['p'], us_dose[ae]['rr'], us_dose[ae]['p'],
            global_people[ae]['rr'], global_people[ae]['p'], us_people[ae]['rr'], us_people[ae]['p']
        ), file=md)

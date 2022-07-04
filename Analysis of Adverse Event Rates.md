# Analysis of Adverse Event Rates

In this section we compare the rate of Global and US reports of post-vaccination adverse events (AE), for the COVID-19 vaccine and the Flu vaccine. For each of the AE, we compare three relevant rates of reporting: i) the rate of reported AE per unit time, ii) the rate of reported AE per dose given, and iii) the rate of reported AE per person vaccinated. 

In Table 0 below, we report the period used for normalizing the data, Global values are reported on the top line, US value on the second line.

| Vaccine  | Time Tracked | Billion Doses Given     | Billion People Vaccinated               |
| -------- | ------------ | ----------------------- | --------------------------------------- |
| COVID-19 | 18 Months    | 12.07<br />0.596        | 5.23<br />0.260                         |
| Flu      | 281 Months   | 66 (estimated)<br />3.3 | 9.23 (simulated)<br />0.388 (simulated) |

*Table 0*

Counting the number of people vaccinated with the COVID-19 vaccine is straightforward because there has only been one worldwide attempt at vaccination and the data has been tracked from day one.  The Flu vaccine is harder because individuals are not tracked and there are yearly seasons where an individual may receive a subsequent vaccination each season. We run a Monte Carlo simulation to estimate the number of people since 1998 that have received at least one Flu vaccine in the US.  

To allow simulation “burn in” for the stochastic nature of this experiment, we start in 1980 with a US population of 229,486,000 (reference: https://population.un.org/), each year a fraction of the total population is vaccinated ($f_{v}$), a fraction of the total population dies ($f_d)$, and a new fraction of the population is born ($f_b$). By simulating the demographics change yearly, we can estimate the total number of people who have received at least one flu vaccine by 2022.  We use the UN population data to estimate $f_b$ and $f_d$ each year (reference: https://population.un.org/) and the conditional probability of Flu vaccination from Kwong, et al. (reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6961264/). Kwong reports that roughly 57% of the population in their study who receives a flu shot in one year repeats it a subsequet (33,234 out of 58,021) year. The CDC reports that approximately 50% of the population is vaccinated in any given year. We estimate $f_v=0.57$ for previously vaccinated individuals and $f_v=0.43$ for previously unvaccinated individuals, which will return the rough CDC approximation of 50% of the population being vaccinated any given year. 

After running the simulation, the final tally for 2022 is a total US population of 289,107,000, with a total of 335,572,000 (116% of the current population) receiving at least one dose of the Flu vaccine since 1998. Our model does not account for migration into the US, and in 2022 the total population is 334,805,000, if we estimate the same fraction of 116% vaccinated since 1998, that results in roughly 388 million people in the US that have received at least one dose of flu vaccine.  Using the same scaling factor for a world population of 7.95 billion, we get an estimate of 9.23 billion people worldwide who have received at least one dose of the flu vaccine since 1998.  These are all rough estimates given the limited data available; however, even if these estimates are high by a factor of 2 (unlikely), the signals reported below are still significant. 

Table 1 below shows the count of AE reported post vaccine in VAERS along with the mean rate of report over the time tracked, the mean rate of report per billion doses given, and the mean rate of report per billion people vaccinated. Report count and rates for the COVID-19 Vaccine are on the top line with the counts and rates for the Flu vaccine below them for each AE.  The same data for global counts and rates is shown in Table 2.

| Adverse Event | US Count of AE reports post Vaccine | US Rate of reported AE<br/>(count/Month) | US Rate of reported AE<br/>(count/billion doses) | US Rate of reported AE<br/>(count/billion people vaccinated) |
| --- | --: | --: | --: | --: |
| Abnormal uterine bleeding (menstrual irregularity) | 6352<br/>54 | 353<br/>0.192 | 10700<br/>16.4 | 24400<br/>139 |
| Miscarriage | 1232<br/>259 | 68.4<br/>0.922 | 2070<br/>78.5 | 4740<br/>668 |
| Fetal chromosomal abnormalities | 7<br/>0 | 0.389<br/>0.00 | 11.7<br/>0.00 | 26.9<br/>0.00 |
| Fetal malformation | 2<br/>1 | 0.111<br/>0.00356 | 3.35<br/>0.303 | 7.69<br/>2.58 |
| Fetal cystic hygroma | 5<br/>0 | 0.278<br/>0.00 | 8.39<br/>0.00 | 19.2<br/>0.00 |
| Fetal cardiac disorders | 10<br/>2 | 0.556<br/>0.00712 | 16.8<br/>0.606 | 38.5<br/>5.15 |
| Fetal arrhythmia | 3<br/>0 | 0.167<br/>0.00 | 5.03<br/>0.00 | 11.5<br/>0.00 |
| Fetal cardiac arrest | 3<br/>0 | 0.167<br/>0.00 | 5.03<br/>0.00 | 11.5<br/>0.00 |
| Fetal vascular mal-perfusion | 5<br/>0 | 0.278<br/>0.00 | 8.39<br/>0.00 | 19.2<br/>0.00 |
| Fetal growth abnormalities | 59<br/>20 | 3.28<br/>0.0712 | 99.0<br/>6.06 | 227<br/>51.5 |
| Fetal abnormal surveillance | 125<br/>36 | 6.94<br/>0.128 | 210<br/>10.9 | 481<br/>92.8 |
| Fetal placental thrombosis | 5<br/>0 | 0.278<br/>0.00 | 8.39<br/>0.00 | 19.2<br/>0.00 |
| Fetal death (stillbirth) | 168<br/>42 | 9.33<br/>0.149 | 282<br/>12.7 | 646<br/>108 |

*Table 1*

| Adverse Event | Global Count of AE reports post Vaccine | Global Rate of reported AE<br/>(count/Month) | Global Rate of reported AE<br/>(count/billion doses) | Global Rate of reported AE<br/>(count/billion people vaccinated) |
| --- | --: | --: | --: | --: |
| Abnormal uterine bleeding (menstrual irregularity) | 12843<br/>65 | 714<br/>0.231 | 1060<br/>0.985 | 2460<br/>7.04 |
| Miscarriage | 3338<br/>325 | 185<br/>1.16 | 277<br/>4.92 | 638<br/>35.2 |
| Fetal chromosomal abnormalities | 10<br/>0 | 0.556<br/>0.00 | 0.829<br/>0.00 | 1.91<br/>0.00 |
| Fetal malformation | 22<br/>2 | 1.22<br/>0.00712 | 1.82<br/>0.0303 | 4.21<br/>0.217 |
| Fetal cystic hygroma | 8<br/>0 | 0.444<br/>0.00 | 0.663<br/>0.00 | 1.53<br/>0.00 |
| Fetal cardiac disorders | 18<br/>2 | 1.00<br/>0.00712 | 1.49<br/>0.0303 | 3.44<br/>0.217 |
| Fetal arrhythmia | 5<br/>0 | 0.278<br/>0.00 | 0.414<br/>0.00 | 0.956<br/>0.00 |
| Fetal cardiac arrest | 20<br/>0 | 1.11<br/>0.00 | 1.66<br/>0.00 | 3.82<br/>0.00 |
| Fetal vascular mal-perfusion | 12<br/>0 | 0.667<br/>0.00 | 0.994<br/>0.00 | 2.29<br/>0.00 |
| Fetal growth abnormalities | 188<br/>24 | 10.4<br/>0.0854 | 15.6<br/>0.364 | 35.9<br/>2.60 |
| Fetal abnormal surveillance | 178<br/>45 | 9.89<br/>0.160 | 14.7<br/>0.682 | 34.0<br/>4.88 |
| Fetal placental thrombosis | 6<br/>0 | 0.333<br/>0.00 | 0.497<br/>0.00 | 1.15<br/>0.00 |
| Fetal death (stillbirth) | 402<br/>64 | 22.3<br/>0.228 | 33.3<br/>0.970 | 76.9<br/>6.93 |

*Table 2*

For all AE, the rates of reports post COVID-19 vaccine are higher than the Flu vaccine across all three normalization methods: by unit time, by dose given, and by person vaccinated. We proceed with two analyses below: 1) compute the p-value to determine if the AE report rates are statistically different between the two vaccines, and 2) compute the relative rate and 95% CI of AE reports after the COVID-19 vaccine versus the Flu vaccine. That is, we answer the questions: 1) “Are the rate of AE reports post COVID-19 vaccine (statistically) different than the rates of report post Flu vaccine?” and 2) “How much more frequently is an AE reported after the COVID-19 vaccine than after the Flu vaccine?”

*Statistical Significance*

We treat each AE report as discrete independent events occurring at the mean rate specified in the tables 1 and 2 which we model as a Poisson distribution. Given two rates $r_1$ and $r_2$ over a period, $P$, we perform a Poisson E-test [reference: https://userweb.ucs.louisiana.edu/~kxk4695/JSPI-04.pdf] to compute the p-value. The E-test is used for Poisson statistics analogous to the traditional t-test used for Gaussian statistics. The p-value is interpreted in the same way: the probability that the observed events came from the same probability distribution. Or stated another way: the probability that the means (in this case rates) are same by random chance.

We use the rates in table 1 and 2 above and normalize the event counts over each period, $P$: the 18-month-, 12 billion-dose-, or XX billion-people-vaccinated-window and report the p-values below in Table 3. Where there is sufficient data, the p-values are small, and where 0.0 is reported, it was too small to represent as a double precision floating point number in our E-test function [reference: https://github.com/nolanbconaway/poisson-etest]. 

*Estimating Relative Reporting Rates* 

For the rates that are statically different ($p<0.05$) and have non-zero counts in the reporting period, we compute ratio of rates of AE reports for each vaccine. That is, we compute how much more often a post COVID-19 vaccination AE is reported compared to post Flu vaccination. Consider a case were Event A is reported at a rate of 100 per month and Event B is reported at a rate of 10 per month. The naïve approach is to simply state that Event A is reported $\frac{100/month}{10/month}=10$ times as often as Event B. However, events do not occur at uniform frequency, they occur at frequencies described by the Poisson distribution. We proceed by computing the ratio distribution, $R$, which is the distribution of the ratio of two different Poisson distributions. That is, given two Poisson distributions, $Poisson(r_1)$ and $Poisson(r_2)$, we aim to compute the ratio distribution, $R$, which represents the probability distribution of the ratio of the distribution of events.
$$
R(r_1,r_2)=\frac{Poisson(r_1)}{Poisson(r_2)}
$$
We estimate the shape of $R$ for each AE and period, $P$, by performing Monte Carlo simulations. We draw 1,000,000 random samples from Poisson distributions with rates $r_1$ and $r_2$ resulting in a sample of paired event counts $n_1$ and $n_2$ , respectively, over the observation window $P$ .

$$
n_i \leftarrow Poisson(r_i)
$$

That is, we create a set of 1,000,000 tuples of event counts $\left\{(n_1,n_2)_1,(n_1,n_2)_2,\dots,(n_1,n_2)_{1000000}\right\}$ drawn from the two Poisson distributions. The ratio distribution, $R$, is built up from the ratio of the draws of each pair of $n_1$ and $n_2$ 
$$
R(r_1,r_2)=\left\{\left(\frac{n_1}{n_2}\right)_1,\left(\frac{n_1}{n_2}\right)_2,\dots,\left(\frac{n_1}{n_2}\right)_{1000000}\right\}
$$

The mean of $R$ is is the expectation value for the ratio of the two Poisson distributions and the empirically-derived quantile function of $R$ is used to estimate the 95% CI of the mean. All computed values have converged to a precision of 1% or better. For AE that are reported infrequently post Flu vaccine there is finite probability that $n_2$ is zero resulting in $R$ being undefined. To mitigate this problem, we use the zero-truncated Poisson distribution [reference: https://www.jstor.org/stable/2527552] and only count instances of non-zero $n_2$ draws. This approach skews the $R$ distribution to the left [reference: https://epubs.siam.org/doi/10.1137/0134043] and makes the AE rates for the COVID-19 vaccine actually look better. That is, in these cases, the AE rate is actually a lower bound.

We did these analyses using a custom-written Python script, and will make it available upon request.

We report in Table 3 below the relative rate of post COVID-19 vaccine AE reports to post Flu vaccine AE report.  Global values are the top line and US values are in the bottom line for each AE.  A relative rate greater than 1 implies that there are more post COVID-19 vaccine AE reports than post Flu vaccine AE report. According to CDC’s Standard Operating Procedures for COVID-19 [reference: https://www.cdc.gov/vaccinesafety/pdf/VAERS-v2-SOP.pdf] when doing a Proportional Reporting Ratio (PRR) analysis (which is analogous to the analysis presented here in this paper), a 2x increase in reporting is a sufficient signal to be concerned.

| Adverse Event | Relative Rate<br/>(by time) | Relative Rate<br/>(by dose) | Relative Rate<br/>(by person vaccinated) |
| --- | --: | --: | --: |
| Abnormal uterine bleeding (menstrual irregularity) | 4059 [1440.6-12878] p=0.0 <br/>2420 [809.38-6413.0] p=0.0| 1192 [673.95-2162.8] p=0.0<br/>738 [391.6-1584] p=0.0| 359 [261.1-506.8] p=0.0<br/>181 [131.1-255.1] p=0.0|
| Miscarriage | 169 [110.3-272.7] p=0.0 <br/>79 [49.0-136] p=0.0| 57 [44.3-74.7] p=0.0<br/>27 [20.2-36.5] p=0.0| 18 [15.7-21.2] p=0.0<br/>7 [6.1-8.4] p=0.0|
| Fetal chromosomal abnormalities |  p=0.00058 <br/> p=0.0048|  p=0.00058<br/> p=0.0048|  p=0.00058<br/> p=0.0048|
| Fetal malformation | 21 [10.0-31.0] p=1.9x10^-07^ <br/> p=0.20| 20 [7.67-31.0] p=1.9x10^-07^<br/> p=0.20| 16 [5.00-30.0] p=2.1x10^-06^<br/> p=0.20|
| Fetal cystic hygroma |  p=0.0024 <br/> p=0.020|  p=0.0024<br/> p=0.020|  p=0.0024<br/> p=0.020|
| Fetal cardiac disorders | 17 [8.00-27.0] p=2.6x10^-06^ <br/>10 [4.00-17.0] p=0.00058| 16 [6.00-26.0] p=2.6x10^-06^<br/>9 [3.0-16] p=0.00058| 13 [4.00-25.0] p=2.7x10^-05^<br/>7 [1.7-15] p=0.0047|
| Fetal arrhythmia |  p=0.020 <br/> p=0.088|  p=0.020<br/> p=0.088|  p=0.020<br/> p=0.088|
| Fetal cardiac arrest |  p=6.9x10^-07^ <br/> p=0.088|  p=6.9x10^-07^<br/> p=0.088|  p=6.9x10^-07^<br/> p=0.088|
| Fetal vascular mal-perfusion |  p=0.00015 <br/> p=0.020|  p=0.00015<br/> p=0.020|  p=0.00015<br/> p=0.020|
| Fetal growth abnormalities | 124 [40.75-210.0] p=0.0 <br/>42 [13.5-72.0] p=0.0| 56 [20.7-189] p=0.0<br/>22 [7.14-64.0] p=0.0| 15 [8.60-27.6] p=0.0<br/>5 [2.6-9.1] p=1.7x10^-08^|
| Fetal abnormal surveillance | 80 [26.1-192] p=0.0 <br/>66 [21.0-140] p=0.0| 25 [12.2-58.7] p=0.0<br/>24 [10.1-63.0] p=0.0| 7 [4.8-11] p=0.0<br/>5 [3.5-8.6] p=0.0|
| Fetal placental thrombosis |  p=0.0096 <br/> p=0.020|  p=0.0096<br/> p=0.020|  p=0.0096<br/> p=0.020|
| Fetal death (stillbirth) | 129 [46.75-409.0] p=0.0 <br/>79 [25.7-183] p=0.0| 38 [21.1-73.0] p=0.0<br/>26 [12.2-60.0] p=0.0| 11 [8.14-16.3] p=0.0<br/>6 [4.1-9.4] p=0.0|

*Table 3*


In the Figures below we show the US and Global relative rates of the reports of AE after the COVID-19 vaccine versus the Flu vaccine for the rates of AE by unit time, by dose given, and by person vaccinated. A value greater than 1 implies that the AE is reported more frequently after the COVID-19 vaccine than after the Flu vaccine. Note the log scale spanning multiple orders of magnitude indicating a large effect across many different AE - all (much) greater than 1. 

![forest-Dose (Global)](forest-Dose%20(Global).png)

![forest-Dose (US)](forest-Dose%20(US).png)

![forest-Month (Global)](forest-Month%20(Global).png)

![forest-Month (US)](forest-Month%20(US).png)

![forest-People (Global)](forest-People%20(Global).png)

![forest-People (US)](forest-People%20(US).png)

## Log

Output log from analysis code

```
******************************
***** Dose (US) *****
[('Abnormal uterine bleeding (menstrual irregularity)', 'AUB', 6352, 54), ('Miscarriage', 'M', 1232, 259), ('Fetal chromosomal abnormalities', 'FCM', 7, 0), ('Fetal malformation', 'FM', 2, 1), ('Fetal cystic hygroma', 'FCM', 5, 0), ('Fetal cardiac disorders', 'FCD', 10, 2), ('Fetal arrhythmia', 'FA', 3, 0), ('Fetal cardiac arrest', 'FCA', 3, 0), ('Fetal vascular mal-perfusion', 'FVMP', 5, 0), ('Fetal growth abnormalities', 'FGA', 59, 20), ('Fetal abnormal surveillance', 'FAS', 125, 36), ('Fetal placental thrombosis', 'FPT', 5, 0), ('Fetal death (stillbirth)', 'FD', 168, 42)]
cperiod= 0.59623
cperiod= 3.3
******************************

*** RATES ***
Abnormal uterine bleeding (menstrual irregularity)        6352 10653.6068     54    16.3636
Miscarriage                                               1232  2066.3167    259    78.4848
Fetal chromosomal abnormalities                              7    11.7404      0     0.0000
Fetal malformation                                           2     3.3544      1     0.3030
Fetal cystic hygroma                                         5     8.3860      0     0.0000
Fetal cardiac disorders                                     10    16.7721      2     0.6061
Fetal arrhythmia                                             3     5.0316      0     0.0000
Fetal cardiac arrest                                         3     5.0316      0     0.0000
Fetal vascular mal-perfusion                                 5     8.3860      0     0.0000
Fetal growth abnormalities                                  59    98.9551     20     6.0606
Fetal abnormal surveillance                                125   209.6506     36    10.9091
Fetal placental thrombosis                                   5     8.3860      0     0.0000
Fetal death (stillbirth)                                   168   281.7705     42    12.7273
******************************

*** P VALUES ***
Abnormal uterine bleeding (menstrual irregularity)      0.000e+00
Miscarriage                                             0.000e+00
Fetal chromosomal abnormalities                         4.759e-03
Fetal malformation                                      1.973e-01
Fetal cystic hygroma                                    1.976e-02
Fetal cardiac disorders                                 5.781e-04
Fetal arrhythmia                                        8.838e-02
Fetal cardiac arrest                                    8.838e-02
Fetal vascular mal-perfusion                            1.976e-02
Fetal growth abnormalities                              0.000e+00
Fetal abnormal surveillance                             0.000e+00
Fetal placental thrombosis                              1.976e-02
Fetal death (stillbirth)                                0.000e+00
******************************

*** RELATIVE RATES ***
Abnormal uterine bleeding (menstrual irregularity)        738.1339   391.6250  1583.5000
Miscarriage                                                26.9146    20.1833    36.5294
Fetal chromosomal abnormalities                             0.0000     0.0000     0.0000
Fetal malformation                                          1.9072     0.0000     5.0000
Fetal cystic hygroma                                        0.0000     0.0000     0.0000
Fetal cardiac disorders                                     9.1187     3.0000    16.0000
Fetal arrhythmia                                            0.0000     0.0000     0.0000
Fetal cardiac arrest                                        0.0000     0.0000     0.0000
Fetal vascular mal-perfusion                                0.0000     0.0000     0.0000
Fetal growth abnormalities                                 21.5757     7.1429    64.0000
Fetal abnormal surveillance                                23.5755    10.1111    63.0000
Fetal placental thrombosis                                  0.0000     0.0000     0.0000
Fetal death (stillbirth)                                   26.2801    12.2000    60.0000
******************************

******************************
***** Month (US) *****
[('Abnormal uterine bleeding (menstrual irregularity)', 'AUB', 6352, 54), ('Miscarriage', 'M', 1232, 259), ('Fetal chromosomal abnormalities', 'FCM', 7, 0), ('Fetal malformation', 'FM', 2, 1), ('Fetal cystic hygroma', 'FCM', 5, 0), ('Fetal cardiac disorders', 'FCD', 10, 2), ('Fetal arrhythmia', 'FA', 3, 0), ('Fetal cardiac arrest', 'FCA', 3, 0), ('Fetal vascular mal-perfusion', 'FVMP', 5, 0), ('Fetal growth abnormalities', 'FGA', 59, 20), ('Fetal abnormal surveillance', 'FAS', 125, 36), ('Fetal placental thrombosis', 'FPT', 5, 0), ('Fetal death (stillbirth)', 'FD', 168, 42)]
cperiod= 18
cperiod= 281
******************************

*** RATES ***
Abnormal uterine bleeding (menstrual irregularity)        6352   352.8889     54     0.1922
Miscarriage                                               1232    68.4444    259     0.9217
Fetal chromosomal abnormalities                              7     0.3889      0     0.0000
Fetal malformation                                           2     0.1111      1     0.0036
Fetal cystic hygroma                                         5     0.2778      0     0.0000
Fetal cardiac disorders                                     10     0.5556      2     0.0071
Fetal arrhythmia                                             3     0.1667      0     0.0000
Fetal cardiac arrest                                         3     0.1667      0     0.0000
Fetal vascular mal-perfusion                                 5     0.2778      0     0.0000
Fetal growth abnormalities                                  59     3.2778     20     0.0712
Fetal abnormal surveillance                                125     6.9444     36     0.1281
Fetal placental thrombosis                                   5     0.2778      0     0.0000
Fetal death (stillbirth)                                   168     9.3333     42     0.1495
******************************

*** P VALUES ***
Abnormal uterine bleeding (menstrual irregularity)      0.000e+00
Miscarriage                                             0.000e+00
Fetal chromosomal abnormalities                         4.759e-03
Fetal malformation                                      1.973e-01
Fetal cystic hygroma                                    1.976e-02
Fetal cardiac disorders                                 5.781e-04
Fetal arrhythmia                                        8.838e-02
Fetal cardiac arrest                                    8.838e-02
Fetal vascular mal-perfusion                            1.976e-02
Fetal growth abnormalities                              0.000e+00
Fetal abnormal surveillance                             0.000e+00
Fetal placental thrombosis                              1.976e-02
Fetal death (stillbirth)                                0.000e+00
******************************

*** RELATIVE RATES ***
Abnormal uterine bleeding (menstrual irregularity)       2419.6343   809.3750  6413.0000
Miscarriage                                                79.4507    49.0000   136.3333
Fetal chromosomal abnormalities                             0.0000     0.0000     0.0000
Fetal malformation                                          1.9666     0.0000     5.0000
Fetal cystic hygroma                                        0.0000     0.0000     0.0000
Fetal cardiac disorders                                     9.6739     4.0000    17.0000
Fetal arrhythmia                                            0.0000     0.0000     0.0000
Fetal cardiac arrest                                        0.0000     0.0000     0.0000
Fetal vascular mal-perfusion                                0.0000     0.0000     0.0000
Fetal growth abnormalities                                 41.8154    13.5000    72.0000
Fetal abnormal surveillance                                66.0033    21.0000   140.0000
Fetal placental thrombosis                                  0.0000     0.0000     0.0000
Fetal death (stillbirth)                                   79.3628    25.7143   183.0000
******************************

******************************
***** People (US) *****
[('Abnormal uterine bleeding (menstrual irregularity)', 'AUB', 6352, 54), ('Miscarriage', 'M', 1232, 259), ('Fetal chromosomal abnormalities', 'FCM', 7, 0), ('Fetal malformation', 'FM', 2, 1), ('Fetal cystic hygroma', 'FCM', 5, 0), ('Fetal cardiac disorders', 'FCD', 10, 2), ('Fetal arrhythmia', 'FA', 3, 0), ('Fetal cardiac arrest', 'FCA', 3, 0), ('Fetal vascular mal-perfusion', 'FVMP', 5, 0), ('Fetal growth abnormalities', 'FGA', 59, 20), ('Fetal abnormal surveillance', 'FAS', 125, 36), ('Fetal placental thrombosis', 'FPT', 5, 0), ('Fetal death (stillbirth)', 'FD', 168, 42)]
cperiod= 0.25996
cperiod= 0.388
******************************

*** RATES ***
Abnormal uterine bleeding (menstrual irregularity)        6352 24434.5284     54   139.1753
Miscarriage                                               1232  4739.1906    259   667.5258
Fetal chromosomal abnormalities                              7    26.9272      0     0.0000
Fetal malformation                                           2     7.6935      1     2.5773
Fetal cystic hygroma                                         5    19.2337      0     0.0000
Fetal cardiac disorders                                     10    38.4675      2     5.1546
Fetal arrhythmia                                             3    11.5402      0     0.0000
Fetal cardiac arrest                                         3    11.5402      0     0.0000
Fetal vascular mal-perfusion                                 5    19.2337      0     0.0000
Fetal growth abnormalities                                  59   226.9580     20    51.5464
Fetal abnormal surveillance                                125   480.8432     36    92.7835
Fetal placental thrombosis                                   5    19.2337      0     0.0000
Fetal death (stillbirth)                                   168   646.2533     42   108.2474
******************************

*** P VALUES ***
Abnormal uterine bleeding (menstrual irregularity)      0.000e+00
Miscarriage                                             0.000e+00
Fetal chromosomal abnormalities                         4.759e-03
Fetal malformation                                      1.973e-01
Fetal cystic hygroma                                    1.976e-02
Fetal cardiac disorders                                 4.682e-03
Fetal arrhythmia                                        8.838e-02
Fetal cardiac arrest                                    8.838e-02
Fetal vascular mal-perfusion                            1.976e-02
Fetal growth abnormalities                              1.675e-08
Fetal abnormal surveillance                             0.000e+00
Fetal placental thrombosis                              1.976e-02
Fetal death (stillbirth)                                0.000e+00
******************************

*** RELATIVE RATES ***
Abnormal uterine bleeding (menstrual irregularity)        180.6712   131.0816   255.0800
Miscarriage                                                 7.1414     6.0950     8.3904
Fetal chromosomal abnormalities                             0.0000     0.0000     0.0000
Fetal malformation                                          1.6826     0.0000     5.0000
Fetal cystic hygroma                                        0.0000     0.0000     0.0000
Fetal cardiac disorders                                     6.9673     1.6667    15.0000
Fetal arrhythmia                                            0.0000     0.0000     0.0000
Fetal cardiac arrest                                        0.0000     0.0000     0.0000
Fetal vascular mal-perfusion                                0.0000     0.0000     0.0000
Fetal growth abnormalities                                  4.7970     2.5882     9.1111
Fetal abnormal surveillance                                 5.4187     3.4839     8.5625
Fetal placental thrombosis                                  0.0000     0.0000     0.0000
Fetal death (stillbirth)                                    6.1986     4.1429     9.3889
******************************

******************************
***** Dose (Global) *****
[('Abnormal uterine bleeding (menstrual irregularity)', 'AUB', 12843, 65), ('Miscarriage', 'M', 3338, 325), ('Fetal chromosomal abnormalities', 'FCM', 10, 0), ('Fetal malformation', 'FM', 22, 2), ('Fetal cystic hygroma', 'FCM', 8, 0), ('Fetal cardiac disorders', 'FCD', 18, 2), ('Fetal arrhythmia', 'FA', 5, 0), ('Fetal cardiac arrest', 'FCA', 20, 0), ('Fetal vascular mal-perfusion', 'FVMP', 12, 0), ('Fetal growth abnormalities', 'FGA', 188, 24), ('Fetal abnormal surveillance', 'FAS', 178, 45), ('Fetal placental thrombosis', 'FPT', 6, 0), ('Fetal death (stillbirth)', 'FD', 402, 64)]
cperiod= 12.07
cperiod= 66
******************************

*** RATES ***
Abnormal uterine bleeding (menstrual irregularity)       12843  1064.0431     65     0.9848
Miscarriage                                               3338   276.5534    325     4.9242
Fetal chromosomal abnormalities                             10     0.8285      0     0.0000
Fetal malformation                                          22     1.8227      2     0.0303
Fetal cystic hygroma                                         8     0.6628      0     0.0000
Fetal cardiac disorders                                     18     1.4913      2     0.0303
Fetal arrhythmia                                             5     0.4143      0     0.0000
Fetal cardiac arrest                                        20     1.6570      0     0.0000
Fetal vascular mal-perfusion                                12     0.9942      0     0.0000
Fetal growth abnormalities                                 188    15.5758     24     0.3636
Fetal abnormal surveillance                                178    14.7473     45     0.6818
Fetal placental thrombosis                                   6     0.4971      0     0.0000
Fetal death (stillbirth)                                   402    33.3057     64     0.9697
******************************

*** P VALUES ***
Abnormal uterine bleeding (menstrual irregularity)      0.000e+00
Miscarriage                                             0.000e+00
Fetal chromosomal abnormalities                         5.781e-04
Fetal malformation                                      1.855e-07
Fetal cystic hygroma                                    2.378e-03
Fetal cardiac disorders                                 2.618e-06
Fetal arrhythmia                                        1.976e-02
Fetal cardiac arrest                                    6.949e-07
Fetal vascular mal-perfusion                            1.473e-04
Fetal growth abnormalities                              0.000e+00
Fetal abnormal surveillance                             0.000e+00
Fetal placental thrombosis                              9.631e-03
Fetal death (stillbirth)                                0.000e+00
******************************

*** RELATIVE RATES ***
Abnormal uterine bleeding (menstrual irregularity)       1191.8561   673.9474  2162.8333
Miscarriage                                                57.1421    44.3421    74.6591
Fetal chromosomal abnormalities                             0.0000     0.0000     0.0000
Fetal malformation                                         20.0241     7.6667    31.0000
Fetal cystic hygroma                                        0.0000     0.0000     0.0000
Fetal cardiac disorders                                    16.3892     6.0000    26.0000
Fetal arrhythmia                                            0.0000     0.0000     0.0000
Fetal cardiac arrest                                        0.0000     0.0000     0.0000
Fetal vascular mal-perfusion                                0.0000     0.0000     0.0000
Fetal growth abnormalities                                 56.1703    20.6667   189.0000
Fetal abnormal surveillance                                25.2665    12.1538    58.6667
Fetal placental thrombosis                                  0.0000     0.0000     0.0000
Fetal death (stillbirth)                                   37.9790    21.0526    73.0000
******************************

******************************
***** Month (Global) *****
[('Abnormal uterine bleeding (menstrual irregularity)', 'AUB', 12843, 65), ('Miscarriage', 'M', 3338, 325), ('Fetal chromosomal abnormalities', 'FCM', 10, 0), ('Fetal malformation', 'FM', 22, 2), ('Fetal cystic hygroma', 'FCM', 8, 0), ('Fetal cardiac disorders', 'FCD', 18, 2), ('Fetal arrhythmia', 'FA', 5, 0), ('Fetal cardiac arrest', 'FCA', 20, 0), ('Fetal vascular mal-perfusion', 'FVMP', 12, 0), ('Fetal growth abnormalities', 'FGA', 188, 24), ('Fetal abnormal surveillance', 'FAS', 178, 45), ('Fetal placental thrombosis', 'FPT', 6, 0), ('Fetal death (stillbirth)', 'FD', 402, 64)]
cperiod= 18
cperiod= 281
******************************

*** RATES ***
Abnormal uterine bleeding (menstrual irregularity)       12843   713.5000     65     0.2313
Miscarriage                                               3338   185.4444    325     1.1566
Fetal chromosomal abnormalities                             10     0.5556      0     0.0000
Fetal malformation                                          22     1.2222      2     0.0071
Fetal cystic hygroma                                         8     0.4444      0     0.0000
Fetal cardiac disorders                                     18     1.0000      2     0.0071
Fetal arrhythmia                                             5     0.2778      0     0.0000
Fetal cardiac arrest                                        20     1.1111      0     0.0000
Fetal vascular mal-perfusion                                12     0.6667      0     0.0000
Fetal growth abnormalities                                 188    10.4444     24     0.0854
Fetal abnormal surveillance                                178     9.8889     45     0.1601
Fetal placental thrombosis                                   6     0.3333      0     0.0000
Fetal death (stillbirth)                                   402    22.3333     64     0.2278
******************************

*** P VALUES ***
Abnormal uterine bleeding (menstrual irregularity)      0.000e+00
Miscarriage                                             0.000e+00
Fetal chromosomal abnormalities                         5.781e-04
Fetal malformation                                      1.855e-07
Fetal cystic hygroma                                    2.378e-03
Fetal cardiac disorders                                 2.618e-06
Fetal arrhythmia                                        1.976e-02
Fetal cardiac arrest                                    6.949e-07
Fetal vascular mal-perfusion                            1.473e-04
Fetal growth abnormalities                              0.000e+00
Fetal abnormal surveillance                             0.000e+00
Fetal placental thrombosis                              9.631e-03
Fetal death (stillbirth)                                0.000e+00
******************************

*** RELATIVE RATES ***
Abnormal uterine bleeding (menstrual irregularity)       4058.5702  1440.5556 12878.0000
Miscarriage                                               168.9349   110.2667   272.6667
Fetal chromosomal abnormalities                             0.0000     0.0000     0.0000
Fetal malformation                                         21.3257    10.0000    31.0000
Fetal cystic hygroma                                        0.0000     0.0000     0.0000
Fetal cardiac disorders                                    17.4372     8.0000    27.0000
Fetal arrhythmia                                            0.0000     0.0000     0.0000
Fetal cardiac arrest                                        0.0000     0.0000     0.0000
Fetal vascular mal-perfusion                                0.0000     0.0000     0.0000
Fetal growth abnormalities                                123.8733    40.7500   210.0000
Fetal abnormal surveillance                                79.6536    26.1429   192.0000
Fetal placental thrombosis                                  0.0000     0.0000     0.0000
Fetal death (stillbirth)                                  129.0915    46.7500   409.0000
******************************

******************************
***** People (Global) *****
[('Abnormal uterine bleeding (menstrual irregularity)', 'AUB', 12843, 65), ('Miscarriage', 'M', 3338, 325), ('Fetal chromosomal abnormalities', 'FCM', 10, 0), ('Fetal malformation', 'FM', 22, 2), ('Fetal cystic hygroma', 'FCM', 8, 0), ('Fetal cardiac disorders', 'FCD', 18, 2), ('Fetal arrhythmia', 'FA', 5, 0), ('Fetal cardiac arrest', 'FCA', 20, 0), ('Fetal vascular mal-perfusion', 'FVMP', 12, 0), ('Fetal growth abnormalities', 'FGA', 188, 24), ('Fetal abnormal surveillance', 'FAS', 178, 45), ('Fetal placental thrombosis', 'FPT', 6, 0), ('Fetal death (stillbirth)', 'FD', 402, 64)]
cperiod= 5.23
cperiod= 9.23
******************************

*** RATES ***
Abnormal uterine bleeding (menstrual irregularity)       12843  2455.6405     65     7.0423
Miscarriage                                               3338   638.2409    325    35.2113
Fetal chromosomal abnormalities                             10     1.9120      0     0.0000
Fetal malformation                                          22     4.2065      2     0.2167
Fetal cystic hygroma                                         8     1.5296      0     0.0000
Fetal cardiac disorders                                     18     3.4417      2     0.2167
Fetal arrhythmia                                             5     0.9560      0     0.0000
Fetal cardiac arrest                                        20     3.8241      0     0.0000
Fetal vascular mal-perfusion                                12     2.2945      0     0.0000
Fetal growth abnormalities                                 188    35.9465     24     2.6002
Fetal abnormal surveillance                                178    34.0344     45     4.8754
Fetal placental thrombosis                                   6     1.1472      0     0.0000
Fetal death (stillbirth)                                   402    76.8642     64     6.9339
******************************

*** P VALUES ***
Abnormal uterine bleeding (menstrual irregularity)      0.000e+00
Miscarriage                                             0.000e+00
Fetal chromosomal abnormalities                         5.781e-04
Fetal malformation                                      2.096e-06
Fetal cystic hygroma                                    2.378e-03
Fetal cardiac disorders                                 2.707e-05
Fetal arrhythmia                                        1.976e-02
Fetal cardiac arrest                                    6.949e-07
Fetal vascular mal-perfusion                            1.473e-04
Fetal growth abnormalities                              0.000e+00
Fetal abnormal surveillance                             0.000e+00
Fetal placental thrombosis                              9.631e-03
Fetal death (stillbirth)                                0.000e+00
******************************

*** RELATIVE RATES ***
Abnormal uterine bleeding (menstrual irregularity)        358.6413   261.0816   506.7602
Miscarriage                                                18.2268    15.7302    21.1975
Fetal chromosomal abnormalities                             0.0000     0.0000     0.0000
Fetal malformation                                         16.2592     5.0000    30.0000
Fetal cystic hygroma                                        0.0000     0.0000     0.0000
Fetal cardiac disorders                                    13.2949     4.0000    25.0000
Fetal arrhythmia                                            0.0000     0.0000     0.0000
Fetal cardiac arrest                                        0.0000     0.0000     0.0000
Fetal vascular mal-perfusion                                0.0000     0.0000     0.0000
Fetal growth abnormalities                                 15.0360     8.6000    27.6250
Fetal abnormal surveillance                                 7.2770     4.7895    11.2667
Fetal placental thrombosis                                  0.0000     0.0000     0.0000
Fetal death (stillbirth)                                   11.4116     8.1364    16.2917
******************************
```

## Extra

![[Abnormal uterine bleeding (menstrual irregularity)-Dose (Global)](Abnormal%20uterine%20bleeding%20(menstrual%20irregularity)-Dose%20(Global).png)

![Abnormal uterine bleeding (menstrual irregularity)-Dose (US)](Abnormal%20uterine%20bleeding%20(menstrual%20irregularity)-Dose%20(US).png)

![Abnormal uterine bleeding (menstrual irregularity)-Month (Global)](Abnormal%20uterine%20bleeding%20(menstrual%20irregularity)-Month%20(Global).png)

![Abnormal uterine bleeding (menstrual irregularity)-Month (US)](Abnormal%20uterine%20bleeding%20(menstrual%20irregularity)-Month%20(US).png)

![Abnormal uterine bleeding (menstrual irregularity)-People (Global)](Abnormal%20uterine%20bleeding%20(menstrual%20irregularity)-People%20(Global).png)

![Abnormal uterine bleeding (menstrual irregularity)-People (US)](Abnormal%20uterine%20bleeding%20(menstrual%20irregularity)-People%20(US).png)

![Fetal abnormal surveillance-Dose (Global)](Fetal%20abnormal%20surveillance-Dose%20(Global).png)

![Fetal abnormal surveillance-Dose (US)](Fetal%20abnormal%20surveillance-Dose%20(US).png)

![Fetal abnormal surveillance-Month (Global)](Fetal%20abnormal%20surveillance-Month%20(Global).png)

![Fetal abnormal surveillance-Month (US)](Fetal%20abnormal%20surveillance-Month%20(US).png)

![Fetal abnormal surveillance-People (Global)](Fetal%20abnormal%20surveillance-People%20(Global).png)

![Fetal abnormal surveillance-People (US)](Fetal%20abnormal%20surveillance-People%20(US).png)

![Fetal arrhythmia-Dose (Global)](Fetal%20arrhythmia-Dose%20(Global).png)

![Fetal arrhythmia-Dose (US)](Fetal%20arrhythmia-Dose%20(US).png)

![Fetal arrhythmia-Month (Global)](Fetal%20arrhythmia-Month%20(Global).png)

![Fetal arrhythmia-Month (US)](Fetal%20arrhythmia-Month%20(US).png)

![Fetal arrhythmia-People (Global)](Fetal%20arrhythmia-People%20(Global).png)

![Fetal arrhythmia-People (US)](Fetal%20arrhythmia-People%20(US).png)

![Fetal cardiac arrest-Dose (Global)](Fetal%20cardiac%20arrest-Dose%20(Global).png)

![Fetal cardiac arrest-Dose (US)](Fetal%20cardiac%20arrest-Dose%20(US).png)

![Fetal cardiac arrest-Month (Global)](Fetal%20cardiac%20arrest-Month%20(Global).png)

![Fetal cardiac arrest-Month (US)](Fetal%20cardiac%20arrest-Month%20(US).png)

![Fetal cardiac arrest-People (Global)](Fetal%20cardiac%20arrest-People%20(Global).png)

![Fetal cardiac arrest-People (US)](Fetal%20cardiac%20arrest-People%20(US).png)

![Fetal cardiac disorders-Dose (Global)](Fetal%20cardiac%20disorders-Dose%20(Global).png)

![Fetal cardiac disorders-Dose (US)](Fetal%20cardiac%20disorders-Dose%20(US).png)

![Fetal cardiac disorders-Month (Global)](Fetal%20cardiac%20disorders-Month%20(Global).png)

![Fetal cardiac disorders-Month (US)](Fetal%20cardiac%20disorders-Month%20(US).png)

![Fetal cardiac disorders-People (Global)](Fetal%20cardiac%20disorders-People%20(Global).png)

![Fetal cardiac disorders-People (US)](Fetal%20cardiac%20disorders-People%20(US).png)

![Fetal chromosomal abnormalities-Dose (Global)](Fetal%20chromosomal%20abnormalities-Dose%20(Global).png)

![Fetal chromosomal abnormalities-Dose (US)](Fetal%20chromosomal%20abnormalities-Dose%20(US).png)

![Fetal chromosomal abnormalities-Month (Global)](Fetal%20chromosomal%20abnormalities-Month%20(Global).png)

![Fetal chromosomal abnormalities-Month (US)](Fetal%20chromosomal%20abnormalities-Month%20(US).png)

![Fetal chromosomal abnormalities-People (Global)](Fetal%20chromosomal%20abnormalities-People%20(Global).png)

![Fetal chromosomal abnormalities-People (US)](Fetal%20chromosomal%20abnormalities-People%20(US).png)

![Fetal cystic hygroma-Dose (Global)](Fetal%20cystic%20hygroma-Dose%20(Global).png)

![Fetal cystic hygroma-Dose (US)](Fetal%20cystic%20hygroma-Dose%20(US).png)

![Fetal cystic hygroma-Month (Global)](Fetal%20cystic%20hygroma-Month%20(Global).png)

![Fetal cystic hygroma-Month (US)](Fetal%20cystic%20hygroma-Month%20(US).png)

![Fetal cystic hygroma-People (Global)](Fetal%20cystic%20hygroma-People%20(Global).png)

![Fetal cystic hygroma-People (US)](Fetal%20cystic%20hygroma-People%20(US).png)

![Fetal death (stillbirth)-Dose (Global)](Fetal%20death%20(stillbirth)-Dose%20(Global).png)

![Fetal death (stillbirth)-Dose (US)](Fetal%20death%20(stillbirth)-Dose%20(US).png)

![Fetal death (stillbirth)-Month (Global)](Fetal%20death%20(stillbirth)-Month%20(Global).png)

![Fetal death (stillbirth)-Month (US)](Fetal%20death%20(stillbirth)-Month%20(US).png)

![Fetal death (stillbirth)-People (Global)](Fetal%20death%20(stillbirth)-People%20(Global).png)

![Fetal death (stillbirth)-People (US)](Fetal%20death%20(stillbirth)-People%20(US).png)

![Fetal growth abnormalities-Dose (Global)](Fetal%20growth%20abnormalities-Dose%20(Global).png)

![Fetal growth abnormalities-Dose (US)](Fetal%20growth%20abnormalities-Dose%20(US).png)

![Fetal growth abnormalities-Month (Global)](Fetal%20growth%20abnormalities-Month%20(Global).png)

![Fetal growth abnormalities-Month (US)](Fetal%20growth%20abnormalities-Month%20(US).png)

![Fetal growth abnormalities-People (Global)](Fetal%20growth%20abnormalities-People%20(Global).png)

![Fetal growth abnormalities-People (US)](Fetal%20growth%20abnormalities-People%20(US).png)

![Fetal malformation-Dose (Global)](Fetal%20malformation-Dose%20(Global).png)

![Fetal malformation-Dose (US)](Fetal%20malformation-Dose%20(US).png)

![Fetal malformation-Month (Global)](Fetal%20malformation-Month%20(Global).png)

![Fetal malformation-Month (US)](Fetal%20malformation-Month%20(US).png)

![Fetal malformation-People (Global)](Fetal%20malformation-People%20(Global).png)

![Fetal malformation-People (US)](Fetal%20malformation-People%20(US).png)

![Fetal placental thrombosis-Dose (Global)](Fetal%20placental%20thrombosis-Dose%20(Global).png)

![Fetal placental thrombosis-Dose (US)](Fetal%20placental%20thrombosis-Dose%20(US).png)

![Fetal placental thrombosis-Month (Global)](Fetal%20placental%20thrombosis-Month%20(Global).png)

![Fetal placental thrombosis-Month (US)](Fetal%20placental%20thrombosis-Month%20(US).png)

![Fetal placental thrombosis-People (Global)](Fetal%20placental%20thrombosis-People%20(Global).png)

![Fetal placental thrombosis-People (US)](Fetal%20placental%20thrombosis-People%20(US).png)

![Fetal vascular mal-perfusion-Dose (Global)](Fetal%20vascular%20mal-perfusion-Dose%20(Global).png)

![Fetal vascular mal-perfusion-Dose (US)](Fetal%20vascular%20mal-perfusion-Dose%20(US).png)

![Fetal vascular mal-perfusion-Month (Global)](Fetal%20vascular%20mal-perfusion-Month%20(Global).png)

![Fetal vascular mal-perfusion-Month (US)](Fetal%20vascular%20mal-perfusion-Month%20(US).png)

![Fetal vascular mal-perfusion-People (Global)](Fetal%20vascular%20mal-perfusion-People%20(Global).png)

![Fetal vascular mal-perfusion-People (US)](Fetal%20vascular%20mal-perfusion-People%20(US).png)

![Miscarriage-Dose (Global)](Miscarriage-Dose%20(Global).png)

![Miscarriage-Dose (US)](Miscarriage-Dose%20(US).png)

![Miscarriage-Month (Global)](Miscarriage-Month%20(Global).png)

![Miscarriage-Month (US)](Miscarriage-Month%20(US).png)

![Miscarriage-People (Global)](Miscarriage-People%20(Global).png)

![Miscarriage-People (US)](Miscarriage-People%20(US).png)

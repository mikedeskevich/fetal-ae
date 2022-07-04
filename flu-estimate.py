import numpy as np
from pyrsistent import v

np.random.seed(1)

#https://population.un.org/
#from https://www.macrotrends.net/countries/USA/united-states/birth-rate
birth_rate = {2022: 12.012, 2021: 12.001, 2020: 11.990, 2019: 11.979, 2018: 11.968, 2017: 12.083, 2016: 12.198, 2015: 12.314, 2014: 12.429, 2013: 12.544, 2012: 12.798, 2011: 13.051, 2010: 13.305, 2009: 13.558, 2008: 13.812, 2007: 13.856, 2006: 13.900, 2005: 13.945, 2004: 13.989, 2003: 14.033, 2002: 14.083, 2001: 14.133, 2000: 14.182, 1999: 14.232, 1998: 14.282, 1997: 14.516, 1996: 14.750, 1995: 14.983, 1994: 15.217, 1993: 15.451, 1992: 15.492, 1991: 15.532, 1990: 15.573, 1989: 15.613, 1988: 15.654, 1987: 15.590, 1986: 15.525, 1985: 15.461, 1984: 15.396, 1983: 15.332, 1982: 15.217, 1981: 15.102, 1980: 14.986}

#https://population.un.org/
#from https://www.macrotrends.net/countries/USA/united-states/death-rate
death_rate = {2022: 9.075, 2021: 8.977, 2020: 8.880, 2019: 8.782, 2018: 8.685, 2017: 8.580, 2016: 8.475, 2015: 8.369, 2014: 8.264, 2013: 8.159, 2012: 8.152, 2011: 8.145, 2010: 8.138, 2009: 8.131, 2008: 8.124, 2007: 8.203, 2006: 8.282, 2005: 8.362, 2004: 8.441, 2003: 8.520, 2002: 8.548, 2001: 8.576, 2000: 8.603, 1999: 8.631, 1998: 8.659, 1997: 8.691, 1996: 8.722, 1995: 8.754, 1994: 8.785, 1993: 8.817, 1992: 8.844, 1991: 8.871, 1990: 8.898, 1989: 8.925, 1988: 8.952, 1987: 8.927, 1986: 8.903, 1985: 8.878, 1984: 8.854, 1983: 8.829, 1982: 8.833, 1981: 8.837, 1980: 8.841}

#from https://www.macrotrends.net/countries/USA/united-states/population
year = 1980
people = np.zeros(229486) #thousands
people[np.where(np.random.random(np.size(people)) < 0.50)] = 1

died_with_vax = 0
while year <= 2021:
    # make some new people to tack on at the end of the year
    new_people = np.zeros(int(np.size(people)*(birth_rate[year]/1000)))

    # decide which people got vaccinated
    vaccinated = np.random.random(np.size(people)) < np.where(people, .57, 1-.57)
    people[np.where(vaccinated)] = 1
    print(np.size(people), int(np.sum(vaccinated)))

    # figure out who's still alive
    alive = np.random.random(np.size(people)) > (death_rate[year]/1000)

    # count people who died having been vaccinated at least once
    if year >= 1998:
        died_with_vax += np.sum(people[np.where(alive == False)])

    # add our new people for this year
    people = np.append(people[np.where(alive)], new_people)

    # eoy summary
    population=np.size(people)
    total_vax=int(np.sum(people)+died_with_vax)
    percent_vax=total_vax/population
    print(year, population, total_vax, percent_vax)

    year += 1

#https://population.un.org/
real_final_population=334805
print(int(real_final_population*percent_vax)*1000)

#https://population.un.org/
world_population=7953953
print(int(world_population*percent_vax)*1000)

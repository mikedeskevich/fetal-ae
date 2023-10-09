## Methods

A retrospective analysis of the AE reports in the VAERS database was performed for events reported between 1 January 1998 and 30 June 2022.  

*Time Tracked*

The start date, 1 January 1998 was chosen because a few months earlier the CDC has approved and recommended the use of the Influenza vaccine for pregnant women.  Reports in VAERS after this date would signify AE due to on-label use of the vaccines.  At the end of the study period of 30 June 2022, there have been 294 months of data for the Influenza vaccine and 18 months of data for the COVID-19 vaccines.

*AE Report Counts*

A query of the VARES database was made for each AE selected by [JIM]: Menstrual Abnormality, Miscarriage, Fetal Chromosomal Abnormalities, Fetal Malformation, Fetal Cystic Hygroma, Fetal Cardiac Disorders, Fetal Arrhythmia, Fetal 

----

Cardiac Arrest, Fetal Vascular Mal-Perfusion, Fetal Growth Abnormalities, Fetal Abnormal Surveillance, Fetal Placental Thrombosis, Low Amniotic Fluid, Fetal death (stillbirth). AE reports were counted globally and within only the US for both the Influenza vaccine and the COVID-19 vaccines. The counts for these events are in tables 1 and 2.

*Doses Given*

The AE report count data is normalized by doses of each vaccine given during the study period.  Using [REFERENCES] we estimate that 12.07 billion doses of the COVID-19 vaccine were given globally and in the US.  Using [REFERENCES], we estimate that 66 billion doses of the Influenza vaccine were given globally and 3.3 billion in the US.

*People Vaccinated*

Additionally, the AE report counts are normalized by the number of people vaccinated during the study period.  Using [REFERENCES] it is estimated that 5.23 billion people received at least one dose of a COVID-19 vaccine globally, 260 million in the US, and 7.71 billion people received at least one dose of the Influenza vaccine globally, 313 million in the US. 



Counting the number of people vaccinated with the COVID-19 vaccine is straightforward; however the Influenza vaccine is difficult to directly count because individuals are not tracked and there are yearly seasons where an individual may choose to receive a subsequent vaccinations. A Monte Carlo simulation is used to estimate the number of people that have received at least one dose of the Influenza vaccine in the since 1998. 

A sample population is tracked where each year a fraction of the eligible population is vaccinated, $f_{v}$, a fraction of the population dies (some of whom may be vaccinated), $f_d$, and a new fraction of the population is becomes eligible (none of whom are vaccinated), $f_e$. UN population data (reference: https://population.un.org/)is used to simulate the yearly demographics change.

The conditional probability of Influenza vaccination from Kwong, et al. (reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6961264/). Kwong reports that roughly 57% (33,234 out of 58,021) of the population in their study who receives a Influenza shot in one year repeats it a subsequent year. The CDC reports that approximately 50% of the population receives the vaccine in any given year. From that, we approximate $f_v=0.57$ for previously vaccinated individuals and $f_v=0.43$ for previously unvaccinated individuals, which will result in the rough CDC approximation of 50% of the population being vaccinated any given year. 



The simulation is started in 1980 with a sample of the eligible population of 100,000,000 people with 50% of them pre-vaccinated from previous years. From 1980 to 1997 the population grows by $f_e$, shrinks by $f_d$, and individuals are vaccinated using a conditional $f_v$ based on their current vaccination status. The simulation continues until 2021 with the addition that in 1998 he number of people who were vaccinated and died are accumulated. After running the simulation, in 2021 the sample population grew to 125,981,000, with a total of 146,200,000 (current vaccinated living plus the accumulated vaccinated dead) receiving at least one dose of the Influenza vaccine since 1998 (116% of the current population). 

Scale this estimate to the true 2022 the total eligible US population of 269.5 million (329.5 million minus 60 million who are too young) (reference: https://population.un.org/), results in roughly a total 313 million people in the US that have received at least one dose of Influenza vaccine. Using the same scaling factor for an eligible global population of 6.65 (7.95 billion minus 1.3 billion), results in an estimate of 7.71 billion people worldwide who have received at least one dose of the Influenza vaccine since 1998.  

## Results

For all AE, the rates of reports post COVID-19 vaccine are higher than the Influenza vaccine across all three normalization methods: by unit time, by dose given, and by person vaccinated. The two analyses below: 1) compute the p-value to determine if the AE report rates are statistically different between the two vaccines, and 2) compute the relative rate and 95% CI of AE reports after the COVID-19 vaccine versus the Influenza vaccine. 

*Statistical Significance*

Each AE report is treaded as discrete independent events occurring at the mean rate specified in Tables 1 and 2 which are model as a Poisson distribution. Given two rates $\lambda_1$ and $\lambda_2$ we perform a Poisson E-test [reference: https://userweb.ucs.louisiana.edu/~kxk4695/JSPI-04.pdf] to compute the p-value.



We use the rates in Tables 1 and 2 and normalize the event counts over the time-, dose-, and people-vaccinated-windows and report the p-values below in Table 3. Where there is sufficient data, the p-values are small, and where 0.0 is reported, it was too small to represent as a double precision floating point number in our E-test function [reference: https://github.com/nolanbconaway/poisson-etest]. 

*Proportional Reporting Ratio*

For the rates that have non-zero counts in the reporting period, the ratio of rates of AE reports for each vaccine and the 95% confidence interval is estimated. The ratio distribution, $R$, which is the distribution of the ratio of two different Poisson distributions, is computed. That is, given two Poisson distributions, $P(\lambda_1)$ and $P(\lambda_2)$,  the ratio distribution, $R$, which represents the probability distribution of the ratio of the distribution of events is estimated with a Monte Carlo simulation.

$$
R(\lambda_1,\lambda_2)=\frac{P(\lambda_1)}{P(\lambda_2)}
$$

1,000,000 random samples are drawn from Poisson distributions with rates $\lambda_1$ and $\lambda_2$ resulting in a sample of paired event counts $n_1$ and $n_2$, respectively and $R$ is the distribution of all $\frac{n_1}{n_2}$ ratios. The mean of $R$ is is the expectation value for the ratio of the two Poisson distributions and the empirically-derived quantile function of $R$ is used to estimate the 95% CI of the mean. All computed values have converged to a precision of 1% or better. For AE that are reported infrequently post Influenza vaccine there is finite probability that $n_2$ is zero resulting in $R$ being undefined. To mitigate this problem, the zero-truncated Poisson distribution [reference: https://www.jstor.org/stable/2527552] is used and only instances of non-zero $n_2$ draws are counted. This approach skews the $R$ distribution to the left [reference: https://epubs.siam.org/doi/10.1137/0134043] and makes the AE rates for the COVID-19 vaccine actually look better, in these cases, the AE rate is a lower bound.


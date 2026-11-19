This section presents the key findings derived from the analysis and interprets their significance. The results are organized to highlight patterns in student risk, funding support, and demographic composition, followed by the comparative performance of predictive models. Incorporating descriptive statistics with model results, the discussion assesses both the precision and significance of the analytical methodology while also placing the findings within the institutional framework. The aim is to connect quantitative evidence with actionable insights, ensuring that the results are both interpretable and useful for decision-making. The results above are obtained from the 330 first year, First Time Entering students in the Diploma of Civil Engineering programme from 2022 to 2025.

## Exploratory Data Analysis

### At-Risk Status Distribution

Figure 4.1 demonstrates the at-risk distribution for the enrolled First Time Entering first year students in the Diploma in Civil Engineering in Cape Peninsula University of Technology from 2022-2025. It is notable that most of the students are not at-risk, with 209 (63.3%) students not at-risk while 121 (36.7%) students are classified as at-risk students. That is more than a third (36.7%) of enrolled students who are at-risk, calling for interventions for these students.

*Figure 4.1: At-Risk Student Distribution*

![figure](assets/figures/fig001.png)

### Demographic Distribution Results

The dataset contains 330 students who are doing the Diploma in Civil Engineering. The results in figure 4.2. demonstrate gender disparity among the students. The program over the course of 4 year had 54.5% of the students as males with 45.5% being females.

*Figure 4.2: Graph showing Gender distribution.*

![figure](assets/figures/fig002.png)

Figure 4.3 below show the distribution of homa language name across the 4-year period in the program. The Xhosa language has been dominating in terms of enrolment with about 129 (39.1%) students being Xhosa. The second most home language name is IsiZulu, with 68 (20.1%) students, followed by English with 32 (9.7%) students. The Home language name that is least represented is the IsiNdebele language with only 3 students, constituting only 0.9% of the enrolled program population.

*Figure 4.3: Home language name distribution*

![figure](assets/figures/fig003.png)

The ethnic group distribution graph (figure 4.4) below represents the proportion and number of the different ethnic groups enrolled in the program. The African ethnic group is dominating with an 89.4% of the enrolled students being African, the other 10.6% is distributed among the other Ethnic groups, with Coloured (8.8%), White (1.5%) and Other (0.3%) constituting that 10.6% respectively.

*Figure 4.4: Graph showing distribution by Ethnicity.*

![figure](assets/figures/fig004.png)

The graph below (figure 4.5) reflects the previous activity distribution for the students. It is notable that most of the students come directly from Grade 12 (192) with about 58.2%, followed by those who were previously unemployed (69) before being enrolled with 20.9%. About 3.3% of the student come from another university while 1.8% comes from a technical college. There is only one student who was enrolled from a foreign institution and 3 who were in labour force.

*Figure 4.5: Previous activity distribution.*

![figure](assets/figures/fig005.png)

From figure 4.6 below, which demonstrated the matric type distribution, matric type B (Admission to bachelor’s degree) dominated with about 94.2% of the students having obtained that admission. This is followed by students who were admitted with Admission to a Diploma’s degree (D) with 4.2%. This reflects the selection criteria for the program in relation to its minimum requirement for a student to be accepted.

*Figure 4.6: Graph showing distribution of matric type.*

![figure](assets/figures/fig006.png)

The results in figure 4.7 demonstrate the different bursaries and how they are distributed among the students. Most students were funded by Nsfas (74.8%), while 21.2% of the students were self-funded and the remaining 3.9% were funded by a private bursary. This shows that most of the students in the program are funded.

*Figure 4.7: Graph showing the distribution of bursary types.*

![figure](assets/figures/fig007.png)

From figure 4.8 below, representing funding status for the students, it can be noted that about 78.8% (260) of the students are funded (either by Nsfas or Private bursary), while 21.2% (70) of the students are not funded (these are the students that are self-funded on the bursary type distribution). This visual supports the previous bursary type distribution (figure 4.7) that majority of the students are actually funded.

*Figure 4.8: Pie chart showing distribution of the funding status.*

![figure](assets/figures/fig008.png)

Figure 4.9 shows the distribution of students who actually live in CPUT owned residence against those who do not live in CPUT owned residences. About 52.4% of the students live in CPUT owned residence, while the remaining 47.6% do not. The distribution is fairly even, but one might argue that approximately half of the students do not actually have residence and so might have challenges as compared to those who do. This is a point that the study aims to investigate.

*Figure 4.9: Distribution of residence status.*

![figure](assets/figures/fig009.png)

Below (figure 4.10) is a visual representing the distribution of the students by quintile. Majority of the students come from quintile 5 (30.6%) meaning these are students who come in well-resources school. The second most quintile is quintile 3 with 21.2% (70), followed by those who come from quintile 2 with 20.3% (67), then the 60 (18.2%) students who come from quintile 1 (least resourced schools). Holistically, most of the students come from quintiles below quintile 4.  These students are from relatively poor to moderate school backgrounds and might need time to adjust to university system.

*Figure 4.10: Secondary School Quintile distribution*

![figure](assets/figures/fig010.png)

The age at enrolment distribution below (figure 4.11) demonstrates different age intervals with the age 19 and age 20 separated from the intervals, while students that are 18 years or younger are grouped together, and those that are 21 years or old are also grouped together. The dominant age for enrolment at the Diploma in Civil Engineering program is age 19 with 128 (38.8%) enrolled at that age, followed by age 20 with 82 (24.8%) students enrolled at that age. 75 (22.7%) students enrolled at the age 21 or older, while 45 (13.6%) students enrolled at the age of 18 or younger.

*Figure 4.11: Age group at enrolment distribution.*

![figure](assets/figures/fig011.png)

### Association with At-Risk Status

Figure 4.12 demonstrate the at-risk rate by year from 2022 to 2025 to establish which academic year had the most at-risk rate. The year with the most at-risk First Time Entering first year students in the Diploma in Civil Engineering was discovered to be 2024 with an at-risk rate of 43%. The year 2022 followed with 37.7% of at-risk students, while 2023 had 35.6% students who were at-risk. The year 2025 had the least at-risk proportion of students with 30% at-risk students. There is a notable decrease of the at-risk proportion from 2024 to 2025 with 13% points.

*Figure 4.12: Graph showing at-risk rate by academic year.*

![figure](assets/figures/fig012.png)

A Chi-Square test of independence was conducted to examine the association between Academic Year and At-Risk status. The test reveals no statistically significant association between a student's academic year and their likelihood of being at-risk (${\chi }^{2}=3.5159$, $p=0.3187$). The effect size, measured by Cramer's V, was 0.103, indicating a weak association. All assumptions for the test were met, with no expected cell count falling below 5. The corrected p-value (1.0) further confirms the lack of significance. Therefore, it can be concluded that a student's academic year does not significantly influence their likelihood of being classified as at-risk in this dataset.

*Table 4.1: Statistical test between Academic year and at-risk status.*

| Feature | Academic Year |
|---|---|
| Type | Categorical |
| Test | Chi-Square |
| Statistic | 3.5159 |
| p-value (Raw) | 0.3187 |
| p-value (Corrected) | 1.0 |
| Effect Size (Cramér's V) | 0.1032 |
| Expected count < 5 (cells) | 0 |
| Significant (α = 0.05) | False |

The figure below (figure 4.13) depicts a gender distribution association with risk rate. The graph shows a slight difference in at-risk rate between the two genders, with male at 37.8% risk rate, while female is at 35.3%. The difference is only 2.5% between the two genders showing that being either gender doesn’t necessarily put an individual at-risk, and that also gender alone might not be a determinant factor to students being at risk.

*Figure 4.13: Graph showing at-risk rate by gender.*

![figure](assets/figures/fig013.png)

Table 4.2 shows the results of a Chi-Square test of association between Gender and the At-Risk status. The Chi-Square test revealed that gender was not significantly associated with the students being at-risk, χ² = 0.1184, p = 0.7308 > 0.05. The effect size was little (Cramer's V = 0.0189), suggesting that gender has little to no practical influence on student risk. Additionally, all expected cell frequencies exceeded 5, satisfying the assumptions of the Chi-Square test. Therefore, gender was not identified as a significant predictor of the At-Risk Status.

*Table 4.2: Statistical test between gender and at-risk status.*

| Feature | Gender |
|---|---|
| Type | Categorical |
| Test | Chi-Square |
| Statistic | 0.1184 |
| p-value (Raw) | 0.7308 |
| p-value (Corrected) | 1.0 |
| Effect Size (Cramér's V) | 0.0189 |
| Expected count < 5 (cells) | 0 |
| Significant (α = 0.05) | False |

Figure 4.14 below demonstrate the distribution of at-risk rate by home language. Tshivenda speaking students appear to be the more likely group to be at risk with 57.1%, followed by Xitsonga and Siswati both at 50%, Sesotho at 47.1%, Xhosa (38.8%), Setswana (37.5%), IsiZulu (36.8%), IsiNdebele (33.3%), Afrikaans (27.3%), Sepedi (26.1%) and English with 21.9%. Students with English as their home language appear to be less at-risk compared to the other groups. It is worth noting that the groups with the highest at-risk rate, specifically the first three have small populations.

*Figure 4.14: At-Risk rate by Home Language name.*

![figure](assets/figures/fig014.png)

Table 4.3 shows results for the Chi-Square test of independence examining the relationship between home language and the at-risk status. The results revealed no statistically significant association between the variables, χ² = 8.086, p = 0.6204 > 0.05. The effect size was weak (Cramer's V = 0.1565), suggesting a limited practical relationship between home language and the at-risk status. Although the findings indicate that home language is not a significant factor associated with the students being at-risk, caution is warranted in interpreting the results because seven cells had expected frequencies below five, which may affect the robustness of the Chi-Square test assumptions.

*Table 4.3: Test statistics between Home Language and At-Risk Status.*

| Feature | Home Language |
|---|---|
| Type | Categorical |
| Test | Chi-Square |
| Statistic | 8.086 |
| p-value (Raw) | 0.6204 |
| p-value (Corrected) | 1.0 |
| Effect Size (Cramér's V) | 0.1565 |
| Expected count < 5 (cells) | 7 |
| Significant (α = 0.05) | False |

The graph below (figure 4.15) shows the distribution of at-risk rate across the different ethnic groups. From the visual it can be observed than the African group has more at-risk students with 37.6%, followed by the Coloured group with31.0%, while the White group has 20% proportion of at-risk students. From this visual, it can be noted that students with high enrolment also appear to have the highest at-risk rate.

*Figure 4.15: Graph showing at-risk rate distribution by ethnic group.*

![figure](assets/figures/fig015.png)

The table below (table 4.4) shows a Chi-Square test of independence ethnic group and the At-Risk status. The results showed no statistically significant relationship between the variables, χ² = 1.6904, p = 0.6391 > 0.05. The effect size was very weak (Cramer's V = 0.0716), indicating a negligible practical association. Although four cells had expected frequencies below five, the results suggest that ethnic group is not significantly associated with the at-risk status and was therefore not identified as an important factor in this study.

*Table 4.4: Test statistics between ethnic group and at-risk status.*

| Feature | Ethnic Group |
|---|---|
| Type | Categorical |
| Test | Chi-Square |
| Statistic | 1.6904 |
| p-value (Raw) | 0.6391 |
| p-value (Corrected) | 1.0 |
| Effect Size (Cramér's V) | 0.0716 |
| Expected count < 5 (cells) | 4 |
| Significant (α = 0.05) | False |

Figure 4.16 indicates notable differences in the proportion of students classified as at risk across the various previous activity categories. Students previously enrolled in the labour force recorded the highest at-risk rate at 66.7%, followed by unemployed students at 47.8% and students classified under other previous activities at 39.6%. The findings indicate that students entering university directly from Grade 12 had the lowest proportion of at-risk cases, implying that they are more likely to perform academically better than students from other entry pathways.

*Figure 4.16: At-risk rate by previous activity.*

![figure](assets/figures/fig016.png)

Table 4.5 demonstrates the Chi-Square test of independence between a student's Previous Activity and At-Risk status. The results indicated no statistically significant association (${\chi }^{2}=7.6286$, $p=0.2666>0.05$). The effect size (Cramer's V = 0.152) suggested only a weak relationship. However, the analysis violated the Chi-Square assumption of minimum expected cell frequencies, with 7 cells falling below the threshold of 5. Consequently, while the findings suggest Previous Activity is not a strong determinant of risk, the results should be interpreted cautiously.

*Table 4.5: Test statistic between Previous activity and at-risk status.*

| Feature | Previous Activity |
|---|---|
| Type | Categorical |
| Test | Chi-Square |
| Statistic | 7.6286 |
| p-value (Raw) | 0.2666 |
| p-value (Corrected) | 1.0 |
| Effect Size (Cramér's V) | 0.152 |
| Expected count < 5 (cells) | 7 |
| Significant (α = 0.05) | False |

The funding distribution by at-risk rate in figure 4.17 shows that students who are funded are slightly more likely to be at-risk with 36.9% compared to those who are not funded with 35.7%. The difference is 1.2% showing that having been funded or not is not significant in whether a student becomes at-risk or not. This rejects the hypothesis made about financial freedom being a determinant of success and financial constraint being a determinant of a student being at-risk.

*Figure 4.17: Distribution of at-risk rate by funding status.*

![figure](assets/figures/fig017.png)

Table 4.6 below demonstrates the Chi-Square test of independence between funding status (funded vs. not funded) and at-risk status. Contrary to the initial hypothesis, the results revealed no statistically significant association between the two variables (${\chi }^{2}=0.0022$, $p=0.9629>0.05$). The effect size was negligible (Cramer's V = 0.0026). All assumptions for the test were robustly met, with zero cells having an expected count of less than 5. This indicates that, within this sample, a student's funding status does not significantly influence their likelihood of being classified as at-risk, suggesting that other socio-economic or environmental factors may play a more dominant role.

*Table 4.6: Test statistics between Funding status and At-Risk status.*

| Feature | Funded |
|---|---|
| Type | Categorical |
| Test | Chi-Square |
| Statistic | 0.0022 |
| p-value (Raw) | 0.9629 |
| p-value (Corrected) | 1.0 |
| Effect Size (Cramér's V) | 0.0026 |
| Expected count < 5 (cells) | 0 |
| Significant (α = 0.05) | False |

The graph in figure 4.18 compares the proportion of students classified as at risk based on whether they reside in university residence or not. Students not living in university residence have a higher at-risk rate (37.6%) compared to the students in university residence with 35.8%. This visual slightly supports the hypothesis that students living in university residence, under conducive environment for studying, access to internet connection and convenience of institutional transportation are somewhat less likely to be at-risk.

*Figure 4.18: Distribution of at-risk rate by residence status.*

![figure](assets/figures/fig018.png)

The table below (Table 4.7) shows the Chi-Square test of independence between Residence status and At-Risk status. The analysis revealed no statistically significant relationship between the two variables (${\chi }^{2}=0.0456$, $p=0.8309>0.05$). The effect size was negligible (Cramer's V = 0.0118), indicating that living in residence does not meaningfully alter a student's likelihood of being at-risk in this sample. All assumptions for the test were met, with zero cells having an expected count of less than 5. This contradicts the initial hypothesis that residence status and the associated environmental stressors would significantly impact academic risk, suggesting that other factors are more influential for this cohort.

*Table 4.7:Test statistics between Residence status (In Residence) and At-Risk Status.*

| Feature | In Residence |
|---|---|
| Type | Categorical |
| Test | Chi-Square |
| Statistic | 0.0456 |
| p-value (Raw) | 0.8309 |
| p-value (Corrected) | 1.0 |
| Effect Size (Cramér's V) | 0.0118 |
| Expected count < 5 (cells) | 0 |
| Significant (α = 0.05) | False |

Figure (4.19) presents a bar chart illustrating the "At-Risk Rate" of students across five different secondary school quintiles (where Quintile 1 typically represents the most disadvantaged schools and Quintile 5 the least disadvantaged). Students from Quintile 2 emerge as a particularly high-risk demographic with 49.3%, followed by students from Quintile 1 with 36.7%. School quintiles 3, 4, and 5 range between 31.2% to 39.3% showing little difference between these demographics. Notably, students from lower quintiles exhibit the highest risk rates with this being evident on quintile 2, demonstrating that students from poor academic background (least resourced schools) may appear to be more vulnerable.

*Figure 4.19: At-Risk rate by secondary school quintile.*

![figure](assets/figures/fig019.png)

The Chi-Square test of independence in table 4.8 demonstrate the association between School Quintile and At-Risk status. The test revealed no statistically significant relationship (${\chi }^{2}=6.1064$, $p=0.1913>0.05$). The effect size was small (Cramer's V = 0.136). All test assumptions were met, with zero cells having an expected count of less than 5. Although the descriptive statistics (Figure 4.19) indicated a higher at-risk rate among students from Quintile 2, this difference was not statistically significant. This suggests that a student's secondary school’s socio-economic quintile does not independently predict their at-risk status in this cohort, and other factors may be more influential.

*Table 4.8: Test statistics between School Quintile and At-Risk status.*

| Feature | School Quintile |
|---|---|
| Type | Categorical |
| Test | Chi-Square |
| Statistic | 6.1064 |
| p-value (Raw) | 0.1913 |
| p-value (Corrected) | 1.0 |
| Effect Size (Cramér's V) | 0.136 |
| Expected count < 5 (cells) | 0 |
| Significant (α = 0.05) | False |

The bar chart (figure 4.20) below illustrates the At-Risk Rate of students categorized by their age at enrollment. Students who enrolled at the age of 19 years old appear to be the most vulnerable with an at-risk rate of 40.6%, followed by those who enrolled at age 21 or older (40.0%) and age 20 (37.8%). Students that enroll at 18 years or younger have the lowest at-risk rate at 17.8%, suggesting that younger students who are likely transitioning directly from high school tend to perform better.

*Figure 4.20: At-risk rate distribution by age at enrolment group.*

![figure](assets/figures/fig020.png)

The Chi-Square test of independence in table 4.9 shows the association between Age Group and At-Risk status. The uncorrected analysis yielded a statistically significant result (${\chi }^{2}=8.1821$, $p=0.0424$), with a small-to-moderate effect size (Cramer's V = 0.1575). Visually, this aligns with earlier descriptive findings where students aged 18 or younger exhibited a markedly lower at-risk rate. However, after applying a multiple-testing correction to account for the number of variables analyzed, the p-value increased to 0.5087. Consequently, while there is a suggestive trend indicating that younger enrollment age may be protective, the relationship does not maintain strict statistical significance when adjusted for multiple comparisons. All test assumptions were met.

*Table 4.9: Test statistics between Age group (age at enrolment) and At-Risk status.*

| Feature | Age Group |
|---|---|
| Type | Categorical |
| Test | Chi-Square |
| Statistic | 8.1821 |
| p-value (Raw) | 0.0424 |
| p-value (Corrected) | 0.5087 |
| Effect Size (Cramér's V) | 0.1575 |
| Expected count < 5 (cells) | 0 |
| Significant (α = 0.05) | False |

## Subject Analysis

Figure 4.21 illustrates the percentages of students failing specific subjects/subjects from 2022 to 2025. The year 2022 shows widespread, elevated failure rates across almost all subjects compared to later years. The subject Theory of Structures has the highest failure rate across all four years with 20.8% (2022), 32.2% (2023), 26.0% (2024), and 15.6% (2025). Theory of Structures improved significantly in 2025; however, it remains with the highest failure rate that year, joint with Surveying (15.6%). Subjects such as Applied Mechanics, and Professional and Technical Communication dropped from 11.3, and 7.5% respectively in 2022 to 0.0% in the subsequent three years. Computer skills significantly improved from 18.9% in 2022 to just 1.1% in 2025, while also reaching 0.0% in 2024. Construction Material Technology consistently remained low, with its highest being 2.2% in 2025. Engineering Mathematics fluctuates, as it records a 13.2% in 2022, 0.0% in 2023, then up to 18.0% in 2024, down again to 12.2 in 2025. Surveying spiked in 2025 (15.6%) after being relatively low in previous years (11.3% in 2022, 4.6% in 2023, 11.0% in 2024). Engineering Physics had its worst year in 2022 with 18,9%. It has gone down to 2.2% in 2025. Overall, there is a general trend of improvement in failure rates from 2022 to 2025.

*Figure 4.21: Subject failure rate (%) by Academic Year*

![figure](assets/figures/fig021.png)

Table 4.10 below shows the number of failures per subject and the failure rate across the 4-year period (2022 to 2025). Theory of structures had the greatest number of students failing with 79 (23.94% of the 330 students) students failing the subject. The subsequent subjects had the most failures, just below Theory of structures, with Engineering Mathematics 1(36), Surveying (35), Engineering Drawing 1 (35) having about 10.91%, 10.61%, and 10.61% respectively. The rest of the subjects had a failure rate of less than 10%, with Computer Skills (5.15%), Engineering Physics (3.94%0, Engineering Chemistry (3.33%), Applied Mechanics (1.84%), and Construction Material (1.52%). Professional and Technical Communication had the least number of students failing, with only 4 of the 330 students failing the subject, revealing that students tend to find non-technical subject easy.

*Table 4.10: Subject failure rate and the number of failures per subject.*

| Subject | Number of Failures | Failure Rate (%) | Pass Rate (%) | 95% CI Lower (%) | 95% CI Upper (%) |
|---|---|---|---|---|---|
| Theory of Structures | 79 | 23.94 | 76.06 | 19.34 | 28.54 |
| Engineering Mathematics 1 | 36 | 10.91 | 89.09 | 7.55 | 14.27 |
| Surveying | 35 | 10.61 | 89.39 | 7.28 | 13.93 |
| Engineering Drawing 1 | 35 | 10.61 | 89.39 | 7.28 | 13.93 |
| Computer Skills | 17 | 5.15 | 94.85 | 2.77 | 7.54 |
| Engineering Physics | 13 | 3.94 | 96.06 | 1.84 | 6.04 |
| Engineering Chemistry | 11 | 3.33 | 96.67 | 1.40 | 5.27 |
| Applied Mechanics | 6 | 1.82 | 98.18 | 0.38 | 3.26 |
| Construction Materials | 5 | 1.52 | 98.48 | 0.20 | 2.83 |
| Professional Communication | 4 | 1.21 | 98.79 | 0.03 | 2.39 |

Table 4.11 below demonstrates the number and proportion of students who failed subjects among the student cohort, categorized by the number of subjects failed (1 through 10). About 69 (57.02% of at-risk students) students failed one subject, representing 20.91% of the entire cohort. This indicates that most at-risk students were experiencing a relatively limited academic setback rather than widespread failure across multiple subjects. About 22 students (18.18%) failed two subjects, while 13 students (10.74%) failed three subjects. Together, students who failed one to three subjects accounted for 85.94% of all at-risk students, suggesting that academic risk was generally concentrated among students with a small number of failed subjects. Only 8 students (6.61%) failed four subjects, 5 students (4.13%) failed five subjects, and just 4 students (3.32%) failed six, seven, nine, or ten subjects combined. No student failed exactly eight subjects.

*Table 4.11: Frequency and Percentage Distribution of Students by Number of Subjects Failed*

| Number of Subjects Failed | Number of Students | Percentage of All Students (%) | Percentage of At-Risk Students (%) |
|---|---|---|---|
| 1 | 69 | 20.91 | 57.02 |
| 2 | 22 | 6.67 | 18.18 |
| 3 | 13 | 3.94 | 10.74 |
| 4 | 8 | 2.42 | 6.61 |
| 5 | 5 | 1.52 | 4.13 |
| 6 | 1 | 0.30 | 0.83 |
| 7 | 1 | 0.30 | 0.83 |
| 8 | 0 | 0.00 | 0.00 |
| 9 | 1 | 0.30 | 0.83 |
| 10 | 1 | 0.30 | 0.83 |

Table 4.12 presents the distribution of student performance across the ten first-year subjects, including the number of students who scored below 50%, the number who achieved marks between 50% and 59%, and the average and median marks for each subject. The results indicate that Theory of Structures was the most challenging subject in the programme. It recorded the highest number of failures, with 79 students obtaining below 50%, and achieved the lowest average mark (56.21%) and lowest median mark (56.0%) among all subjects. In addition, a further 122 students obtained marks between 50% and 59%, indicating that a large proportion of students performed at a borderline level. These findings suggest that Theory of Structures represents a major academic hurdle for first-year (First Time Entering) Civil Engineering students. The next highest failure rates were observed in Engineering Mathematics 1 (36 failures), Engineering Drawing 1 (35 failures), and Surveying (35 failures). These subjects also recorded relatively low average marks, ranging from 61.23% to 62.56%, highlighting their importance as key areas of academic difficulty. The concentration of failures in these technical subjects suggests that weaknesses in quantitative and engineering-related competencies may contribute substantially to academic risk within the programme.

Engineering Physics shows that a low failure count can hide widespread difficulty. Only 13 students failed it, yet it had the second-lowest mean (58.13%) and median (58.0%) mark, and 184 students (the most of any subject) scored between 50% and 59%, so many students passed only narrowly. By contrast, Professional and Technical Communication performed best (mean 74.89%, median 76.0%, 4 failures), and Computer Skills also had a high mean (70.29%) and median (71.0%) despite 17 failures. Overall, the highest failure rates and lowest marks were concentrated in the technical subjects (Theory of Structures, Engineering Mathematics 1, Engineering Drawing 1, Surveying and Engineering Physics), which supports targeted tutoring and supplementary support in these subjects.

*Table 4.12: Mark grouping distribution*

| Subject | Students < 50% | Students 50%–59% | Average Mark | Median Mark |
|---|---|---|---|---|
| Applied Mechanics | 6 | 107 | 65.72 | 65.0 |
| Computer Skills | 17 | 28 | 70.29 | 71.0 |
| Construction Materials | 5 | 72 | 66.18 | 66.0 |
| Engineering Chemistry | 11 | 48 | 67.10 | 68.0 |
| Engineering Drawing 1 | 35 | 111 | 61.28 | 61.0 |
| Engineering Mathematics 1 | 36 | 109 | 61.23 | 62.0 |
| Engineering Physics | 13 | 184 | 58.13 | 58.0 |
| Professional Communication | 4 | 19 | 74.89 | 76.0 |
| Surveying | 35 | 97 | 62.56 | 63.0 |
| Theory of Structures | 79 | 122 | 56.21 | 56.0 |

The heatmap in figure 4.22 shows the subject co-failure rate (%) between different subjects. Computer Skills and Professional and Technical Communication have a 100% co-failure rate, showing that students who failed Professional and Technical Communication also failed Computer skills. Critically looking at table 4.10, there were 4 students who failed Professional and Technical Communication, while there were 17 students who failed computer skills, it can be concluded from this that all 4 of the students who failed Professional and Technical Communication also failed computer skills. Engineering Drawing 1 and Professional and Technical Communication show the second highest co-failure rate at 75%, followed by Engineering Drawing and Surveying (51%), Engineering Chemistry and Professional and Technical Communication (50%), Applied Mechanics and Professional and Technical Communication (50%), Engineering Physics and Professional and Technical Communication (50%). This shows that failing Professional and Technical Communication almost certainly means you are going to fail most of the subjects. Professional and Technical Communication and Theory of Structures (3%) have the least co-failure rate, showing that a student can fail Theory of Structure but still be likely to pass Professional and Technical Communication.

*Figure 4.22: Subject co-failure rate (%)*

![figure](assets/figures/fig022.png)

Figure 4.23 shows the average subject per subject. Professional and Technical Communication has the highest average with just above 70% average, followed by Computer skills with just below 70%. Subjects like Engineering Chemistry, Construction Material Technology, and Applied Mechanics cluster around the mid-60s, reflecting moderate achievement and balanced difficulty. Theory of Structure has the lowest average mark, approximately 56-57%, followed by Engineering Physics with approximately 58%. Surveying, Engineering Drawing 1, and Engineering Mathematics 1 hover between 61-64%, implying steady but challenging technical engagement.

*Figure 4.23: Average mark per subject*

![figure](assets/figures/fig023.png)

The results under Subject analysis reveal that non-technical subjects contribute slightly to students being at-risk, while technical subjects contribute significantly.

## Predictive Model Results

This section presents the results obtained from the predictive modelling analysis performed to identify First Time Entering first-year students who may be at risk of poor academic performance or failing in the Diploma in Civil Engineering in CPUT. The modelling was based on the defined At-Risk Status outcome, where a student was classified as at risk if they obtained a mark below 50% in at least one of their registered subjects. This result served as a substitute indicator of possible academic challenges and was selected to support the identification of students who may require timely academic interventions.

Two classification methods were evaluated, namely Logistic Regression and Random Forest for the predictive power and interpretability. Model performance was assessed using Accuracy, Precision, Recall, F1-score, and the Receiver Operating Characteristic Area Under the Curve (ROC-AUC).

### Logistic Regression Results

This section outlines the logistic regression results, inclusive of analysis of its coefficients, feature ranking in relation to at-risk and model performance results.

Table 4.13 compares the classification performance of the logistic regression model across three scenarios (a baseline using Feature Set A (without marks), Feature Set B (with marks), and a hyperparameter-tuned model using Feature Set B). Model performance was evaluated using accuracy, precision, recall, F1-Score, and the area under the receiver operating characteristic curve (ROC-AUC). In addition, 95% confidence intervals (CIs) for the ROC-AUC values are reported to assess the reliability of the model's discriminatory ability.

*Table 4.13: Logistic regression summary.*

| Scenario | Accuracy | Precision | Recall | F1-Score | ROC-AUC | AUC 95% CI low | AUC 95% CI high | Best Parameters |
|---|---|---|---|---|---|---|---|---|
| Without Marks (Set A) | 0.59596 | 0.454545 | 0.555556 | 0.5 | 0.571869 | 0.45338 | 0.694724 | – |
| With Marks (Set B) | 0.858586 | 0.823529 | 0.777778 | 0.8 | 0.932099 | 0.878123 | 0.973948 | – |
| Tuned With Marks (Set B) | 0.808081 | 0.72973 | 0.75 | 0.739726 | 0.914903 | 0.856812 | 0.961538 | C = 0.1; solver = liblinear |

The model without marks performed marginally better than chance, with an accuracy of 59.60% and a ROC-AUC of 57.19%. It achieved a confidence interval (CI) for the ROC-AUC of 0.453 to 0.695. Since this interval include 0.50, the model's ability to distinguish between at-risk and not-at-risk students is not statistically different from chance. Precision (0.455) indicates that fewer than half of the students flagged as at risk were truly at risk. Similarly, the recall value of 0.556 indicates that a substantial proportion of genuinely at-risk students were not detected by the model. The resulting F1-score of 0.500 reflects this weak balance between the two.

The model that included final assessment marks performed significant better across all the metrics compared to the model without marks, with an accuracy of 85.86%, precision of 82.35%, recall of 77.78%, F1-Score of 80% and an ROC-AUC of 93.21% with a confidence interval of 0.8781 to 0.9739. The ROC-AUC confidence interval was not inclusive of 0.50, indicating that the model's ability to discriminate between at-risk and not-at-risk students was statistically significantly better than chance. The model also identified most at-risk students (recall of 0.778) while keeping false alarms relatively low (precision of 0.824).

The hyperparameter tuning (on model with final assessment marks) selected an inverse regularization strength of C = 0.1 and the liblinear solver. The tuned model achieved an accuracy of 0.808, precision of 0.730, recall of 0.750, F1-score of 0.740, and ROC-AUC of 0.915 (95% CI: 0.857 to 0.962). These values are slightly lower than those of the untuned model with marks. However, the ROC-AUC confidence intervals overlap almost entirely, so the two models cannot be said to differ meaningfully in discriminatory ability. The "Best Params" entry is not applicable (NaN) for the first two scenarios because they used default hyperparameters and no search was performed.

#### Logistic Regression Odds Ratio

Figure 4.24 below shows the odds ratios, with 95% bootstrap confidence intervals, from the logistic regression model fitted with marks. Odds ratio below 1 indicates that the predictor is associated with lower odds of a student being classified as at risk, whereas an odds ratio above 1 indicates higher odds of being classified as at risk. Higher performance in Theory of Structures was associated with substantially lower odds of being classified as at risk, making it the strongest protective factor (OR ≈ 0.09). Computer Skills and Surveying also demonstrated protective effects (OR ≈ 0.40), with confidence intervals entirely below 1, indicating statistically reliable associations. However, prior labour force experience was associated with increased odds of being classified as at risk (OR ≈ 2.3), although its confidence interval was close to and bordered the null value of 1. Most home-language indicators had confidence intervals that included 1, suggesting that they were not significantly associated with academic risk once assessment performance was accounted for in the model.

*Figure 4.24: Logistic Regression Odds ratio.*

![figure](assets/figures/fig024.png)

#### Logistic Regression Confusion Matrix

*Figure 4.25 presents the confusion matrix for the logistic regression model (with marks) on the test set (n=99). The model correctly classified 57 (True Negative) of 63 students who were not at-risk and 28 (True Positive) of 36 students who were at-risk. However, 6 students who were not at risk were incorrectly classified as at risk (false positives), while 8 at-risk students were incorrectly classified as not at risk (false negatives).*

*Figure 4.25: Logistic Regression confusion matrix.*

![figure](assets/figures/fig025.png)

### Random Forest Results

This section evaluates its ability to identify at-risk students under the same three scenarios used for logistic regression, so that the two algorithms can be compared directly.

Table 4.14 presents the Random Forest classifier performance across the three modelling scenarios (Set A: Without Marks, Set B: With Marks, and Tuned with Marks). Model performance was evaluated using accuracy, precision, recall, F1-score, and the area under the receiver operating characteristic curve (ROC-AUC). Additionally, 95% confidence intervals (CIs) were calculated for the ROC-AUC to assess the precision and reliability of the model's discriminative performance.

*Table 4.14:  Random Forest Summary*

| Scenario | Accuracy | Precision | Recall | F1-Score | ROC-AUC | AUC 95% CI low | AUC 95% CI high | Best Parameters |
|---|---|---|---|---|---|---|---|---|
| Without Marks (Set A) | 0.535354 | 0.380952 | 0.444444 | 0.410256 | 0.497354 | 0.376137 | 0.618985 | – |
| With Marks (Set B) | 0.868687 | 0.848485 | 0.777778 | 0.811594 | 0.940476 | 0.895037 | 0.977388 | – |
| Tuned With Marks (Set B) | 0.868687 | 0.870968 | 0.75 | 0.80597 | 0.93739 | 0.886877 | 0.976608 | max_depth = 8; … |

The model without marks performed poorly on all metrics, with a/an accuracy (53.53%), Precision (38.10%), recall (44.44%), F1-score (41.03%), and ROC-AUC (0.4974) with a confidence interval of 0.3761 to 0.6190. The confidence interval includes 0.50 indicating that the model's ability to distinguish between at-risk and not-at-risk students is not statistically different from chance.

The inclusion of assessment marks (Set B) substantially improved performance (accuracy = 0.869; precision = 0.848; recall = 0.778; F1-score = 0.812; ROC-AUC = 0.940, 95% CI: 0.895-0.977). The ROC-AUC confidence interval did not include 0.50, suggesting that the model's ability to discriminate between at-risk and not-at-risk students was statistically significantly better than chance. The model identified 77.78% of at-risk students while keeping false alarms relatively low with a precision of 84.85%.

The hyperparameter tuning (maximum depth = 8) yielded comparable discrimination (ROC-AUC = 0.937) and identical accuracy but altered the precision-recall trade-off by increasing precision to 0.871 while reducing recall to 0.750.

#### Random Forest Impurity Importance

Figure 4.26 presents the top 15 predictors ranked by Random Forest impurity-based importance for the model with marks. Performance in Theory of Structures was by far the most influential variable (importance = 0.259), contributing more than twice as much as any other predictor. Applied Mechanics (0.109), Engineering Mathematics 1 (0.108), and Surveying (0.093) were the next most influential predictors. Engineering Drawing 1, Engineering Physics, Engineering Chemistry, and Computer Skills also demonstrated meaningful contributions, with importance scores between 0.062 and 0.076. Together, module marks accounted for approximately 91% of the total importance, whereas demographic and background variables, including age at enrolment, home language, residence status and previous activity, each contributed less than 0.015. These findings suggest that academic performance was the dominant predictor of student risk in this dataset, substantially outweighing the contribution of demographic and background characteristics.

Figure .: Random Forest impurity importance

![figure](assets/figures/fig026.png)

#### Random Forest Confusion Matrix

Figure 4.27 presents the confusion matrix for the Random Forest model with assessment marks on the test set (n = 99). The model achieved correct classification for 58 of 63 not-at-risk students (true negatives) and 28 of 36 at-risk students (true positives). Only 5 students were incorrectly identified as at risk (false positives), while 8 at-risk students were incorrectly classified as not at risk (false negatives). These results indicate that the model was highly effective in distinguishing between at-risk and not-at-risk students, with relatively few classification errors. The lower number of false positives compared to false negatives suggests that the model was slightly more conservative when assigning students to the at-risk category.

Figure .: Random Forest confusion matrix

![figure](assets/figures/fig027.png)

## Model Comparison

The area under the ROC curve (AUC) represents the probability that a randomly chosen at-risk student is assigned a higher predicted risk than a randomly chosen student who is not at risk. This makes it a strong measure of how effectively the model distinguishes between classes.

The ROC curve shows the balance between sensitivity (true positive rate) and specificity (false positive rate). AUC illustrates the trade-off between correctly identifying at-risk students and incorrectly flagging those who are not at risk. The AUC summarizes the trade-off between sensitivity and specificity into a single metric, enabling straightforward comparison of model performance. The diagonal dashed line represents the chance baseline (AUC = 0.50), where classification performance is equivalent to random guessing.

Figure 4.28 shows that both models' ROC curves lie well above the chance line (AUC = 0.50), indicating strong discriminatory ability in distinguishing between at-risk and not-at-risk students. The Random Forest model (orange curve, AUC = 0.94) achieved a marginally higher AUC than the logistic regression model (blue curve, AUC = 0.93), suggesting a slight overall advantage in classification performance. The Random Forest model exhibited higher true positive rates at low false positive rates (below approximately 0.10) and at higher false positive rates (above approximately 0.35), whereas the logistic regression model performed slightly better in the intermediate range (approximately 0.15 to 0.30). Despite these differences, the substantial overlap between the two curves indicates that both models demonstrated comparable predictive performance, with Random Forest providing only a marginal improvement in overall discrimination.

![figure](assets/figures/fig028.png)

*Figure 4.28: Roc Curve- Logistic Regression vs. Random Forest.*

Figure 4.29 shows permutation importance on the test set for both the logistic regression and random forest models, with marks and without marks, measured as the reduction in ROC-AUC when each predictor is randomly shuffled. Theory of Structures was the most influential predictor in both models, reducing the ROC-AUC by approximately 0.20 in the logistic regression model and 0.14 in the Random Forest model when permuted. A second tier of technical modules, including Surveying, Engineering Mathematics 1, Engineering Chemistry and Engineering Drawing 1, contributed reductions of roughly 0.01 to 0.04, whereas demographic and background variables such as age at enrolment, previous activity, matric type and gender contributed negligibly, with several intervals including zero. These findings are consistent with the odds ratio estimates from logistic regression and the impurity-based importance measures from Random Forest, both of which indicate that performance in core engineering modules is the primary determinant of student risk classification. Applied Mechanics ranked highly in impurity importance but was not influential under permutation importance, a discrepancy suggesting that impurity measures overstated its contribution, possibly because of correlation among subject marks.

*Figure 4.29: Comparison of feature importance for Logistic Regression and Random Forest*

![figure](assets/figures/fig029.png)

Figure 4.30 shows comparison between the test set recall of the logistic regression and Random Forest models, with and without the final assessment marks. Recall is a critical metric in this context, as it reflects the proportion of genuinely at-risk students who are correctly identified, and failure to detect such students means that no support is provided. Without final assessment marks (Set A), recall was 55.6% for logistic regression (20 of 36 at-risk students) and 44.4% for Random Forest (16 of 36). Given that both models also yielded ROC-AUC values close to 0.50, these figures are consistent with near-random classification and do not indicate meaningful detection capability.

The inclusion of final assessment marks (Set B) substantially improved recall, with both models correctly identifying 28 of the 36 at-risk students, corresponding to a recall of 77.8%. This represents an increase of 22.2 percentage points for logistic regression and 33.3 percentage points for Random Forest. The two algorithms therefore performed identically with respect to recall when marks were available. Nevertheless, approximately 22% of at-risk students (8 students) remained undetected in both models, which represents the principal limitation for early-intervention purposes, as students who are not identified as at risk would not be targeted for additional support.

*Figure 4.30: Recall for Logistic Regression and Random Forest.*

![figure](assets/figures/fig030.png)

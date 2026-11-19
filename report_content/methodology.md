## Data Source

The data was acquired from CPUT through the Fundani CHED department for the purpose of developing dashboards. Approval was granted to use the same data for this study in accordance with the POPIA Act. From the data provided, this study will focus solely on first year students enrolled in the Diploma in Civil Engineering. The data comprises of Registration data, Residence data, financial data and Academic Records data. From all the datasets, only the academic year 2022 to 2025 will be considered for the purpose of this study.

A target variable column (At-Risk Status) was created, where if a student failed at least one subject/subject, then that student was classified as an “At-Risk Student”, while a student who passes all their subjects/ subjects was classified as “Not At-Risk Student”. To be specific, under the At-Risk Status column, there will be a “Yes/No” response, “Yes” meaning the student is at-risk, while “No” will mean the student is not at-risk. These will be furthermore encoded, so that the target variable for predictive modelling is binary, making the study a binary classification problem. This means that “Yes” will be encoded to be 1, and “No” will be encoded as 0.

$$
\text{AtRisk}=\begin{cases}1,   \text{if the student failed at least one first-year module} \\ 0,  \text{if the student passed all first year modules}              \end{cases}
$$

## Data Description

This section offers a summary of the dataset utilized in the project, detailing format, main variables, and features to create a comprehensive grasp of the data being examined.

*Table 3.1: Data Description.*

| Variable Name | Type | Definition |
|---|---|---|
| Academic Year | Categorical | Year from 2022 to 2025. |
| Applied Mechanics | Numeric (Float) | Shows students’ subject final marks. |
| Computer Skills | Numeric (Float) | Shows students’ subject final marks. |
| Construction Material Technology | Numeric (Float) | Shows students’ subject final marks. |
| Engineering Chemistry | Numeric (Float) | Shows students’ subject final marks. |
| Engineering Drawing 1 | Numeric (Float) | Shows students’ subject final marks. |
| Engineering Mathematics 1 | Numeric (Float) | Shows students’ subject final marks. |
| Engineering Physics | Numeric (Float) | Shows students’ subject final marks. |
| Professional and Technical Communication | Numeric (Float) | Shows students’ subject final marks. |
| Surveying | Numeric (Float) | Shows students’ subject final marks. |
| Theory of Structures | Numeric (Float) | Shows students’ subject final marks. |
| Bursary Type | Categorical | Shows type of bursary student has, i.e. NSFAS, Private Bursary, Self-Funded |
| Funded | Categorical | Shows whether a student is funded or not funded (Yes/No). Regards Self-Funded students as No for being funded, NSFAS and Private Bursary as Yes for being Funded. |
| Matric Type | Categorical | Tell us what type of matric the student did (i.e., 'NSC - ADMISSION TO BACHELOR', 'NSC - ADMISSION TO DIPLOMA', etc.) |
| Previous Activity | Categorical | Tell us what the student was doing before being enrolled in the institution (i.e., GRADE12 LEARNER', 'UNEMPLOYED', 'LABOUR FORCE’, UNIVERSITY STUDENT’, OTHER', etc.) |
| Language Name | Categorical | Tell us the home language of the student (i.e., English, IsiXhosa, IsiZulu, IsiNdebele, etc.) |
| Ethnic Group | Categorical | Tell us the ethnic group that the student belongs in (i.e., African, Indian, White, etc.) |
| Gender | Categorical | Tell us whether the student is a Male/ Female/ Unknown (i.e., F, M, U) |
| Secondary School Quintile | Numeric (Integer) | Tell us the quintile of the secondary school to which the student was studying at |
| Age At Enrolment | Numeric (Integer) | Tell us about the age at which the student registered (i.e., 17, 21, 45, etc.) |
| At Risk Status | Categorical | Tells whether a student is at risk of minimum completion or is not at risk (Yes/No) |
| Residence Status | Categorical | Tells whether a student has residence allocated or not (Yes/No) |

## Data Preparation

Data preparation was done to ensure the accuracy and reliability of the research findings. Data Preprocessing was performed in Visual Studio Code using Python libraries such as Pandas, NumPy and Scikit-learn. This enabled improved data quality and ensured that the dataset was suitable for predictive modelling.

### Data Cleaning and Integration

Since the Diploma in Civil Engineering is a full-time, non-ECP program, all First Time Entering students are expected to be registered for the complete set of ten first-year subjects. Therefore, to ensure the integrity of the subject difficulty analysis and the at-risk classification, only students with a complete record of all subject marks were retained in the final dataset. Cases with missing subject records were excluded as they represent registration anomalies rather than genuine academic performance gaps.

The datasets were obtained in excel/csv files. The first set of data cleaning was done using excel. This included renaming columns for consistence with the other dataset. Qualification names were filtered to leave only the required qualification (Diploma in Civil Engineering). The dataset was further filtered by period of study and Ften status to ensure that only First Time Entering, first year students remained. Redundant and irrelevant columns such as bursary names and residence names were deleted/dropped. However, both funding columns, Funded and Funding Type were retained, to use for exploratory data analysis for evaluation of the most used bursary type by students.

Further data cleaning and integration was performed using Python (Visual Studio Code). This included the checking and dropping of duplicates. Further consistent renaming which included stripping of spaces in some columns. Data types were checked along with variable names to ensure consistency across all datasets. Student numbers were turned to student id using hashing to protect student identity and privacy. Student identifiers were dropped to protect student privacy and abide by POPIA Act. The datasets were then merged into a single dataset using student id and academic years. After the merge, subject records were pivoted into columns to enable measuring of their effects.

Missing values were identified, where only student records with complete subject performance results were retained based on the institutional expectation that all First Time Entering First Year students should be taking all their prescribed subjects within their curriculum. Categorically variables were imputed mode, specifically secondary school quintile. There were no numerical missing values.

Outliers were examined to assess the presence of anomalies within the dataset. Outlier on subject performance records were retained, as they were considered to represent outstanding academic performance rather than data entry errors, inaccuracies, or data leakage. Furthermore, no outliers were detected in the remaining variables included in the analysis.

Feature such as At-Risk Status, Residence Status, etc, were encoded into numerical values using label encoding, mapping each binary category to 0/1 (e.g., 'Yes' = 1, 'No' = 0), which introduces no artificial ordering for two-category variables.

Only minimal data preparation was undertaken prior to model development. This included standardising labels, removing the student identification variable, excluding records with missing subject marks, and constructing the binary outcome variable (1 = at risk; 0 = not at risk). All preprocessing steps, including imputation, scaling, and encoding, were incorporated within the modelling pipelines and fitted exclusively on the training data, as well as on the training partition of each cross-validation fold. This approach prevented information leakage from validation or test samples during preprocessing. Numerical variables, comprising age at enrolment and the ten subject marks, were imputed using the median and subsequently standardised. Categorical variables, including binary indicators, school quintile, and matric type, were imputed using the most frequent category and then one-hot encoded. Categories not encountered during training were ignored during prediction.

## Data Analysis

Data analysis was employed to produce meaningful insight that address the study’s objectives. The analysis focuses on identifying patterns, correlations, and predictors of academic risk among first year students.

### Descriptive Statistics

Descriptive statistics were used to summarize and describe the underlying issues or patterns. This gave an overview of the variables and assisted in identifying patterns and inconsistencies within the data. Python libraries such as Pandas, NumPy, and Matplotlib were utilized to generate descriptive statistics.

### Exploratory Data Analysis

Exploratory data analysis was performed to explore relationships, trends and patterns within the dataset. This provided insight into the data, identified influential variables, detected anomalies, and supported feature selection for the development of predictive modelling. Python libraries including Pandas, Matplotlib, and Seaborn were used to perform the analysis. This provided a baseline understanding before applying advanced predictive models.

#### Statistical Tests for the Exploratory Analysis

Associations between each categorical predictor and at-risk status were tested with chi-square tests of independence, and the continuous variable (age at enrolment) with the Mann–Whitney U test, at a 5% significance level. Effect sizes were measured with Cramér’s V for the chi-square tests and the rank-biserial correlation for the Mann–Whitney U test. The chi-square assumption that expected cell counts be at least five was checked for each test, and violations were noted. To control for the number of tests, the 12 raw p-values were adjusted for multiple comparisons using the Holm–Bonferroni method, and significance was judged on the adjusted values.

## Model Development and Evaluation

### Dataset and Train-Test Split

The final modelling dataset comprised 330 student records across 20 variables, including 10 subject’s results (academic performance results), Age at Enrolment, and 9 categorical features (Gender, Language Name, Ethnic Group Name, Previous Activity Description, Matric Type, Bursary Type, Funding Status, Residence Status, and Secondary School Quintile). The target variable, At-Risk Status, was moderately imbalanced, with 209 students (63.3%) classified as Not At-Risk and 121 students (36.7%) classified as At-Risk.

*The dataset was partitioned once into a training set (n = 231, 70%) and a test set (n = 99, 30%) using stratified sampling based on the target variable, with a fixed random seed of 42 to ensure reproducibility. This identical train-test split was applied to both feature sets, enabling a fair comparison by evaluating model performance on the same group of students. Furthermore, the test set was reserved exclusively for final model evaluation and was not involved in any stage of model selection, hyperparameter tuning, or training.*

*Table 3.2:Train-test split summary*

| Dataset | Students | At risk | At-risk rate (%) |
|---|---|---|---|
| Train (70%) | 231 | 85 | 36.8 |
| Test (30%) | 99 | 36 | 36.4 |

### Models and Class Imbalance

Three classifiers were fitted for each feature set. A majority-class baseline predicted the more frequent class for every student and provided a reference for accuracy. Logistic Regression used the scikit-learn defaults (L2 regularisation, C = 1) with balanced class weights and a maximum of 1,000 iterations. The Random Forest used 300 trees with a minimum of three observations per leaf and balanced class weights. Because the target was moderately imbalanced (63.3% not at risk, 36.7% at risk), class weighting and stratified splits and folds were used, and the test set was left unmodified.

### Feature Sets A and B

Two feature sets were defined so that the contribution of assessment results could be isolated. Feature Set A (without marks) contained the ten variables known at registration: gender, home language, ethnic group, previous activity, matric type, age at enrolment, bursary type, funding status, residence status and secondary school quintile. Feature Set B (with marks) contained Set A plus the final marks for the ten first-year subjects, giving 20 predictors. Academic year was excluded from both sets because a new cohort carries a year value the model has never seen, so it cannot generalise from it, and student identifiers were removed to protect privacy. Because the at-risk outcome is defined directly from the subject marks (a mark below 50% in at least one subject), Set B can only recover the rule that generates the label, whereas Set A is the only feature set that represents a genuine early-warning scenario.

## Cross-Validation

Cross-validation was performed on the training set only, using repeated stratified 10-fold cross-validation with three repeats (30 validation scores per model). Accuracy, precision, recall, F1-score and ROC-AUC were calculated for each fold, and the mean and, for ROC-AUC, the standard deviation across folds. The cross-validated estimates are more stable than the single test-set estimates, because the test set contains only 99 students, and they were used to compare the models and to assess stability, not to tune against the test set.

## Hyperparameter Tuning

Hyperparameters were tuned separately for each feature set using an exhaustive grid search on the training set only, with ROC-AUC as the scoring metric and stratified 3-fold cross-validation (shuffled, seed 42). For Logistic Regression the grid covered the inverse regularisation strength C (0.1, 1 and 10) with the liblinear solver. For the Random Forest the grid covered maximum depth (5, 8 and unlimited), minimum samples to split a node (2 and 5) and number of trees (100 and 200). The best configuration was refitted on the full training set and evaluated once on the test set. The report presents the tuned models for Feature Set B only, because the models without marks performed at chance level.

## Models

### Logistic Regression

Logistic Regression model is a statistical method used to model the relationship between a dependent variable and one or more independent variables (Tchamga, 2025:1). The study employed logistic regression because it provides easily interpretable coefficients while modeling relationship between predictor variables and the target variable. The coefficients show the direction and strength of the relationship between each predictor and the probability of being at-risk, while keeping all other variables constant. A positive coefficient indicates a higher likelihood of being at-risk, whereas a negative coefficient indicates a lower likelihood of being at-risk.

Logistic Regression Equation:

$$
P\left(Y=1 | X\right)=\frac{1}{{1+e}^{-({\beta }_{0}+{\beta }_{1}{X}_{1}+{\beta }_{ 2}{X}_{2}+\dots +{\beta }_{k}{X}_{k})}}
$$

Parameters Explained:

- $Y$: The dependent variable (At-Risk Status)
- $P\left(Y=1 | X\right)$: The probability that the outcome is equal to 1 (success), given the predictor.
- ${\beta }_{0}$: The intercept (constant term) – represents the baseline log-odds of success when all predictors ${X}_{i}$ are zero.
- ${\beta }_{1}, {\beta }_{2},\dots , {\beta }_{k}$: Are coefficients of the predictors.
- ${X}_{1}, {X}_{2},\dots , {X}_{k}$: Independent (predictor) variables.
- $e$: The base of the natural logarithm (~2.718), ensuring an S-shaped curve (sigmoid).
### Random Forest Model

Random Forest was used as a classification model to identify students at-risk based on all available academic and background features (including the identified socio-economic, financial, and residence-related factors). It was specifically used to analyze and predict student’s at-risk trends in the Diploma in Civil Engineering program at CPUT. This model ensembles many decision trees, each trained on a random subset of data and predictors. Decision Tree is a non-parametric supervised learning method that can be used for classification and regression (Tchamga, 2025).

Utilizing Random Forest, the final prediction is made by aggregating the results of these trees, whilst reducing overfitting and improving accuracy. Random forests construct each tree in the forest using distinct training data and incorporate randomization during the tree-building process. In a regression problem, the predictions from each tree are averaged, while in a classification problem, they vote on a class, resulting in the predicted value for the dependent variable (McClarren et al., 2021).

In classification tree, the splitting rule determines how the algorithm selects the best predictors variables and threshold to divide a node into 2 child nodes so that the resulting groups are as pure (homogeneous) as possible. They use Gini Impurity to quantify how pure or mixed the classes are within a node. “It measures the probability that a randomly selected observation from the node would be incorrectly classified if it were randomly labelled according to the class distribution in that node” (Eldud, 2026:17).

Gini Impurity Function:

$$
\text{Gini}=1-\sum_{k=I}^{K} {{p}_{k}^{2}}
$$

$$
\text{Gini} \left(\text{Parent}\right)=I\left(\text{Parent}\right)=1-\sum_{k=I}^{K} {{p}_{k}^{2}}
$$

Where:

- ${p}_{k}$= Proportion of class k in the node
- K = Number of classes
Splitting rule for classification tree:

$$
\text{min}(\frac{{n}_{l}}{n}I\left(L\right)+\frac{{n}_{R}}{n}I\left(R\right)
$$

Where:

- $I\left(L\right)$= impurities on the left nodes
- $I\left(R\right)$= impurities on the right nodes
- ${n}_{l}=$number of observations in the left child node
- ${n}_{R}$= number of observations in the right node
- $n$= total observations in parent node
## Evaluation and Confidence Intervals

Each model was fitted on the full training set and evaluated once on the test set using accuracy, precision, recall, F1-score and ROC-AUC, with the at-risk class treated as the positive class and a classification threshold of 0.5. A 95% confidence interval for the ROC-AUC was obtained by resampling the test students 1,000 times with replacement and taking the 2.5th and 97.5th percentiles of the resampled AUC values. These intervals reflect variability due to the small test set; they do not reflect variability in model training.

Recall received emphasis, as the study aimed to correctly identify students who are at risk. A model with high recall will be considered more useful because this will mean that the number of at-risk students who are incorrectly classified will be at minimum.

The at-risk status variable was defined such that a student was classified as at risk if they failed at least one first-year subject. Thus, the performance variables of the subject are anticipated to significantly impact the prediction of at-risk status, as they serve as the foundation for creating the target variable.

A Random Forest model was fitted to the pre-processed training data to evaluate the relative importance of the predictors in each feature set (20 predictors in Feature Set B). Logistic Regression was also employed as a classification model, providing interpretable coefficients that describe the direction and magnitude of the relationship between the predictors and the log-odds of the outcome. No feature selection was performed, all predictors in each feature set were retained, and the importance measures were used only to interpret the fitted models.

## Model Interpretation Methods

Three complementary approaches were used. First, Logistic Regression odds ratios were obtained by exponentiating the coefficients of the model fitted on the training set, with 95% intervals from 500 bootstrap resamples of the training set (percentile method). Because numeric predictors were standardized, the odds ratio for a subject mark is expressed per one standard deviation increase in that mark. Categorical predictors were one-hot encoded without a dropped reference category, and the coefficients were L2-regularised, so their odds ratios describe each category relative to the model's overall baseline and are shrunk towards one, not compared with a single reference group. Second, Random Forest impurity importance (mean decrease in Gini impurity) was taken from the fitted forest on the training data, with importance for a categorical variable divided across its one-hot columns. Third, permutation importance was computed on the unseen test set for both models, as the mean drop in ROC-AUC over 30 random shuffles of each original feature (with its one-hot columns shuffled together), reported with the standard deviation across shuffles. Permutation importance is considered more reliable than impurity importance because it is measured on unseen data and is less biased towards continuous or high-cardinality features.

## Software and Reproducibility

Analysis was performed in Python (3.13.9) using pandas, NumPy, scikit-learn, Matplotlib and Seaborn. A fixed random seed (42) was used for the train-test split, cross-validation folds, model fitting, bootstrap resampling and permutation procedures so that all results are reproducible.

## Ethical Considerations

The data was acquired from CPUT through the Fundani CHED department for the purpose of developing dashboards. Approval was granted to use the same data for this study in accordance with the POPIA Act. The data was originally provided for the development of institutional dashboards, and permission was subsequently granted to use the same dataset for this research. The use of the data complies with the requirements of the Protection of Personal Information Act (POPIA) (Act No. 4 of 2013). To ensure ethical compliance throughout the study, the following measures were taken. Identifiers (e.g., student names, student numbers, etc.) were removed to protect students. The data was used for academic purposes only and was anonymized so that students cannot be identified. The data will be secured on password protected device. The research strictly complied with CPUT’s research ethics requirements and institutional policies governing the use of student data. Findings were reported in aggregate form for confidentiality.

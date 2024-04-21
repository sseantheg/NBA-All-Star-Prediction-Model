# NBA All-Star Prediction Model
This is my Final Year Project (FYP) for my CS degree at Asia Pacific University of Technology & Innovation (APU) in 2020 where I built a prediction model that predicts if an NBA player will blossom into an All-Star based on their rookie (and sophomore) year data. The project is carried out on Jupyter Notebook using Python libraries like `pandas`, `numpy`, `sklearn`, `seaborn`, and `matpotlib`.


# List of Items:
## A. Documentation
The documentation of the full study is included as a PDF file. The content covered:
1. Introduction
2. Literature Review
3. Technical Research
4. Methodology  
5. Data Analysis
6. Results and Discussion

## B. Jupyter Notebooks
There is a total of 5 notebooks for the end-to-end processes of this project. The description is as follows:
1. `AllStar Preprocessing`: processing the All-Star list to acquire a single list with two columns - _the year of first All-Star selection_ and _Player Full name_ (unique)
2. `Historical Data Preprocessing & Integration`: process all the historical data measuring players' performance to acquire a list of all players (in the history) rookie & sophomore year performance metrics. Dealt with missing data, added in All-Star binary column, removed low minutes player (relative to future all-stars).
3. `AllStar only exploratory & graphs`: Study All-Star players to understand the distributions & tendencies. Performed univariate analysis, bivariate analysis & outlier analysis. Understanding the distribution here helps with outlier removal in the next step, as we don't want to remove all-star data from the dataset.
4. `MasterData Exploratory, Univariate & Bivariate Analysis, Outlier Removal`: Performed univariate, bivariate, correlation and outlier analysis on the main dataset (future all-stars and non). Heavily correlated fields are dealt with before deploying a feature selection method. Outlier detection by percentile is executed concerning study from notebook #3—final Dataset generated for modelling.
5. `Modeling`: dealt with class imbalance, tested a few models with a train test split: Logistic Regression, MLPClassifier (NN), Support Vector Machine (SVC), and Random Forest Classifier. Did a randomized search for parameter optimization.

## C. Data
1. The all-star datasets are acquired from a few different websites, namely _data.world_, _kaggle.com_ and _basketball-reference.com_. 
2. The historical player performance data can be found at backpicks.com. This dataset contains traditional stats as well as advanced stats of NBA players from 1955 to 2019. Data is only accessible for Patreon members of the Thinking Basketball community.
_Full links of the websites can be found in the documentation pdf file._

## D. Demonstration Python program
A minimalistic Python program named `presentation` was used to demonstrate the outcome of the project. Provides a simple user interface for users to select a player by inputting their name, where the program will produce the prediction result of whether the player will turn into an All-Star player in the future.


## E. Future Enhancement
1. One random idea that came up out of the blue was to make this project a two-step prediction. We can predict the player's later year data (define some fixed number year after) from the rookie year data, then make the classification based on the later year predicted performance. Will that lead to better performance? also, we can do more clustering analysis (to the rookie year or later year data)?

2. another random thought: we can do 3 different prediction targets which is to predict the players' likelihood of becoming an all-star in 3 years, 5 years and 7 years. This may cater better to business needs instead of a single target prediction (in this case likelihood in 7 years).

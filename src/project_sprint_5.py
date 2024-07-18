# -*- coding: utf-8 -*-
"""Project Sprint 5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XsO_Go4aaDU3armdBCIXodFeDOJasJx9

# **Campaign Plan for 2017**

## **Introduction**

The project aims to assist the Ice company in understanding historical video game sales, enabling them to formulate an improved sales strategy for the year 2017.

**Goal**

The objectives of this project are outlined below.

1. Identifying patterns that determine whether a game can be deemed successful or not.
2. Discovering the most promising games and planning their advertising campaigns.

**Stages**

The project's phases are outlined below.

1. Open the data file and study its general information.

2. Prepare the data.

- Rename the column (use lowercase letters for all).
- Convert the data to the required data type.
- Describe which columns have had their data types changed and explain the reasons.
- If necessary, missing values will be handled
- Calculate the total sales (sales quantity across all regions) for each game and input these values into a separate column.

3. Analyze the data.

- Examine the quantity of games released in different years.
- Analyze how sales vary from one platform to another. Select the platform with the highest total sales and create its distribution based on yearly data. Identify platforms that were popular in the past but now have no sales. How long does it usually take for a new platform to emerge and for an old platform to lose popularity?
- Determine the data collection period.
- Which platforms have the highest sales? Which platforms are growing or shrinking? Choose several potentially profitable platforms.
- Generate a box plot for the global sales of all games grouped by platform. Are the sales differences significant? How about the average sales across different platforms?
- Investigate how user and professional reviews impact sales on a popular platform. Create a scatter plot and calculate the correlation between reviews and sales. Then, draw conclusions.
- Compare the sales of the same game on different platforms.
- Observe the general distribution of games based on genre. What conclusions can we draw regarding the most profitable genres?

4. Perform user profiling for each region.


For each region (NA, EU, JP), ascertain:

- The top 5 platforms. Explain the market share variations from one region to another.
- The top 5 genres. Elucidate their differences.
- Does the ESRB rating influence sales in each region?

5. Test hypotheses.

- The average user rating of the Xbox One and PC platforms is the same.
- The average user rating of the Action and Sports genres is different.

6. Conclusions drawing.

**Content of Data**

The data consist of these contents:

- Name
- Platform
- Year_of_Release
- Genre
- NA_sales (sales in North America in millions of USD)
- EU_sales (sales in Europe in millions of USD)
- JP_sales (sales in Japan in millions of USD)
- Other_sales (sales in other countries in millions of USD)
- Critic_Score (review score from critics, maximum 100)
- User_Score (review score from users, maximum 10)
- Rating (ESRB)

Note: Data for the year 2016 may be incomplete.

## **Data Preparation and Processing**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats as st
from scipy.stats import ttest_ind
import scipy.stats as stats

data = pd.read_csv('/content/games.csv')

data.head()

data.shape

data.columns

data.info()

data.isnull().sum()

(data.isnull().sum() / len(data) * 100).sort_values()

data.describe().round(2)

data.duplicated().sum()

"""Based on data given, it is concluded:

1. The data has 16715 rows and 11 columns.
2. The name columns are in capital.
3. There are two type of data that is not suitable. They are Year_of_Release and User_Score that should be in integer.
4. Missing value has been found in column: Name, Genre, Year_of_Release, User_Score, Rating, and Critic_Score.
5. There is no duplicate value.

From the findings above, several actions might be needed:

1. Change the name of the columns into lower case format.
2. Change the data type into its suitable type.
3. Deal with missing value with suitable action.

## **Data Preparation**

### **Set column name into lower case**
"""

data.columns

data.columns = ['name',
                'platform',
                'year_of_release',
                'genre',
                'na_sales',
                'eu_sales',
                'jp_sales',
                'other_sales',
                'critic_score',
                'user_score',
                'rating']

data.columns

"""### **Change the unfit type of data**

**Year of release**
"""

(data['year_of_release'].isnull().sum() / len(data) * 100)

"""We will input 0 for missing value in year_of_release columns since its only 1.6%"""

data['year_of_release'].fillna(0, inplace=True)
data['year_of_release'].isnull().sum()

"""Since missing value already filled, the change the data type"""

data['year_of_release'] = data['year_of_release'].astype(int)
data.info()

"""**Critic Score**"""

(data['critic_score'].isnull().sum() / len(data) * 100)

"""As we can see 51% of critic score is missing its value"""

data['critic_score'].unique()

data['critic_score'].describe()

"""Because the missing value is to much, so drop the missing value wont be an option. For now we can fill it with 0 first."""

data['critic_score'].fillna(0, inplace=True)
data['critic_score'].unique()

data['critic_score'].isnull().sum()

data['critic_score'] = data['critic_score'].astype(int)
data.info()

"""### **Handling missing value**

**Name and Genre**
"""

(data.isnull().sum() / len(data) * 100).sort_values()

"""Since  its only 0.01% missing value in name and genre, we can drop them all altogether"""

data.dropna(subset=['name'], inplace=True)
data.dropna(subset=['genre'], inplace=True)

(data.isnull().sum() / len(data) * 100).sort_values()

"""**User Score**"""

data['user_score'].unique()

data['user_score'].describe()

"""There is TBD value in column user_score, since TBD means to be determined which is still Nan, we can assume that the value is the same with nan."""

data['user_score'] = data['user_score'].replace('tbd', np.nan)

data['user_score'].unique()

data['user_score'].describe()

(data['user_score'].isnull().sum() / len(data) * 100)

"""For now we can leave it this way"""

data['user_score'] = data['user_score'].astype(float)

data.info()

"""**Rating**"""

data['rating'].unique()

"""Since the data has missing value in column rating, it is make sense to fill it with unknown for future analysis (filter)."""

data['rating'].fillna('Unknown', inplace=True)

data['rating'].unique()

"""**Checking**"""

data.info()

(data.isnull().sum() / len(data) * 100)

data.info()

data.shape

"""Summary

1. All columns has been set into lower case.
2. Data type has been set as below:

- name : object
- platform : object
- year_of_release : integer
- genre : object
- na_sales : float
- eu_sales : float
- jp_sales : float
- other_sales : float
- critic_score : integer
- user_score : float
- rating : object

3. Missing value in column name and genre has been eliminated.
4. Missing value in user_score still Nan 54%, this need further analysis.
5. Missing value in rating score filled with "Unknown" value.
6. Final data consist of 16713 rows and 11 columns.

## **Exloratory Data Analysis**
"""

data.head()

"""Adding column total_sales for further analysis"""

data['total_sales'] = data['na_sales'] + data['eu_sales'] + data['jp_sales'] + data['other_sales']

data.head(2)

"""### **Examine the quantity of games released in different years**"""

data_1 = pd.pivot_table(data, index='year_of_release', values='name', aggfunc='count').reset_index()

data_1.head(2)

plt.figure(figsize=(16,5))
plt.bar(data_1.index, data_1['name'], label='Games', color='blue')
plt.xlabel('Year')
plt.ylabel('Quantity')
plt.title('Total Games Released')
plt.xticks(data_1.index, data_1['year_of_release'], rotation=45)
plt.legend()
plt.show()

"""Insight

From calculation above, it shows that the peak of games released were at 2008 and 2009 period.

### **Analyze how sales vary from one platform to another**
"""

data_2 = pd.pivot_table(data, index='platform', values='name', aggfunc='count').sort_values(by='name', ascending=False).reset_index()

data_2.head(2)

data_3 = data.loc[data['platform'] == 'PS2']
data_4 = pd.pivot_table(data_3, index='year_of_release', values='total_sales', aggfunc='sum').reset_index()
data_4.head(2)

plt.figure(figsize=(10,5))
plt.bar(data_4.index, data_4['total_sales'], label='PS2', color='green')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.title('Sales Performance of PS2')
plt.xticks(data_4.index, data_4['year_of_release'], rotation=45)
plt.legend()
plt.show()

data_4['total_sales'].describe()

"""Based on the calculation of PS2 as sample, the uphill trend of PS2 Sales started in 2001, peaked at 211 million USD in 2004 and steadily decline after that.

### **Determine the data collection period**

Since the goal of the project is to help Sales division for upcoming year of 2017. This project will observe the 2 year prior which are 2016 and 2015.
"""

main_data = data.loc[data['year_of_release'] > 2014].reset_index()

main_data.head()

main_data.info()

"""### **Which platforms have the highest sales? Which platforms are growing or shrinking?**"""

main_data_1 = pd.pivot_table(main_data, index='platform', values='total_sales', aggfunc='sum').sort_values(by='total_sales', ascending=False).reset_index()

plt.figure(figsize=(10,5))
plt.bar(main_data_1.index, main_data_1['total_sales'], color='red')
plt.xlabel('Platform')
plt.ylabel('Total Sales in million USD')
plt.title('Total Sales of all Platforms')
plt.xticks(main_data_1.index, main_data_1['platform'], rotation=45)
plt.show()

main_data_2 = data.loc[data['year_of_release'] > 2009]

main_data_3 = pd.pivot_table(main_data_2, index=['platform', 'year_of_release'],
                             values='total_sales', aggfunc='sum').reset_index()
main_data_3

ps_4 = main_data_3.loc[main_data_3['platform'] == 'PS4']
x_one = main_data_3.loc[main_data_3['platform'] == 'XOne']
ds_3 = main_data_3.loc[main_data_3['platform'] == '3DS']
wii_u = main_data_3.loc[main_data_3['platform'] == 'WiiU']
ps_3 = main_data_3.loc[main_data_3['platform'] == 'PS3']
pc = main_data_3.loc[main_data_3['platform'] == 'PC']
x_360 = main_data_3.loc[main_data_3['platform'] == 'X360']
psv = main_data_3.loc[main_data_3['platform'] == 'PSV']
wii = main_data_3.loc[main_data_3['platform'] == 'Wii']
psp = main_data_3.loc[main_data_3['platform'] == 'PSP']

plt.figure(figsize=(12,5))
plt.plot(ps_4['year_of_release'], ps_4['total_sales'], label='PS4', color='blue')
plt.plot(x_one['year_of_release'], x_one['total_sales'], label='XOne', color='red')
plt.plot(ds_3['year_of_release'], ds_3['total_sales'], label='3DS', color='green')
plt.plot(wii_u['year_of_release'], wii_u['total_sales'], label='WiiU', color='purple')
plt.plot(ps_3['year_of_release'], ps_3['total_sales'], label='PS3', color='yellow')
plt.plot(pc['year_of_release'], pc['total_sales'], label='PC', color='pink')
plt.plot(x_360['year_of_release'], x_360['total_sales'], label='X360', color='black')
plt.plot(psv['year_of_release'], psv['total_sales'], label='PSV', color='brown')
plt.plot(wii['year_of_release'], wii['total_sales'], label='Wii', color='cyan')
plt.plot(psp['year_of_release'], psp['total_sales'], label='PSP', color='grey')
plt.xlabel('Year')
plt.ylabel('Total Sales in million USD')
plt.title('Total Sales of popular platform from 2010 to 2016')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()

"""Insight

1. The downfall trend in 2016 caused by incomplete data in 2016 because the year of 2016 is not over yet.
2. Based on the line graph almost all of the platform selling performance are declining but PS4 and Xbox One.

### **Generate a box plot for the global sales of all games grouped by platform**

The data using in this chapter is sales of games within the year of 2015 and 2016 only.
"""

plt.figure(figsize=(10,10))
sns.boxplot(x='platform', y='total_sales', data=main_data)
plt.xlabel('Platform')
plt.ylabel('Total Sales')
plt.title('Boxplot of Total Sales by Platform')
plt.show()

data_6 = pd.pivot_table(main_data, index='platform', values='total_sales', aggfunc='mean').sort_values(by='total_sales', ascending=False).reset_index()
data_6

plt.figure(figsize=(10,5))
plt.bar(data_6.index, data_6['total_sales'], color='red')
plt.xlabel('Platform')
plt.ylabel('Average Sales in million USD')
plt.title('Average Sales of all platform from 2015 to 2016')
plt.xticks(data_6.index, data_6['platform'], rotation=45)
plt.show()

"""Insight

1. The boxplot shows that on average the total sales of games in all platform are likely the same, but as we can see the sales PS4, Xbox One, 3DS, and WiiU are relatively vary and tend to sell higher at some cases.
2. The average sales of all platforms observed in time of 2015 to 2016 shows that PS4, Xbox One, and WiiU are at higher top. Therefore the sales division should focus on these platforms for the year of 2017.

### **Create a scatter plot and calculate the correlation between reviews and sales**

Investigate how user and professional reviews impact sales on a popular platform. Create a scatter plot and calculate the correlation between reviews and sales. Then, draw conclusions.
"""

main_data.columns

main_data['critic_score'].unique()

main_data['user_score'].unique()

main_data['user_score'] = main_data['user_score'].fillna(0)

main_data.info()

"""#### **PS4**"""

data_7 = main_data.groupby(['platform', 'name']).agg(
    critic_score=('critic_score', 'sum'),
    user_score=('user_score', 'sum'),
    total_sales=('total_sales', 'sum')
).query('platform == "PS4" & critic_score > 0 & user_score > 0').reset_index()

data_7

"""Correlations"""

correlation_matrix = data_7[['critic_score', 'user_score', 'total_sales']].corr()
total_sales_correlation = correlation_matrix['total_sales']
total_sales_correlation

sns.heatmap(correlation_matrix.corr(), annot=True)

"""Scatter Plot"""

plt.figure(figsize=(12,5))
sns.scatterplot(x='critic_score', y='total_sales', data=data_7);

plt.figure(figsize=(12,5))
sns.scatterplot(x='user_score', y='total_sales', data=data_7);

"""#### **3DS**"""

data_8 = main_data.groupby(['platform', 'name']).agg(
    critic_score=('critic_score', 'sum'),
    user_score=('user_score', 'sum'),
    total_sales=('total_sales', 'sum')
).query('platform == "3DS" & critic_score > 0 & user_score > 0').reset_index()

data_8.head(2)

"""Correlations"""

correlation_matrix_3ds = data_8[['critic_score', 'user_score', 'total_sales']].corr()
total_sales_correlation_3ds = correlation_matrix_3ds['total_sales']
total_sales_correlation_3ds

sns.heatmap(correlation_matrix_3ds.corr(), annot=True)

"""Scatter Plot"""

plt.figure(figsize=(12,5))
sns.scatterplot(x='critic_score', y='total_sales', data=data_8);

plt.figure(figsize=(12,5))
sns.scatterplot(x='user_score', y='total_sales', data=data_8);

"""Insight

1. Here are the correlation calculation of PS4 between user review, critic review and total sales.

- critic_score :   0.392074
- user_score   :  -0.064368
- total_sales  :   1.000000
- Surprisingly, the correlations show the negative value between user score and total sales.

2. Both scatter plot of user review vs total sales and critic review vs total sales show the align statement that most of the PS4 are in Quadrant 4 which is even the score is high the total sales is not high as well.

3. Here are the correlation calculation of 3DS between user review, critic review and total sales.

- critic_score :   0.177575
- user_score   :   0.240477
- total_sales  :   1.000000
- The correlations are tend to have low correlation.

4. Same with PS4, most of the dots are in Quadrant 4 even though we can still see for some sales that high critic review and user review also has high selling number.

### **Observe the general distribution of games based on genre**

Observe the general distribution of games based on genre. What conclusions can we draw regarding the most profitable genres?
"""

data_9 = pd.pivot_table(main_data, index='genre', values='total_sales', aggfunc='sum').sort_values(by='total_sales', ascending=False).reset_index()
data_9

plt.figure(figsize=(10,5))
plt.bar(data_9.index, data_9['total_sales'], color='green')
plt.xlabel('Genre')
plt.ylabel('Total Sales in million USD')
plt.title('Total Sales of all genres from 2015 to 2016')
plt.xticks(data_9.index, data_9['genre'], rotation=45)
plt.show()

"""Insight

Based on the calculation of all region, the top 3 sales for genre are shooter, action, and sports

### **User profiling for each region**

#### **Best selling platform in each region**
"""

main_data.head()

data_10 = pd.pivot_table(main_data, index='platform', values=['na_sales', 'eu_sales', 'jp_sales'], aggfunc='sum').reset_index()
data_10.sort_values(by='eu_sales', ascending=False)

sns.barplot(data=data_10.sort_values(by='eu_sales', ascending=False), x='platform', y='eu_sales');

data_10.sort_values(by='jp_sales', ascending=False)

sns.barplot(data=data_10.sort_values(by='jp_sales', ascending=False), x='platform', y='jp_sales');

data_10.sort_values(by='na_sales', ascending=False)

sns.barplot(data=data_10.sort_values(by='na_sales', ascending=False), x='platform', y='na_sales');

data_10.plot(x='platform', kind='bar')

"""Insight

Based on the calculation, the top 3 platform games in each regions are:
    
1. European Union  : PS4, Xbox One, PC
2. Japan           : 3DS, PS4, PSV
3. North America   : PS4, Xbox One, 3DS

#### **Top 5 best selling genre**
"""

main_data.head(2)

data_11 = pd.pivot_table(main_data, index='genre', values=['na_sales', 'eu_sales', 'jp_sales'], aggfunc='sum').reset_index()
data_11

plt.figure(figsize=(12,5))
sns.barplot(data=data_11.sort_values(by='eu_sales', ascending=False), x='genre', y='eu_sales');

plt.figure(figsize=(12,5))
sns.barplot(data=data_11.sort_values(by='jp_sales', ascending=False), x='genre', y='jp_sales');

plt.figure(figsize=(12,5))
sns.barplot(data=data_11.sort_values(by='na_sales', ascending=False), x='genre', y='na_sales');

data_11.plot(x='genre', kind='bar');

"""Insight

Based on the analysis, here are the top 3 genres in each regions:

1. European Union : Shooter, Action, Sports
2. Japan          : Action, Role-Playing, Shooter
3. North America  : Shooter, Action, Sports

#### **ESRB Rating impact on sales in each region**

The Entertainment Software Rating Board (ESRB) is a self-regulatory organization that assigns age and content ratings to consumer video games in the United States and Canada.

ESRB Chart definition:

1. E - Everyone : Games with this rating contain content that that the ESRB believes is suitable for all ages.
2. E10+ - Everyone 10+ : Games with this rating contain content that the ESRB believes is suitable for ages 10 and over, including cartoon, fantasy, or mild violence, mild language, and/or minimal suggestive themes.
3. M - Mature 17+ : Games with this rating contain content that the ESRB believes is suitable for ages 17 and over, including intense violence, blood and gore, sexual content, strong language, drug use, nudity, and/or crude humor.
4. T - Teen : Games with this rating contain content that the ESRB believes is suitable for ages 13 and over, including violence, suggestive themes, crude humor, minimal blood, and/or infrequent use of strong language.
"""

main_data.head()

main_data['rating'].unique()

data_12 = main_data.loc[main_data['rating'] != 'Unknown']

data_12['rating'].unique()

data_13 = pd.pivot_table(data_12, index='rating', values=['na_sales', 'eu_sales', 'jp_sales'], aggfunc='sum').reset_index()
data_13

data_13.sort_values(by='eu_sales', ascending=False)

sns.barplot(data=data_13.sort_values(by='eu_sales', ascending=False), x='rating', y='eu_sales');

data_13.sort_values(by='jp_sales', ascending=False)

sns.barplot(data=data_13.sort_values(by='jp_sales', ascending=False), x='rating', y='jp_sales');

data_13.sort_values(by='na_sales', ascending=False)

sns.barplot(data=data_13.sort_values(by='na_sales', ascending=False), x='rating', y='na_sales');

"""Insight

Based on the analysis, the top ESRB rating in each region is:
    
1. European Union: Mature
2. Japan: Teen
3. North America: Mature

## **Testing Hyphothesis**

### **Hyphothesis 1**

1. H0: The average user rating of the Xbox One and PC platforms is the same.
2. H1: The average user rating of the Xbox One and PC platforms is not the same.
3. alpha : 0.05

In this test we will use method for one way and independent.
"""

main_data['platform'].unique()

data_xbox = main_data.query('platform == "XOne" & user_score > 0').reset_index()
data_ps = main_data.query('platform == "PC" & user_score > 0').reset_index()

data_xbox.shape

data_ps.shape

np.var(data_xbox['user_score']), np.var(data_ps['user_score'])

alpha = 0.05

p_value_levene = stats.levene(data_xbox['user_score'], data_ps['user_score']).pvalue
print(p_value_levene)

if p_value_levene > alpha:
    print('H0 is accepted: The average user rating of the Xbox One and PC platforms is the same.')
else:
    print('H0 is rejected: The average user rating of the Xbox One and PC platforms is not the same.')
print('Xbox one average user rating is', data_xbox['user_score'].mean())
print('PS one average user rating is', data_ps['user_score'].mean())

p_value = stats.ttest_ind(data_xbox['user_score'], data_ps['user_score'], equal_var=False).pvalue
print(p_value)

if p_value > alpha:
    print('H0 is accepted: The average user rating of the Xbox One and PC platforms is the same.')
else:
    print('H0 is rejected: The average user rating of the Xbox One and PC platforms is not the same.')
print('Xbox one average user rating is', data_xbox['user_score'].mean())
print('PS one average user rating is', data_ps['user_score'].mean())

"""### **Hyphothesis 2**

1. H0: The average user rating of the Action and Sports genres is the same.
2. H1: The average user rating of the Action and Sports genres is not different.
3. Alpha : 0.05

In this test we will use method for one way and independent.
"""

main_data['genre'].unique()

data_action = main_data.query('genre == "Action" & user_score > 0').reset_index()
data_sports = main_data.query('genre == "Sports" & user_score > 0').reset_index()

data_action.shape

data_sports.shape

np.var(data_action['user_score']), np.var(data_sports['user_score'])

p_value_levene = stats.levene(data_action['user_score'], data_sports['user_score']).pvalue
print(p_value_levene)

if p_value_levene > alpha:
    print('H0 is accepted: The average user rating of the Action and Sports genres is different.')
else:
    print('H0 is rejected: The average user rating of the Action and Sports genres is not different.')
print('Action genre average user rating is', data_action['user_score'].mean())
print('Sports genre average user rating is', data_sports['user_score'].mean())

p_value = stats.ttest_ind(data_action['user_score'], data_sports['user_score'], equal_var=False).pvalue
print(p_value)

if p_value > alpha:
    print('H0 is accepted: The average user rating of the Action and Sports genres is different.')
else:
    print('H0 is rejected: The average user rating of the Action and Sports genres is not different.')
print('Action genre average user rating is', data_action['user_score'].mean())
print('Sports genre average user rating is', data_sports['user_score'].mean())

"""Insight

Based on the hyphothesis testing, the result are below:
    
1. Hyphothesis 1: The average user rating of the Xbox One and PC platforms is the same.

- p_value: 0.07122249094391404
- H0 is accepted: The average user rating of the Xbox One and PC platforms is the same.
- Xbox one average user rating is 6.542148760330578
- PS one average user rating is 6.29642857142857

2. Hyphothesis 2: The average user rating of the Action and Sports genres is different.

- p_value: 1.060035862066395e-05
- H0 is rejected: The average user rating of the Action and Sports genres is not different.
- Action genre average user rating is 6.808290155440415
- Sports genre average user rating is 5.198780487804878

## **Conclusion**

The project aims to assist the Ice company in understanding historical video game sales, enabling them to formulate an improved sales strategy for the year 2017.

1. Data Initiation

Based on data given, it is concluded:

- The data has 16715 rows and 11 columns.
- The name columns are in capital.
- There are two type of data that is not suitable. They are Year_of_Release and User_Score that should be in integer.
- Missing value has been found in column: Name, Genre, Year_of_Release, User_Score, Rating, and Critic_Score.
- There is no duplicate value.
From the findings above, several actions might be needed:

- Change the name of the columns into lower case format.
- Change the data type into its suitable type.
- Deal with missing value with suitable action.

2. Data Preparation

- All columns has been set into lower case.
- Data type has been set as below:

- name : object
- platform : object
- year_of_release : integer
- genre : object
- na_sales : float
- eu_sales : float
- jp_sales : float
- other_sales : float
- critic_score : integer
- user_score : float
- rating : object

- Missing value in column name and genre has been eliminated.
- Missing value in user_score still Nan 54%, this need further analysis.
- Missing value in rating score filled with "Unknown" value.
- Final data consist of 16713 rows and 11 columns.

4. Data Analyzing

- From calculation above, it shows that the peak of games released were at 2008 and 2009 period.
- Based on the calculation of PS2 as sample, the uphill trend of PS2 Sales started in 2001, peaked at 211 million USD in 2004 and steadily decline after that.
- The downfall trend in 2016 caused by incomplete data in 2016 because the year of 2016 is not over yet.
- Based on the line graph almost all of the platform selling performance are declining but PS4 and Xbox One.
- The boxplot shows that on average the total sales of games in all platform are likely the same, but as we can see the sales PS4, Xbox One, 3DS, and WiiU are relatively vary and tend to sell higher at some cases.
- The average sales of all platforms observed in time of 2015 to 2016 shows that PS4, Xbox One, and WiiU are at higher top. Therefore the sales division should focus on these platforms for the year of 2017.
Here are the correlation calculation of PS4 between user review, critic review and total sales.

- critic_score :   0.392074
- user_score   :  -0.064368
- total_sales  :   1.000000
- Surprisingly, the correlations show the negative value between user score and total sales.

Both scatter plot of user review vs total sales and critic review vs total sales show the align statement that most of the PS4 are in Quadrant 4 which is even the score is high the total sales is not high as well.

Here are the correlation calculation of 3DS between user review, critic review and total sales.

- critic_score :   0.177575
- user_score   :   0.240477
- total_sales  :   1.000000
- The correlations are tend to have low correlation.

- Same with PS4, most of the dots are in Quadrant 4 even though we can still see for some sales that high critic review and user review also has high selling number.
Based on the calculation of all region, the top 3 sales for genre are shooter, action, and sports
Based on the analysis, the top ESRB rating in each region is:

- European Union: Mature
- Japan: Teen
- North America: Mature

5. Hyphothesis Testing

Based on the hyphothesis testing, the result are below:

Hyphothesis 1: The average user rating of the Xbox One and PC platforms is the same.
- p_value: 0.07122249094391404
- H0 is accepted: The average user rating of the Xbox One and PC platforms is the same.
- Xbox one average user rating is 6.542148760330578
- PS one average user rating is 6.29642857142857

Hyphothesis 2: The average user rating of the Action and Sports genres is different.
- p_value: 1.060035862066395e-05
- H0 is rejected: The average user rating of the Action and Sports genres is not different.
- Action genre average user rating is 6.808290155440415
- Sports genre average user rating is 5.198780487804878

## **Recommendation**

Based on the analysis of this project, the recommendation are these below:
    
1. Sales division need to focus in selling PS4, Xbox One, 3DS, and WiiU globally.
2. European Union and North America region mostly have the same characteristic in sales, therefore the strategy could be the same for both region.
- The most popular game platform in EU and NA is PS4, meanwhile in JP is Nintendo 3DS.
- The rating that commonly found in EU and NA is Mature, but in JP is T.
- The most popular genre in EU and NA is shooting, but in JP is action.
"""


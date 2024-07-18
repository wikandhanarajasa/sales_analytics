# Video Game Sales Insights

## Introduction

The project aims to assist the Ice company in understanding historical video game sales, enabling them to formulate an improved sales strategy for the year 2017.

## Goal

The objectives of this project are outlined below.

- Identifying patterns that determine whether a game can be deemed successful or not.
- Discovering the most promising games and planning their advertising campaigns.

## Stages

The project's phases are outlined below.

1. **Open the data file and study its general information.**

2. **Prepare the data.**
   - Rename the columns (use lowercase letters for all).
   - Convert the data to the required data type.
   - Describe which columns have had their data types changed and explain the reasons.
   - Handle missing values if necessary.
   - Calculate the total sales (sales quantity across all regions) for each game and input these values into a separate column.

3. **Analyze the data.**
   - Examine the quantity of games released in different years.
   - Analyze how sales vary from one platform to another. Select the platform with the highest total sales and create its distribution based on yearly data. Identify platforms that were popular in the past but now have no sales. Determine the usual time it takes for a new platform to emerge and for an old platform to lose popularity.
   - Determine the data collection period.
   - Identify which platforms have the highest sales, and which platforms are growing or shrinking. Choose several potentially profitable platforms.
   - Generate a box plot for the global sales of all games grouped by platform. Evaluate if the sales differences are significant and analyze the average sales across different platforms.
   - Investigate how user and professional reviews impact sales on a popular platform. Create a scatter plot and calculate the correlation between reviews and sales. Draw conclusions.
   - Compare the sales of the same game on different platforms.
   - Observe the general distribution of games based on genre and draw conclusions regarding the most profitable genres.

4. **Perform user profiling for each region.**
   - For each region (NA, EU, JP), ascertain:
     - The top 5 platforms and explain the market share variations from one region to another.
     - The top 5 genres and elucidate their differences.
     - Determine if the ESRB rating influences sales in each region.

5. **Test hypotheses.**
   - The average user rating of the Xbox One and PC platforms is the same.
   - The average user rating of the Action and Sports genres is different.

6. **Draw conclusions.**

## Data Description

The dataset includes the following columns:

- **Name:** Name of the game
- **Platform:** Platform of the game (e.g., Xbox, PlayStation)
- **Year_of_Release:** Year the game was released
- **Genre:** Genre of the game
- **NA_sales:** Sales in North America in millions of USD
- **EU_sales:** Sales in Europe in millions of USD
- **JP_sales:** Sales in Japan in millions of USD
- **Other_sales:** Sales in other countries in millions of USD
- **Critic_Score:** Review score from critics (maximum 100)
- **User_Score:** Review score from users (maximum 10)
- **Rating:** ESRB rating of the game

Note: Data for the year 2016 may be incomplete.

# Sqlalchemy-challenge

## Climate Analysis and Exploration
I used Python and SQLAlchemy to do basic climate analysis and data exploration of my climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

- I used the hawaii.sqlite files to complete the climate analysis and data exploration.
- I chose a start date and end date for your trip making sure the vacation range is approximately 3-15 days total.
- I used SQLAlchemy create_engine to connect to your sqlite database.
- I used SQLAlchemy automap_base() to reflect the tables into classes and saved a reference to those classes called Station and Measurement.

## Precipitation Analysis

- Design a query to retrieve the last 12 months of precipitation data.
- Select only the date and prcp values.
- Load the query results into a Pandas DataFrame and set the index to the date column.
- Sort the DataFrame values by date.
- Plot the results using the DataFrame plot method.
- Use Pandas to print the summary statistics for the precipitation data.

## Station Analysis
  After analyzing precipitation data, I did a quick analysis of the station data. Specifically, I designed a query to show how many stations are available in this dataset. After that, I created another query to find the most active station (i.e., the station with the highest number of temperature observations.). Using the results from this query, I was able to calculate the lowest temperature recorded, the highest temperature recorded, and the average temperature of the most active station. Finally, I took the last 12 months of temperature observation data for the most active station and plotted the results as a histogram with bins=12.
  

## Climate App
Design a Flask API based on the queries that you have just developed and use Flask to create your routes.
To run the app:

Clone or download this repository to a local directory on your computer.
Change directory to the root directory (sqlalchemy-challenge) of this repository.
Run python app.py from the root directory (sqlalchemy-challenge). The app starts up at localhost:5000 by default.

### Routes
- /
  - Home page.
  - List all routes that are available.

- /api/v1.0/precipitation
  - Convert the query results to a dictionary using date as the key and prcp as the value.
  - Return the JSON representation of your dictionary.

- /api/v1.0/stations
  - Return a JSON list of stations from the dataset.

- /api/v1.0/tobs
  - Query the dates and temperature observations of the most active station for the last year of data.
  - Return a JSON list of temperature observations (TOBS) for the previous year.

- /api/v1.0/<start> and /api/v1.0/<start>/<end>
  - Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  - When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
  - When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
  
  
  
## Bonus Analyses

### Temperature Analysis I

Hawaii is reputed to enjoy mild weather all year. So, I wanted to determine if there is a meaningful difference between the temperature in, for example, June and December. To do this, I used SQLAlchemy to query the temperatures in June at all stations across all available years in the dataset. I also did the same query for December.

After querying for the temperature data, I identified the average temperature for June and December, plotted the temperature values on a scatter plot to show the distribution of the values, and plotted those values on a histogram to show the difference in means. Just looking at the histogram, there appears to be a difference in the means for June and December.

I decided to do an independent t-test. An independent t-test compares the means of 2 independent populations (June temperatures in Hawaii and December temperatures in Hawaii). We want to use an independent t-test (unpaired) rather than a paired t-test because we want to compare the means of two independent populations. A paired t-test (one sample t-test) looks at comparing the sample to the population, which we don't want in this case. Assumptions include data are normally distributed, data are independent, and data are homogenous (the standard deviations are roughly equal).

The independent t-test was calculated using scipy.stats.ttest_ind from the scipy package. After calculating the results, it was determined that there is a statistically significant difference in means (p-value of less than 0.05). In other words, the p-value is a very small value, so the means of these two populations are significantly different, and there is a lower probability that the difference is random. As a result, we can reject the null hypothesis, which is that there is no meaningful difference between the temperature in June and December in Hawaii.

### Temperature Analysis II
- Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").
- Plot the min, avg, and max temperature from your previous query as a bar chart.
  - Use the average temperature as the bar height.
  - Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).
 
 ### Daily Rainfall Average
- Calculate the rainfall per weather station using the previous year's matching dates.
- Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.
-I was provided with a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. I was suppose to use all historic TOBS that match that date string.
- Create a list of dates for your trip in the format %m-%d. Use the daily_normals function to calculate the normals for each date string and append the results to a list.
- Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.
- Use Pandas to plot an area plot (stacked=False) for the daily normals.

### Tools Used
- **SQLAlchemy**
- **Jupyter Notebook**
- **Python**
- **Matplotlib**
- **Pandas**
- **Flask**
- **datetime**
- **dateutil.relativedelta**
- **Scipy**

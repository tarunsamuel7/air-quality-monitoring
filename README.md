# air-quality-monitoring

Commit 1 : Data-preprocessinng part 
1. Checked missing values in both files
2. Dropped unwanted columns.
3. Found and visualized outliers.
4. Filled missing values based on outliers in both files.
5. Concatenated both files into one dataframe.

Commit 2: EDA_featureEngineering
1. Performed EDA and visualization to check co-relation, distibution, trends
2. feature Engineering: Added columns - AQI, AQI_Category, AQI_Numerical


Commit 3 : #ARIMA MODEL
1. I have started from building ARIMA model from an already done EDA part 
2. After Building it i have forcasted the results for the next 60 days
3. Repeated these steps for all the pollutants
4. calculated the metrics
5. Optimized the model for better results
6. Obtained optimized metric results
7. Compared original values and optimized values using bar chart
8. Visualised the forecasted data.
9. Interpretation from the obtained metrics

Commit 4: XGBoost
1.I have made the XGboost model and started after the EDA process done in the Arima model
2.Defining the features and targets.
3.Training and evaluating an XGBoost regression model for each target variable.
4.Storing and printing evaluation metrics.
5.Plotting the actual vs. predicted values for visual comparison

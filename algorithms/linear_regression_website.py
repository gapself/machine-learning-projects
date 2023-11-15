import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
website = pd.read_csv('../datasets/website.csv')

# Print the first five rows
print(website.head())

# Create a scatter plot of time vs age
plt.scatter(website.time_seconds, website.age)
# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict time_seconds based on age
model = sm.OLS.from_formula('time_seconds ~ age', data=website)
results = model.fit()
# Plot the scatter plot with the line on top
print(results.params)
y = results.params[1] * website.age + 128.98
plt.scatter(website.age,website.time_seconds)
plt.xlabel('age')
plt.ylabel('time')
plt.plot(website.age, y)
plt.show()
plt.clf()
# Calculate fitted values
predicted_values = results.predict(website.age)
# Calculate residuals
residuals = website.time_seconds - predicted_values
print(residuals.head())

# Check normality assumption
plt.hist(residuals)
plt.show()
plt.clf()

# Check homoscedasticity assumption
plt.scatter(predicted_values, residuals)
plt.show()
plt.clf()

# Predict amount of time on website for 40 year old
y_40_year_old = results.params[1] * 40 + results.params[0]
print('Amount of time for 40 yr:', y_40_year_old)

# Fit a linear regression to predict time_seconds based on the browser
model = sm.OLS.from_formula('time_seconds ~ browser', website)
results = model.fit()
print(results.params)

# Calculate and print the group means (for comparison)
mean_safari_1 = np.mean(website.time_seconds[website.browser == 'Safari'])
mean_chrome_0 = np.mean(website.time_seconds[website.browser == 'Chrome'])
print(mean_safari_1)
print(mean_chrome_0)
interc =  mean_safari_1 - mean_chrome_0
print(interc) #[T.sth] corresponds to 1 = YES (slope)
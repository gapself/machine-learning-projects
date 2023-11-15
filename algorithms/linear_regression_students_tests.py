import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

students = pd.read_csv('../datasets/students_test_data.csv')
# predicting scores based on predictor: hours_studied
model = sm.OLS.from_formula('score ~ hours_studied', data=students)
results = model.fit()
print(results.params,
      'Intercept:', results.params[0],
      'Slope is', results.params[1])

# Interpretation of the intercept and slope
print('A student who studied for 0 hours is expected to score a {} on the test.'.format(results.params[0].round(2)))
print('For every additional 1 hour of studying, students are expected to score {} points higher on the test.'.format(results.params[1].round(2)))
# calculating predicted scores for 3hrs of studying. using formula y= ax +b
pred_3hr = results.params[1] * 3 + results.params[0]
print(pred_3hr)

# Write equation for a line
y = 9.85 * students.hours_studied + 43
# Create the plot here:
plt.scatter(students.hours_studied, students.score)
plt.xlabel('hours_studied')
plt.ylabel('score')
plt.plot(students.hours_studied, y)
plt.show()
plt.clf()


new_data = {"hours_studied":[5]}
pred_5hr = results.predict(new_data)
print('pred_5hr:', pred_5hr)

fitted_values=results.predict(students.hours_studied)
residuals= students.score - fitted_values
print(residuals.head())

#plot histogram of the residuals
# make sure that the distribution looks approximately normal
plt.hist(residuals)
plt.show()
plt.clf()

plt.scatter(fitted_values, residuals)
plt.show()
plt.clf()

# CATEGORICAL PREDICTORS:

# Calculate group means
print(students.groupby('breakfast').mean().score)
# Create the scatter plot here:
plt.scatter(students.breakfast, students.score)
# Add the additional line here:
plt.plot([0,1], [61.664151, 73.721277])
plt.show()

# Calculate and print group means
mean_score_no_breakfast = np.mean(students.score[students.breakfast == 0])
mean_score_breakfast = np.mean(students.score[students.breakfast == 1])
print('Mean score (no breakfast): ', mean_score_no_breakfast)
print('Mean score (breakfast): ', mean_score_breakfast)
print(mean_score_breakfast - mean_score_no_breakfast)
# Fit the model and print the coefficients
model = sm.OLS.from_formula('score ~ breakfast', students)
results = model.fit()
print(results.params) #[T.sth] corresponds to 1 = YES (slope)




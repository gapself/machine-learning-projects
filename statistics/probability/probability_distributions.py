import numpy as np
import scipy.stats as stats

# create 6 sided "die", roll the "die" the set amount of times
die_6 = range(1, 7)
num_rolls = 10
results_1 = np.random.choice(die_6, size = num_rolls, replace = True)
print(results_1)

# roll the 12-sided "die" 10 times
die_12 = range(1, 13)
results_2 = np.random.choice(die_12,size=num_rolls, replace=True)
print(results_2)

#flip coin
# x: the value of interest
# n: the number of trials
# p: the probability of success
x=6
n=10
p=0.5
print(stats.binom.pmf(x, n, p))

# probability of observing between 2 and 4 heads from 10 coin flips
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5))
# less than 3 heads
print(stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5) + stats.binom.pmf(2, n=10, p=.5))
# less than or equal to 8
print(1 - (stats.binom.pmf(9, n=10, p=.5) + stats.binom.pmf(10, n=10, p=.5)))
# more than 2 heads from 10 coin flips
prob_2 = 1 - (stats.binom.pmf(0, n=10, p=0.5) + stats.binom.pmf(1, n=10, p=0.5) + stats.binom.pmf(2, n=10, p=0.5))
print(prob_2)

# probability of observing 6 or fewer heads from 10 fair coin flips (0 to 6 heads)
print(stats.binom.cdf(6, 10, 0.5))
#observing between 4 and 8 heads
print(stats.binom.cdf(8, 10, 0.5) - stats.binom.cdf(3, 10, 0.5))
#more than 6 heads
print(1 - stats.binom.cdf(6, 10, 0.5))
#same-less than 3:
prob_1 = stats.binom.cdf(3, 10, 0.5)
# compare to pmf code
print(prob_1)
print(stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5) + stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5))


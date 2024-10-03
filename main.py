import numpy as np
import matplotlib.pyplot as plt

scores= np.array([10, 12, 13, 13, 14, 14, 15, 17, 17, 18,
                  18, 18, 18, 19, 19, 19, 20, 20, 21, 21,
                  22, 22, 22, 22, 22, 23, 24, 24, 24, 26,
                  27, 27, 28, 28, 30, 32, 34, 38, 39, 40.])

#mean, Median, Mode
median=np.median(scores)
mean=np.mean(scores)

print("Zac Angelo Mesias//10-Digos//Peta")
print("Median = ", median)
print("Mean = ", mean)

def find_mode(scores):
#i created a function that finds in a dictionary(scores)what is the most frequent number
    frequency = {}#
    for num in scores:
        frequency[num] = frequency.get(num, 0) + 1#keeps track how many times number(num)is present 
    
    mode = None 
    max_frequency = 0#create mode and max frequency variables
    for num, freq in frequency.items():
        if freq > max_frequency:
            mode = num
            max_frequency = freq
    #finds how many times there is a reapeted number with the .items function and compare the next data on how much it repeats to determine what is the mode
    #example(1,1,2,2,2,3)
            #1: 1, 2: 3, 3: 1
            #mode=2
    return mode

mode= find_mode(scores)

print("Mode = ", mode)
print('-----------------------')

# Var, Std
vrc= np.var(scores)
stdv=np.std(scores)
print('Standard Diviation = ', round(stdv, 2))
print('Variance = ', round(vrc, 2))
print('---------------------------')

# quartile, percentile, decile
#numpy percentile function is (percentile/100) x (Number + 1)
Q3= np.percentile(scores, 75)#100 seperate in to 4's 100/4 = 25 x 3(Q3)=75     
D7= np.percentile(scores, 70)#100 seperate in to 10's since finding D7, means 70/100
P76= np.percentile(scores,76)#76 = 76/100print('Quartile 3 = ', Q3)

print('Quartile 3 = ', Q3)
print('Decile 7 = ', D7)
print('percentile 76 = ', P76)

## graphing
# Calculate the cumulative percentage for each percentile
percentiles = [D7, Q3, P76]  # Percentiles to compare
cumulative_percentages = [np.percentile(scores, p) for p in percentiles]

# Calculate the percentage of scores below each percentile
percent_below = [np.sum(scores <= p) / len(scores) * 100 for p in cumulative_percentages]


plt.bar(['Q3', 'D7', 'P76'], percent_below, color=['blue', 'orange', 'green'])
plt.xlabel('Percentiles')
plt.ylabel('Percentage of Scores')
plt.title('Comparison of Percentiles')
plt.show()



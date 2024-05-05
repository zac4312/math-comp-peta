import numpy as np
import matplotlib.pyplot as plt

labels = ['Q3', 'D7', 'P76'] 
scores= np.array([24,20,24,27,39,13,19,27,10,22,
                  14,28,17,18,21,28,18,20,32,22,
                  34,13,26,23,17,21,12,30,22,14,
                  38,19,15,40,18,18,22,24,22,19])

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

Q3= np.percentile(scores, 30)
D7= np.percentile(scores, 70)
P76= np.percentile(scores,76)

print('Quartile 3 = ', Q3)
print('Decile 7 = ', D7)
print('percentile 76 = ', P76)

## graphing
hist, bins = np.histogram(scores, bins=[0, Q3, D7, P76, 40])

hist = hist[1:]
labels = labels[:len(hist)]


plt.pie(hist, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')

plt.title('Students Scores Pie Chart')
plt.show()
















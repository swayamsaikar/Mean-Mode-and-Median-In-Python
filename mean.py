import csv

with open('data.csv', newline="") as f:
    rawData = csv.reader(f)
    dataList = list(rawData)

dataList.pop(0)

dataList = dataList
# print(dataList)

weights = []
for num in range(len(dataList)):
    # each array in the dataList represents row in data.csv file, so we need the weights here
    w = dataList[num][2]  # 2 represents the 3rd element in data.csv
    # if we do not write this float keyboard then all the numbers will be appended as a string in the weights array
    weights.append(float(w))


# now we got the list of all the weights of the people
# print(weights)


total = 0

# Then we are gonna loop through every weight value in this weights array and add that integer value to the current value of total

for i in weights:
    total = total+i

# now to find the mean we have to divide the total/length of the dataList array (average)
lengthOfTheData = len(dataList)
mean = total/lengthOfTheData

print(mean)

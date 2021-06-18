import csv

with open('data.csv', newline="") as f:
    rawData = csv.reader(f)
    dataList = list(rawData)

dataList.pop(0)
dataList.sort()

dataList = dataList
# print(dataList)

weights = []
for num in range(len(dataList)):
    # each array in the dataList represents row in data.csv file, so we need the weights here
    w = dataList[num][2]  # 2 represents the 3rd element in data.csv
    # if we do not write this float keyboard then all the numbers will be appended as a string in the weights array
    weights.append(float(w))

lengthOfTheData = len(dataList)


# now we got the list of all the weights of the people
# print(weights)

# % means remainder and // means quotient of the division


# We are checking that if the total length of this array is divided by 2 or not
if lengthOfTheData % 2 == 0:
    # WE HAVE TO FIND THE MEDIAN OF THE WEIGHT HERE
    median1 = float(dataList[lengthOfTheData//2][2])
    median2 = float(dataList[(lengthOfTheData//2)-1][2])
    median = (median1+median2)/2
else:
    median = dataList[lengthOfTheData//2]
print(f"The Median is {median}")

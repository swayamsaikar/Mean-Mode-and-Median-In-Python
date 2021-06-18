import csv
from collections import Counter

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

data = Counter(weights)
print(data.items())

#! MAM THIS ONE I HAVE COPIED FROM THE CLASS CODE BECAUSE IT I CANNOT FIGURE OUT WHAT IS GOING ON AFTER 40th LINE (Before 40th line everything is clear)

mode_data_for_range = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}
for weight, occurrence in data.items():
    if 50 < float(weight) < 60:
        mode_data_for_range["50-60"] += occurrence
    elif 60 < float(weight) < 70:
        mode_data_for_range["60-70"] += occurrence
    elif 70 < float(weight) < 80:
        mode_data_for_range["70-80"] += occurrence


# HERE I CANNOT UNDERSTAND

mode_range, mode_occurrence = 0, 0
for range, occurrence in mode_data_for_range.items():
    if occurrence > mode_occurrence:
        mode_range, mode_occurrence = [
            int(range.split("-")[0]), int(range.split("-")[1])], occurrence
mode = float((mode_range[0] + mode_range[1]) / 2)

print(f"Mode is -> {mode}")  # MAM I AM GETTING THE MODE 75 HERE

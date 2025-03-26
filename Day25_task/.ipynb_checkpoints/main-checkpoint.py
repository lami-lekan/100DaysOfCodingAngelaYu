# data = []
# with open("weather_data.csv") as weather_data:
#    for weather_data in weather_data.readlines():
#       data.append(weather_data.strip())

# print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].to_list()

# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# mon_temp_fhr = (monday.temp * 1.8) + 32
# print(mon_temp_fhr)

# data_dict = {
#     "students":["Amy", "James", "Angela"],
#     "scores": [76, 56, 90]
# }

# student_score = pandas.DataFrame(data_dict)
# student_score.to_csv("student_score.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250323.csv")
grey_squirrel = 0
red_squirrel = 0
black_squirrel = 0

for _ in range(len(squirrel_data)):
    if squirrel_data[squirrel_data.Colorjujnotes == "Gray"]:
        print("True")



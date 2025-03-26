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

fur_color_list = squirrel_data["Primary Fur Color"].to_list()
for color in fur_color_list:
    if color == "Gray":
        grey_squirrel += 1
    elif color == "Cinnamon":
        red_squirrel += 1
    elif color == "Black":
        black_squirrel += 1

squirrel_color_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_squirrel, red_squirrel, black_squirrel],
}

squirrel_count = pandas.DataFrame(squirrel_color_dict)
squirrel_count.to_csv("squirrel_count.csv")
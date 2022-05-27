# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg_temp = data.temp.mean()
# print(avg_temp)

# max_temp = data.temp.max()
# print(max_temp)

# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# temp_c = int(monday.temp)
# temp_f = temp_c * 9/5 + 32
# print(temp_f)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_colors = squirrel_data["Primary Fur Color"]
squirrel_gray = squirrel_colors[squirrel_colors == "Gray"]
squirrel_red = squirrel_colors[squirrel_colors == "Cinnamon"]
squirrel_black = squirrel_colors[squirrel_colors == "Black"]

squirrel_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [len(squirrel_gray), len(squirrel_red), len(squirrel_black)],
}

squirrel_count = pandas.DataFrame(squirrel_dict)
squirrel_count.to_csv("squirrel_count.csv")

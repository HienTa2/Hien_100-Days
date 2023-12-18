# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(row[1])
#     print(temperature)


data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data[["temp", "condition"]])

# Print the first 5 rows of the specified columns
print(data[["temp", "condition"]].head())
# Or, print the last 5 rows of the specified columns
print(data[["temp", "condition"]].tail())


# print(data["temp"].mean())
# print(data["temp"].max())

# get the max temp day
# print(data[data.temp == data.temp.max()])
#
# # get monday temp in F
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# # save to csv
# data.to_csv("new_data.csv")


# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

# creating dataframe with the values count above.
# data_dict = {
#     "Fur Color":["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("Squirrels_Count.csv")

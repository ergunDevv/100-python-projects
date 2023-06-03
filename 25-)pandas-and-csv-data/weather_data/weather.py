# with open("25-)pandas-and-csv-data\weather_data.csv") as file:
#     weather_week = file.read()

# data = weather_week.splitlines()
# print(data)


# import csv

# with open("25-)pandas-and-csv-data\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if not row[1] == "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)


import pandas

data = pandas.read_csv("25-)pandas-and-csv-data\weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)

# print(data["temp"].max())

# # Pandas get data in columns(They are sane)
# print(data["condition"])
# print(data.condition)

# Get the row
# print(data[data.day == "Monday"])

# Get the max temperature row
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])


# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_fahrenheit = monday_temp*9/5 + 32
# print(monday_fahrenheit)

# # create data frame from scratch.
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("25-)pandas-and-csv-data/new_data.csv")

import csv
import pandas

# with open("226 weather-data.csv") as f:
#     data = f.readlines()

# print(data)

# with open("226 weather-data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv("226 weather-data.csv")

# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# avg = data["temp"].mean()
# print(avg)

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# moday_temp = int(monday.temp)
# monday_F = moday_temp * 9/5 + 32
# print(monday_F)

# Create a dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data_frame = pandas.DataFrame(data_dict)
# data_csv = data_frame.to_csv("student_scores.csv")

data = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

print(f"There are {gray} gray, {cinnamon} cinnamon, and {black} black squirrels in Central Park.")

data_dict = {
    "Colors": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

data_frame = pandas.DataFrame(data_dict)
data_csv = data_frame.to_csv("Squirrels_count_in_central_park.csv")
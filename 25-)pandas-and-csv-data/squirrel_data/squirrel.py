import pandas

data = pandas.read_csv(
    "25-)pandas-and-csv-data\squirrel_data\squirrel_data.csv")
squirrel_fur = data["Primary Fur Color"]
fur_data_dict = {
    "Fur Color": ["gray", 'cinnamon', 'black'],
    "Count": [0, 0, 0]
}
for fur in squirrel_fur:
    if fur == "Gray":
        fur_data_dict["Count"][0] += 1
    elif fur == "Cinnamon":
        fur_data_dict["Count"][1] += 1
    elif fur == "Black":
        fur_data_dict["Count"][2] += 1
# Another solution
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_squirrel_fur = pandas.DataFrame(fur_data_dict)
data_squirrel_fur.to_csv(
    "25-)pandas-and-csv-data\squirrel_data\squirrel_fur_data.csv")

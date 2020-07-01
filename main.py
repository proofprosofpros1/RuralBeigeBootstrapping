import pandas
from pandas import DataFrame

teams = ["N/A", "Pickle Rickies", "HMMph h", "Dilly Pick", "Fake Sport", "Pickle Ball", "Yeeeee"]
wins = [0,7,13,14,21,69,420]
loses = [0,54,3,65,4,756,43]
dataset = list(zip(teams,wins,loses))
df = DataFrame(data = dataset, columns = ["teams", "wins","loses"])
print(dataset)
print(df)
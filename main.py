import pandas as pd
import csv


data=pd.read_csv("squril data.csv")
# data[data.Fur color == ]
# fur_col=data["Primary Fur Color"].tolist()
# print(fur_col)
grey=data[data["Primary Fur Color"] == "Gray"]
red=data[data["Primary Fur Color"] == "Cinnamon"]
black=data[data["Primary Fur Color"] == "Black"]
# print(type(grey))
# print(grey)
# print(red)
# redc=red.count
# print(redc)
red_rows = red['Primary Fur Color'].count()
print(red_rows + 1)
black_rows = black['Primary Fur Color'].count()
print(black_rows + 1)
grey_rows = grey['Primary Fur Color'].count()
print(grey_rows + 1)
# with open("colors.csv","w+") as f:
#     writer = csv.writer(f)
#     writer.writerow(red_rows)
data_dic={
    "fur color": ["grey","black","red" ],
    "count":[red_rows,black_rows,grey_rows]
}
df=pd.DataFrame(data_dic)
df.to_csv("colorss")
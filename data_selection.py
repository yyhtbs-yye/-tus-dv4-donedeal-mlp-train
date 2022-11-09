import pandas as pd
from preproc import *
df = pd.read_csv("DoneDealCarsInDetail.csv")

print(df.columns)
df = df[df["Make"]=="Volkswagen"]
ndf = pd.DataFrame()
ndf["Price"] = df["Price"].apply(pricePreproc).to_list()
ndf["Mileage"] = df["Mileage"].apply(mileagePreproc).to_list()
ndf["Year"] = df["Year"].apply(yearPreproc).to_list()
ndf["EngSize"] = df["Engine Size (Litres)"].apply(engSizePreproc).to_list()
ndf["Power"] = df["Power"].apply(powerPreproc).to_list()

ndf.dropna(inplace=True)

ndf.to_csv("DoneDealCars4Regression.csv")
a = 1

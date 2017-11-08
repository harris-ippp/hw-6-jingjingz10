import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import glob

data = glob.glob("*.csv")
election=[]

for i in data:


    header = pd.read_csv(i, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv(i, index_col = 0,thousands = ",", skiprows = [1])

    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = i[-8:-4:1]
    election.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])
df = pd.concat(election)

#Republican share
df["Republican Share"]=df["Republican"]/df["Total Votes Cast"]

#accomack_county
accomack_county = df.loc['Accomack County'].sort_values(by = 'Year', ascending = True)
figure1 = accomack_county.plot(x ="Year", y="Republican Share")
plt.title("Republican Share of Accomack County")
figure1.get_figure().savefig('accomack_county.pdf')

#albemarle_county
albemarle_county = df.loc['Albemarle County'].sort_values(by = 'Year', ascending = True)
figure2 = albemarle_county.plot(x ="Year", y="Republican Share")
plt.title("Republican Share of Albemarle County")
figure2.get_figure().savefig('albemarle_county.pdf')

#alexandria_city
alexandria_city = df.loc['Alexandria City'].sort_values(by = 'Year', ascending = True)
figure3 = alexandria_city.plot(x ="Year", y="Republican Share")
plt.title("Republican Share of Alexandria City")
figure3.get_figure().savefig('alexandra_city.pdf')

#alleghany_county
alleghany_county = df.loc['Alleghany County'].sort_values(by = 'Year', ascending = True)
figure4 = alleghany_county.plot(x ="Year", y="Republican Share")
plt.title("Republican Share of Alleghany County")
figure4.get_figure().savefig('alleghany_county.pdf')

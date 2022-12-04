import pandas as pd
import matplotlib.pyplot as plt

lista = pd.DataFrame({})
names = []
companies = []
file = pd.read_csv('flights.csv')
df = pd.DataFrame(file)


for i in range(len(df["CARGO"])):
        if df["CARGO"][i] not in names:
               names.append(df["CARGO"][i])

for name in names:
        company = df.loc[df["CARGO"] == name]
        print(" Avio company:", name, "\n" , "Number of flights:", len(company), "\n",
              "Full price:" , company["PRICE"].sum(), "\n", "Full weight:", company["WEIGHT"].sum(), "\n")
        companies.append([name,len(company), company["PRICE"].sum(),company["WEIGHT"].sum()])

index = []
flights = []
price = []
weight = []
for i in companies:
    index.append(i[0])
    flights.append(i[1])
    price.append(i[2])
    weight.append(i[3])

df1 = pd.DataFrame({'Number of flights': flights}, index=index)
df2 = pd.DataFrame({'Price': price}, index=index)
df3 = pd.DataFrame({'Weight': weight}, index=index)
ax1 = df1.plot.bar(rot=0)
plt.savefig("flights.png")
ax2 = df2.plot.bar(rot=0)
plt.savefig("price.png")
ax3 = df3.plot.bar(rot=0)
plt.savefig("weight.png")
plt.show()

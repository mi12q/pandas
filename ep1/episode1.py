import pandas as pd
ok_val = []
suma = 0
file = pd.read_csv ('transactions.csv')
df = pd.DataFrame(file)

ok_status = df.loc[df["STATUS"] == "OK"]
umbrella = df.loc[df["CONTRACTOR"] == "Umbrella, Inc"]
ok_val.sort(reverse= True)
print("3 самых крупных платежа из реально проведённых (status OK):\n",
      (ok_status["SUM"].nlargest(n = 3, keep = "first").to_string(index=False)))
print("Полная суммa реально проведённых платежей в адрес Umbrella, Inc:", umbrella["SUM"].sum())




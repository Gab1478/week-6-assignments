# D1
import pandas as pd
people = pd.series([87, 120, 45])
print(people)

# D2
import pandas as pd
data = {
    "label": ["R-001", "R-002","R-003"]
    "value": [87,120,45],
    "limit": [100, 100, 100]
}
df = pd.DataFrame(data)

print(df)
print(df.shape)

# D3
import pandas as pd

df=pd.read_csv("records_sample.csv")

print(df)
print(df.dtypes)



# D4
df["percentage"]=(df["value"] / df["limit"]) * 100
print(df)

# D5
print(df.iloc[0]["label"])
print(df.loc[2, "value"])

# D6
print(df["label"])
print(df[["label", "percentage"]])

# D7
df_filtered= df[df["percentage"] >= 100]
print(df_filtered)
print(len(df_filtered))

# D8
print(df[(df["percentage"] >= 90) & (df["percentage"] < 100)])
print(df[(df["percentage"] < 50) | (df["percentage"] > 110)])


# D9
df_sorted = df.sort_values(by="percentage", ascending=False)
print(df_sorted)


# D10
printdf(group by)


# D11
double = lambda x: x * 2
print(double(21))
def double_def(x):
    return x *2
print(double_def(21))


# D12
df['status'] = df['amount_spent'].apply(lambda x: 'OVER_LIMIT' if x >= 100 else('WARNING' if x >= 50 else 'OK'))
printdf[['name','status']]
print(df['status'].value_counts())


# D13
print(df.describe())
df.to_csv('summary_output.csv', index=False)


# D14
import matplotlib.pyplot as plt
df['status'].value_counts().plot(kind='bar')
plt.title('Status Counts')
plt.show()

# C1
df= pd.read_csv


# C2
print(df.groupby('staus')['amount_spent'].mean().round(1))
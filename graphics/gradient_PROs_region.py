import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "C://dev//Balancing Philosophy TKA Screening 12.30.2024.xlsx"
df = pd.read_excel(file_path, sheet_name="ANP final inclusions")

df["PROs?"] = df["PROs?"].astype(str).str.split("\n")

all_outcomes = sorted(set(outcome for outcomes in df["PROs?"] for outcome in outcomes))

country_matrix = pd.DataFrame(0, index=df["Region"].unique(), columns=all_outcomes)

for _, row in df.iterrows():
    for outcome in row["PROs?"]:
        country_matrix.at[row["Region"], outcome] += 1  # Aggregate PRO counts per country

print("PRO Counts by Region:")
print(country_matrix)

plt.figure(figsize=(18, 12))
sns.heatmap(country_matrix, cmap="Blues", linewidths=0.5, linecolor="gray", cbar=True)

plt.xlabel("PROs")
plt.ylabel("Region")
plt.xticks(rotation=90)
plt.title("Frequency of PRO Mentions by Region")

plt.show()

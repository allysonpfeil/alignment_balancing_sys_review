import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "C://dev//Balancing Philosophy TKA Screening 12.30.2024.xlsx"
df = pd.read_excel(file_path, sheet_name="ANP final inclusions")
# df = df[df["Gap Balancing Type (symmetric v asymmetric)"] != "not specified"]
# Split on newline (Alt+Enter in Excel) (.split('\n') in Python)
df["PROs??"] = df["PROs??"].astype(str).str.split("\n")  

all_outcomes = sorted(set(outcome for outcomes in df["PROs??"] for outcome in outcomes))

binary_matrix = pd.DataFrame(0, index=df["Author"], columns=all_outcomes)
for i, row in df.iterrows():
    for outcome in row["PROs??"]:
        binary_matrix.at[row["Author"], outcome] = 1

column_sums = binary_matrix.sum(axis=0)
for pro, count in column_sums.items():
    print(f"{pro}: {count}")

plt.figure(figsize=(18, 18))
sns.heatmap(binary_matrix, cmap="Blues", linewidths=0.5, linecolor="gray", cbar=False)
plt.xticks(rotation=90)
plt.title("PROs Across Papers")
plt.show()

print(all_outcomes)

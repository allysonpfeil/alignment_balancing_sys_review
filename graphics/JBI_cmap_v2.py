import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

file_path = "C://dev//JBI data.xlsx"
df = pd.read_excel(file_path)

def convert_to_numeric(value):
    if value == "Y":
        return 1
    elif value == "N":
        return 0
    elif value == "N/A":
        return 2
    else:
        return 2

data_columns = df.columns[1:]
df[data_columns] = df[data_columns].applymap(convert_to_numeric)

df.set_index(df.columns[0], inplace=True)

custom_cmap = mcolors.ListedColormap(["#bf0000", "#02c100", "#a9a9a9"])

plt.figure(figsize=(10, len(df) * 0.5))
ax = sns.heatmap(df, cmap=custom_cmap, linewidths=3, linecolor="white", square=False, annot=False, cbar=False)

ax.xaxis.tick_top()

ax.set_yticklabels(df.index, rotation=0)

plt.xlabel("")
plt.ylabel("")
plt.title("")

for spine in ax.spines.values():
    spine.set_visible(False)
    spine.set_edgecolor("gray")
    spine.set_linewidth(2)

plt.show()

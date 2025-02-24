import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

file_path = "C://dev//Balancing Philosophy TKA Screening 12.30.2024.xlsx"
df = pd.read_excel(file_path, sheet_name="ANP final inclusions")

no_values = {"N/R"} 

def convert_to_binary(value):
    return 0 if value in no_values else 1

data_columns = ["Robot System",
                "Robot Software Version",
                "Implant Type", 
                "Surgeon(s) Experience",
                "Surgeon(s) Volume"
                ]

df[data_columns] = df[data_columns].applymap(convert_to_binary)

df.set_index("Concat", inplace=True)

heatmap_data = df[data_columns]
custom_cmap = mcolors.LinearSegmentedColormap.from_list("custom", ["#bad6eb", "#356384"])

plt.figure(figsize=(10, len(df) * 0.5))
ax = sns.heatmap(heatmap_data, cmap=custom_cmap, linewidths=0.5, annot=False, cbar=False)
ax.xaxis.tick_top()
#plt.title("Binary Heatmap of Yes/No Data")
#plt.xlabel("Data Columns")
#plt.ylabel("Labels")
plt.show()

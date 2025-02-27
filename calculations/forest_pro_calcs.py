import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2, norm

def compute_summary_stats(group):
    weights = 1 / (group['StDev/Weighted StDev'] ** 2)
    weighted_mean = np.sum(weights * group['Ave/Weighted Ave']) / np.sum(weights)
    weighted_var = 1 / np.sum(weights)
    weighted_std = np.sqrt(weighted_var)
    
    ci_low, ci_high = weighted_mean - 1.96 * weighted_std, weighted_mean + 1.96 * weighted_std
    
    # heterogeneity (Cochran's Q test)
    Q = np.sum(weights * (group['Ave/Weighted Ave'] - weighted_mean) ** 2)
    df = len(group) - 1
    p_value_heterogeneity = 1 - chi2.cdf(Q, df)  # p-value for heterogeneity
    I2 = max(0, (Q - df) / Q) * 100 if Q > df else 0
    
    # test for overall effect (Z-test for weighted mean)
    standard_error = weighted_std / np.sqrt(np.sum(weights))
    z_stat = weighted_mean / standard_error
    p_value_effect = 2 * (1 - norm.cdf(np.abs(z_stat)))
    
    return weighted_mean, weighted_std, ci_low, ci_high, I2, p_value_heterogeneity, p_value_effect, standard_error

def create_forest_plots(file_path):
    data = pd.read_excel(file_path)
    grouped = data.groupby(['Alignment', 'Score Name'])
    
    for (alignment, score), group in grouped:
        if len(group) < 3:
            continue
        
        weighted_mean, weighted_std, ci_low, ci_high, I2, p_value_heterogeneity, p_value_effect, standard_error = compute_summary_stats(group)
        
        fig, ax = plt.subplots(figsize=(8, 6))
        
        y_pos = range(len(group))
        means = group['Ave/Weighted Ave']
        std_devs = group['StDev/Weighted StDev']
        authors = group['Author']
        
        print(f"Summary Statistics for {alignment} - {score}:")
        for idx, row in group.iterrows():
            article_mean = row['Ave/Weighted Ave']
            article_std = row['StDev/Weighted StDev']
            article_count = row['Count/Total Count']
            print(f"  {row['Author']}: Mean = {article_mean:.2f}, Std Dev = {article_std:.2f}, count = {article_count:.2f}")
        
        print(f"\nTotal Summary for {alignment} - {score}:")
        print(f"  Weighted Mean: {weighted_mean:.2f}")
        print(f"  Weighted Std Dev: {weighted_std:.2f}")
        print(f"  95% CI: ({ci_low:.2f}, {ci_high:.2f})")
        print(f"  Heterogeneity (I²): {I2:.2f}%")
        print(f"  Chi-squared (Q): {weighted_mean:.2f}, p-value for heterogeneity: {p_value_heterogeneity:.4f}")
        print(f"  Test for overall effect: Z = {weighted_mean/standard_error:.2f}, p-value: {p_value_effect:.4f}\n")
        
        # article names
        ax.errorbar(means, y_pos, xerr=std_devs, fmt='s', color='black', label=score, markersize=5)
        
        ci_width = ci_high - ci_low
        diamond_size = ci_width * 50

        # total weighted mean
        ax.scatter(weighted_mean, -1, color='red', zorder=5, label='Total Weighted Mean', s=50, edgecolor='black', marker='D')
        
        ax.set_yticks(y_pos)
        ax.set_yticklabels(authors)
        ax.set_xlabel(score)
        ax.set_title(f'{alignment} - {score}, 95% CI')
                     # \nWeighted Mean: {weighted_mean:.2f} (95% CI: {ci_low:.2f}, {ci_high:.2f})\nHeterogeneity (I²): {I2:.2f}%')
        
        # ax.legend()
        
        # plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

file_path = 'C://dev//balancing_pro_data.xlsx'
create_forest_plots(file_path)

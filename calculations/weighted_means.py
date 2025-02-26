import numpy as np

def combine_means_stds(n1, mean1, std1, n2, mean2, std2, n3=None, mean3=None, std3=None):
    """
    Combine means and standard deviations for two or three groups.
    
    """
    if n3 is None:
        total_n = n1 + n2
        weighted_mean = (n1 * mean1 + n2 * mean2) / total_n
        weighted_var = ((n1 - 1) * std1**2 + (n2 - 1) * std2**2 + 
                        n1 * (mean1 - weighted_mean)**2 + 
                        n2 * (mean2 - weighted_mean)**2) / (total_n - 1)
    else:
        total_n = n1 + n2 + n3
        weighted_mean = (n1 * mean1 + n2 * mean2 + n3 * mean3) / total_n
        weighted_var = ((n1 - 1) * std1**2 + (n2 - 1) * std2**2 + (n3 - 1) * std3**2 +
                        n1 * (mean1 - weighted_mean)**2 +
                        n2 * (mean2 - weighted_mean)**2 +
                        n3 * (mean3 - weighted_mean)**2) / (total_n - 1)

    combined_std = np.sqrt(weighted_var)

    print(f"Total Sample Size: {total_n}")
    print(f"Combined Mean: {weighted_mean:.2f}")
    print(f"Combined Standard Deviation: {combined_std:.2f}")
    
    return weighted_mean, combined_std, total_n
# 2 group comparison
combine_means_stds(n1=80, mean1=88.8, std1=10.0, 
                   n2=84, mean2=86.7, std2=14.0)

# 3 group comparison
# combine_means_stds(n1=283, mean1=10.9, std1=17.9, 
#                    n2=183, mean2=13.1, std2=21.5, 
#                    n3=187, mean3=10.1, std3=20.6)

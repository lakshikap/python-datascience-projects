import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (assuming it's saved as 'lung_cancer_data.csv')
df = pd.read_csv('lungcancer.csv')
lc_corr2 = pd.DataFrame(df)

# Convert 'Lung Cancer' column to binary (1 = No, 2 = Yes) for correlation analysis
lc_corr2['LUNG_CANCER'] = lc_corr2['LUNG_CANCER'].map({'YES': 2, 'NO': 1})

# Select only symptoms and 'Lung Cancer' columns for correlation
symptoms = ['YELLOW_FINGERS', 'ANXIETY', 'COUGHING', 'WHEEZING', 'CHEST_PAIN', 'LUNG_CANCER']
df_symptoms = lc_corr2[symptoms]

# Calculate the correlation matrix
correlation_matrix = df_symptoms.corr()

# Plotting the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation between Symptoms and Lung Cancer Diagnosis')
plt.show()

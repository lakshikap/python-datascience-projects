import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
disease_data = pd.read_csv('heart_disease.csv')

# Convert Yes and No to 1 and 0
disease_data['HeartDisease'] = disease_data['HeartDisease'].map({'No': 0, 'Yes': 1})

# Select relevant columns for correlation analysis
columns_of_interest = ['HeartDisease', 'BMI', 'PhysicalHealth', 'MentalHealth', 'SleepTime']
df_corr = disease_data[columns_of_interest]

# Calculate the correlation matrix
corr_matrix = df_corr.corr()

# Plotting the correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt=".2f")
plt.title('Correlation Heatmap for Heart Disease and Other Patient Features')
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
disease_data = pd.read_csv('heart_disease.csv')

# Plotting the count plot
plt.figure(figsize=(10, 6))
sns.countplot(data=disease_data, x='Stroke', hue='HeartDisease', palette='viridis', dodge=True)
plt.title('Count Plot of Stroke Categorized by Heart Disease')
plt.xlabel('Stroke History')
plt.ylabel('Count')
plt.legend(title='Heart Disease', loc='upper right')
plt.show()

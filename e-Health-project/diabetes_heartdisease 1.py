import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('heart_disease.csv')

# Plotting the count plot
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Diabetic', hue='HeartDisease', palette='viridis', dodge=True)
plt.title('Count Plot of Diabetic Status Categorized by Heart Disease')
plt.xlabel('Diabetic Status')
plt.ylabel('Count')
plt.legend(title='Heart Disease', loc='upper right')
plt.show()

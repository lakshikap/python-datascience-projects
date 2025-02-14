import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
disease_data = pd.read_csv("heart_disease.csv")
print(disease_data.head)
print(disease_data.describe)
print(disease_data.columns)

# Select relevant columns
columns_of_interest = ['HeartDisease', 'Asthma', 'KidneyDisease', 'SkinCancer']
disease_data = disease_data[columns_of_interest]

# Melt the DataFrame for better visualization
df_melted = disease_data.melt(id_vars='HeartDisease', value_vars=['Asthma', 'KidneyDisease', 'SkinCancer'],
                              var_name='Condition', value_name='Presence')

# Plotting
plt.figure(figsize=(12, 6))
sns.countplot(data=df_melted, x='Condition', hue='HeartDisease', dodge=True, palette='viridis')
plt.title('Count Plot of Asthma, Kidney Disease, and Skin Cancer by Heart Disease Status')
plt.xlabel('Condition')
plt.ylabel('Count')
plt.legend(title='Heart Disease', loc='upper right')
plt.show()

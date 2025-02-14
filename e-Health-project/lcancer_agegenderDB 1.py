import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (assuming it's saved as 'lung_cancer_data.csv')
df = pd.read_csv("lungcancer.csv")

lcancer = pd.DataFrame(df)

# Map Gender and Smoking values for better readability
lcancer['SMOKING'] = lcancer['SMOKING'].map({2: 'Yes', 1: 'No'})

# Gender and Age Distribution #

# Plotting Gender distribution
plt.figure(figsize=(10, 5))
sns.countplot(data=lcancer, x='GENDER', palette='pastel')
plt.title('Gender Distribution of Patients')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Plotting Age distribution with gender overlay
plt.figure(figsize=(10, 5))
sns.histplot(data=lcancer, x='AGE', hue='GENDER', kde=True, palette='muted', multiple='stack')
plt.title('Age Distribution by Gender')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Smoking vs. Non-Smoking Breakdown by Gender and Age #

# Grouping data by Smoking status, Gender, and Age
plt.figure(figsize=(10, 6))
sns.boxplot(data=lcancer, x='SMOKING', y='AGE', hue='GENDER', palette='coolwarm')
plt.title('Smoking Status by Gender and Age')
plt.xlabel('Smoking Status')
plt.ylabel('Age')
plt.legend(title='Gender')
plt.show()

# Analyzing Lung Cancer Diagnosis by Smoking Status
plt.figure(figsize=(10, 5))
sns.countplot(data=lcancer, x='SMOKING', hue='LUNG_CANCER', palette='Set2')
plt.title('Lung Cancer Diagnosis by Smoking Status')
plt.xlabel('Smoking Status')
plt.ylabel('Count')
plt.legend(title='Lung Cancer')
plt.show()

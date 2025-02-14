import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (ensure the file path is correct)
df = pd.read_csv('lungcancer.csv')

# Strip any extra spaces from column names to avoid errors
df.columns = df.columns.str.strip()

# Preview the first few rows of the dataframe to check the column names and data
print("Dataset preview:\n", df.head())

# Assuming 'LUNG_CANCER' contains 'YES'/'NO' for lung cancer diagnosis
df['LUNG_CANCER'] = df['LUNG_CANCER'].map({'YES': 1, 'NO': 0})

# List of symptoms to analyze that are most likely to affect treatment
# (Update based on your actual dataset)
treatment_symptoms = ['ANXIETY', 'CHRONIC_DISEASE', 'COUGHING', 'YELLOW_FINGERS', 'WHEEZING', 'CHEST_PAIN', 'FATIGUE']

# Check if all symptoms are present in the dataset
missing_columns = [symptom for symptom in treatment_symptoms if symptom not in df.columns]
if missing_columns:
    print(f"Warning: The following symptom columns are missing: {missing_columns}")

# Convert symptom columns to 1/0 for easier analysis (YES = 1, NO = 0)
for symptom in treatment_symptoms:
    if symptom in df.columns:
        df[symptom] = df[symptom].map({'YES': 1, 'NO': 0})
    else:
        print(f"Warning: Column {symptom} is missing in the dataset.")

# Filter out patients with lung cancer (LUNG_CANCER == 1)
lung_cancer_patients = df[df['LUNG_CANCER'] == 1]

# Calculate the prevalence of each symptom in lung cancer patients
symptom_prevalence = lung_cancer_patients[treatment_symptoms].mean() * 100  # Convert to percentage

# Sort symptoms by prevalence
symptom_prevalence_sorted = symptom_prevalence.sort_values(ascending=False)

# Plot the prevalence of symptoms in lung cancer patients
plt.figure(figsize=(10, 6))
symptom_prevalence_sorted.plot(kind='bar', color='salmon', width=0.8)

# Labeling the plot
plt.title('Prevalence of Symptoms in Patients with Lung Cancer (Treatment Considerations)')
plt.xlabel('Symptom')
plt.ylabel('Prevalence (%)')
plt.xticks(rotation=45)
plt.ylim(0, 100)

# Adding percentage labels on top of each bar
for i, v in enumerate(symptom_prevalence_sorted):
    plt.text(i, v + 1, f'{v:.1f}%', ha='center', color='black')

# Display the plot
plt.tight_layout()
plt.show()

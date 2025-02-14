import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (assuming it's saved as 'lung_cancer_data.csv')
df = pd.read_csv('lungcancer.csv')
lc_corr2 = pd.DataFrame(df)

# Convert 'Lung Cancer' to binary for consistency in counting
lc_corr2['LUNG_CANCER'] = lc_corr2['LUNG_CANCER'].map({'YES': 2, 'NO': 1})

# Separate the dataset by lung cancer diagnosis
lung_cancer_yes = lc_corr2[lc_corr2['LUNG_CANCER'] == 2]
lung_cancer_no = lc_corr2[lc_corr2['LUNG_CANCER'] == 1]

# Calculate the incidence of chronic diseases and allergies
chronic_disease_yes = lung_cancer_yes['CHRONIC_DISEASE'].value_counts(normalize=True).get(2, 0) * 100
allergy_yes = lung_cancer_yes['ALLERGY'].value_counts(normalize=True).get(2, 0) * 100

chronic_disease_no = lung_cancer_no['CHRONIC_DISEASE'].value_counts(normalize=True).get(2, 0) * 100
allergy_no = lung_cancer_no['ALLERGY'].value_counts(normalize=True).get(2, 0) * 100

# Create a DataFrame for visualization
incidence_df = pd.DataFrame({
    'Condition': ['CHRONIC_DISEASE', 'ALLERGY'],
    'With Lung Cancer (%)': [chronic_disease_yes, allergy_yes],
    'Without Lung Cancer (%)': [chronic_disease_no, allergy_no]
})

# Plotting the incidence of chronic disease and allergy with lung cancer status
plt.figure(figsize=(10, 6))
bar_width = 0.35  # Width of each bar

# Position of the bars on the x-axis
index = range(len(incidence_df['Condition']))

# Plot bars for patients with lung cancer
plt.bar(index, incidence_df['With Lung Cancer (%)'], width=bar_width, label='With Lung Cancer', color='salmon')

# Plot bars for patients without lung cancer
plt.bar([i + bar_width for i in index], incidence_df['Without Lung Cancer (%)'], width=bar_width,
        label='Without Lung Cancer', color='skyblue')

# Labeling
plt.title('Incidence of Chronic Disease and Allergy in Patients With and Without Lung Cancer')
plt.xlabel('Condition')
plt.ylabel('Incidence (%)')
plt.xticks([i + bar_width / 2 for i in index], incidence_df['Condition'], rotation=45)
plt.legend()
plt.ylim(0, 100)  # Set y-axis limit to 100% for percentage

# Adding data labels on each bar
for i, val in enumerate(incidence_df['With Lung Cancer (%)']):
    plt.text(i, val + 1, f'{val:.1f}%', ha='center', color='salmon')
for i, val in enumerate(incidence_df['Without Lung Cancer (%)']):
    plt.text(i + bar_width, val + 1, f'{val:.1f}%', ha='center', color='skyblue')

plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (assuming it's saved as 'lung_cancer_data.csv')
df = pd.read_csv('lungcancer.csv')

# Sample DataFrame structure (for example)
# Uncomment above to load real data

lc_symp = pd.DataFrame(df)

# Map symptoms to binary values for prevalence calculation (1 = No, 2 = Yes)
symptoms = ['YELLOW_FINGERS', 'ANXIETY', 'COUGHING', 'WHEEZING', 'CHEST_PAIN']

# Calculate prevalence of each symptom (percentage of patients with the symptom)
prevalence = {symptom: (lc_symp[symptom].value_counts(normalize=True)[2] * 100) for symptom in symptoms}

# Convert the prevalence dictionary to a DataFrame for easy plotting
prevalence_df = pd.DataFrame(list(prevalence.items()), columns=['Symptom', 'Prevalence (%)'])

# Plotting the prevalence rates of symptoms
plt.figure(figsize=(10, 6))
bars = plt.bar(prevalence_df['Symptom'], prevalence_df['Prevalence (%)'], color='teal')
plt.title('Prevalence Rates of Symptoms in Lung Cancer Patients')
plt.xlabel('Symptom')
plt.ylabel('Prevalence (%)')
plt.ylim(0, 100)  # Ensuring the y-axis is percentage-based
plt.xticks(rotation=45)
# Description of the chart
plt.figtext(0.5, 0.01,
            "This chart displays the prevalence rates of various symptoms in lung cancer patients. "
            "Each bar represents the percentage of lung cancer patients experiencing each symptom. "
            "This visualization helps identify which symptoms are most common in lung cancer patients, "
            "which can be important for treatment considerations and patient management strategies.",
            ha='center', va='center', fontsize=12, wrap=True)

# Add percentage labels on each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2, height, f'{height:.1f}%',
        ha='center', va='bottom', fontsize=10
    )

plt.show()

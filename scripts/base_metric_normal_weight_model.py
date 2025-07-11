# This is to create a standard distibution of data to reference against for fat loss tracking
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the CSV file, skipping the extra header line and keeping only needed columns
df = pd.read_csv('/Users/callummelrose/Documents/BodyFat - Extended 2.csv', skiprows=1, usecols=['BodyFat', 'Sex', 'Weight', 'Height'])


# Convert data to numeric in case there are formatting issues
df['BodyFat'] = pd.to_numeric(df['BodyFat'], errors='coerce')
df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
df['Height'] = pd.to_numeric(df['Height'], errors='coerce')

# Drop rows with missing values in key columns
df = df.dropna(subset=['BodyFat', 'Sex', 'Weight'])

# Plot 1: Distribution of weight
plt.figure(figsize=(8, 5))
sns.histplot(df['Weight'], bins=30, kde=True)
plt.title('Weight Distribution')
plt.xlabel('Weight (kg)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: Body fat % by sex
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Sex', y='BodyFat')
plt.title('Body Fat % by Sex')
plt.xlabel('Sex')
plt.ylabel('Body Fat %')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 3: Relationship between weight and body fat %
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Weight', y='BodyFat', hue='Sex', alpha=0.7)
plt.title('Relationship Between Weight and Body Fat %')
plt.xlabel('Weight (kg)')
plt.ylabel('Body Fat %')
plt.grid(True)
plt.tight_layout()
plt.show()


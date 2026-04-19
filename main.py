# Step 1: Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Step 2: Load the dataset
# If using seaborn built-in dataset
tips = sns.load_dataset("tips")
# Step 3: Display first 5 rows of dataset
print("First 5 rows of dataset:")
print(tips.head())
# Step 4: Check dataset information
print("\nDataset Information:")
print(tips.info())
# Step 5: Check missing values
print("\nMissing Values:")
print(tips.isnull().sum())
# Step 6: Basic statistical summary
print("\nStatistical Summary:")
print(tips.describe())
# Step 7: Relationship between total bill and tip
plt.figure(figsize=(6,4))
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Total Bill vs Tip Amount")
plt.show()
11
# Step 8: Average tip based on gender
plt.figure(figsize=(6,4))
sns.barplot(x="sex", y="tip", data=tips)
plt.title("Average Tip by Gender")
plt.show()
# Step 9: Tips based on day
plt.figure(figsize=(6,4))
sns.barplot(x="day", y="tip", data=tips)
plt.title("Tips by Day")
plt.show()
# Step 10: Tips based on time (Lunch/Dinner)
plt.figure(figsize=(6,4))
sns.barplot(x="time", y="tip", data=tips)
plt.title("Tips by Time")
plt.show()
# Step 11: Group size vs tip
plt.figure(figsize=(6,4))
sns.boxplot(x="size", y="tip", data=tips)
plt.title("Group Size vs Tip")
plt.show()
# Step 12: Correlation heatmap
plt.figure(figsize=(6,4))
sns.heatmap(tips.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()
# Step 13: Conclusion message
print("\nData analysis completed successfully.")

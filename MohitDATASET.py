import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
# Load dataset
df = pd.read_csv("students_performance_dataset.csv")
 
# Preview
print(df.head())
print(df.info())
 
# -------------------------------
# 1. HANDLE MISSING VALUES
# -------------------------------
print("\nMissing Values:\n", df.isnull().sum())
 
# Fill numeric columns with mean
for col in df.select_dtypes(include=np.number).columns:
    df[col].fillna(df[col].mean(), inplace=True)
 
# Fill categorical columns with mode
for col in df.select_dtypes(include='object').columns:
    df[col].fillna(df[col].mode()[0], inplace=True)
 
# -------------------------------
# 2. OUTLIER DETECTION (IQR METHOD)
# -------------------------------
def remove_outliers(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
 
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
 
    return df[(df[col] >= lower) & (df[col] <= upper)]
 
# Apply on numeric columns
for col in df.select_dtypes(include=np.number).columns:
    df = remove_outliers(df, col)
 
# -------------------------------
# 3. BAR CHART
# Example: Gender distribution
# -------------------------------
plt.figure()
df['Gender'].value_counts().plot(kind='bar')
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
 
# -------------------------------
# 4. LINE CHART
# Example: Study hours trend
# -------------------------------
plt.figure()
df['How many hour do you study daily?'].plot(kind='line')
plt.title("Study Hours Trend")
plt.xlabel("Index")
plt.ylabel("Hours")
plt.show()
 
# -------------------------------
# 5. PIE CHART
# Example: Scholarship distribution
# -------------------------------
plt.figure()
df['Do you have meritorious scholarship ?'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Scholarship Distribution")
plt.ylabel("")
plt.show()
 
# -------------------------------
# 6. HISTOGRAM
# Example: Age distribution
# -------------------------------
plt.figure()
plt.hist(df['Age'], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
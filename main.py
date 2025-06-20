import pandas as pd
from src import imputation
import missingno as msno
import matplotlib.pyplot as plt
import time

# === 1. Load dataset ===
print("📥 Loading dataset...\n")
df = pd.read_csv("data/recipeData.csv", encoding="latin1")

# === 2. Show missing values before ===
print("❌ Missing values BEFORE imputation:\n")
missing_before = df.isnull().sum()
missing_before = missing_before[missing_before > 0]
print(missing_before.sort_values(ascending=False))

# === 3. Horizontal bar chart of missing values ===
plt.figure(figsize=(10, 6))
missing_before.sort_values().plot(kind='barh', color='salmon')
plt.title("Missing Values per Column (Before Imputation)")
plt.xlabel("Number of Missing Values")
plt.ylabel("Columns")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("images/missing_before_barh.png")
plt.show()

# === 4. Generate and display missing value matrix (before) ===
plt.figure()
msno.matrix(df)
plt.title("Before Imputation")
plt.savefig("images/before_imputation.png")
plt.show()

# === 5. Simulate progress ===
print("\n⏳ Please wait, filling in the data...\n")
time.sleep(2)

# === 6. Apply imputations ===
df = imputation.imput_boilgravity(df)
df = imputation.imput_mashthickness(df)
df = imputation.imput_knn(df, ['PrimaryTemp', 'PitchRate', 'OG', 'ABV', 'IBU'])
df = imputation.imput_categorical(df)
df = imputation.imput_userid(df)

# === 7. Show missing values after ===
print("✅ Missing values AFTER imputation:\n")
print(df.isnull().sum())

# === 8. Generate and display missing value matrix (after) ===
plt.figure()
msno.matrix(df)
plt.title("After Imputation")
plt.savefig("images/after_imputation.png")
plt.show()

# === 9. Save final dataset ===
df.to_csv("data/recipeData_imputed.csv", index=False)
print("\n💾 File saved as 'recipeData_imputed.csv'.")
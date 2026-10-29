from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_path = Path(__file__).with_name("sample_data_assignment_07(1).csv")
df = pd.read_csv(csv_path)

# Check that the required columns exist
required = ["Student", "Maths", "Python", "Attendance", "City"]
missing = [c for c in required if c not in df.columns]   # columns is an attribute, not a method
if missing:
    raise SystemExit(f"Missing columns: {missing}")

print("\nDataset:")
print(df)

# Average values
print("\nAverage Maths marks   :", round(df["Maths"].mean(), 2))
print("Average Python marks  :", round(df["Python"].mean(), 2))
print("Average Attendance    :", round(df["Attendance"].mean(), 2))

# Line Plot
plt.figure(figsize=(7, 4.5))
plt.plot(df["Student"], df["Python"], marker="o", label="Python Marks")
plt.title("Python Marks of Students")
plt.xlabel("Student")
plt.ylabel("Python Marks")
plt.legend()
plt.grid(True)
plt.show()

# Bar Plot
plt.figure(figsize=(7, 4.5))
plt.bar(df["Student"], df["Maths"], label="Maths Marks")
plt.title("Maths Marks of Students")
plt.xlabel("Student")
plt.ylabel("Maths Marks")
plt.legend()
plt.show()

# Scatter Plot
plt.figure(figsize=(7, 4.5))
plt.scatter(df["Maths"], df["Python"], s=70, label="Students")
plt.title("Maths vs Python Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Python Marks")
plt.legend()
plt.grid(True)
plt.show()

# Heatmap
correlation = df[["Maths", "Python", "Attendance"]].corr()
print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(6.5, 5))
sns.heatmap(correlation, annot=True, cmap="Blues", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()

# Extension 1: Histogram of Python marks
plt.figure(figsize=(7, 4.5))
plt.hist(df["Python"], bins=5, edgecolor="black", label="Python Marks")
plt.title("Histogram of Python Marks")
plt.xlabel("Python Marks")
plt.ylabel("Number of Students")
plt.legend()
plt.show()

# Extension 2: Box plot of Maths and Python marks
plt.figure(figsize=(7, 4.5))
plt.boxplot([df["Maths"], df["Python"]])
plt.xticks([1, 2], ["Maths", "Python"])
plt.title("Box Plot of Maths and Python Marks")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# Extension 3: Pie chart of students per city
city_counts = df["City"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(city_counts, labels=city_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Number of Students from Each City")
plt.legend(city_counts.index, title="City", loc="best")
plt.show()

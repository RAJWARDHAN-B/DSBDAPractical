# ==========================================================
# ADULT / CENSUS BUREAU DATASET VISUALIZATION USING PYTHON
# ==========================================================

# OBJECTIVES:
# a. Histograms
# b. Dot Plots
# c. Bar Plots
# d. Line Charts
# e. Histogram + Scatter Plot + Box Plot
# f. Pie Charts
# g. Box Plots
# h. Scatter Plots
# i. Scatterplot with Boxplots

# ==========================================================
# IMPORT LIBRARIES
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ==========================================================
# LOAD DATASET
# ==========================================================

# Ensure adult.csv is in same folder

df = pd.read_csv("adult.csv")

# ==========================================================
# COLUMN NAMES
# ==========================================================

df.columns = [
    'age',
    'workclass',
    'fnlwgt',
    'education',
    'education_num',
    'marital_status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'capital_gain',
    'capital_loss',
    'hours_per_week',
    'native_country',
    'income'
]

# ==========================================================
# BASIC INFORMATION
# ==========================================================

print("\nFIRST 5 RECORDS\n")
print(df.head())

print("\nDATASET INFO\n")
print(df.info())

print("\nSTATISTICAL SUMMARY\n")
print(df.describe())

# ==========================================================
# HISTOGRAMS
# ==========================================================

# Objective:
# Understand distribution of continuous variables

# ----------------------------------------------------------
# HISTOGRAM OF AGE
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(
    df['age'],
    bins=15,
    color='skyblue',
    edgecolor='black'
)

plt.title("Histogram of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

# ----------------------------------------------------------
# HISTOGRAM OF HOURS PER WEEK
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(
    df['hours_per_week'],
    bins=15,
    color='orange',
    edgecolor='black'
)

plt.title("Histogram of Working Hours Per Week")
plt.xlabel("Hours Per Week")
plt.ylabel("Frequency")

plt.show()

# ==========================================================
# DOT PLOT
# ==========================================================

# Objective:
# Visualize spread and density of age values

plt.figure(figsize=(10,2))

plt.plot(
    df['age'],
    np.zeros_like(df['age']),
    'o',
    color='red'
)

plt.title("Dot Plot of Age")
plt.xlabel("Age")
plt.yticks([])

plt.show()

# ==========================================================
# BAR PLOTS
# ==========================================================

# Objective:
# Compare categorical frequencies

# ----------------------------------------------------------
# BAR PLOT OF EDUCATION
# ----------------------------------------------------------

plt.figure(figsize=(12,6))

sns.countplot(
    y='education',
    data=df,
    palette='viridis'
)

plt.title("Education Distribution")
plt.xlabel("Count")
plt.ylabel("Education")

plt.show()

# ----------------------------------------------------------
# BAR PLOT OF INCOME CLASS
# ----------------------------------------------------------

plt.figure(figsize=(6,5))

sns.countplot(
    x='income',
    data=df,
    palette='Set2'
)

plt.title("Income Distribution")
plt.xlabel("Income Class")
plt.ylabel("Count")

plt.show()

# ==========================================================
# LINE CHARTS
# ==========================================================

# Objective:
# Show trends and variations

# ----------------------------------------------------------
# LINE CHART OF AGE
# ----------------------------------------------------------

plt.figure(figsize=(12,5))

plt.plot(
    df['age'],
    color='blue'
)

plt.title("Age Trend")
plt.xlabel("Record Index")
plt.ylabel("Age")

plt.show()

# ----------------------------------------------------------
# LINE CHART OF HOURS PER WEEK
# ----------------------------------------------------------

plt.figure(figsize=(12,5))

plt.plot(
    df['hours_per_week'],
    color='green'
)

plt.title("Hours Per Week Trend")
plt.xlabel("Record Index")
plt.ylabel("Hours Per Week")

plt.show()

# ==========================================================
# PIE CHART
# ==========================================================

# Objective:
# Show percentage distribution of income classes

income_counts = df['income'].value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    income_counts,
    labels=income_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette('pastel')
)

plt.title("Income Class Distribution")

plt.show()

# ==========================================================
# BOX PLOTS
# ==========================================================

# Objective:
# Detect outliers and spread of age values

plt.figure(figsize=(8,5))

sns.boxplot(
    x=df['age'],
    color='lightblue'
)

plt.title("Box Plot of Age")

plt.show()

# ----------------------------------------------------------
# BOXPLOT OF HOURS PER WEEK
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

sns.boxplot(
    x=df['hours_per_week'],
    color='orange'
)

plt.title("Box Plot of Working Hours")

plt.show()

# ==========================================================
# SCATTER PLOTS
# ==========================================================

# Objective:
# Analyze relationship between age and working hours

plt.figure(figsize=(8,5))

plt.scatter(
    df['age'],
    df['hours_per_week'],
    color='red'
)

plt.title("Age vs Hours Per Week")
plt.xlabel("Age")
plt.ylabel("Hours Per Week")

plt.show()

# ----------------------------------------------------------
# SCATTER PLOT OF AGE VS CAPITAL GAIN
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

plt.scatter(
    df['age'],
    df['capital_gain'],
    color='purple'
)

plt.title("Age vs Capital Gain")
plt.xlabel("Age")
plt.ylabel("Capital Gain")

plt.show()

# ==========================================================
# HISTOGRAM + SCATTER + BOXPLOT
# ==========================================================

# Objective:
# Compare distribution, relationship and outliers together

fig, axes = plt.subplots(1, 3, figsize=(18,5))

# ----------------------------------------------------------
# HISTOGRAM
# ----------------------------------------------------------

sns.histplot(
    df['age'],
    kde=True,
    ax=axes[0],
    color='skyblue'
)

axes[0].set_title("Histogram of Age")

# ----------------------------------------------------------
# BOXPLOT
# ----------------------------------------------------------

sns.boxplot(
    x=df['age'],
    ax=axes[1],
    color='orange'
)

axes[1].set_title("Box Plot of Age")

# ----------------------------------------------------------
# SCATTER PLOT
# ----------------------------------------------------------

axes[2].scatter(
    df['age'],
    df['hours_per_week'],
    color='red'
)

axes[2].set_title("Scatter Plot")
axes[2].set_xlabel("Age")
axes[2].set_ylabel("Hours Per Week")

plt.tight_layout()

plt.show()

# ==========================================================
# SCATTERPLOT WITH BOXPLOTS
# ==========================================================

# Objective:
# Analyze relationship and distribution simultaneously

fig = plt.figure(figsize=(10,10))

# ----------------------------------------------------------
# MAIN SCATTERPLOT
# ----------------------------------------------------------

ax_scatter = plt.axes([0.1, 0.1, 0.65, 0.65])

ax_scatter.scatter(
    df['age'],
    df['hours_per_week'],
    color='blue'
)

ax_scatter.set_xlabel("Age")
ax_scatter.set_ylabel("Hours Per Week")
ax_scatter.set_title("Scatterplot with Boxplots")

# ----------------------------------------------------------
# TOP BOXPLOT
# ----------------------------------------------------------

ax_boxx = plt.axes([0.1, 0.77, 0.65, 0.15])

sns.boxplot(
    x=df['age'],
    ax=ax_boxx,
    color='lightgreen'
)

ax_boxx.set_xticks([])
ax_boxx.set_yticks([])

# ----------------------------------------------------------
# RIGHT BOXPLOT
# ----------------------------------------------------------

ax_boxy = plt.axes([0.77, 0.1, 0.15, 0.65])

sns.boxplot(
    y=df['hours_per_week'],
    ax=ax_boxy,
    color='orange'
)

ax_boxy.set_xticks([])
ax_boxy.set_yticks([])

plt.show()

# ==========================================================
# CORRELATION HEATMAP
# ==========================================================

# Objective:
# Understand feature relationships

plt.figure(figsize=(10,8))

numeric_df = df.select_dtypes(include=np.number)

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.show()

# ==========================================================
# END OF PROGRAM
# ==========================================================

print("\nAdult Dataset Visualization Completed Successfully!")
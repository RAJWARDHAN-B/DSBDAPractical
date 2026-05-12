# ============================================
# HEART DISEASE DATASET VISUALIZATION PROJECT
# ============================================

# Objective:
# Visualize Heart Disease Dataset using:
# 1. Histograms
# 2. Dot Plots
# 3. Bar Plots
# 4. Line Charts
# 5. Box Plot + Histogram + Scatter Plot
# 6. Correlation Heatmap

# ============================================
# IMPORT LIBRARIES
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ============================================
# LOAD DATASET
# ============================================

# Make sure heart.csv is in same folder

df = pd.read_csv("heart.csv")

# ============================================
# DISPLAY BASIC INFORMATION
# ============================================

print("\nFIRST 5 RECORDS\n")
print(df.head())

print("\nDATASET INFORMATION\n")
print(df.info())

print("\nSTATISTICAL SUMMARY\n")
print(df.describe())

# ============================================
# HISTOGRAMS
# ============================================

# Objective:
# Understand distribution of continuous variables

# --------------------------------------------
# HISTOGRAM - AGE
# --------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(
    df['age'],
    bins=10,
    color='skyblue',
    edgecolor='black'
)

plt.title("Histogram of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

# --------------------------------------------
# HISTOGRAM - CHOLESTEROL
# --------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(
    df['chol'],
    bins=15,
    color='orange',
    edgecolor='black'
)

plt.title("Histogram of Cholesterol")
plt.xlabel("Cholesterol")
plt.ylabel("Frequency")

plt.show()

# ============================================
# DOT PLOT
# ============================================

# Objective:
# Visualize spread and density of observations

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

# ============================================
# BAR PLOTS
# ============================================

# Objective:
# Compare categorical variables

# --------------------------------------------
# BAR PLOT - HEART DISEASE COUNT
# --------------------------------------------

plt.figure(figsize=(7,5))

sns.countplot(
    x='num',
    data=df,
    palette='viridis'
)

plt.title("Heart Disease Count")
plt.xlabel("Disease Severity")
plt.ylabel("Count")

plt.show()

# --------------------------------------------
# BAR PLOT - CHEST PAIN TYPE
# --------------------------------------------

plt.figure(figsize=(7,5))

sns.countplot(
    x='cp',
    data=df,
    palette='Set2'
)

plt.title("Chest Pain Type Distribution")
plt.xlabel("Chest Pain Type")
plt.ylabel("Count")

plt.show()

# ============================================
# PIE CHART
# ============================================

# Objective:
# Show percentage distribution of heart disease levels

disease_counts = df['num'].value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    disease_counts,
    labels=disease_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette('pastel')
)

plt.title("Heart Disease Distribution")

plt.show()

# ============================================
# LINE CHARTS
# ============================================

# Objective:
# Show trends and variations

# --------------------------------------------
# LINE CHART - CHOLESTEROL
# --------------------------------------------

plt.figure(figsize=(10,5))

plt.plot(
    df['chol'],
    color='blue',
    linewidth=2
)

plt.title("Cholesterol Trend")
plt.xlabel("Patient Index")
plt.ylabel("Cholesterol")

plt.show()

# --------------------------------------------
# LINE CHART - MAX HEART RATE
# --------------------------------------------

plt.figure(figsize=(10,5))

plt.plot(
    df['thalach'],
    color='green'
)

plt.title("Maximum Heart Rate Trend")
plt.xlabel("Patient Index")
plt.ylabel("Heart Rate")

plt.show()

# ============================================
# SCATTERPLOT WITH BOXPLOTS
# ============================================

# Objective:
# Combine scatterplot and boxplots to analyze
# relationship and spread together

fig = plt.figure(figsize=(10,10))

# Scatter plot
ax_scatter = plt.axes([0.1, 0.1, 0.65, 0.65])

ax_scatter.scatter(
    df['age'],
    df['chol'],
    color='blue'
)

ax_scatter.set_xlabel("Age")
ax_scatter.set_ylabel("Cholesterol")
ax_scatter.set_title("Scatterplot with Boxplots")

# Top boxplot
ax_boxx = plt.axes([0.1, 0.77, 0.65, 0.15])

sns.boxplot(
    x=df['age'],
    ax=ax_boxx,
    color='lightgreen'
)

ax_boxx.set_xticks([])
ax_boxx.set_yticks([])

# Right boxplot
ax_boxy = plt.axes([0.77, 0.1, 0.15, 0.65])

sns.boxplot(
    y=df['chol'],
    ax=ax_boxy,
    color='orange'
)

ax_boxy.set_xticks([])
ax_boxy.set_yticks([])

plt.show()

# ============================================
# BOX PLOT
# ============================================

# Objective:
# Detect outliers and distribution spread

plt.figure(figsize=(8,5))

sns.boxplot(
    x=df['chol'],
    color='lightblue'
)

plt.title("Box Plot of Cholesterol")

plt.show()

# ============================================
# HISTOGRAM WITH KDE
# ============================================

# Objective:
# Visualize probability density and distribution

plt.figure(figsize=(8,5))

sns.histplot(
    df['chol'],
    kde=True,
    color='purple'
)

plt.title("Histogram of Cholesterol with KDE")

plt.show()

# ============================================
# SCATTER PLOT
# ============================================

# Objective:
# Study relationship between age and cholesterol

plt.figure(figsize=(8,5))

plt.scatter(
    df['age'],
    df['chol'],
    color='red'
)

plt.title("Age vs Cholesterol")
plt.xlabel("Age")
plt.ylabel("Cholesterol")

plt.show()

# ============================================
# COMBINED VISUALIZATION
# ============================================

# Objective:
# Compare histogram, boxplot and scatter together

fig, axes = plt.subplots(1, 3, figsize=(18,5))

# --------------------------------------------
# HISTOGRAM
# --------------------------------------------

sns.histplot(
    df['chol'],
    kde=True,
    ax=axes[0],
    color='skyblue'
)

axes[0].set_title("Histogram")

# --------------------------------------------
# BOXPLOT
# --------------------------------------------

sns.boxplot(
    x=df['chol'],
    ax=axes[1],
    color='orange'
)

axes[1].set_title("Box Plot")

# --------------------------------------------
# SCATTER PLOT
# --------------------------------------------

axes[2].scatter(
    df['age'],
    df['chol'],
    color='red'
)

axes[2].set_title("Scatter Plot")
axes[2].set_xlabel("Age")
axes[2].set_ylabel("Cholesterol")

plt.tight_layout()

plt.show()

# ============================================
# CORRELATION HEATMAP
# ============================================

# Objective:
# Analyze feature relationships

plt.figure(figsize=(12,8))

sns.heatmap(
    df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.show()

# ============================================
# END OF PROGRAM
# ============================================

print("\nVisualization Completed Successfully!")
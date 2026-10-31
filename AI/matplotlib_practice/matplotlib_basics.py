# Matplotlib practice: line, bar, scatter, pie, histogram, subplots

import os
import matplotlib
matplotlib.use("Agg")          # saves images; remove this line to see popup windows
import matplotlib.pyplot as plt
import random

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plots")
os.makedirs(out, exist_ok=True)

# 1. Line plot
x = list(range(1, 11))
y = [i * i for i in x]
plt.figure()
plt.plot(x, y, marker="o", color="teal", label="y = x²")
plt.title("Line Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(out, "1_line.png"))
plt.close()

# 2. Bar chart
subjects = ["Math", "Physics", "AI", "English"]
marks = [85, 72, 93, 78]
plt.figure()
plt.bar(subjects, marks, color="steelblue")
plt.title("Marks by Subject")
plt.ylabel("Marks")
plt.savefig(os.path.join(out, "2_bar.png"))
plt.close()

# 3. Scatter plot
random.seed(7)
hours = [random.uniform(1, 10) for _ in range(30)]
score = [h * 8 + random.uniform(-8, 8) for h in hours]
plt.figure()
plt.scatter(hours, score, color="darkorange")
plt.title("Study Hours vs Score")
plt.xlabel("Hours")
plt.ylabel("Score")
plt.savefig(os.path.join(out, "3_scatter.png"))
plt.close()

# 4. Pie chart
langs = ["Python", "C", "Java", "Others"]
share = [45, 20, 20, 15]
plt.figure()
plt.pie(share, labels=langs, autopct="%1.0f%%", startangle=90)
plt.title("Language Usage")
plt.savefig(os.path.join(out, "4_pie.png"))
plt.close()

# 5. Histogram
ages = [random.randint(18, 30) for _ in range(100)]
plt.figure()
plt.hist(ages, bins=6, color="seagreen", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig(os.path.join(out, "5_histogram.png"))
plt.close()

# 6. Subplots
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(x, y, color="purple")
ax[0].set_title("Line")
ax[1].bar(subjects, marks, color="salmon")
ax[1].set_title("Bar")
fig.tight_layout()
fig.savefig(os.path.join(out, "6_subplots.png"))
plt.close(fig)

print("All plots saved in:", out)

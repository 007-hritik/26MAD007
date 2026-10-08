import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(data=emp, x="salary", ax=axes[0])
sns.boxplot(data=emp, x="dept_name", y="salary", ax=axes[1])

plt.tight_layout()
plt.show()
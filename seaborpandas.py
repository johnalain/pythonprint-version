import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame
df = pd.DataFrame({
    "Math": [85, 90, 78],
    "Science": [88, 92, 80],
    "English": [75, 85, 82]
}, index=["Alice", "Bob", "Charlie"])

# Plot heatmap
sns.heatmap(df, annot=True)
plt.show()

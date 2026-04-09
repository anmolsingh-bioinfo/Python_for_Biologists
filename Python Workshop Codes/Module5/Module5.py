import matplotlib.pyplot as plt
import seaborn as sns

# Sample gene expression data 
genes = ["GeneA", "Gene", "GeneC", "GeneD"]
expression = [23,45, 12, 67]

# Bar plot with matplotlib
plt.bar(genes, expression)
plt.title("Gene Expression Levels")
plt.ylabel("Expression")
plt.xlabel("Genes")
plt.show()

# Histogram with seaborn
import numpy as np
expression_values = np.random.normal(loc= 50, scale =10, size = 100)
print(expression_values)

sns.histplot(expression_values, kde = True)
plt.title("Distribution of Gene Expression")
plt.show()

# EXAMPLE

# Importing libraries (not needed if already done above)
import matplotlib.pyplot as plt
import seaborn as sns

# Example dataset for a plot: sequence length vs gc content
sequence_length = [200, 300, 400, 500, 600, 700, 800]
gc_content = [32.3, 43.2, 54.1, 65.4, 76.5, 87.6, 98.7]

#create scatter plot
sns.set(style= 'whitegrid')
plt.figure(figsize=(8,5))
sns.scatterplot(x= sequence_length,y=  gc_content, s = 100, color = 'purple')

# Add labels and titles
plt.title("GC Content VS Sequence Length", fontsize =14)
plt.xlabel("Sequence length (in bp)")
plt.ylabel("GC Content (%)")
plt.show()

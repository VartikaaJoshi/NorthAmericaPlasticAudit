# Waste Composition Analysis in North America
  
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = 'Users/vj/Documents/Experiential_Learning/north_america.csv'
north_america_data = pd.read_csv(file_path)

# Trend Analysis
trend_analysis = north_america_data.groupby('year').size().reset_index(name='count')

# Brand Analysis
top_brands = north_america_data['brand_name'].value_counts().head(10).reset_index()
top_brands.columns = ['brand_name', 'count']

# Item Type Analysis
top_item_types = north_america_data['type_product'].value_counts().head(10).reset_index()
top_item_types.columns = ['type_product', 'count']

# Plotting
sns.set(style="whitegrid")
fig1 = sns.lineplot(x='year', y='count', data=trend_analysis, marker='o')
fig2 = sns.barplot(x='count', y='brand_name', data=top_brands)
fig3 = sns.barplot(x='count', y='type_product', data=top_item_types)

plt.show()

    

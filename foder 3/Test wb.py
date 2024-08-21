import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the file
file_path = r"C:\Visual studio code\foder 3\Website Access Category.csv"
data = pd.read_csv(file_path)

# Group data by ProductName and sum the Quantity
product_distribution = data.groupby('ProductName')['Quantity'].sum()

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(product_distribution, labels=product_distribution.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribution of Products Purchased by Customers')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()

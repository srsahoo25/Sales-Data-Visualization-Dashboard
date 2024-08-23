import pandas as pd  # Importing pandas for data manipulation
import matplotlib.pyplot as plt  # Importing matplotlib for data visualization

# Load data from an Excel file into a pandas DataFrame
df = pd.read_excel('C:\\Users\\91628\\Desktop\\Sales Data Visualization Dashboard\\sales_data.xlsx')  # Specify the path to your Excel file

# Example 1: Line chart for visualizing the sales trend over time
plt.figure(figsize=(10, 6))  # Create a new figure with a specific size (10x6 inches)
plt.plot(df['Date'], df['Sales'], marker='o', linestyle='-', color='b')  # Plot sales data with blue lines and markers
plt.title('Sales Trend Over Time')  # Add a title to the chart
plt.xlabel('Date')  # Label the x-axis as 'Date'
plt.ylabel('Sales')  # Label the y-axis as 'Sales'
plt.grid(True)  # Enable the grid for better readability
plt.xticks(rotation=45)  # Rotate x-axis labels by 45 degrees for better visibility
plt.tight_layout()  # Adjust the layout to ensure nothing is cut off
plt.savefig('C:\\Users\\91628\\Desktop\\Sales Data Visualization Dashboard\\line_graph.png')  # Save the chart as a PNG image file in the desired location.
plt.show()  # Display the chart on the screen

# Example 2: Bar chart for visualizing sales by product
plt.figure(figsize=(10, 6))  # Create another figure with a specific size (10x6 inches)
plt.bar(df['Product'], df['Sales'], color='green')  # Create a bar chart with green bars representing sales by product
plt.title('Sales by Product')  # Add a title to the chart
plt.xlabel('Product')  # Label the x-axis as 'Product'
plt.ylabel('Sales')  # Label the y-axis as 'Sales'
plt.xticks(rotation=45)  # Rotate x-axis labels by 45 degrees for better visibility
plt.tight_layout()  # Adjust the layout to ensure nothing is cut off
plt.savefig('C:\\Users\\91628\\Desktop\\Sales Data Visualization Dashboard\\bar_graph.png')  # Save the bar chart as a PNG image file in the desired location.
plt.show()  # Display the bar chart on the screen

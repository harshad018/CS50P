import matplotlib.pyplot as plt

# Data for the pie chart
countries = ['China', 'India', 'United States', 'Indonesia', 'Pakistan',
             'Nigeria', 'Brazil', 'Bangladesh', 'Russia', 'Mexico', 'Rest of the World']
populations = [1410, 1370, 332, 275, 240, 223, 216, 170, 144, 130, 3750]  # in millions

# Create the pie chart
plt.figure(figsize=(10, 7))
plt.pie(populations, labels=countries, autopct='%1.1f%%', startangle=140)
plt.title('World Population by Country')
plt.show()

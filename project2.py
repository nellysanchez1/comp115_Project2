import matplotlib.pyplot as plt
import seaborn as sns
from data_module import load_data
import pandas as pd

sns.set_style('darkgrid') #background and window sizing
plt.figure(figsize=(12, 8))

color_35 = 'blue'
color_50 = 'purple'
color_65 = 'red'


average_values_35, average_values_50, average_values_65 = load_data() # Bring data from data_module to create the graphs
time_values = range(0, 36, 5)  # Time values


plt.plot(time_values, average_values_35, marker='*', color=color_35, label='Temperature 35')
plt.plot(time_values, average_values_50, marker='*', color=color_50, label='Temperature 50')
plt.plot(time_values, average_values_65, marker='*', color=color_65, label='Temperature 65')
# add more values to the line plot if needed

# Modifications and naming on line chart
plt.xlabel('Time(min)')
plt.ylabel('Average CO2 Changes(cm)')
plt.title('Average CO2 changes over time at different temperatures', fontsize = 15)
plt.legend(fontsize=12)

plt.grid(True)
plt.show()

# This graph is specially helpful on knowing which of the temperatures produces more CO2, the experiment is to find out the ideal temperature. 
#This graph show a clear better temperature for this trend. Which is going to be helpful while explaining the results.


plt.figure(figsize=(12, 8))
plt.boxplot([average_values_35, average_values_50, average_values_65], 
            labels=['Temperature 35', 'Temperature 50', 'Temperature 65'],
            patch_artist=True)
plt.title('CO2 Changes at Different Temperatures', fontsize=15)
plt.ylabel('Average CO2 Changes(cm)')
plt.grid(True)
plt.show() #Box plot to visualize the amount of CO2 production changed in 35 min


# Included some values that will be helpful while reading the charts and to interpret results, specially for the box plot
stats = pd.DataFrame({
    'Temperature': ['35', '50', '65'],
    'Mean': [average_values_35.mean(), average_values_50.mean(), average_values_65.mean()],
    'Standard Deviation': [average_values_35.std(), average_values_50.std(), average_values_65.std()]
})


print("Descriptive Statistics:") #Extra info needed for more calculation and explain the results of the data
print(stats)


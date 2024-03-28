import pandas as pd

def load_data():
#create a module with the data at different temps
    CO2changes_data_at35 = {
    'Time':[0, 5, 10, 15, 20, 25, 30, 35],
    'Trial1':[1.8, 2.8, 4.0, 4.8, 5.4, 6.1, 7.1, 8.0],
    'Trial2':[2.1, 2.6, 2.9, 3.3, 4.2, 5.2, 5.3, 6.5],
    'Trial3':[1.9, 2.4, 2.9, 3.4, 4.1, 5.1, 5.7,6.6],
    'Trial4':[1.3, 1.6, 2.1, 2.5, 3.5, 4.6, 4.9, 5.4]
}
    CO2changes_data_at50 = {
    'Time': [0, 5, 10, 15, 20, 25, 30, 35],
    'Trial1': [1.1, 1.7, 3.2, 5.6, 6.7, 8.2, 8.6, 9.2],
    'Trial2': [1.8, 1.8, 2.7, 4.8, 7.4, 7.6, 7.9, 8.3],
    'Trial3': [1.7, 1.7, 3.8, 6.7, 7.8, 9.1, 9.4, 10.1],
    'Trial4': [1.9, 2.5, 4.7, 7.8, 8.1, 9.5, 9.8, 10.3],
}
    CO2changes_data_at65 = {
    'Time': [0, 5, 10, 15, 20, 25, 30, 35],
    'Trial1': [1.6, 2.1, 6.3, 7.1, 7.1, 7.4, 7.4, 7.5],
    'Trial2': [2.1, 2.6, 6.2, 6.6, 6.9, 7.4, 7.4, 7.4],
    'Trial3': [2.0, 2.7, 6.5, 6.9, 7.1, 7.5, 7.5, 7.6],
    'Trial4': [2.0, 2.2, 6.1, 6.7, 6.9, 7.1, 7.2, 7.4]
}

#Averages that will be used to create a line plot and create data frame to be called fot it
    df_changes_35 = pd.DataFrame(CO2changes_data_at35)
    average_values_35 = df_changes_35[['Trial1','Trial2','Trial3','Trial4']].mean(axis=1)

    df_changes_50 = pd.DataFrame(CO2changes_data_at50)
    average_values_50 = df_changes_50[['Trial1', 'Trial2', 'Trial3', 'Trial4']].mean(axis=1)

    df_changes_65 = pd.DataFrame(CO2changes_data_at65)
    average_values_65 = df_changes_65[['Trial1', 'Trial2', 'Trial3', 'Trial4']].mean(axis=1)

    load_data= [average_values_35,average_values_50,average_values_65]
    return average_values_35, average_values_50, average_values_65

    


    
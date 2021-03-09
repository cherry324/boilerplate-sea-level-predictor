import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    print(df)

    # Create scatter plot

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    
    plt.plot(x, intercept + slope*x, 'r', label = 'Fitted Line 1')
    plt.legend()
    plt.show()
    
    (slope,
     intercept,
     r_value,
     p_value,
     std_err) = linregress(df[df['Year'] >= 2000]['Year'],
                           df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    x_fit_from_2000 = pd.Series([*range(2000, 2050)])
    y_fit_from_2000 = intercept + slope*x_fit_from_2000
    plt.plot(x_fit_from_2000, y_fit_from_2000, 'r')

    
    # Create second line of best fit
    


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
#!/usr/bin/env python
# coding: utf-8
import tkinter
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib

def get_main_df():
    #reading the csv, setting the linebreak as 'tab', setting datetime format for the Month index, and setting three indexes (month, region, proptype)
    main_df = pd.read_csv(Path('data/redfin_table.csv'), on_bad_lines='skip', sep='\t', infer_datetime_format=True, parse_dates=True, index_col=['Month', 'Region', 'For-Sale Property Type'])

    #removing the '$' '%' ',' from the datapoints so they can be converted to ints as needed
    main_df.loc[ : , 'Average Monthly Rent'] = main_df.loc[ : , 'Average Monthly Rent'].str.replace(r'$', '', regex=True)
    main_df.loc[ : , 'Monthly mortgage, 5% down'] = main_df.loc[ : , 'Monthly mortgage, 5% down'].str.replace(r'$', '', regex=True)
    main_df.loc[ : , 'Monthly mortgage, 20% down'] = main_df.loc[ : , 'Monthly mortgage, 20% down'].str.replace(r'$', '', regex=True)
    main_df.loc[ : , 'Median sale price'] = main_df.loc[ : , 'Median sale price'].str.replace(r'$', '', regex=True)
    main_df.loc[ : , 'Average Monthly Rent'] = main_df.loc[ : , 'Average Monthly Rent'].str.replace(r',', '', regex=True)
    main_df.loc[ : , 'Monthly mortgage, 5% down'] = main_df.loc[ : , 'Monthly mortgage, 5% down'].str.replace(r',', '', regex=True)
    main_df.loc[ : , 'Monthly mortgage, 20% down'] = main_df.loc[ : , 'Monthly mortgage, 20% down'].str.replace(r',', '', regex=True)
    main_df.loc[ : , 'Median sale price'] = main_df.loc[ : , 'Median sale price'].str.replace(r',', '', regex=True)
    main_df.loc[ : , 'Average Rent YoY'] = main_df.loc[ : , 'Average Rent YoY'].str.replace(r'%', '', regex=True)
    main_df.loc[ : , 'Monthly mortgage, 5% down YoY'] = main_df.loc[ : , 'Monthly mortgage, 5% down YoY'].str.replace(r'%', '', regex=True)
    main_df.loc[ : , 'Monthly mortgage, 20% down YoY'] = main_df.loc[ : , 'Monthly mortgage, 20% down YoY'].str.replace(r'%', '', regex=True)
    main_df.loc[ : , 'Median sale price YoY'] = main_df.loc[ : , 'Median sale price YoY'].str.replace(r'%', '', regex=True)
    main_df['Average Monthly Rent'] = main_df['Average Monthly Rent'].astype('int')
    main_df['Monthly mortgage, 5% down'] = main_df['Monthly mortgage, 5% down'].astype('int')
    main_df['Monthly mortgage, 20% down'] = main_df['Monthly mortgage, 20% down'].astype('int')
    main_df['Median sale price']=main_df['Median sale price'].astype('int')
    main_df['Average Rent YoY']=main_df['Average Rent YoY'].astype('float')
    main_df['Monthly mortgage, 5% down YoY']=main_df['Monthly mortgage, 5% down YoY'].astype('float')
    main_df['Monthly mortgage, 20% down YoY']=main_df['Monthly mortgage, 20% down YoY'].astype('float')
    main_df['Median sale price YoY']=main_df['Median sale price YoY'].astype('float')
    #main_df.sort_index(level=['Month', 'Region', 'For-Sale Property Type'], ascending=[2, 1, 0], inplace=True)
    #doesn't look like I need to sort the indexes for what we are doing, keeping it here for reference.
    
    main_df = main_df.loc[slice(None), ['Austin, TX', 'San Diego, CA', 'Atlanta, GA', 'Washington, DC', 'West Palm Beach, FL', 'Indianapolis, IN', 'Pittsburg, PA', 'Detroit, MI', 'Denver, CO', 'Boston, MA'], slice(None)]


    return main_df

def get_city_list():
    df = get_main_df()
    df.reset_index(inplace=True)
    return df['Region'].unique().tolist()
#main_df.loc['2019-02-01', 'National', 'Townhouse']
#Since there are three indexes, you can use .loc to specifically find the datapoint as per Time/Region/Type
#If you want to refer to the actual datapoint and not this list of data, see the next cell.





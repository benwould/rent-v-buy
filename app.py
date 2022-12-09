#!/usr/bin/env python
# coding: utf-8
import tkinter
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib

def get_main_df():
    #reading the csv, setting the linebreak as 'tab', setting datetime format for the Month index, and setting three indexes (month, region, proptype)
    main_df = pd.read_csv(Path('data/redfin_table.csv'), on_bad_lines='skip', sep='\t', infer_datetime_format=True, parse_dates=True, index_col=['Month', 'Region'])

    main_df.sort_index(level=['Month', 'Region'], ascending=[1, 0], inplace=True)
    #drop unnecessary column
    main_df = main_df.drop(['For-Sale Property Type'], axis=1)

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

    #shorten the DF to only include chosen cities
    main_df = main_df.loc[slice(None), ['Austin, TX', 'San Diego, CA', 'Atlanta, GA', 'Washington, DC', 'West Palm Beach, FL', 'Indianapolis, IN', 'Pittsburg, PA', 'Detroit, MI', 'Denver, CO', 'Boston, MA'], : ]
    return main_df

def get_city_list():
    df = get_main_df()
    df.reset_index(inplace=True)
    return df['Region'].unique().tolist()

def get_tax_rates():
    # Return a data frame with columns Region, state_code, tax_rate
    #   for all cities in our main dataframe
    main_df = get_main_df()
    main_df.reset_index(inplace=True)
    df = pd.DataFrame(main_df.Region.unique(), columns=(['Region']))
    df['state_code'] = df['Region'].apply(lambda x: x[-2:])
    tax_df = pd.read_csv("./data/tax_rates_state.csv")
    df_final = pd.merge(df, tax_df, how='right', on=['state_code', 'state_code'])
    df_final.dropna(inplace=True)
    df_final['tax_rate'] = df_final['tax_rate'].str.replace(r'%', '', regex=True).astype('float') / 100
    df_final.reset_index(inplace=True, drop=True)
    return df_final





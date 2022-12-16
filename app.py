#!/usr/bin/env python
# coding: utf-8
import tkinter
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib

def get_main_df():
    #reading the csv, setting the linebreak as 'tab', setting datetime format for the Month index
    #I am setting the index as Month so that we can apply formatting parameters, which will be conserved even as we reset the index a few times within the function
    #i.e. the index will be changed a few times in this function, but at the end it will be set as multi-index for Month and Region, and these parameters will still work then
    main_df = pd.read_csv(Path('data/redfin_table.csv'), on_bad_lines='skip', sep='\t', infer_datetime_format=True, parse_dates=True, index_col=['Month'])
   
    #add state code column using the last two letters from the Region column, and set it as the index. This will be used as a common column for merging the second DF.
    main_df['state_code'] = main_df['Region'].apply(lambda x: x[-2:])
    main_df.reset_index(inplace=True)
    main_df.set_index(keys=['state_code'], inplace=True)
    
    #create second DF for tax rates from CSV and set index to 'state_code'
    tax_df = pd.read_csv("./data/tax_rates_state.csv")
    tax_df = tax_df.drop('state', axis=1)
    tax_df['tax_rate'] = tax_df['tax_rate'].str.replace(r'%', '', regex=True).astype('float')/100
    tax_df= tax_df.query("state_code == ('MA', 'TX', 'CA', 'GA', 'DC', 'FL', 'IN', 'PA', 'CO', 'MI')")
    tax_df = tax_df.set_index(keys='state_code')
    
    #create third df for latlong from csv and set index to 'state_code'
    
    ll_df = pd.read_csv(Path('data/statelatlong.csv'))
    ll_df = ll_df.rename({'State': 'state_code'}, axis='columns')
    ll_df= ll_df.query("state_code == ('MA', 'TX', 'CA', 'GA', 'DC', 'FL', 'IN', 'PA', 'CO', 'MI')")
    ll_df.set_index(keys=['state_code'], inplace=True)
    
    #merge the main and tax DF's using the state_code column as the merge point
    main_df = pd.merge(main_df, tax_df, on='state_code')
    
    #merge the main and latlong DF using the state_code column as the merge point
    main_df = pd.merge(main_df, ll_df, on='state_code')
    
    #reset index again, this time as month and region and for-sale property type
    main_df.reset_index(inplace=True)
    main_df.set_index(keys=['Month', 'Region', 'For-Sale Property Type'], inplace=True)
    main_df.sort_index(level=['Month', 'Region', 'For-Sale Property Type'], ascending=[2, 1, 0], inplace=True)
   
    #drop all rows in the for-sale property type that arent All Residential
    idx=pd.IndexSlice
    main_df = main_df.loc[idx[:,:,['All Residential']]]
                            
    
    #reset index again, this time as month and region; this is the final index format
    main_df.reset_index(inplace=True)
    main_df.set_index(keys=['Month', 'Region'], inplace=True)
    main_df.sort_index(level=['Month', 'Region'], ascending=[1, 0], inplace=True)
    
    #drop unnecessary columns
    main_df = main_df.drop(['For-Sale Property Type', 'state_code', 'City'], axis=1)
    
    #shorten the DF to only include the 10 chosen cities
    main_df = main_df.loc[slice(None), ['Austin, TX', 'San Diego, CA', 'Atlanta, GA', 'Washington, DC', 'West Palm Beach, FL', 'Indianapolis, IN', 'Pittsburgh, PA', 'Detroit, MI', 'Denver, CO', 'Boston, MA'], :]
    
    #clean data of $/%/,
    cols = ['Average Monthly Rent', 'Average Rent YoY', 'Monthly mortgage, 5% down', 'Monthly mortgage, 5% down YoY', 'Monthly mortgage, 20% down', 'Monthly mortgage, 20% down YoY', 'Median sale price', 'Median sale price YoY'] 
    main_df[cols] = main_df[cols].replace({'\$': '', ',': '', '\%': ''}, regex=True)
    
    #set data as int/float where needed
    main_df['Average Monthly Rent'] = main_df['Average Monthly Rent'].astype('int')
    main_df['Monthly mortgage, 5% down'] = main_df['Monthly mortgage, 5% down'].astype('int')
    main_df['Monthly mortgage, 20% down'] = main_df['Monthly mortgage, 20% down'].astype('int')
    main_df['Median sale price']=main_df['Median sale price'].astype('int')
    main_df['Average Rent YoY']=main_df['Average Rent YoY'].astype('float')
    main_df['Monthly mortgage, 5% down YoY']=main_df['Monthly mortgage, 5% down YoY'].astype('float')
    main_df['Monthly mortgage, 20% down YoY']=main_df['Monthly mortgage, 20% down YoY'].astype('float')
    main_df['Median sale price YoY']=main_df['Median sale price YoY'].astype('float')
    
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



def av_rent(city):
    main_df = get_main_df()
    idx=pd.IndexSlice
    main_df = main_df.loc[idx[:, city], 'Average Monthly Rent']
    main_df = main_df.iloc[-1]
    return main_df

def yoy_rent(city):
    main_df=get_main_df()
    main_df = main_df.drop(columns=['Monthly mortgage, 5% down', 'Monthly mortgage, 20% down', 'Monthly mortgage, 5% down YoY', 'Monthly mortgage, 20% down YoY', 'Median sale price YoY','Average Rent YoY','Median sale price']).drop_duplicates().reset_index('Region')
    main_df=main_df.loc[main_df['Region']== city]
    main_df=main_df['Average Monthly Rent'].pct_change().dropna().mean()*12
    main_df = round(main_df * 100)
    
    return main_df

def med_home_val(city):
    main_df = get_main_df()
    idx=pd.IndexSlice
    main_df = main_df.loc[idx[:, city], 'Median sale price']
    main_df = main_df.iloc[-1]
    return main_df

def yoy_home_val(city):
    main_df = get_main_df()
    idx=pd.IndexSlice
    main_df = main_df.loc[idx[:, city], 'Median sale price YoY']
    main_df = main_df.iloc[-1]
    return main_df

def mort_5(city):
    main_df = get_main_df()
    idx=pd.IndexSlice
    main_df = main_df.loc[idx[:, city], 'Monthly mortgage, 5% down']
    main_df = main_df.iloc[-1]
    return main_df

def mort_20(city):
    main_df = get_main_df()
    idx=pd.IndexSlice
    main_df = main_df.loc[idx[:, city], 'Monthly mortgage, 20% down']
    main_df = main_df.iloc[-1]
    return main_df

def prop_tax_pct(city):
    main_df = get_main_df()
    idx=pd.IndexSlice
    main_df = main_df.loc[idx[:, city], 'tax_rate']
    main_df = main_df.iloc[-1]
    return main_df

def calc_mortgage(city):

    sales_price = med_home_val(city)
    property_tax_pct = prop_tax_pct(city)

    loan_terms = [{"down_payment_pct":5, "interest_rate":6.3, "mortgage_years":15}
                  ,{"down_payment_pct":20, "interest_rate":5.831, "mortgage_years":15}
                  ,{"down_payment_pct":5, "interest_rate":7.5, "mortgage_years":30}
                  ,{"down_payment_pct":20, "interest_rate":7.015, "mortgage_years":30}]
    outputs = []
    for term in loan_terms:
        down_payment_pct = term["down_payment_pct"]
        interest_rate = term["interest_rate"]
        mortgage_years = term["mortgage_years"]

        loan_amount = sales_price * (1 - down_payment_pct / 100)
        # calculates the loan amount from the above formulas

        loan_term = int(12 * mortgage_years)
        # current interest rates will be used

        # yearly interest
        interest_annualized = 1 + (interest_rate) / (12 * 100)

        # calculates monthly mortgage amount
        mortgage_monthly = loan_amount * (interest_annualized ** loan_term) * (1 - interest_annualized) / (1 - interest_annualized ** loan_term)

        #A = (1 + interest_rate) ** loan_term

        monthly_interest = []
        monthly_balance = []

        for i in range(1, loan_term + 1):
            interest = loan_amount * (interest_annualized - 1)
            paid_loan_amount = mortgage_monthly * loan_term
            monthly_interest = np.append(monthly_interest, interest)
            sum_monthly_interest = np.sum(monthly_interest)
            monthly_balance = np.append(monthly_balance, loan_amount)
            sum_monthly_balance = np.sum(monthly_balance)

        output_dict = {}
        output_dict["City"] = city
        output_dict["Home Price($)"] = round(sales_price)
        output_dict["Down Payment(%)"] = down_payment_pct
        output_dict["Loan Amount($)"] = round(sales_price * (1 - down_payment_pct / 100))
        output_dict["Interest Rate(%)"] = interest_rate
        output_dict["Loan Duration(months)"] = loan_term
        #output_dict["Monthly Principal (P&I)"] = mortgage_monthly
        output_dict["Monthly Taxes"] = round((sales_price * property_tax_pct)/12)
        output_dict["Total Monthly Payment"] = round(mortgage_monthly + (sales_price * property_tax_pct)/12)
        output_dict["Total Cost of Loan"] = round(paid_loan_amount)
        #output_dict["Total Interest Paid"] = sum_monthly_interest
        # print the following sets of data for the user for the entire term of the loan

        outputs.append(output_dict)
    df = pd.DataFrame.from_records(outputs,index=['1','2','3','4'])
    return df


# Chat GPT --> "python pandas amortization schedule for a 30 year fixed mortgage"
def amort_schedule(loan_amount, interest_rate, num_periods):
    df_schedule = pd.DataFrame(columns=['period', 'interest', 'principal', 'cumulative_interest', 'cumulative_principal'])

    # Set the loan amount, interest rate, and number of periods
    # loan_amount = 100000
    # interest_rate = 0.05
    # num_periods = 360

    # Calculate the periodic payment amount
    payment = (interest_rate / 12) * loan_amount / (1 - (1 + (interest_rate / 12)) ** (-num_periods))

    # Iterate over the number of periods and calculate the interest and principal payments
    # for each period
    for period in range(1, num_periods + 1):
        interest_payment = round(loan_amount * (interest_rate / 12), 2)
        principal_payment = round(payment - interest_payment, 2)
        loan_amount -= principal_payment

        # Add the interest and principal payments for this period to the schedule data frame
        df_schedule.loc[period] = [period, interest_payment, principal_payment, 0, 0]

    # Calculate the cumulative interest and principal payments
    df_schedule['cumulative_interest'] = df_schedule['interest'].cumsum()
    df_schedule['cumulative_principal'] = df_schedule['principal'].cumsum()

    # Round the values in the data frame to the desired precision
    df_schedule = df_schedule.round(2)

    # Format the values in the data frame for display
    df_schedule.style.format({
        'interest': '{:.2f}',
        'principal': '{:.2f}',
        'cumulative_interest': '{:.2f}',
        'cumulative_principal': '{:.2f}'
    })
    return df_schedule

def city_rent_v_buy(city,interest_rate):
    df_amort = pd.DataFrame()
    sales_price = med_home_val(city)
    tax_rate = prop_tax_pct(city)
    df_amort = amort_schedule(sales_price,interest_rate=interest_rate,num_periods=360)
    df_amort['city'] = city
    df_amort['interest_rate'] = interest_rate
    df_amort['rent'] = av_rent(city)
    df_amort['cumulative_rent'] = -1*df_amort['rent'].cumsum()
    df_amort['taxes'] = tax_rate * sales_price/12
    df_amort['cumulative_taxes'] = tax_rate * sales_price/12
    df_amort['cumulative_buying_profits'] = df_amort['cumulative_principal'] - (df_amort['cumulative_interest']+df_amort['cumulative_taxes'])

    return df_amort

def rent_v_buy_all_cities(interest_rate):
    cities = get_city_list()
    df_city_amorts = pd.DataFrame()
    i=1
    for city in cities:
        df = city_rent_v_buy(city,interest_rate)
        if i==1:
            df_city_amorts = df
        else:
            df_city_amorts = df_city_amorts.append(df)
        i+=1
    return df_city_amorts

#NOT CURRENTLY BEING USED FOR ANYTHING
def calc_equity_over_time_df(region, current_equity, mortgage_15_or_30):
    monthly_payment_totals = mortgage_15_or_30 * 12
    fut_home_value = get_main_df()
    idx=pd.IndexSlice
    fut_home_value= fut_home_value.loc[idx[:, region], 'Median sale price']
    fut_home_value = fut_home_value.iloc[16]
    fut_monthly_payment = (fut_home_value - current_equity) / monthly_payment_totals
    future_equity = 0
    future_equity_count = []
    for i in range(monthly_payment_totals):
        future_equity = future_equity + fut_monthly_payment
        i = fut_monthly_payment + current_equity
        future_equity_count.append(future_equity)
    return pd.DataFrame(future_equity_count)
# this python file is for the mortgage calculator to run in the background on various locations
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import app

# install PyPi library,  pip install amortization

# import mainframe from Jupyter Notebook

# from Ben.dataframe_test import main_df


def calc_mortgage(city):

    sales_price = app.med_home_val(city)
    property_tax_pct = app.property_tax_pct(city)

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
        output_dict["Home Price($)"] = sales_price
        output_dict["Down Payment(%)"] = down_payment_pct
        output_dict["Loan Amount($)"] = sales_price * (1 - down_payment_pct / 100)
        output_dict["Interest Rate(%)"] = interest_rate
        output_dict["Loan Duration(months)"] = loan_term
        output_dict["Monthly Principal (P&I)"] = mortgage_monthly
        output_dict["Monthly Taxes"] = (sales_price * property_tax_pct)/12
        output_dict["Total Monthly Payment"] = mortgage_monthly + (sales_price * property_tax_pct)/12
        output_dict["Total Cost of Loan"] = paid_loan_amount
        output_dict["Total Interest Paid"] = sum_monthly_interest
        # print the following sets of data for the user for the entire term of the loan

        outputs.append(output_dict)
        # print(f"The Home Sales Price is: = ${sales_price}")
        # print(f"The Down Payment as a Percentage of Sales Price is: = {down_payment_pct} %")
        # print(f"The Loan Amount is: = {sales_price * (1 - down_payment_pct / 100)} ")
        # print(f"The Interest Rate on Annual Percentage Basis is: = {interest_rate} %")
        # print(f"The duration of this loan, that is the Loan Term (in months) is: = {loan_term} month")
        # print(f"Total Paid Loan amount over your {loan_term} months was {paid_loan_amount: .2f}")
        # print(f"Monthly Payment for this Mortgage(P & I) is: = {mortgage_monthly: .2f}")
        # print(f"Total interest paid over life cycle of the loan is: = {(sum_monthly_interest): .2f}")
    df = pd.DataFrame.from_records(outputs,index=['1', '2','3','4'])
    return df



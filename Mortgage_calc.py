#this python file is for the mortgage calculator to run in the background on various locations
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#install PyPi library,  pip install amortization

#import mainframe from Jupyter Notebook

#from Ben.dataframe_test import main_df

def calc (region):
    main_df('Austin, TX', '')


Sales_Price = float(input('Mediam Sales Price: pull from df:'))
    #Median Sale Price from RedFin Dataframe
Down_Payment =  float(input('5$: or 20%: enter 5 or 20: '))
    #select a % of sale price you will put as DP
Loan_Amount = Sales_Price*(1-Down_Payment/100)
    #calculates the loan amount from the above formulas
Mortgage_Years =  float(input('enter years by 10,15,30: '))
    #how long do you expect to stay at your new location
Stay_Years = float(input('How many years do you plan to stay: '))
Stay_Term =     int(12* Stay_Years)
Loan_Term =     int(12* Mortgage_Years)
Interest_Rate =  float(input('Interst rate by precent, enter 4 for 4%: '))
    #current interest rates will be used

R = 1 +(Interest_Rate)/(12*100)
# yearly interest
X = Loan_Amount*(R**Loan_Term)*(1-R)/(1-R**Loan_Term) 
# calculates monthly mortgage amount
A = (1 + Interest_Rate) ** Loan_Term

Monthly_Interest = []
Monthly_Balance  = []


Stay_R = 1 +(Interest_Rate)/(12*100)
#interest rate growth 
Stay_X = Loan_Amount*(Stay_R**Stay_Term)*(1-Stay_R)/(1-Stay_R**Stay_Term) 
# calculates monthly mortgage payment
Stay_A = (1 + Interest_Rate) ** Stay_Term
# 
Stay_Monthly_Interest = []
Stay_Monthly_Balance = []


for i in range(1,Loan_Term+1):

    Interest = Loan_Amount*(R-1)
    Paid_Loan_Amount = X * Loan_Term
    Monthly_Interest = np.append(Monthly_Interest,Interest)
    Sum_Monthly_Interest = np.sum(Monthly_Interest)
    Monthly_Balance = np.append(Monthly_Balance, Loan_Amount)
    Sum_Monthly_Balance = np.sum(Monthly_Balance)
    


for istay in range(1,Stay_Term+1):
    Stay_Interest = Loan_Amount*(Stay_R-1)
    Stay_Paid_Loan_Amount = X * Stay_Term
    Stay_Loan_Amount = Loan_Amount - Stay_Paid_Loan_Amount
    Stay_Monthly_Interest = np.append(Stay_Monthly_Interest,Stay_Interest)
    Sum_Stay_Monthly_Interest = np.sum(Stay_Monthly_Interest)
    Stay_Monthly_Balance = np.append(Stay_Monthly_Balance, Loan_Amount)
    

#print the following sets of data for the user for the entire term of the loan

print(f"The Home Sales Price is: = ${Sales_Price}")
print(f"The Down Payment as a Percentage of Sales Price is: = {Down_Payment} %")
print(f"The Loan Amount is: = {Sales_Price*(1-Down_Payment/100)} ")
print(f"The Interest Rate on Annual Percentage Basis is: = {Interest_Rate} %")
print(f"The duration of this loan, that is the Loan Term (in months) is: = {Loan_Term} month")
print(f"Total Paid Loan amount over your {Loan_Term} months was {Paid_Loan_Amount: .2f}")
print(f"Monthly Payment for this Mortgage(P & I) is: = {X: .2f}")
print(f"Total interest paid over life cycle of the loan is: = {(Sum_Monthly_Interest): .2f}")




#print the following sets of data for the user for their intented STAY term of the loan


print(f"The Home Sales Price is: = ${Sales_Price}")
print(f"The Down Payment as a Percentage of Sales Price is: = {Down_Payment} %")
print(f"The Loan Amount is: = {Sales_Price*(1-Down_Payment/100)} ")
print(f"The Interest Rate on Annual Percentage Basis is: = {Interest_Rate} %")
print(f"The duration of this loan, that is the Loan Term (in months) is: = {Stay_Term} month")
print(f"Monthly Payment for this Mortgage(P & I) is: = {X: .2f}")
print(f"Total Paid Loan amount over your {Stay_Term} month stay was {Stay_Paid_Loan_Amount: .2f}")
print(f"Total Loan Amount remaining is: $ {Stay_Loan_Amount: .2f}")
print(f"Total Interest Paid over life cycle of the loan is: = {Sum_Stay_Monthly_Interest: .2f}")


#print(f"Your Amortization amount is ${Amortization_Cumulative}")

#visualizations of mortgage in tables
"""
#interest visualization
plt.plot(range(1,Loan_Term+1),Stay_Monthly_Interest, 'r',lw=2)
plt.xlabel('month')
plt.ylabel('monthly interest ($)')
plt.show()

#loan balance visualization
plt.plot(range(1,Loan_Term+1),Stay_Monthly_Balance,'b',lw=2)
plt.xlabel('month')
plt.ylabel('monthly loan balance ($)')
plt.show()
"""
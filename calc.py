#!/usr/bin/env python
# coding: utf-8

# In[54]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import app


# In[55]:


#Variables inputted in the first Tkinter page
#rent_or_own, city, monthly_payment, income, home_value, home_equity, interest_rate, tax_rate


# In[56]:


#def calc_equity_current_home(current_equity, my_mortgage_total, my_monthly_payment, my_interest_rate, my_tax_rate):
   # current_equity_df = []
    
    #DO WE SHOW THEM PROJECTED EQUITY OVER THE LIFETIME OF THEIR MORTGAGE?
    #WHAT WILL THIS RETURN? JUST A PLOT OF 
    #SHOULD WE ADD A USER INPUT FOR THEIR CURRENT AND TOTAL MORTGAGE DURATION?
        #WOULD WE MAKE IT SPECIFIC TO PAYMENTS? OR YEARS? 12 PAYMENTS PER YEAR FOR 15/30 YEARS?
            #PEOPLE MIGHT NOT KNOW WHICH PAYMENT THEY ARE ON OUT OF 180/360 TOTAL PAYMENTS
    #SHOULD WE ADD USER INPUT FOR PMI? SIMPLIFIED TO:
        #'IF 5% ADD PMI, IF 20% NO PMI'
        #WOULD WE USE AN AVG PMI?
            #SHOULD I ADD AVG PMI BY CITY TO THE MAIN DF?


# In[57]:


def calc_equity_future_home(fut_home_value, current_equity, mortgage_15_or_30):
#ARE WE CARRYING OVER CURRENT EQUITY TO THE NEW HOME? MAKE THIS AN OPTION?
    monthly_payment_totals = mortgage_15_or_30 * 12
    fut_monthly_payment = (fut_home_value - current_equity) / monthly_payment_totals
    future_equity = 0
    future_equity_count = []
    for i in range(monthly_payment_totals):
        future_equity = future_equity + fut_monthly_payment
        i = fut_monthly_payment + current_equity
        future_equity_count.append(future_equity)
    return pd.DataFrame(future_equity_count)


#DO WE WANT THEM TO INPUT VALUE OR FUTURE HOME OR JUST A REGION AND WE ESTIMATE?


# In[50]:


#mortgage_15_or_30 = 15
#fut_home_value = 200000
#current_equity = 20000
#city = 'Austin, TX'


# In[58]:


#df = calc_equity_future_home(fut_home_value, current_equity, mortgage_15_or_30)
#df = df.plot()


# In[ ]:





# In[4]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[54]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import app



def calc_equity_future_home(region, current_equity, mortgage_15_or_30):
#ARE WE CARRYING OVER CURRENT EQUITY TO THE NEW HOME? MAKE THIS AN OPTION?
    monthly_payment_totals = mortgage_15_or_30 * 12
    fut_home_value = app.get_main_df()
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





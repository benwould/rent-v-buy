#!/usr/bin/env python
# coding: utf-8

# In[16]:


import tkinter as tk
from tkinter import *
from tkinter import ttk
import app
import json
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import calc

LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.app_vars = {
            "results": {},
            "city": None
        }

        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
    
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.pre_show()
        frame.tkraise()
  
# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # label of frame Layout 2
        label = ttk.Label(self, text ="Rent vs Buy: User Data", font = LARGEFONT)
         
        my_city = tk.StringVar(self, name="My City",value='')
        
        label = tk.Label( self , text = "What city will you move to?" )
        label.grid(row=0,column=0)
        cities = app.get_city_list()
# Create Dropdown menu
        def command(city):
            controller.app_vars['city'] = city
        drop_cities = tk.OptionMenu( self , my_city , *cities, command = command)
        drop_cities.grid(row=0,column=1)

        data_labal_var = tk.StringVar()
        data_label = tk.Label(self, textvariable=data_labal_var)
        data_label.grid(row=10,column=0,padx=0)
        
        def print_data():
            city=my_city.get()
            data_labal_var.set(f"""My Data:
                                     city:  {city}
                                    """)
            
        
        def get_data():
            return {
                "city": my_city.get(),
            }

        #label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Page 1",
        command = lambda : controller.show_frame(Page1))
         
        # putting the button in its place by
        # using grid
        button1.grid(row = 9, column = 0, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Page 2",
        command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 9, column = 1, padx = 10, pady = 10)
        

    # Execute tkinter
        
    def pre_show(self):
        pass
  
  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text ="Page 1", font = LARGEFONT)
        self.label.grid(row = 0, column = 4, padx = 10, pady = 10)

        self.result_var = tk.StringVar()
        self.result_label = tk.Label(self, textvariable=self.result_var)
        self.result_label.grid(row = 1, column = 4, padx = 10, pady = 10)
        
        
        #app.get_info(THIS IS WHERE THE VARIABLE USER INPUT WILL GO, HOW DO I REFER TO THE APP-VARS?
        
        #AVERAGE RENT IN AREA
        self.av_rent = tk.StringVar()
        label_av_rent = tk.Label(self , textvariable = self.av_rent)
        label_av_rent.grid(row=3,column=0)
        '''
        #YoY % Rent
        self.yoy_rent = tk.StringVar()
        label_yoy_rent = tk.Label( self , textvariable = self.yoy_rent )
        label_yoy_rent.grid(row=4,column=0)
        
        #Median Home Value in Area
        self.med_hval = tk.StringVar()
        label_med_hval = tk.Label( self , textvariable = self.med_hval  )
        label_med_hval.grid(row=5,column=0)
        
        #YoY% increase home priced
        self.yoy_inc_home = tk.StringVar()
        label_yoy_inc_home = tk.Label( self , textvariable = self.yoy_inc_home )
        label_yoy_inc_home.grid(row=3,column=1)
        
        #mortgage payment if 5%
        self.mort_5 = tk.StringVar()
        label_mort_5 = tk.Label( self , textvariable = self.mort_5 )
        label_mort_5.grid(row=4,column=1)
        
        #mortgage payment if 20%
        self.mort_20 = tk.StringVar()
        label_mort_20 = tk.Label( self , textvariable = self.mort_20 )
        label_mort_20.grid(row=5,column=1)'''
        
    
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

    def pre_show(self):
        city = self.controller.app_vars['city']
        if not city :
            self.av_rent.set('City not selected')
            return
        city += app.av_rent(city)
        self.av_rent.set(city)
        
        
  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        self.label.grid(row = 0, column = 4, padx = 10, pady = 10)
        
        
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 2, column = 1, padx = 10, pady = 10)
  
        

        
        '''def plot(self):
  
            # the figure that will contain the plot
            fig = Figure()

            # calculation function
            y = calc.calc_equity_future_home(mortgage_15_or_30 = 15,
fut_home_value = 200000,
current_equity = 20000)

            # adding the subplot
            plot1 = fig.add_subplot(111)

            # plotting the graph
            plot1.plot(y)

            # creating the Tkinter canvas
            # containing the Matplotlib figure
            canvas = FigureCanvasTkAgg(fig, self)  
            canvas.draw()

            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().grid()

            # creating the Matplotlib toolbar
            toolbarFrame = Frame(master=self)
            toolbarFrame.grid(row=22,column=4)
            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

            # placing the toolbar on the Tkinter window
            canvas.get_tk_widget().grid()

        
        
        
        # button that displays the plot
        plot_button = ttk.Button(self, 
                     command = plot(self),
                     text = "Plot")
  
        # place the button 
        # in main window
        plot_button.grid(row = 4, column = 1, padx = 10, pady = 10)'''
        
    
    def pre_show(self):
        pass

    
class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = ttk.Label(self, text ="Page 3", font = LARGEFONT)
        self.label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 2, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 1, column = 1, padx = 10, pady = 10)
       
        # button to show frame 2 with text
        # layout2
        button3 = ttk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)
    
    def pre_show(self):
        pass
  
# Driver Code

apptk = tkinterApp()
apptk.mainloop()


# In[ ]:





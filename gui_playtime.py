#!/usr/bin/env python
import tkinter as tk
from tkinter import *
from tkinter import ttk
import app
import tkintermapview
import pandas as pd

LARGEFONT =("Verdana", 35)


class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def pre_show(self):
        pass


class Navbar(tk.Frame):
    def __init__(self, parent, labels, pages):
        tk.Frame.__init__(self, parent)
        
        self.parent = parent
        self.buttons = []
        self.nav_pages = []
        
        for label, page in zip(labels, pages):
            self.register_page(label, page)

    def register_page(self, label, page):
        page_index = len(self.nav_pages)
        button = ttk.Button(self, text=label, command=lambda: self.select(page_index))
        button.grid(row=0, column=page_index)

        self.nav_pages.append(page)
        self.buttons.append(button)

    def select(self, page_index):
        self.parent.show_page(self.nav_pages[page_index])
        for i, button in enumerate(self.buttons):
            if i == page_index:
                button["state"] = "disabled"
            else:
                button["state"] = "normal"

class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.app_vars = {
            "city": None
        }
        
        # Create container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # Create frames
        self.page_map = {
            "Start Page": StartPage(container, self),
            "Page 1": Page1(container, self),
            "Page 2": Page2(container, self), 
            "Page 3": Page3(container, self)
        }
        for page in self.page_map.values():
            page.grid(row=0, column=0, sticky="nsew")

        self.navbar = Navbar(self, tuple(self.page_map.keys()), tuple(self.page_map.values()))
        self.navbar.pack()

        self.navbar.select(0)

    def show_page(self, page):
        print("Showing", page)
        page.pre_show()
        page.tkraise()


class StartPage(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        self.configure(bg='green')
        
        #label of frame Layout 2
        #label = ttk.Label(self, text ="Rent vs Buy: User Data", font = LARGEFONT)
        #label.place(anchor=CENTER)
        
        my_city = tk.StringVar(self, name="My City",value='')
        
        label = tk.Label(self, font = ('Times New Roman', 25), text = "What city will you move to?" )
        label.place(relx=0.5, rely=0.5, anchor=CENTER)

        drop_cities = tk.OptionMenu( self , my_city , *app.get_city_list(), command = self.cache_city)
        drop_cities.place(relx=0.5, rely=0.6, anchor=CENTER)

        data_labal_var = tk.StringVar()
        data_label = tk.Label(self, textvariable=data_labal_var)
        data_label.grid(row=10,column=0,padx=0)
        
    def cache_city(self, city):
        self.controller.app_vars['city'] = city


class Page1(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        self.configure(bg='green')
        
        self.title_svar=tk.StringVar()
        tk.Label(self, textvariable = self.title_svar, font = ('Times New Roman', 25)).place(relx=0.5, rely=0.1, anchor=N)

        #self.result_var = tk.StringVar()
        #tk.Label(self, textvariable=self.result_var).place(relx=0.5, rely=0.5, anchor=S)
        
        
        #app.get_info(THIS IS WHERE THE VARIABLE USER INPUT WILL GO, HOW DO I REFER TO THE APP-VARS?
        
        #AVERAGE RENT IN AREA
        self.av_rent = tk.StringVar()
        label_av_rent = tk.Label(self , textvariable = self.av_rent)
        label_av_rent.place(relx=0.5, rely=0.9, anchor=S)
        
        #YoY % Rent
        self.yoy_rent = tk.StringVar()
        label_yoy_rent = tk.Label( self , textvariable = self.yoy_rent )
        label_yoy_rent.place(relx=0.5, rely=0.8, anchor=S)
        #Median Home Value in Area
        self.med_hval = tk.StringVar()
        label_med_hval = tk.Label( self , textvariable = self.med_hval  )
        label_med_hval.place(relx=0.5, rely=0.7, anchor=S)
        
        #YoY% increase home priced
        self.yoy_inc_home = tk.StringVar()
        label_yoy_inc_home = tk.Label( self , textvariable = self.yoy_inc_home )
        label_yoy_inc_home.place(relx=0.5, rely=0.6, anchor=S)
        
        #mortgage payment if 5%
        self.mort_5 = tk.StringVar()
        label_mort_5 = tk.Label( self , textvariable = self.mort_5 )
        label_mort_5.place(relx=0.5, rely=0.5, anchor=S)
        
        #mortgage payment if 20%
        self.mort_20 = tk.StringVar()
        label_mort_20 = tk.Label( self , textvariable = self.mort_20 )
        label_mort_20.place(relx=0.5, rely=0.4, anchor=S)


    def pre_show(self):
        city = self.controller.app_vars['city']
        if not city :
            self.av_rent.set('City not selected')
            self.title_svar.set('Please Select a City')
            return
        self.title_svar.set(f"Rent/Buy Data for {city}")
        self.av_rent.set(f'{city} has an average rent of: ${str(app.av_rent(city))}')
        self.yoy_rent.set(f'{city} has an yearly rent increase of: {str(app.yoy_rent(city))}%')
        self.med_hval.set(f'{city} has a median home value of: ${str(app.med_home_val(city))}')
        self.yoy_inc_home.set(f'{city} home prices increase yearly by: {str(app.yoy_home_val(city))}%')
        self.mort_5.set(f'A home in {city} with a 5% down payment would have a monthly mortgage payment of: ${str(app.mort_5(city))}')
        self.mort_20.set(f'A home in {city} with a 20% down payment would have a monthly mortgage payment of: ${str(app.mort_20(city))}')


# third window frame page2
class Page2(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.title_svar=tk.StringVar()
        tk.Label(self, textvariable = self.title_svar, font = LARGEFONT).place(relx=0.5, rely=0.1, anchor=N)
        
        
        #NEED TO CHANGE THIS TO THE DATAFRAMES WE ARE USING


        self.configure(bg='green')
    def pre_show(self):
        city = self.controller.app_vars['city']
        df = app.calc_mortgage(city) 
        text = tk.Text(self)
        text.insert(tk.END, str(df))
        text.place(relx=0.5, rely=0.6, anchor=CENTER)
        if not city :
            self.title_svar.set('Please Select a City')
            return
        self.title_svar.set(f"Table Data for {city}")
        
        
class Page3(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
    def pre_show(self):
        city = self.controller.app_vars['city']
        self.map_widget = tkintermapview.TkinterMapView(self, width=800, height=600, corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.map_widget.set_zoom(15)
        self.map_widget.set_address(self.controller.app_vars['city'])
        
tkinterApp().mainloop()
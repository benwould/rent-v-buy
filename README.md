# rent-v-buy


We have been hired as a Fintech data analyst at FTX. We will have to determine where to move to next. FTX has offices in 10 cities across the US. We get to select one to move too, the question is which one makes the most fiscal sense to move to. We need to determine if we should purchase a home with a mortgage on various terms or rent our new home in your selected city.

To help determine what you should do use our Rent-v-Buy module to use current housing data and your personal imputs to determine if you shoudl Rent or Purchase you new home in your city of choice. In order to make the best choice you will be presented with the accrued equity in a mortgage of your home purchase and your cost incurred from Renting a home for your selected amount of years. 



## Technologies

This code was created with Python 3.9 and Jupyter Lab

* [pandas] - To create DataFrames and create functions to manipulate the DataFrames into various outputs

* [tkinter] - For greating the GUI input field and for displaying our outputs as graphs, dataframes, and 

* [numpy] - For creating mortgage calculations

* [matplotlib] - For implementing our plots and data into our GUI

* []



## Installation Guide


'''python
pip install pandas
pip install numpy
pip install matplotlib
pip install tkinter

'''

## Usage

Welcome to our Rent v. Buy application!

To begin this application run our File "GUI _____.ipynb" this creates 
a pop out GUI where we are presented with our first step.

Step 1: Select the city we are moving to, the dropdown menu displays 10 cities that can be selected from

        Pick a city we would like to move to in our new role at FTX

Step 2: Click on Page 1 to continue, here the GUI displays a various data points related to the city we selected
        
Step 3: Analyze the print out
        Here are the relevant data points that were pulled from our RedFin DataFrame,
        Keep in mine this is only a list list for the selected city:

        -Monthly Mortgage Payment with a 20% downpayment
        -Monthly Mortgage Payment with a 5% downpayment
        -Average yearly Home Price percentage increase 
        -Median Home Value
        -Averaage yearly Rent Price percentage increase
        -Average Monthly Rent Price


Step 4: Click on Page 2 to contiue, here the GUI displays a breakdown 

Step 5: Analyze the print out
        Here you will see a breakdown of the Average Mortgage details for the possible options.
        We've been given 4 different Mortage options:
        1) 15 year, 5% downpayment
        2) 15 year, 20% downpayment
        3) 30 year, 5% downpayment
        4) 30 year, 20% downpayment


        From these 4 Mortgage options we are being shown the details of the Mortgage
        -Home Price, Median home price pulled from our DataFrame
        -DownPayment, percentage shown from the the above Mortgage options
        -Loan Amount, which is calculated from the total loan subtract the downpayment
        -Interest Rate, is pulled from a database of current average rates for each Mortgage option
        -Loan Duration, determined by the loan term and displated in Months
        -Monthly Taxes, pulled from our dataset and calculated for home price
        -Total Monthly Payment, calculated from Loan Amount, Loan Duration and Interest
        -Total Cost of Loan, creates a sum of all costs for the loan duration


    *** graphs for amortization and loan terms


Step 6: Click on Page 3 to continue, here the GUI displays the map of the selected city

Step 7: Here we are able to look around the general area of the selected city



Below is a Demo Video link to see how the GUI can be used      

    *** add in video


## Contributors

Austin Caras
Ben Harrington
Madhuri Krishna
Brian Peebles
Ben Wood


## License

MIT
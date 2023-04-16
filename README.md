AUTHOR: Hamza Imran
AFFILIATION: Capital University of Science and Technology
DATE CREATED: April 16, 2023
DESCRIPTION: This program is a currency converter app written in Python using the tkinter library and the Open Exchange Rates API. It allows users to convert between different currencies based on current exchange rates.

HOW TO RUN THE PROGRAM:
	1- Make sure you have the lastest version of Python installed on your computer and connected with your IDE.
	2- Make sure your computer is connected to the internet.
	3- Open the "main" file in the IDE of your choice in a new project.
	4- Run the program.
	
	
DESCRIPTION OF THE APP:
	The App has two drop down menus, one to select the base currency, and one to select the target currency. After selecting the desired currencies, enter the amount of base currency, that you want to convert to your target currency, and press enter. The resultant amount in the target currency will be displayed. Click on clear button to immediately clear all input.


HOW THE PROGRAM WORKS: 
	1- First all the avaialable currencies are fetched from the "openexchangerates.org".
	2- Then GUI window is used to display the currencies and take inputs.
	3- After the inputs are taken from the user, exchange rates of all the currencies are fetched from the "openexchangerates.org", which are given in USDs
	4- Then program calculates a conversion rates using the formuala "conversion rate = exchange rate of target currency / exchange rate of base currency". i.e. conversion rate =  279 PKR / 1 USD.
	5- Then total converted amount is calculated by using the formula "converted amount = amount of base currency * conversion rate". i.e. amount=100 USD, conversion rate=279, so converted amount = 27,900 PKR. 
	
SOURCE: https://github.com/hamza0923/Currency-Converter-Using-Python-Tkinter-Library

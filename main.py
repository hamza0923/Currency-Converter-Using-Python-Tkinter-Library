# Author: Hamza Imran
# Affiliation: Capital University of Science and Technology
# Date created: April 16, 2023.
# Description: This program is a currency converter app written in Python
# using the tkinter library and the Open Exchange Rates API.
# It allows users to convert between different currencies based on current exchange rates.


from tkinter import Button, Label, Tk, ttk, Frame, Entry, END
import requests

# App ID for Open Exchange Rates
api_key = '56b5774e71ee42aab3f82bc0b68fe632' #GET YOUR OWN API FROM "https://openexchangerates.org"


# ==========================API TO GET ALL AVAILABLE CURRENCIES===============================================
url = "https://openexchangerates.org/api/currencies.json"

# Make request to Open Exchange rates Server to get all available currencies
response = requests.get(url)

# check if server responded successfully
if response.status_code == 200:
    # fetch the data in jason format
    currencies = response.json()
    # properly format the currency names for drop down menu as "USD - United States Dollar" and store them in a list
    currency_names = [f"{currency_code} - {currency_name}" for currency_code, currency_name in currencies.items()]
    # LOG ENTRY
    print('\n', "=>Program Fetched Following Currencies Successfully", '\n', currency_names)

# if server response failed
else:
	# Print error message with corresponding error code
    print("Error:", response.status_code, response.reason)


# ==========================Function Convert the Input Values with API=====================================
def convert():

	# Get the base currency, target currency and amount from the drop-down menus
	base_currency = From_drop.get()[:3]		# only using the currency code like "USD"
	target_currency = To_drop.get()[:3]		# only using the currency code like "USD"
	amount = float(Input.get())				# parsing the entered string value to Int

	# LOG ENTRY
	print('\n', "=>From:", base_currency, "To:", target_currency, "with amount:", amount)

	#format the url with App ID key
	api_url = f'https://openexchangerates.org/api/latest.json?app_id={api_key}'
	# Make a request to the API to get the latest exchange rates
	api_response = requests.get(api_url)

	# check if server responded successfully
	if api_response.status_code == 200:
		# fetch the data in jason format
		data = api_response.json()
		# only fetch the rates from the data
		exchange_rates = data['rates']

		# LOG ENTRY
		print('\n', "=>Program fetched Following exchange Rates Successfully", '\n', exchange_rates)

		# Calculate the conversion rate from base currency to target currency
		conversion_rate = exchange_rates[target_currency] / exchange_rates[base_currency]

		# Convert the amount from base currency to target currency
		converted_amount = amount * conversion_rate
		converted_amount = f'{converted_amount:.3f}'   # format to only 3 values after decimal
		result = f'{converted_amount} {target_currency}'

		# LOG ENTRY
		print('\n', "=>RESULT: ", amount, base_currency, " = ", result)

		# Display the converted Rate on GUI
		Result['text'] = result

	# if server response failed
	else:
		# Print error message with corresponding error code
		print("Error:", response.status_code, response.reason)

# ==================================Function to Reset the GUI==============================================
def reset():
	# deleting the values of all input fields
	From_drop.delete(0, END)
	To_drop.delete(0, END)
	Input.delete(0, END)
	Result['text'] = "0.000"
	# LOG ENTRY
	print("=>Screen Cleared")
# ===========================================GUI===========================================================
# -----------------------------------COLOR PALLET----------------------------------------
color1 = "#2c3439"    # Blueish Black      (primary)
color2 = "#dbd6cb"    # Gray               (secondary)
color3 = "#32424b"    # Blueish Dark Gray  (background)  (text color for interactive elements)
color4 = "#667985"    # steel blue         (accent color)


# -----------------------------------GUI WINDOW-------------------------------------------
main_win = Tk()									# Creating a window
main_win.title("Currency Converter")			# with title "Currency Converter",
main_win.geometry("800x450")					# dimensions "800x450",
main_win.resizable(width=False, height=False)	# not resizable,
main_win.config(background=color3)				# with background color "color 3"



# -------------------------------------HEADER------------------------------------------
# Creating a header
header = Frame(main_win, width=800, height=60, background=color2)
header.grid(row=0, column=0)

# giving the title bar a name
title = Label(text="Currency Converter", background=color2, foreground=color1, font=('open sans', 26, "bold"))
title.grid(row=0, column=0)



#---------------------------------------BODY---------------------------------------------
# making a body section
body = Frame(main_win, width=800, height=390, background=color3, padx=100, pady=50)
body.grid(row=1, column=0)



#--------------------------------------INPUTS---------------------------------------------
#label for base currency
From = Label(body, text="From", font=("open sans", 14), background=color3, foreground=color2)
From.place(x=0, y=20)
#drop down menu for base currency
From_drop = ttk.Combobox(body, width=14, font=("open sans", 14))
From_drop['values'] = currency_names
From_drop.place(x=0, y=50)

#label for target currency
To = Label(body, text="To", font=("open sans", 14), background=color3, foreground=color2)
To.place(x=205, y=20)
#drop down menu for target currency
To_drop = ttk.Combobox(body, width=14, font=("open sans", 14))
To_drop['values'] = currency_names
To_drop.place(x=205, y=50)

#label for input field
In = Label(body, text="Amount to Convert From", font=("open sans", 14), background=color3, foreground=color2)
In.place(x=0, y=100)
Input = Entry(body, justify="center", width=29, font=("open sans", 17, "bold"))
Input.place(x=0, y=130)



#-------------------------------------RESULT DISPLAY------------------------------------------
# output label to display the converted amount
Result = Label(body, text="0.000", justify="center", width=12, height=4, background=color2, foreground=color1, font=("open sans", 18, 'bold'))
Result.place(x=420, y=70)
# label for output screen
Out = Label(body, text="Result", justify="center", width=16, padx=3, font=("open sans", 14), background=color2, foreground=color1)
Out.place(x=420, y=70)

#----------------------------------------BUTTONS-----------------------------------------------
# button to convert the entered amount
Convert = Button(body, text="Convert", width=31, height=1, pady=8, font=("open sans", 14, "bold"), command=convert)
Convert.place(x=0, y=200)

# button to reset the GUI window
Reset = Button(body, text="Clear", width=19, padx=4, height=1, font=("open sans", 12), command=reset)
Reset.place(x=420, y=200)

#-------------------------------------MAIN LOOP-----------------------------------------------
main_win.mainloop()

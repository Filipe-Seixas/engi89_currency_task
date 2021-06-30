# Currency Task

<h2>exchange_rate_parser.py</h2>

- In this file we have three functions, one that shows all available rates in the JSON file, another to show only the currency code that the user has inputted.
- The third function makes use of a live API to get data regarding currency.
```python
import json
import requests


# Create a class to show currency exchange rates
class ExchangeCurrency:

    # Open JSON file and assign it to variable
    rates_file = open('exchange_rates.json', )
    # Return a JSON object as a dict and assign to variable
    rates = json.load(rates_file)

    # Function to show all exchange rates
    def show_all_rates(self):
        print("Here are all our available rates")
        # print keys and values of dict
        for code, rate in self.rates['rates'].items():
            print(str(code) + ": " + str(rate))
        return "Thank you!"

    # Function to show the user inputted rate
    def show_rate(self, code):
        # If the code matches a key in the JSON file
        if code in self.rates['rates'].keys():
            print(f"{code} exchange rate is {self.rates['rates'][code]}")
        else:
            return "Sorry we don't recognize that currency code."
        return "Thank you!"

    # Function to get currency data from Fixer API
    def rates_api(self):
        # Call API
        check_response = requests.get("http://data.fixer.io/api/latest?access_key=f1e83da1e71ebd3966749e7d2472fa68")
        # If the response is successful, code 200
        if check_response:
            # Turn response to json format
            json_response = check_response.json()
            # Get dicts
            base = json_response['base']
            date = json_response['date']
            currencies = json_response['rates']
            # Return base, date, and all currencies from API
            return f"Date: {date}\n" \
                   f"Base: {base}\n" \
                   f"Currencies: {currencies}"
        else:
            return "Sorry something went wrong..."
```
<h2>program.py</h2>

- This is where we run our program because we have built a package. 
- Here we ask the user for their input to see which function we should run, there are also some options to make it more user-friendly.
```python
# Import class from .py file
from app.exchange_rate_parser import ExchangeCurrency

# Create class object
currency = ExchangeCurrency()

while True:
    desired_rate = input("Hello! Please input your desired country code (type 'help' for options):  ")
    # If user inputs 'all' run the show_all func
    if desired_rate.upper() == "ALL":
        print(currency.show_all_rates())
    # If user inputs 'api' run the func that connects to currency API
    elif desired_rate.upper() == "API":
        print(currency.rates_api())
    # If user inputs 'help' give them some options
    elif desired_rate.upper() == "HELP":
        print("You can type a currency code you know \n"
              "OR type 'all' to show all currencies exchange rates \n"
              "OR type 'api' to show currency data from a live API \n"
              "OR type 'exit' to close program.")
    elif desired_rate.upper() == "EXIT":
        break
    else:
        # Print all rates from function
        print(currency.show_rate(desired_rate.upper()))
```
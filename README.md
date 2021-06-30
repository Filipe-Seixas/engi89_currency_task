# Currency Task

<h2>exchange_rate_parser.py</h2>

- In this file we have two functions, one that shows all available rates in the JSON file, and another to show only the currency code that the user has inputted.
```python
import json


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
    # If user inputs 'help' give them some options
    elif desired_rate.upper() == "HELP":
        print("You can type a currency code you know \n"
              "OR type 'all' to show all currencies exchange rates \n"
              "OR type 'exit' to close program.")
    elif desired_rate.upper() == "EXIT":
        break
    else:
        # Print all rates from function
        print(currency.show_rate(desired_rate.upper()))
```
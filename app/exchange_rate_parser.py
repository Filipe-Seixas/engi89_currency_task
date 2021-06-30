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

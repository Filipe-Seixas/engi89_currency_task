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

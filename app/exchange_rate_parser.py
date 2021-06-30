import json


# Create a class to show currency exchange rates
class ExchangeCurrency:

    # Open JSON file and assign it to variable
    rates_file = open('exchange_rates.json', )
    # Return a JSON object as a dict and assign to variable
    rates = json.load(rates_file)

    # Function to show exchange rate
    def show_all_rates(self):
        print("Here are all our available rates")
        for code, rate in self.rates['rates'].items():
            print(str(code) + ": " + str(rate))
        return "Thank you!"

    def show_rate(self):
        pass


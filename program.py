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

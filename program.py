# Import class from .py file
from app.exchange_rate_parser import ExchangeCurrency

# Create class object
currency = ExchangeCurrency()

while True:
    desired_rate = input("Hello! Please input your desired country code:  ")


# Print all rates from function
# print(currency.show_all_rates())
print(currency.show_rate())

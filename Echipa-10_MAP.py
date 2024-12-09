import requests
import tkinter as tk
from tkinter import ttk, messagebox

#Fetch the exchange rate using the API
def get_exchange_rate(from_currency, to_currency):
    api_url = f"https://v6.exchangerate-api.com/v6/your-api-key/latest/{from_currency}" #replace your-api-key with your API key from here https://app.exchangerate-api.com/keys
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rates'][to_currency]  # Extract conversion rate for the target currency
    else:
        raise Exception("API request failed")

#Validate that the currency is one of the accepted codes
def validate_currency(currency):
    valid_currencies = ['USD', 'EUR', 'RON', 'GBP']
    if currency not in valid_currencies:
        raise ValueError(f"Invalid currency code. Available options are: {', '.join(valid_currencies)}")

#Handle currency conversion logic when the user presses the 'Convert' button
def convert_currency():
    try:
        from_currency = from_currency_combobox.get().strip().upper()
        to_currency = to_currency_combobox.get().strip().upper()
        amount = float(amount_entry.get())

        # Validate selected currencies
        validate_currency(from_currency)
        validate_currency(to_currency)

        # Get exchange rate and perform conversion
        rate = get_exchange_rate(from_currency, to_currency)
        converted_amount = rate * amount

        # Display the result
        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Currency Converter")
# Set the size of the window
root.geometry("500x400")

# Add labels
tk.Label(root, text="Currency Converter", font=("Arial", 16)).pack(pady=10)

# Base currency selection
tk.Label(root, text="Select base currency:").pack(pady=5)
from_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "RON", "GBP"])
from_currency_combobox.set("USD")  # Default value
from_currency_combobox.pack(pady=5)

# Target currency selection
tk.Label(root, text="Select target currency:").pack(pady=5)
to_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "RON", "GBP"])
to_currency_combobox.set("EUR")  # Default value
to_currency_combobox.pack(pady=5)

# Amount input field
tk.Label(root, text="Enter amount:").pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_currency, bg="green")
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
    
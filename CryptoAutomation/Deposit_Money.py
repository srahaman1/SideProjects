import cbpro

auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)

# Set Parameters
payment_id = auth_client.get_payment_methods()[0].get("id")
amount = "10.00"  # Coinbase has a $10.00 USD minimum deposit
currency = "USD"

"""Each time the following is run successfully, 
your bank account will be debited."""
# # Deposit USD
auth_client.deposit(amount, currency, payment_id)
print(f"{amount} {currency} has been deposited to Coinbase!")

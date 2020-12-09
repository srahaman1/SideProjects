import cbpro

auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)
amount = NULL  # Insert amount here
currency = "USD"

# Convert(Buy) to Coin (BTC Default)
transaction = auth_client.place_market_order(
    product_id="BTC-USD", side="buy", funds=amount
)
transaction_id = str(transaction.get("id"))
transaction_status = auth_client.get_order(transaction_id).get("status")
print(f"An order for {amount} {currency} has been placed")
# Wait until order is posted to block chain
while transaction_status == "pending":
    print("pending...")
    transaction_status = auth_client.get_order(transaction_id).get("status")
print("Posted to Blockchain! The coin is all yours!")

"""
Sources:
https://docs.pro.coinbase.com/#crypto
https://github.com/danpaquin/coinbasepro-python/blob/master/cbpro/authenticated_client.py
"""

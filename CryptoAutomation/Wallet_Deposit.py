import cbpro

auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)
"""account_id can be foundusing the following. Identify the id
 associated with the cryptocurrency you are looking to deposit from."""
print(auth_client.get_accounts())
"""insert account_id below"""
# Send whatever has been waiting in wallet to Celcius
withdrawal_amount = auth_client.get_account("insert_account_id").get("balance")

wallet = insert_wallet_address  # put wallet address here, ensure it is correct.
print(auth_client.crypto_withdraw(withdrawal_amount, "BTC", wallet))
print("Sent to Wallet!(Now pending in Coinbase)")
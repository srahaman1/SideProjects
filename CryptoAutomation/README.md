# CAUTION: USING THIS CODE WILL USE REAL MONEY. THIS IS FOR EDUCATIONAL PURPOSES ONLY. IN USING THIS CODE, YOU AGREE THAT I AM NOT RESPONSIBLE/ CAN NOT BE HELD RESPONSIBLE FOR THE RESULTS.
## USE Deposit_Money.py with extreme caution
# Overview

This project came about because while looking through my own personal investments regarding cryptocurrencies, I noticed that while the cryptocurrency exchange, Coinbase, offered its users an API, it did not offer a recurring investment option on its exchange. Therefore, I set out to build my own!

This consisted of depositing USD into the exchange for use (Deposit_Money.py) and using those funds to purchase the currency of choice, in one case for me it was Bitcoin (Convert_to_BTC.py). Furthermore, I programmed the code to immediately deposit any crypto I have on the exchange into a wallet for security reasons (Wallet_Deposit.py).

The code has been separated into thirds as a safety precaution. 

To reassemble, into a single file, my original file was ordered Wallet_Deposit.py, Deposit_Money.py, and then Convert_to_BTC.py

The rationale for this order is because Coinbase takes approxiamately 1 week with the bank for the initial deposit and the currency cannot be moved from the exchange until the deposit is cleared.

# Future Considerations
In this project, I set out to build a recurring investment tool for my coinbase and is technically incomplete as far as complete automation goes. For instance, I have not added a scheduling functionality in the code. 

As it stands now, the code needs me to run each time I would like to purchase crypto. For now, this functionality is intentionally removed as I would like to have active control of the amounts, currencies, and wallets.

# bitvavo_wallet_monitor
Monitor crypto currency balance held across various accounts/wallets

Easily monitor the balance and value of your crypto currencies using this simple program.
Even better: when you have moved currencies to an offline wallet (e.g. hardware wallet like Ledger Nano), you can still monitor the value using this simple program.

Setup:
Enter the details of your purchases in the purchases.csv file
date &time: date and time of purchase (optional)
currency: Currency code (e.g BTC)
number: number of coins you purchased
investment: countervalue of the purchase
base: currency of the investment (e.g. EUR)

The program will create a new file (analysis.csv) that will show
- today's opening rate
- current rate
- current value of the position (in the purchase currency)
- value increase (compared to the purchase price)
- value increase (in percent, relative to purchase price)
- day delta: price increase (in %) compared to today's opening rate

 It will print some of the above details on screen too:
 - currency
 - current value
 - increase (amount in base currency)
 - increase (in percent)

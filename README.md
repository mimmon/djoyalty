# djoyalty
*Very basic django based loyalty system* 

This is supposed to run in browser at "brick and mortar" store. The cashier will identify the customer by his code. 
Customer has cards with barcoded number code so it can be input with bar code scanner.
When customer makes a purchase the price is recorded as a Transaction. After reaching a threshold the customer is entitled to ask for discount.
If a transaction is flagged as discounted, it is not added to "credit transactions", but the negative threshold value is added to transactions. The value of the discounted purchase can be recorded for statistic purposes but is not considered in any other calculations (in current design).

## Example
Threshold = 50 (EUR, USD, points, stamps)

Purchase 1: customer buys goods for 35 EUR. Earns 35 credits. Has 35 credits.
Not entitled to get a discount yet.

Purchase 2: customer buys goods for 25 EUR. Earns 25 credits. Has 60 credits.
Entitled to get a discount.

Purchase 3: customer buys goods for 100 EUR. Asks for 10% discount. Pays 90 EUR. (-50 EUR is added to customer's trasnactions.) 
At the next visit customer has 10 credits and is not entitled for discount.

## Technical details
### Models:
- Customer
- Txn (transactions)
- Event

** Customer **
The model stores customer details: name, address, contact + additional

** Txn (Transaction) **
The model stores all transactions related with earning or spending credits. Transactions can be full-priced, discounted and spending (=negative, when spending credits).

** Event **
Helper model to store tracked events (e.g. editing customer details, spending credits, backuping database etc.). Events can be customer related or non customer related.

from linked_binary_search_tree import SearchTree
from Stock import Stock

owned_stocks = SearchTree()
buy_more = "yes"

while buy_more == "yes":
    symbol = input("Enter the symbol of the stock you wish to buy.")
    name = input("Enter the name of the stock you wish to buy.")
    purchase_price = input("Enter the cost of the stock you wish to buy.")
    quantity = input("How much of the stock do you wish to buy?")
    stock_bought = Stock(symbol, name, purchase_price, quantity)
    owned_stocks.add(stock_bought)

    buy_more = input("Do you want to buy more stock? (yes/no)")


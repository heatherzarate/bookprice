# Program name: ZARATE_HEATHERFP
# Author: Heather Zarate
# Date: 5/16/2022
# Summary: write functions to get book price and calculate sales tax
# Variables:
#	bookPrice: book price entered by the user (float)
#	salesTaxAmt: amount of sales tax (float)
#	SALES_TAX_RATE: percentage rate for the sales tax (float)
#	amt: a local variable in getBookPrice() for the price of the book (float)
#   price: local variable in calculate taxes (float)
#   total: the total price of the book with tax (float)



# Declare constants
SALES_TAX_RATE = 0.07


# Ask for book price, do calculations, print
def main():
    bookPrice = getBookPrice ()
    salesTaxAmt = calculateTaxes (bookPrice)
    
    print("Total price: $", format(salesTaxAmt, ".2f" ), sep="")

    
def getBookPrice():
    amt = float(input ("Enter the price of the book: "))
    return amt
    
def calculateTaxes(amt):
    sales = amt * SALES_TAX_RATE
    total = amt + sales
    return total
    
main ()
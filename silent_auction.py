#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Flo
#
# Created:     10/05/2015
# Copyright:   (c) Flo 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

def setting_auction():
    #These are the questions the auctioneer answers before the auction starts
    reserve = input("What is the reserve price for the item?")
    print("Beginning auction...")
    print("The reserve price is ${:.2f}.".format(float(reserve)))

def get_bids(names, bid):
#Collects bid information - name, amount of bid
    print ("Collecting Bids")
    name = ""
    while name.upper() != 'F':
        name = input("What is the customer's name? (\"F\" to finish)")
        if name.upper()!= "F":
            names.append(name)
            thing = read_float("How much does " + name + " wish to bid?")
            bid.append(thing)
            highest_bid = (max(bid))
            print("{} bid ${:.2f}. The highest bid is ${:.2f}".format(name, bid[-1], highest_bid))

def show_report(bid):
#displays summary - total eggs, number of dozens to be ordered, average eggs per customer
    if len(names) == 0:
        print ("No bids")
    else:
        print("Summary of Auction")
        for i in range(len(names)):
            highest_bid = max(bid)
            print("{} bid ${:.2f}.".format(names[i], bid[i]))
        print("The highest bid was ${:.2f}".format(highest_bid))

def read_float(prompt):
#This checks whether the bid amount is a valid response
    money = -1;
    while money == -1:
        try:
            money = float(input(prompt))
            if money < bid:
                print ("Please raise your bid.")
        except ValueError:
            print ("Not a valid integer")
        return money


#main routine
names = []
bid = []
setting_auction()
get_bids(names, bid)
show_report(bid)

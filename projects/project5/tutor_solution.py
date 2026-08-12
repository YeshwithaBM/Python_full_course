import os 
def find_winner(bidder_details):
    highest_bidder=0
    winner=''
    for bidder in bidder_details:
        bidding_price=bidder_details[bidder]
        if bidding_price>highest_bidder:
            higest_bidder=bidding_price
            winner=bidder
    print(bidder_details)
    print(f"the winner is {winner} with the bid of {higest_bidder}")

bidder_data={}
while True:
    name=input("whats the name?:")
    price=int(input('what is the bid?:'))
    bidder_data[name]=price
    more_bidders=input("Are they any other bidders? Type 'Yes' or 'No'?:").lower()
    if more_bidders=='no':
        find_winner(bidder_data)
        break
    elif more_bidders=='yes':
        os.system('cls')



    

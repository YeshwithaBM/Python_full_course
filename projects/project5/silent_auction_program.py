import os
def silent_bid():
    data=[]
    while True:
        ask_name=input("what is your name?:")
        ask_bid=int(input("what is your bid?:"))
        details={}
        details['name']=ask_name
        details['bid']=ask_bid
        data.append(details)
        ask_any_other_bid=input("Are they any other bidders? Type 'Yes' or 'No': ").lower()
        if ask_any_other_bid=='no':
            wn_lst=[]
            for i in range(len(data)):
                wn_lst.append(data[i]['bid'])
        
            win=max(wn_lst)
            access_index=wn_lst.index(win)
            name_of_win=data[access_index]['name']

            print(f"the winner is {name_of_win} with bid of {win}")
            print(data)
            break
        elif ask_any_other_bid=='yes':
            os.system('cls')
        else:
            print("invalid input")
            os.system('cls')


silent_bid()        

            
        


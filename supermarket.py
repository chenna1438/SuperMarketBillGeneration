from datetime import datetime

print("----------------------------welcome----------------------------")
name=input("Enter your name:")
#list of items
lists='''
rice    Rs 50/Kg
Sugar   Rs 20/kg
Salt    Rs 20/kg
Oil     Rs 80/liter
Panner  Rs 120/kg
Maggie  Rs 40/kg
Boost   Rs 90/each
Colgate Rs 85/each
'''
#declaration

price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items  in dict format
items={'rice':50, 
       'sugar':20,
       'salt' :20,
       'oil':80,
       'panner':120, 'boost':90,'colgate':80}
option=int(input("for list of items press 1 : "))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If you want to buy press 1 or 2 for exit : "))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your item: ")
        quantity=int(input("Enter Quantity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you entered item is not available")
    else:
        print("You entered wrong number")
    inp=input("Can I bill items yes or no : ")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","chenna supermarket",25*"=")
            print(28*" ","vanaparthy")
            print("Name:",name,35*" ","Date:",datetime.now())
            print(75*"-")
            print("SNo.",8*" ",'Items',8*" ",'Quantity',8*" ",'Price')
            for i in range(len(pricelist)):
                print(i,11*' ',ilist[i],11*' ',qlist[i],12*" ",plist[i])
            print(75*"-")
            print(50*" ",'Total Amount:','Rs',totalprice)
            print(50*" ",'GST Amount:  ','Rs',gst)
            print(75*"-")
            print(50*" ",'Final Amount:','Rs',finalamount)
            print(75*"-")
            print(30*" ","Thanks for visiting")
            print(75*"-")
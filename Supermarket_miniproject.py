# supermarket bill generation

from datetime import datetime
print('***************************welcome*************************')
name=input('enter your name:')
address=input('enter your address:')

lists='''
milk    Rs 40/lit
sugar   Rs 35/kg
maaza   Rs 50/lit
oil     Rs 150/lit
Rice    Rs 15/kg
banana  Rs 45/dozen
apple   Rs 100/kg
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
plist=[]
qlist=[]
rlist=[]

items={'milk':40,'sugar':35,'maaza':50,'oil':150,'Rice':15,'banana':45,'apple':100}
opt=int(input('list of items press 1:'))
if opt==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input('if you want to buy press 1 or 2 for exit:'))
    if inp1==2:
        break
    if inp1==1:
        item=input('enter items:')
        quantity=int(input('enter quantity:'))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            plist.append(item)
            qlist.append(quantity)
            rlist.append(price)
            gst=(totalprice*8)/100
            finalprice=gst+totalprice
        else:
            print('sorry the items is not available')
    else:
        print('you entered wrong number')
    inp=input('you want to bill items yes or no:')
    if inp=='yes':
        pass
        if finalprice!=0:
            print(30*'=','prasad supermarket',30*'=')
            print(26*' ','madanapalle')
            print('Name:',name,35*' ','Date:',datetime.now())
            print(70*'-')
            print('sno,',7*' ','items',7*' ','quantity',4*' ','price')
            for i in range(len(pricelist)):
                print(i,5*' ',4*' ',plist[i],7*' ',qlist[i],rlist[i])
            print(70*'-')
            print(50*' ','totalamount:','Rs',totalprice)
            print('gst amount',50*' ','Rs',gst)
            print(70*'-')
            print(50*' ','finalamount:','Rs',finalprice)
            print(70*'-')
            print(25*' ','Thanks for visiting')
            print(70*'-')





                   
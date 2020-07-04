import xml.etree.ElementTree as ET

class BillingItems():
    # First we create a constructor for this class
    # and add members to it, here models

    def __init__(self):
        self

    def addItems(self, item, price, quantity):
        self.ITEMSList = [item, price, quantity]
        return self.ITEMSList

itemlist=[]
pricelist=[]
tree=ET.parse("product list.xml")
root=tree.getroot()
for child in root:
    itemlist.append(child.find('name').text)
    pricelist.append(child.find('price').text)
bill=0
dicti={}
dicti = dict(zip(itemlist,pricelist))
BILLINGSTATUS =True
productList = []
billingITEMS = BillingItems()
while BILLINGSTATUS:
    productName = input(" Enter the item name:")
    if(productName!='exit'):
        productPrice=0
        tempItem=''
        if productName not in dicti:
            tempItem = input(" This item is not in the list ,do yu want to add this item (y/n)")
            if tempItem == 'y':
                productPrice = int(input(" Enter the price you want to add for the item "))

            else:
                if tempItem == 'n':
                    print(" thankyou")
        else:
            productPrice =int(dicti[productName])
        if tempItem!='n':
            productQuantity =int(input("Enter "+productName+" Quantity:"))
            productList.append(billingITEMS.addItems(productName,productPrice,productQuantity))
            totalprice=productPrice*productQuantity
            bill=bill+totalprice
    else:
        BILLINGSTATUS = False
print(" The overall bill generated is ",bill)


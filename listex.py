fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
fruits.insert(0,"lemon")
print(fruits)
fruits.remove("banana")
print(fruits)
print(fruits.__len__())
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory["pocket"]=['seashell', 'strange berry','lint']
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
inventory["gold"]+= 50


prices={"banana":4,
    "apple":2,
    "orange":1.5,
    "pear":3}
for key,values in prices.items():
    print(key,":",values)
total=0
while total > 0:
   prices=total * key
print(prices)     
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
def compute_bill(stock):
    total=0
    for key in prices:
        if stock >= 0:
         key += total
        else:
            total -= key 
        return total
print(compute_bill(stock))        
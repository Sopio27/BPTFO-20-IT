import json

class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

listOfProducts = []

apples = product("apples", 1, 5)
bananas = product("bananas", 0.9, 3)

listOfProducts.append([apples.name, apples.price, apples.quantity])
listOfProducts.append([bananas.name, bananas.price, bananas.quantity])


json_string = json.dumps(listOfProducts)

with open("dumps.json", "w") as json_file:
    json.dump(json_string, json_file)


with open("dumps.json", "r") as json_file_2:
    python_data = json.load(json_file_2)
   
lst = json.loads(python_data)

for item in lst:
    for i in range(1):
        name = item[0]
        price = item[1]
        quantity = item[2]
        productx = product(name, price, quantity)
        print(f"Data: {productx.name, productx.price, productx.quantity}")

    
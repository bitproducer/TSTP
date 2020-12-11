class Customer:
    def __init__(self, name, email):
        self.name = name										# create variable name
        self.email = email										# create variable email
        self.purchases = []										# create a list for purchases

    def purchase(self, inventory, product):
        inventory_dict = inventory.inventory					# create dictionary
        if product in inventory_dict:							# is the product in the inventory dictionary
            if inventory_dict[product] > 0:						# is there more then 0 of the product in the inventory
                self.purchases.append(product)					# add product to costumer purchase list
                inventory_dict[product] -= 1					# reduce the product amount in the inventory dictionary
            else:
                print('We are out of stock!')
        else:
            print("We don't have that product!")

    def print_purchases(self):									# print list of all purchases for customer
        print("The customer has purchased")
        for item in self.purchases:
            print(item.name)


class Product:													# create class for products with name and price
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Inventory:												# create inventory class with inventory dictionary
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):					# function to add a product to dictionary
        if product not in self.inventory:						# check if product already exists in dictionary
            self.inventory[product] = quantity					# if not add it
        else:
            self.inventory[product] += quantity					# if it does increase of quantity

    def print_inventory(self):									# print inventory list
        for key, value in self.inventory.items():				# get the key and value for each item in the inventory dictionary
            print(key.name + ':' + str(value))					# print key and convert int value to str
        print()


customer = Customer('Joe', 'joe@gmail.com')						# create customer with name and email
#print(customer.name)
#print(customer.email)

apple_watch = Product('Apple Watch', 299)						# create product
#print(apple_watch.name)
#print(apple_watch.price)

mac = Product('Mac', 1999)										# create another product
#print(mac.name)
#print(mac.price)

inventory = Inventory()											# create inventory object
inventory.add_product(apple_watch, 100)							# add product to inventory list
#inventory.print_inventory()
inventory.add_product(mac, 498)									# add another product

inventory.print_inventory()
customer.purchase(inventory, apple_watch)
customer.purchase(inventory, mac)
inventory.print_inventory()
customer.print_purchases()

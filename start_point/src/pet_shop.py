# WRITE YOUR FUNCTIONS HERE
# import pdb

def get_pet_shop_name(shop):
    return shop["name"]


def get_total_cash(admin_cash):
    return admin_cash["admin"]["total_cash"]


def add_or_remove_cash(admin_cash, added_removed_cash):
#     pdb.set_trace()
    admin_cash["admin"]["total_cash"] += added_removed_cash
    return admin_cash

def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(pets_sold, new_sales):
    pets_sold["admin"]["pets_sold"] += new_sales
    return pets_sold

def get_stock_count(stock):
    return len(stock["pets"])

def get_pets_by_breed(shop, breed):
    same_breed = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            same_breed.append(pet)

    return same_breed

def find_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            shop["pets"].remove(pet)

def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]
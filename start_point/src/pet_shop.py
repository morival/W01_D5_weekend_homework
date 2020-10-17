# WRITE YOUR FUNCTIONS HERE
import pdb

def get_pet_shop_name(shop):
    return shop["name"]


def get_total_cash(shop):
    return shop["admin"]["total_cash"]


def add_or_remove_cash(shop, added_removed_cash):
    shop["admin"]["total_cash"] += added_removed_cash
    return shop

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

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash
    return customer

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(shop, pet_name, customer):
    for pet in shop["pets"]:
        if pet == pet_name:
            if customer_can_afford_pet(customer, pet_name):
                return add_pet_to_customer(customer, pet_name), increase_pets_sold(shop, get_customer_pet_count(customer)), remove_customer_cash(customer, pet["price"]), add_or_remove_cash(shop, pet["price"])
          


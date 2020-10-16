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


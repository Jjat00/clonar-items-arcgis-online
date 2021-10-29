from package.ArcgisOnline import ArcgisOnline

# Portal
portal = "https://www.arcgis.com"

# Credentials source portal
source_admin = "source_admin"
source_admin_password = "passwword_source_admin"
source_user = "source_admin"

# Credentials target portal
target_admin = "target_admin"
target_admin_password = "password_admin"
target_user = "target_admin"

# Create instance ArcgisOnline
def create_connections():
    source_connection = ArcgisOnline(portal, source_admin, source_admin_password, source_user)
    target_connection = ArcgisOnline(portal, target_admin, target_admin_password, target_user)
    return (source_connection, target_connection)

# Get item by id
def get_item_by_id(id, user_conection):
    item = user_conection.get_item_by_id(id)
    print("item name: %s" % (item.title))
    print("\n \n \n")
    return item

# Clone item from source_connection to target_connection
def clone_item(item, user_connection, folder_name):
    user_connection.clone_item(item, folder_name)

# Get all items users (Dashboard, wep app, web map, feature, ...)
def get_all_items(user_connection):
    user_inventory = user_connection.get_user_items()
    return user_inventory

# print item inventory users
def print_all_items(user_connection, user_inventory):
    print("inventory: \n")
    user_connection.print_user_inventory(user_inventory)

# Clonte all items user by type item
def clone_items_by_type(user_connection, user_inventory, type, folder_name):
    user_connection.clone_items_by_type(user_inventory, type, folder_name)

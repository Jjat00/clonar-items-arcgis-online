from clone_items import *

def run():
    # User connections
    source_connection, target_connection = create_connections()

    # Get item by ID
    #item = get_item_by_id("f1e743395da548b4805494800167b1d7", source_connection)

    # Clone item 
    #clone_item(item, target_connection, "copy-item")

    # Get all items
    print("SOURCE INENTORY: \n")
    source_user_inventory = get_all_items(source_connection)
    print_all_items(source_connection, source_user_inventory)

    print("TARGET INENTORY: \n")
    target_user_inventory = get_all_items(target_connection)
    print_all_items(target_connection, target_user_inventory)
    
    # Clone items by type
    #clone_items_by_type(target_connection, source_user_inventory, "Dashboard", "copy-all-dashboard")

if __name__ == '__main__':
    run()


 
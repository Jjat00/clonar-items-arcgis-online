# import libraries
import sys

from arcgis.gis import GIS
from arcgis.mapping import WebMap
from arcgis.env import active_gis

class ArcgisOnline():
    """
    This class clone items from account  agol to other agol.
    """

    def __init__(self, portal, owner, password, user):
        self.portal = portal
        self.owner = owner
        self.user = user
        self.password = password
        self.create_user_conection_gis()

    def create_user_conection_gis(self):
        """
        Create connection GIS

        return:
            :connection: connection GIS
                        return user connection account agol
        """
        self.user_connection = GIS(("%s%s" % ("https://", self.portal)), self.user, self.password, verify_cert=False)
        print(self.user_connection)
        print("Connected to Portals")
        #select source user
        connection_user = self.user_connection.users.search (self.user)
        print("User name: %s User role: %s" % (connection_user[0].username, connection_user[0].role ))

    def get_item_by_id(self, id_item):
        """
        Get item from Agol by ID
        paraters:
            :id_item: string
                id item layer, web app, web map, etc.
        return: 
            :item: arcgis object
                item -> i.e (Dashboard, Web app, Wem map, Leayer feature, ++)
        """
        item = self.user_connection.content.get(id_item)
        # Infotmation about layer
        print("title: ", item.title)
        print("id: ", item.id)
        print("type:", item.type)
        print("url: ", item.homepage)
        return item

    def clone_item(self, item, folder_name):
        """
        Clone item from account to another account
        Parameters: 
            :item: Arcgis Object
                item is: Dashboard, Web app, Wem map, Leayer feature, ++
            :folder_name: string
                folder name
        """
        # Clone item to target content
        cloned_flyr = self.user_connection.content.clone_items(items=[item],
                                                folder=folder_name)
        print(cloned_flyr)

    def get_user_items(self):
        """
        
        """
        user = self.user_connection.users.me
        user_inventory = {}
        user_items = self.user_connection.content.search(query=f"* AND owner:{user.username}", 
                                            max_items=500)
        for item in user_items:
            if item.type not in user_inventory:
                user_inventory[item.type] = [i for i in user_items 
                                            if i.type == item.type]
        return user_inventory   

    def clone_items(self, items, folder_name):
        """
        Clone item from account to another account
        Parameters: 
            :item: Arcgis Object
                item is: Dashboard, Web app, Wem map, Leayer feature, ++
            :folder_name: string
                folder name
        """
        # Clone item to target content
        for item in items:
            cloned_flyr = self.user_connection.content.clone_items(items=[item],
                                                    folder=folder_name)
            print("items cloned successfully")                                                    
            print(cloned_flyr)

    def print_user_inventory(self, inventory):
        """
        Show all items in user inventory
        paramters:
            :inventory: Dictionary Arcgis Object
        """
        for itype, ilist in inventory.items():
            try:
                print(f"{itype}\n{'-'*50}")
                for i in ilist:
                    print(f"{' ':3}{i.title:50}")
                print("\n")
            except Exception as e:
                print(f"\t\tOperation failed on: {i.title}")
                print(f"\t\tException: {sys.exc_info()[1]}")
                continue


    def clone_items_by_type(self, inventory, type, folder_name):
        """
        Clone items from account to another account by type.
        Paremeters:
            :inventory: Dictionary Arcgis Object
                    ""
            :type: string
                i.e: (Feature Service, Web Map, Service Definition, Web Mapping Application,
                    Dashboard, CSV)
        """
        if type == 'Feature Service' :
            items = inventory['Feature Service']
            self.clone_items(items, folder_name)
        if type == 'Web Map' :
            items = inventory['Web Map']
            self.clone_items(items, folder_name)
        if type == 'Service Definition' :
            items = inventory['Service Definition']
            self.clone_items(items, folder_name)
        if type == 'Web Mapping Application' :
            items = inventory['Web Mapping Application']
            self.clone_items(items, folder_name)
        if type == 'Dashboard' :
            items = inventory['Dashboard']
            self.clone_items(items, folder_name)
        if type == 'CSV' :
            items = inventory['CSV']
            self.clone_items(items, folder_name)
    
    


    



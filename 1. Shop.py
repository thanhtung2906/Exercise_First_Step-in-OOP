class Shop:
    def __init__(self,name,item):
        self.name = name
        self.item = item 
    def get_items_count(self):  
        count = len(self.item)
        print(count)

shop = Shop("My Shop",["Apple","Bananas","Cucumber"])
shop.get_items_count()
    
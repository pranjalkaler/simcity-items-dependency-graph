from enum import Enum

class Category(Enum):
    FACTORY_MADE = 1
    BUILDING_SUPPLIES = 2
    HARDWARE_STORE = 3
    GARDENING_SUPPLIES = 4
    FARMERS_MARKET = 5
    FURNITURE_STORE = 6
    DONUT_SHOP = 7
    FASHION_STORE = 8
    FAST_FOOD_RESTAURANT = 9

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
from node import Node
from scg_dependency_graph.constants.item_category import Category
from scg_dependency_graph.constants.item_type import Type
from scg_dependency_graph.render_graph import render_di_graph
def generate_dependency_graph():
    metal = Node(Type.INDUSTRIAL, 'Metal', Category.FACTORY_MADE)
    wood = Node(Type.INDUSTRIAL, 'Wood', Category.FACTORY_MADE)
    plastic = Node(Type.INDUSTRIAL, 'Plastic', Category.FACTORY_MADE)
    seeds = Node(Type.INDUSTRIAL, 'Seeds', Category.FACTORY_MADE)
    minerals = Node(Type.INDUSTRIAL, 'Minerals', Category.FACTORY_MADE)
    chemical = Node(Type.INDUSTRIAL, 'Chemical', Category.FACTORY_MADE)
    animal_feed = Node(Type.INDUSTRIAL, 'Animal Feed', Category.FACTORY_MADE)
    glass = Node(Type.INDUSTRIAL, 'Glass', Category.FACTORY_MADE)
    sugar_and_spices = Node(Type.INDUSTRIAL, 'Sugar and Spices', Category.FACTORY_MADE)
    textiles = Node(Type.INDUSTRIAL, 'Textiles', Category.FACTORY_MADE)

    # Building Supplies Store
    nails = Node(Type.COMMERCIAL, 'Nails', Category.BUILDING_SUPPLIES)
    planks = Node(Type.COMMERCIAL, 'Planks',  Category.BUILDING_SUPPLIES)
    bricks = Node(Type.COMMERCIAL, 'Bricks',  Category.BUILDING_SUPPLIES)
    cement = Node(Type.COMMERCIAL, 'Cement', Category.BUILDING_SUPPLIES)
    glue = Node(Type.COMMERCIAL, 'Glue', Category.BUILDING_SUPPLIES)
    paint = Node(Type.COMMERCIAL, 'Paint', Category.BUILDING_SUPPLIES)

    # Hardware Store
    hammer = Node(Type.COMMERCIAL, 'hammer', Category.HARDWARE_STORE)
    tape = Node(Type.COMMERCIAL, 'measuring tape', Category.HARDWARE_STORE)
    shovel = Node(Type.COMMERCIAL, 'Shovel', Category.HARDWARE_STORE)
    cooking_utensils = Node(Type.COMMERCIAL, 'Cooking Utensils', Category.HARDWARE_STORE)
    ladder = Node(Type.COMMERCIAL, 'Ladder', Category.HARDWARE_STORE)

    # Gardening Supplies
    grass = Node(Type.COMMERCIAL, 'Grass', Category.GARDENING_SUPPLIES)
    tree_saplings = Node(Type.COMMERCIAL, 'Tree Saplings', Category.GARDENING_SUPPLIES)
    gardening_furniture = Node(Type.COMMERCIAL, 'Gardening Furniture', Category.GARDENING_SUPPLIES)
    fire_pit = Node(Type.COMMERCIAL, 'Fire Pit', Category.GARDENING_SUPPLIES)


    # Farmer's Market
    vegetables = Node(Type.COMMERCIAL, 'Vegetables', Category.FARMERS_MARKET)
    flour_bag = Node(Type.COMMERCIAL, 'Flour Bag', Category.FARMERS_MARKET)
    fruit_and_berries = Node(Type.COMMERCIAL, 'Fruit and Berries', Category.FARMERS_MARKET)
    cream = Node(Type.COMMERCIAL, 'Cream', Category.FARMERS_MARKET)
    corn = Node(Type.COMMERCIAL, 'Corn', Category.FARMERS_MARKET)
    cheeze = Node(Type.COMMERCIAL, 'Cheeze', Category.FARMERS_MARKET)
    beef = Node(Type.COMMERCIAL, 'Beef', Category.FARMERS_MARKET)

    # Furniture Store
    chairs = Node(Type.COMMERCIAL, 'Chairs', Category.FURNITURE_STORE)
    tables = Node(Type.COMMERCIAL, 'Tables', Category.FURNITURE_STORE)
    home_textiles = Node(Type.COMMERCIAL, 'Home Textiles', Category.FURNITURE_STORE)
    cupboard = Node(Type.COMMERCIAL, 'Cupboard', Category.FURNITURE_STORE)

    # Donut Shop
    donuts = Node(Type.COMMERCIAL, 'Donuts', Category.DONUT_SHOP)
    green_smoothie = Node(Type.COMMERCIAL, 'Green Smoothie', Category.DONUT_SHOP)
    bread_roll = Node(Type.COMMERCIAL, 'Bread Roll', Category.DONUT_SHOP)
    cherry_cheezecake = Node(Type.COMMERCIAL, 'Cherry Cheezecake', Category.DONUT_SHOP)
    frozen_yogurt = Node(Type.COMMERCIAL, 'Frozen Yogurt', Category.DONUT_SHOP)

    # Fashion Store
    cap = Node(Type.COMMERCIAL, 'Cap', Category.FASHION_STORE)
    shoes = Node(Type.COMMERCIAL, 'Shoes', Category.FASHION_STORE)
    watch = Node(Type.COMMERCIAL, 'Watch', Category.FASHION_STORE)

    # Fast Food Restaurant
    ice_cream_sandwich = Node(Type.COMMERCIAL, 'Ice Cream Sandwich', Category.FAST_FOOD_RESTAURANT)
    pizza = Node(Type.COMMERCIAL, 'Pizza', Category.FAST_FOOD_RESTAURANT)

    # Building Supplies Store
    nails.requires(metal, 5)

    planks.requires(wood, 2)

    bricks.requires(minerals, 2)

    cement.requires(minerals, 2)
    cement.requires(chemical, 1)

    glue.requires(plastic, 1)
    glue.requires(chemical, 2)

    paint.requires(metal, 2)
    paint.requires(minerals, 2)
    paint.requires(chemical, 2)

    # Hardware Store
    hammer.requires(metal, 1)
    hammer.requires(wood, 1)

    tape.requires(metal, 1)
    tape.requires(plastic, 1)

    shovel.requires(metal, 1)
    shovel.requires(wood, 1)
    shovel.requires(plastic, 1)

    cooking_utensils.requires(metal, 2)
    cooking_utensils.requires(wood, 2)
    cooking_utensils.requires(plastic, 2)

    ladder.requires(metal, 2)
    ladder.requires(planks, 2)

    # Farmer's Market
    vegetables.requires(seeds, 2)

    flour_bag.requires(seeds, 2)
    flour_bag.requires(textiles, 2)

    fruit_and_berries.requires(seeds, 2)
    fruit_and_berries.requires(tree_saplings, 1)

    cream.requires(animal_feed, 1)

    corn.requires(minerals, 1)
    corn.requires(seeds, 4)

    cheeze.requires(animal_feed, 2)

    beef.requires(animal_feed, 3)

    # Gardening Supplies
    grass.requires(seeds, 1)
    grass.requires(shovel, 1)

    tree_saplings.requires(seeds, 2)
    tree_saplings.requires(shovel, 1)

    gardening_furniture.requires(planks, 2)
    gardening_furniture.requires(plastic, 2)
    gardening_furniture.requires(textiles, 2)

    fire_pit.requires(bricks, 2)
    fire_pit.requires(cement, 2)
    fire_pit.requires(shovel, 1)

    # Furniture Store
    chairs.requires(wood, 2)
    chairs.requires(nails, 1)
    chairs.requires(hammer, 1)

    tables.requires(planks, 1)
    tables.requires(nails, 2)
    tables.requires(hammer,1)

    home_textiles.requires(textiles, 2)
    home_textiles.requires(tape, 1)

    cupboard.requires(glass, 2)
    cupboard.requires(planks, 2)
    cupboard.requires(paint, 1)

    # Donut Shop
    donuts.requires(flour_bag, 1)
    donuts.requires(sugar_and_spices, 1)

    green_smoothie.requires(vegetables, 1)
    green_smoothie.requires(fruit_and_berries, 1)

    bread_roll.requires(flour_bag, 2)
    bread_roll.requires(cream, 1)

    cherry_cheezecake.requires(flour_bag, 1)
    cherry_cheezecake.requires(fruit_and_berries, 1)
    cherry_cheezecake.requires(cheeze, 1)

    frozen_yogurt.requires(cream, 1)
    frozen_yogurt.requires(fruit_and_berries, 1)
    frozen_yogurt.requires(sugar_and_spices, 1)

    # Fashion Store
    cap.requires(textiles, 2)
    cap.requires(tape, 1)

    shoes.requires(textiles, 2)
    shoes.requires(plastic, 1)
    shoes.requires(glue, 1)

    watch.requires(plastic, 2)
    watch.requires(glass, 1)
    watch.requires(chemical, 1)

    # Fast Food Restaurant
    ice_cream_sandwich.requires(bread_roll, 1)
    ice_cream_sandwich.requires(cream, 1)

    pizza.requires(flour_bag, 1)
    pizza.requires(cheeze, 1)
    pizza.requires(beef, 1)


    return [
        metal,
        wood,
        plastic,
        seeds,
        minerals,
        chemical,
        animal_feed,
        glass,
        sugar_and_spices,
        textiles,

        nails,
        planks,
        bricks,
        cement,
        glue,
        paint,

        hammer,
        tape,
        shovel,
        cooking_utensils,
        ladder,

        grass,
        tree_saplings,
        gardening_furniture,
        fire_pit,

        vegetables,
        flour_bag,
        fruit_and_berries,
        cream,
        corn,
        cheeze,
        beef,

        chairs,
        tables,
        home_textiles,
        cupboard,

        donuts,
        green_smoothie,
        bread_roll,
        cherry_cheezecake,
        frozen_yogurt,

        cap,
        shoes,
        watch,

        ice_cream_sandwich,
        pizza
    ]

if __name__ == '__main__':
    graph = generate_dependency_graph()
    render_di_graph(graph)

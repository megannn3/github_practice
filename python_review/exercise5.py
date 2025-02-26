menu = { "Pizza": 1.99, "Soda":  0.69, "Double Chunk Chocolate Chip Cookie": 2.49}

def add(item,price):
    menu.update({item:price})
    print(menu)

add("muffin", "1.30")
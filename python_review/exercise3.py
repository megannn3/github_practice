groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

while True:
    print(groceries)
    user = input("What do you want to remove from the list? Type 'stop' to end. \n")
    if user == "stop":
        break
    else:
        groceries.remove(user)
   




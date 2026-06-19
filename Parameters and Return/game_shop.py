"""
PROGRAM: Game Shop
This program runs a game shop for items.
"""

# INSTRUCTIONS
# TODO Code a game shop for players to buy and sell items

game_shop_items = {
    "sword": {"buy_price": 100, "sell_price": 50},
    "shield": {"buy_price": 80, "sell_price": 40},
    "health potion": {"buy_price": 20, "sell_price": 10},
    "magic wand": {"buy_price": 150, "sell_price": 75},
    "bow": {"buy_price": 120, "sell_price": 60},
    "arrow": {"buy_price": 5, "sell_price": 2}
}

user_items = {
    "animal hide": {"buy_price": 30, "sell_price": 15},
    "iron ore": {"buy_price": 50, "sell_price": 25},
    "wooden plank": {"buy_price": 10, "sell_price": 5},
    "gemstone": {"buy_price": 200, "sell_price": 100}
}

user_gold = 500

def gameshop():
    global user_gold 
    
    print("Welcome to the Game Shop!")
    print(f"You have {user_gold} gold.\n")
    
    choicesellbuy = input("Would you like to buy or sell an item? (Enter 'buy' or 'sell'): ").lower().strip()

    if choicesellbuy == "buy":
        print("\n--- Items available for purchase ---")
        for in_game_item, data in game_shop_items.items():
            print(f"- {in_game_item.title()}: {data['buy_price']} gold")
            
        choicebuy = input("\nEnter the name of the item you want to buy: ").strip().lower()
        
        if choicebuy in game_shop_items:
            item_price = game_shop_items[choicebuy]["buy_price"]
            if user_gold >= item_price:
                user_gold -= item_price
                print(f"Success! You bought a {choicebuy} for {item_price} gold. You have {user_gold} gold left.")
            else:
                print("Transaction failed: You don't have enough gold to buy that item.")
        else:
            print("Sorry, we don't carry that item here.")
    
    elif choicesellbuy == "sell":
        print("\n--- Your items available for sale ---")
        for user_item, data in user_items.items():
            print(f"- {user_item.title()}: Sells for {data['sell_price']} gold")
            
        choicesell = input("\nEnter the name of the item you want to sell: ").strip().lower()
        
        if choicesell in user_items:
            item_price = user_items[choicesell]["sell_price"]
            user_gold += item_price
            print(f"Success! You sold your {choicesell} for {item_price} gold. You now have {user_gold} gold.")
        else:
            print("You don't seem to own that item.")
            
    else:
        print("Invalid choice. Please enter 'buy' or 'sell'.")

# Run the game shop
gameshop()
    
    # TODO Get user input for buying or selling items and update their gold and inventory accordingly.









#===============================
#===============================
# EXTENSION
# Display extra info for each item (on top of price): attack, defence, item_description, etc.
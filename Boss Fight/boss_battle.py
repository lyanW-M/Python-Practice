print("Nivedh the paladin is fighting Big Chungus the Maximus in a battle to the death!\n")
print("Nivedh has 100 health and Big Chungus has 150 health.\n")
print("Use your weapons strategically depending on the situation.\n")

#Stats
import random
bossHealth = 150
playerHealth = 100

#Equipment
import random
healAmount = 30
healBottle = 3

#Heal

def end():
    if bossHealth <= 0:
        print("Congratulations! You have defeated Big Chungus the Maximus!")
        return True
    elif playerHealth <= 0:
        print("Nivedh sucks and has been defeated by Big Chungus the Maximus.")
        return True
    return False

#Battle
while end() == False:
    print("Player Health:", playerHealth)
    print("Boss Health:", bossHealth)
    print()

    action = input("What would you like to do? (sword, bow, heal)\n").strip().lower()
    print()
    if action == "sword":
        damageSword = random.randint(15, 20)
        bossHealth -= damageSword
        print("You attack Big Chungus with your sword and deal", damageSword, "damage!")
        print()

    elif action == "bow":
        damageBow = random.randint(10, 20)
        bossHealth -= damageBow
        print("You attack Big Chungus with your bow and deal", damageBow, "damage!")
        print()

    elif action == "heal":
        if healBottle > 0:
            healBottle -= 1
            playerHealth += healAmount
            print("You use a heal bottle and restore", healAmount, "health!")
            print()
            
        elif healBottle == 0:
            print("You have no heal bottles left.")
            print()
            continue
        
    else:
        print("Invalid action. Please choose 'sword', 'bow', or 'heal'.")
        continue

    if bossHealth > 0:
        bossDamage = random.randint(15, 25)
        playerHealth -= bossDamage
        print("Big Chungus attacks you and deals", bossDamage, "damage!")
        print()
    
    continue


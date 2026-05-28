import random

print("Nivedh the paladin is fighting Big Chungus the Maximus in a battle to the death!\n")
print("Nivedh has 100 health and Big Chungus has 150 health.\n")
print("Use your weapons strategically depending on the situation.\n")

# Stats
bossHealth = 150
playerHealth = 100

# Equipment
healAmount = 45
healBottle = 3

# Ending conditions
def end():
    if bossHealth <= 0:
        print("Congratulations! You have defeated Big Chungus the Maximus!")
        return True
    elif playerHealth <= 0:
        print("Nivedh sucks and has been defeated by Big Chungus the Maximus.")
        return True
    return False

# Battle Loop
while not end():
    print(f"Player Health: {playerHealth}")
    print(f"Boss Health: {bossHealth}")
    print()

    # Roll for fly mechanic ONCE at the start of the turn
    is_flying = random.randint(1, 100) <= 20
    if is_flying:
        print("-> Big Chungus is now flying and getting ready for a powerful attack!")
    print()

    action = input("What would you like to do? (sword, bow, heal)\n").strip().lower()
    print()
    
    if action == "sword":
        if is_flying:
            damageSword = 0
            print("Your sword is too small to reach Big Chungus while he's flying!")
        else:
            damageSword = random.randint(15, 20)
            bossHealth -= damageSword
            print(f"You attack Big Chungus with your sword and deal {damageSword} damage!")
        print()

    elif action == "bow":
        damageBow = random.randint(10, 20)
        if is_flying:
            damageBow *= 2
            print("Your bow deals double damage while Big Chungus is flying!")
        
        bossHealth -= damageBow
        print(f"You attack Big Chungus with your bow and deal {damageBow} damage!")
        print()

    elif action == "heal":
        if healBottle > 0:
            healBottle -= 1
            playerHealth += healAmount
            print(f"You use a heal bottle and restore {healAmount} health!")
            print()
        else:
            print("You have no heal bottles left.\n")
            continue
        
    else:
        print("Invalid action. Please choose 'sword', 'bow', or 'heal'.\n")
        continue

    if bossHealth <= 0:
        continue
    
    #Boss attack
    bossDamage = random.randint(15, 20)
    if is_flying and action == "sword":
        bossDamage *= 2
        print("Big Chungus leaps into the air and slams down on you, dealing DOUBLE damage!")    
    elif is_flying and action == "bow":
        bossDamage *= 1.5
        print("You slightly negate Big Chungus' powerful attack with your bow but he retaliates dealing 1.5x damage!")
    elif is_flying and action == "heal":
        bossDamage *= 3
        print("Big Chungus is enraged by your attempt to heal and underestimate him, and unleashes a devastating attack dealing TRIPLE damage!")
    playerHealth -= bossDamage
    print(f"Big Chungus attacks you and deals {bossDamage} damage!")
    print()


user_name = input("Enter athlete name: ")  
steps_string = input("How many steps did you walk? ")  
steps_int = int(steps_string)  
km_walked = steps_int / 1312 # 1,312 steps = roughly 1 kilometer 
km_rounded = round(km_walked, 2) 
print(user_name + " walked " + str(km_rounded) + " km.")
goal_reached = km_rounded >= 5.0 
print("Daily 5km Goal Met:")
print(goal_reached)
gameOver = False
won = False
choice = "not q"
print("You have hotwired a police car and stolen it. Little did you know, the police were keeping track of your location. It seems that the police are chasing you now! Your mission is to outrun the cops and make it across the Canadian border without being caught. You are in San Francisco, CA. The cop car that you stole has a radio that cops use, so you can hear their conversations.")
print("----------------------------------------------------------------------")
print("\nThe cops are on your tail! You speed through the roads of San Francisco. You hear the cops talking. 'Dispatch! I have a visual of the suspect. Calling for backup. I repeat! Calling for backup.' Escape the cop before the dispatcher sends backup!")
while (not gameOver and choice != "q" and not won):
        winningDistance = 950
        gameOver = False
        copSpeed = 80
        distanceTraveled = 0
        copDistance = 3
        sleepiness = 0
        fuel = 10
        replacementFuel = 5
        print("\n\nHere are your options:\nA. Drive over the speed limit.\nB. Drive and abide to the rules.\nC. Refuel\nD. Stop for the night\nE. Status Check")
        choice = input("Enter you choice. If you want to quit, enter 'q':\n").lower()
        if (choice == "a"):
            print("You have decided to drive over the speed limit.")
        elif (choice == "b"):
            print("You have decided to drive at a moderate speed and abide to the rules")
            print("The pursuit continues.")
        elif (choice == "c"):
                print("You have decided to refuel. You don't get anymore tired, but your fuel tank is full. The pursuit continues.")
        elif (choice == "d"):
            print("You stopped for the night. You are healthy and active.")
        elif (choice == "e"):
            print("\nYou have travelled " + str(distanceTraveled) + " miles. \nYou have to drive " + str(winningDistance - distanceTraveled) + " miles until you reach Canada.\nYou have a sleepiness level of " + str(sleepiness) + " out of 15.\nThe cops are " + str(copDistance) + " miles away.\nYou have " + str(fuel) + " gallons of fuel in your tank.\nYou have " + str(replacementFuel) + " refills left")
          
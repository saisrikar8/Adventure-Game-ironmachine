import random
import time
game = "yes"
while(game == "yes" or game == "y"):
  gameOver = False
  copSpeed = 80
  distanceTraveled = 0
  copDistance = 3
  sleepiness = 0
  fuel = 16
  replacementFuel = 2
  won = False
  disguise = False
  quit = False
  print("You have hotwired a police car and stolen it. Little did you know, the police were keeping track of your location. It seems that the police are chasing you now! Your mission is to outrun the cops and make it across the Canadian border without being caught. You are in San Francisco, CA. The cop car that you stole has a radio that cops use, so you can hear their conversations.")
  print("\nThe cops are on your tail! You speed through the roads of San Francisco. You hear the cops talking. 'Dispatch! I have a visual of the suspect. Calling for backup! Over.' Escape the cop before the dispatcher sends backup!")
  print("----------------------------------------------------------------------")
  choice = "not q"
  while (choice != "q"):
      print("\n\nChoose a route:\nA. Merge onto U.S. 101 and go across the Golden Gate Bridge.\nB. Take Interstate 80 and go across the San Francisco-Oakland Bay Bridge.")
      choice = input("Enter you choice:\n").lower()
      if (choice == "a"):
          print("Ok. You merged onto U.S. 101 and are making your way to the Golden Gate Bridge.")
          winningDistance = 1000
          print("Loading System...")
          time.sleep(2)
          print("Driving over Golden Gate..")
          time.sleep(2)
          print("Welcome to Sausolito! THE COPS ARE STILL BEHIND YOU! HURRY!")
          highway = 101
          choice = "q"
      elif (choice == "b"):
          print("You have merged onto Interstate 80 and you are on the Bay Bridge.")
          print("Loading System...")
          time.sleep(2)
          print("Crossing Bay Bridge...")
          time.sleep(2)
          print("WELCOME TO OAKLAND! The cops are still behind you! HURRY!")
          time.sleep(2)
          winningDistance = 950
          highway = 80
          choice = "q"
      elif (choice != "q"):
          print("INVALID INPUT. TRY AGAIN.\n\n")
      else:
        quit = True
  if (not quit):
    choice = "not q"
  while (not gameOver and choice != "q" and won == False):
      print("Loading Options...")
      time.sleep(2)
      print("\n\nHere are your options:\nA. Drive over the speed limit.\nB. Drive and abide to the rules.\nC. Refuel\nD. Stop for the night\nE. Status Check")
      choice = input("Enter you choice. If you want to quit, enter 'q':\n").lower()
      if (choice == "a"):
          miles = random.randint(50,70)
          distanceTraveled += miles 
          copDistance += miles - copSpeed*0.5
          fuel -= 2
          sleepiness += 2
          print("You have traveled " + str(miles) + " miles in 30 minutes. You burned 2 gallons of fuel. You are more tired than before")
      elif (choice == "b"):
          miles = random.randint(35,50)
          distanceTraveled += miles
          copDistance += miles - copSpeed * 0.5
          fuel -= 1
          print("You have travelled " + str(miles) + " miles in 30 minutes. You burned 1 gallon of fuel. You feel a little more tired than before")
          sleepiness += 1
          print("The pursuit continues.")
      elif (choice == "c"):
          if (replacementFuel == 0):
              print("You don't have anymore replacement fuel left.")
          elif (fuel >= 10):
            print("You already have a lot of fuel. There is no need for a refill. Your fuel tank is " + str(int(fuel/15 * 100)) + " % full.")
          else:
              print("You have decided to refuel. You don't get anymore tired, but your fuel tank is full. The pursuit continues.")
              fuel = 20
              replacementFuel -= 1
              copDistance -= (copSpeed)/20
      elif (choice == "d"):
          print("You rested at a motel for some time. You are healthy and active.")
          sleepiness = 0
          copDistance -= 30
      elif (choice == "e"):
          if (replacementFuel == 1):
            replace = " refill"
          else:
            replace = " refills"
          print("\nYou have travelled " + str(distanceTraveled) + " miles. \nYou have to drive " + str(winningDistance - distanceTraveled) + " miles until you reach Canada.\nYou have a sleepiness level of " + str(sleepiness) + " out of 15.\nThe cops are " + str(copDistance) + " miles away.\nYou have " + str(fuel) + " gallons of fuel in your tank.\nYou have " + str(replacementFuel) + replace + " left")
          time.sleep(3)
      elif (choice != "q"):
          print("Sorry. Invalid input. Try again.\n\n")
      else:
        break
      if (distanceTraveled >= winningDistance):
          won = True
      if (copDistance <= 0):
        print("The cops surrounded you and took back the stolen car. You got arrested on the spot.")
        gameOver = True
      elif (copDistance < 10 and copDistance > 0):
        print('A cop starts talking on the radio. "Dispatch! I have a visual!" You look through the rearview mirror and notice blue and red flashes. THE COPS ARE RIGHT BEHIND YOU!')
      if (sleepiness > 15):
        print("You nod off while driving and crash into a nearby car. Fortunately, it was only a minor crash. You stay asleep. When you wake up, you are in handcuffs.")
        gameOver = True
      elif (13 <= sleepiness):
        print("WARNING! YOU SHOULD STOP AND TAKE SOME REST OR ELSE YOU WILL CRASH!")
      if (fuel <= 0 and won == False):
        winOrLose = random.randint(1,50)
        otherInt = random.randint(1,50)
        if (winOrLose == otherInt):
          print("You notice an abandoned gas station next to the highway. You pull over on the highway and walk there. You are able to trasport fuel to the car and fill it up with fuel. You also get into the gas station and find some spray paint. You use the spray paint to disguise your car. When you start driving again, the police pass right by you. You have an advantage!")
          disguise = True
        else:
          print("You ran out of fuel. As a result, your car stopped moving. You try to pull over, but crash into the railing. You are knocked unconcious. When you wake up, you are in handcuffs.")
          gameOver = True
      elif (fuel - 3 <= 0 and gameOver != True):
          print("WARNING! YOU ARE ALMOST OUT OF FUEL!")
      if (highway == 101 and distanceTraveled > 200 and distanceTraveled < 300):
        print("You merged onto U.S. 199 North")
        highway = 199
      elif(highway == 80 and distanceTraveled > 125 and distanceTraveled < 200):
        print("You merged onto Interstate 5 North")
        highway = 5
      elif (highway == 199 and distanceTraveled < 375 and distanceTraveled > 275):
        print("You merged onto Interstate 5 North.")
        highway = 5
      randOne = random.randint(1,10)
      randTwo = random.randint(1,10)
      if (randOne == randTwo and disguise == True):
        print('You notice a cop talking on the radio. "DISPATCH! I HAVE A VISUAL OF THE SUSPECT! HE SEEMS TO HAVE CREATED A DISGUISE WITH SPRAY PAINT! I CAN SEE HIS LICENSE PLATE. CALLING FOR BACKUP! Over." The cops have found you!' )
        copDistance = 3
  if (choice == "q"):
      print("Thanks for playing! I'm sorry that you had to quit.")
  elif (gameOver == True):
      print("You were " + str(winningDistance - distanceTraveled) + " miles away from Canada.")
      print("\nGAME OVER")
  elif (won == True):
      print("YOU MADE IT TO CANADA! CONGRATULATIONS! YOU WON!!!!!!!!")
  game = input("\nWould you like to play again?:\n").lower()
print("THANKS FOR PLAYING!!! BYE BYE!!!!!!")
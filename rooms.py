#Import all tools/files needed
import var
import time
import random
import art
import sys 
#Intro to the game. Description
def intro():
  print('\033[0;34;48m')
  print ("Welcome to the haunted house, you brave soul. \nThere are 6 rooms in this house; Living room, \nDining room, Kitchen, Kid bedroom and Master \nbedroom. \n\nYou only have 3 lives, use them carefully, don’t \nlet the spirit get you!\n")
  time.sleep(3)
  print ("Your goal is to collect all the objects and add them to your backpack also, you need at least one or more lives in order to leave")
  print('\033[0;33;48m')
  time.sleep(2)
  name= input("\nWhat is your name?")
  var.varname=name
  return name 


# Where does the player want to go
def where():
  print('\033[0;37;48m')
  answer = input("\nOkay " +  var.varname  + " where do you want to go? Living Room, \n Dining Room, Kitchen, Kid bedroom, Master bedroom, or do you want to leave\n").lower()
   
  while answer!="living room" and answer!= "dining room" and answer!= "kitchen"  and answer!= "kid bedroom" and answer!= "master bedroom" and answer!= "leave" and answer!="garage":
    answer= input("\n\nOkay " +  var.varname  + " where do you want to go? Living Room, \n Dining Room, Kitchen, Kid bedroom, Master bedroom, Garage or do you want to leave\n").lower()
  

#When they want to leave 
  if answer=="leave":
    if "key" and "flashlight" and "food" not in var.backpack:
      print('\033[0;31;48m')
      print ("Sorry, you have not collected everything to leave the house, try again when you have everything")
      print('\033[0;37;48m')
      where()
    if "key" and "flashlight" and "food" in var.backpack and var.lives>1 or var.lives==1:
      print ("Congratulations!", var.varname, "you have safely escaped the house")
      sys.exit()

   

#Living Room Events 
  if answer=="living room":
     art.living()
     choice= input ("\nWelcome to the living room " + var.varname +  " take a \"seat\" or \"explore?\"").lower()
     while choice!= "explore" and choice!= "seat":
       choice= input ("\n\nWelcome to the living room " + var.varname +  " take a \"seat\" or \"explore?\"").lower()
     if choice=="seat":
       x=random.randrange(0,2)
       if x==1:
        print('\033[0;31;48m')
        print ("Noooo, you have fallen into a trap!! The spirit has taken a life!")
        loselife(1)
        print('\033[0;37;48m')
        print ("You have", var.lives, "lives""\n")
        time.sleep(1)
        where()
       if x==0:
         print ("You have rested! Time to get back to searching")
         time.sleep(1)
         where()
     if choice=="explore":
        print('\033[0;33;48m')
        pickup= input("Wow! You have found a key, would you like to pick it up, you will lose one life if picked up, yes/no?").lower()
        while pickup!= "yes" and pickup!= "no":
          pickup= input(" \n\nWow! You have found a key, would you like to pick it up, you will lose one life if picked up, yes/no?").lower()
        if pickup=="yes":
          var.backpack.append("key")
          loselife(1)
          print ("The key has been added to your backpack\n\n Your backpack", var.backpack, "\n You have", var.lives, "lives""\n")
          time.sleep
          where()
        if pickup=="no":
           print('\033[0;31;48m')
           print ("You have left the key\n")
           time.sleep(1)
           where()
    

#Dining Room Events
  if answer=="dining room":
     art.dining()
     print('\033[0;33;48m')
     choice= input ("\nWelcome to the dining room " + var.varname +  " are you here to \"eat\" or \"explore?\"").lower()
     if choice=="eat":
        var.lives+=1 
        print ("Congratulation! You have earned a life! You have ", var.lives, "lives.")
        time.sleep
        where()
     if choice=="explore":
       x=random.randrange(0,2)
       if x==0:
         print ("This is a trap! You have lost a life.")
         print('\033[0;31;48m')
         print ("The spirit has taken a life!")
         loselife(1)
         print ("You have", var.lives, "lives""\n")
         time.sleep(1)
         where()
       if x==1:
         print ("Okay, let's see where you go.\n")
         time.sleep(1)
         print ("You have entered  the formal living room,  this is a dead end\n")
         time.sleep(1)
         print('\033[0;37;48m')
         where()
     while choice!="explore" or choice!="eat":
       choice= input ("\nWelcome to the dining room " + var.varname +  " are you here to \"eat\" or \"explore?\"").lower()


#Kitchen Events
  if answer=="kitchen":
    print('\033[0;33;48m')
    choice= input ("\nWelcome to the  kitchen " + var.varname +  " do you want \"food\" or do you want to\"search?\"").lower()
    while choice!="food" and choice!="search":
       choice= input ("\nWelcome to the  kitchen " + var.varname +  " do you want \"food\" or do you want to\"search?\"").lower()
    if choice== "food":
       yes= input("You have made some food, would you like to add it to your backpack? yes/no").lower()
       if yes=="yes":
         print ("The food has been added to your backpack")
         var.backpack.append("food")
         print (var.backpack)
         time.sleep(1)
         where()
       if yes=="no":
         print ("You have left the food")
         time.sleep(1)
         where()
       while yes!="yes" and yes!="no":
         yes= input("You have made some food, would you like to add it to your backpack? yes/no").lower()
    if choice=="search":
       var1=input("You have opened the wrong cabinet, would you like to close it? yes/no").lower()
       if var1=="yes":
          print ("Good job! You are safe now")
          time.sleep(1)
          where()
       if var1=="no":
          x=random.randrange(0,2)
          if x==0:
            print('\033[0;31;48m')
            print ("The spirit has taken a life!")
            loselife(1)
            print ("You have", var.lives, "lives""\n")
            where()
          if x==1:
            print ("You are lucky! You are safe now!")
            time.sleep(1)
            where()
       while var1!="yes" and var1!="no":
         var1=input("You have opened the wrong cabinet, would you like to close it? yes/no").lower()
         



#Master Bedroom Events
  if answer=="master bedroom":
    print('\033[0;31;48m')
    print ("You need a key to enter this room.")
    if "key" not in var.backpack:
       print ("You don't have the key \nGet the key to enter this room")
       time.sleep(1)
       where()
    if "key" in var.backpack:
       art.master()
       print('\033[0;33;48m')
       choice=input ("\nWelcome to the Master Bedroom "  + var.varname +  " would you like to \"sleep\" or \"explore\"").lower()
       x=random.randrange(0,2)
       if choice=="sleep":
         if x==0:
          print ("The spirit has taken a life!")
          loselife(1)
          print ("You have", var.lives, "lives""\n")
          where()
         if x==1:
           print ("You got lucky! You are safe!")
           time.sleep(1)
           where()        
       if choice=="explore":
         var2= input("You have found a flashlight! Would you like to add it to your backpack, remember you will lose ONE life? yes/no").lower()
         if var2=="no":
           print ("You have left the flashlight")
           time.sleep(1)
           where()
         if var2=="yes":
           print ("You have picked up the flashlight!")
           var.backpack.append("flashlight")
           loselife(1)
           print ("Your backpack", var.backpack)
           print ("You have", var.lives ,"lives")
           time.sleep(1)
           where()
         while var2!="no" and var2!="yes":
           var2=input ("You have found a flashlight! Would you like to add it to your backpack, remember you will lose ONE life? yes/no").lower()


#Kid Bedroom Events 
  if answer=="kid bedroom":
     liveChance = random.randrange(0,2)
     if liveChance == 0:
       print('\033[0;33;48m')
       art.kidbedroom
       choice=input ("\nWelcome to the Kid Bedroom "  + var.varname +  " would you like to \"play\" or \"explore\"").lower()
       while choice!= "play" and choice!= "explore":
         choice=input ("\nWelcome to the Kid Bedroom "  + var.varname +  " would you like to \"walk\" or \"explore\"").lower()
       if choice=="walk":
         todo= input("You have found the closet\n\n Would you like to enter. yes/no").lower()
         if todo=="yes":
           x=random.randrange(0,2)
           if x==0:
            print ("This closet has nothing in it.")
            time.sleep(1)
            where()
           if x==1:
             print ("This is a trap, but you got out safe. You DID NOT lose a life!")
         if todo=="no":
           print ("Alright!")
           time.sleep(1)
           where()
       if choice=="explore":
        var1= input ("Would you like to enter the closet? yes/no").lower()
        if var1=="no":
          print ("That was smart.")
          where()
        if var1=="yes":
          print ("The spirit is in here! You have lost a life.")
          loselife(1)
          print ("You have", var.lives ,"lives")
          time.sleep(1)
          where()
     else:
        print('\033[0;35;48m')
        print ("This room is a trap!\n\n You have lost one life!")
        loselife(1)
        print ("You have", var.lives, "lives""\n")
        time.sleep(1)
        where()



#For losing lives
def loselife(lives):
  var.lives = var.lives - lives
  if var.lives <= 0:
    print('\033[0;31;48m')
    print("You lost all of your lives! Goodbye", var.varname)
    sys.exit()
    
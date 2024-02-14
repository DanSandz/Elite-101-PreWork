print("Welcome to the Elite 101 ChatBot!")
user_name = input("What is your name? ")
user_age = input(f"Nice to meet you, {user_name}! How old are you? ")
print(f"Welcome {user_name}! How can I assist you today?")

print("\nPlease choose from the following options: ")
print("1: Return an item\n2: Exchange an item\n3: Exit the conversation")

action = 0
inUse = True

while inUse:
  
  action = input("\nEnter the number of your choice: ")
  
  if action == "1":
    canReturn = 0 #  0=no, 1=yes
    hasReceipt = input("Do you have the receipt for this item? ")
    if hasReceipt == "yes".lower():
      itemCondition = input("Is the item still free of wear and stains? ")
      if itemCondition == "yes".lower():
        canReturn = 1
      elif itemCondition == "no".lower():
        print("I'm sorry, but you cannot return this item.")
        inUse = False
      
    elif hasReceipt == "no".lower(): 
      print("If you have purchased this item less than 30 days ago with ")
      print("a credit card, we may be able to find your purchase in our system. ")
      timeBought = input("How many days ago did u purchase this item? ")
      timeBoughtList = []
      for char in timeBought:
        if char.isnumeric():
          timeBoughtList.append(char)
      if not timeBoughtList:
        timeBoughtList.append(999999)
      timeBoughtReal = ("".join(timeBoughtList))
      if int(timeBoughtReal) <= 30:
        cardPurchase = input("Did you purchase it with a debit/credit card? ")
        if cardPurchase == "yes".lower():
          print("Okay. I will check the systems to find your purchase.")
          itemCondition = input("Is the item still unused? ")
          if itemCondition == "yes".lower():
            canReturn = 1
          elif itemCondition == "no".lower():
            print("I'm sorry, but you cannot return this item.")
            inUse = False
        elif cardPurchase == "no".lower():
          print("I'm sorry, but you cannot return this item.")
          inUse = False
      elif int(timeBought) > 30:
        print("I'm sorry, but you cannot return this item anymore.")
        inUse = False
  
    
    if canReturn == 1:
      shipOrBringAnswer = ""
      returnOptions = ["bring", "ship"]
      print("No worries! You are eligible to return your item.")
      
      while shipOrBringAnswer != "bring" and shipOrBringAnswer != "ship":
        shipOrBring = input("\nWould you like to ship it or bring it in to our store? ")
        shipOrBringList = list(shipOrBring.split(" "))
        for word in shipOrBringList:
          if word == returnOptions[0]:
            shipOrBringAnswer = "bring"
          elif word == returnOptions[1]:
            shipOrBringAnswer = "ship"
        if shipOrBringAnswer != "bring" and shipOrBringAnswer != "ship":
          print("I'm sorry. I didnt quite catch that. ")
          
      if shipOrBringAnswer == "ship":
        print("Alright. To ship it to us, just package it and send it")
        print ("to 225 Cool People Road.")
        print(f"Have a wonderful day, {user_name}")
        inUse = False
      if shipOrBringAnswer == "bring":
        print("We are open from 10am to 8pm. You can simply bring it to the front desk")
        print("Our address is 225 Cool People Road")
        if hasReceipt:
          print("Don't forget to bring your receipt!")
          inUse = False
        else:
          print("Your item is in our system. You can refund your item in person.")
          print("We'll see you soon!")
          inUse = False
        
        
      
      
        
        
  
  
  #some businesses offer a step-by-step guide and specific 
  #instructions on how to ship the item back.
  #what if the apayment is invalid? - exchange
  #how does chatbot respond to valid or invalid payment
  
  #also i want to add a buy option to buy from the daily catalog.
  
  #suggest an item for the user randomized!!!1
  
  elif action == "2":
    print("option 2 was chosen!!!!!")
    
  
  elif action != "3":
    print("Invalid option. Try again.")
  
  
if action == "3":
  print(f"Goodbye {user_name}! Have a great day!")
  quit()
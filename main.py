print("Welcome to the Elite 101 ChatBot!")
user_name = input("What is your name? ")
user_age = input(f"Nice to meet you, {user_name}! How old are you? ")
print(f"Welcome {user_name}! How can I assist you today?")

print("\nPlease choose from the following options: ")
print("1: PLaceholder 1\n2: Placeholder 2\n3: Placeholder 3\n4: Exit the conversation")


action = 0

while action != "4":
  action = input("\nEnter the number of your choice: ")
  
  if action == "1":
    print("[Insert action for option 1]")
    #code
    #code
    action = 0


  elif action == "2":
    print("option 2 was chosen!!!!!")
    #code
    #code
    action = 0


  elif action == "3":
    print("do option 3 stuff")
    #code
    #code
    action = 0


if action == "4":
  print(f"Goodbye {user_name}! Have a great day!")
  quit()
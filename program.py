import random

print("Welcome to Snake , Water and Gun Game!")
print("Choice : Snake , Water , Gun :")

#computer choice
comp = random.choice(["Snake ", "Water", "Gun"])

#user input
user = input("Enter your choice : ")
print ("computer choose" , comp)

#condition
if user == comp:
    print("Its a draw.")
    
elif user == "Snake":
    if comp == "Water":
        print("You Won!")
    else:
        print("You Lose")
        
elif user == "Water":
    if comp == "Gun":
        print("You Won!")
    else:
        print("You Lose")
        
elif user == "Gun":
    if comp == "Snake":
        print("You Won!")
    else:
        print("You Lose")
    
else:
    print("Invalid choice . Please select from Snake , Water , Gun.")
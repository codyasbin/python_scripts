print ("Press Enter to start the game!\n Press Ctrl+C to exit the game.")
if input() == "":
 while True:
    print ("Welcome to the asbins game!")
    number=int(input("Enter a number: "))
    if number%2==0:
        print ("You win!")
    else:
        print ("You lose!")
    print ("Press Enter to play again!\n Press Ctrl+C to exit the game.")
    if input().lower()=="q":
        break

    


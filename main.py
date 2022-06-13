print("Welcome to the Quiz Game!!")
points = 0
user_input = input("Would you like to play the game? ")
if user_input != "yes":
    print("thank you for your time! bye bye now :)")
    quit()
else:
    print("looks like you have chosen to play!")
    print("The Question bank comes from https://www.opinionstage.com/blog/trivia-questions/ ")
    print(" ")
    print("Lets get started with the questions, this is a ten question game about the world get as many points "
          "as possible")
    answer = input("1) What year was the very first model of the iPhone released?")
    if answer == "2007":
        print("Correct")
        points += points + 1
        print("Points: ", points)
    else:
        print("Incorrect")
        print("Points:", points)
    answer = input("2) What’s the shortcut for the “copy” function on most computers?")
    if answer == "control c":
        print("Correct")
        points += points + 1
        print("Points: ", points)
    else:
        print("Incorrect")
        print("Points:", points)
    answer = input("3) What is often seen as the smallest unit of memory?")
    if answer == "kilobyte":
        print("Correct")
        points += points + 1
        print("Points: ", points)
    else:
        print("Incorrect")
        print("Points:", points)
    answer = input("4) Who discovered penicillin?")
    if answer == "Alexander Fleming":
        print("Correct")
        points += points + 1
        print("Points: ", points)
    else:
        print("Incorrect")
        print("Points:", points)
    answer = input("5) What is the symbol for potassium?")
    if answer == "k":
        print("Correct")
        points += points + 1
        print("Points: ", points)
    else:
        print("Incorrect")
        print("Points:", points)
    answer = input("6) What does “HTTP” stand for?")
    if answer == "HyperText Transfer Protocol":
        print("Correct")
        points += points + 1
        print("Points: ", points)
    else:
        print("Incorrect")
        print("Points:", points)
    answer = input("7) What was Twitter’s original name?")
    if answer == "twttr":
        print("Correct")
        points += points + 1
        print("Points: ", points)
    else:
        print("Incorrect")
        print("Points:", points)
    answer = input("8) Who is often called the father of the computer?")
    if answer == "Charles Babbage":
        print("Correct")
        points += points + 1
        print("Points: ", points)
    else:
        print("Incorrect")
        print("Points:", points)
    answer = input("9) Which email service is owned by Microsoft?")
    if answer == ("outlook" or "hotmail"):
        print("Correct")
        points += points + 1
        print("Points: ", points)
    else:
        print("Incorrect")
        print("Points:", points)
    answer = input("10) Is Java a type of OS?")
    if answer == "no":
        print("Correct")
        points += points + 1
        print("Points: ", points)
    else:
        print("Incorrect")
        print("Points:", points)
print("This is the End of hte Quiz!!")
print("your score is: ", points)
print("thank you for playing!!")
quit()

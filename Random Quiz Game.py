print("welcome C my computer quiz game")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("playing! lets play!!")
Score = 0

answer = input("Is Russian in Europe or North America?" )
if answer.lower() == "europe":
    print('Correct')
    Score += 1
else: print("incorrect!")


answer = input("First Country to gain independce?" )
if answer.lower() == "united states":
    print('Correct')
    Score += 1
else: print("incorrect!")


answer = input("Which continent is belgium located?" )
if answer.lower() == "europe":
    print('Correct')
    Score += 1
else: print("incorrect!")


answer = input("Which country is above the United States?" )
if answer.lower() == "canada":
    print('Correct')
    Score += 1
else: print("incorrect!")


answer = input("Which country is below the United States?" )
if answer.lower() == "mexico":
    print('Correct')
    Score += 1
else: print("incorrect!")


answer = input("Is Mexico in South America?" )
if answer.lower() == "no":
    print('Correct')
    Score += 1
else: print("incorrect!")


print("you got " + str((Score /6) * 100) + "%.")


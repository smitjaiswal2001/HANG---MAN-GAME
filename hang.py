import time
import random
def hang():
    word = random.choice(["america" , "austrila" , "india" , "pakistan" , "srilanka" , "bangladesh" , "canada" , "unitedkingdoms" , "africa" , "southafrica"])
    validletters = "abcdefghijklmnopqrstuvxyz"
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("you win|")
            break
        print("guess the word:" , main)
        guess = input() 
                

        if guess in validletters:
            guessmade = guessmade + guess

        else:
            print("enter a valid character")
            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("---------")
                time.sleep(2)
                print("    0    ")
            if turns == 8:
                print("8 turns left")
                print("----------")
                time.sleep(2)
                print("     0    ")
                time.sleep(2)
                print("     |    ")
            if turns == 7:
                print("7 turns left")
                print("------------")
                time.sleep(2)
                print("      0     ")
                time.sleep(2)
                print("      |     ")
                time.sleep(2)
                print("     /      ")
            if turns == 6:
                print("6 turns left")
                print("------------")
                time.sleep(2)
                print("      0     ")
                time.sleep(2)    
                print("      |     ")            
                time.sleep(2)
                print("     / \    ")
            if turns == 5:
                print("5 turns left")
                print("------------")
                time.sleep(2)
                print("    \ 0     ")
                time.sleep(2)    
                print("      |     ")
                time.sleep(2)            
                print("     / \    ")

            if turns == 4:
                print("4 turns left")
                print("------------")
                time.sleep(2)
                print("    \ 0 /   ")
                time.sleep(2)    
                print("      |     ")
                time.sleep(2)            
                print("     / \    ")

            if turns == 3:
                print("3 turns left")
                print("------------")
                time.sleep(2)
                print("         ^  ")
                time.sleep(2)
                print("    \ 0 /   ")    
                time.sleep(2)
                print("      |     ")
                time.sleep(2)            
                print("     / \    ")
            if turns == 2:
                print("2 turns left")
                print("------------")
                time.sleep(2)
                print("        ^   ")
                time.sleep(2)
                print("    \ 0 |/  ")
                time.sleep(2)    
                print("      |     ")
                time.sleep(2)            
                print("     / \    ")
            if turns == 1:
                print("last turn  ")
                print("------------")
                time.sleep(2)
                print("        ^   ")
                time.sleep(2)
                print("    \ 0_|/  ")
                time.sleep(2)    
                print("      |     ")
                time.sleep(2)            
                print("     / \    ") 
            if turns == 0:
                print("you are dead")
                print("------------")
                time.sleep(2)
                print("        ^   ")
                time.sleep(2)
                print("      0_|   ")
                time.sleep(2)    
                print("    / | \   ")
                time.sleep(2)            
                print("     / \    ")
                break 
  
  

                


                   

name= input("enter the name")
time.sleep(0.7)
print("welcome too the hang man game." , " MR/MRS" , name)
time.sleep(0.7)
print("////////////////////////////////////////////////////")
time.sleep(2)
print("can you complete this hang man game in 10 attempts" , name , "?")
hang()
print()
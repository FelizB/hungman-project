import random
from stages import stage
from items import item

guess=random.choice(item).lower()
blank=[]
lives=6
print (guess)
for _ in guess:
    blank+="_"
print(blank)

circles=False

while not circles:
    userEntry=input("Enter a letter: ").lower()
    entry=userEntry[0]

    print("\033[H\033[2J")

    if entry in blank:
        print("You have already guessed the letter. Try again")
    
    for position in range(len(guess)):
        if entry==guess[position]:
           blank[position]=entry
           print(f"Great!!, Good work done. You still have a total of {lives} lives")
           # if lives<6:
           #    lives+=1
           # else:
           #    lives=6
                
                
    print(blank)
     
    if entry not in guess:
       lives-=1
       if lives>=3:
          print(f"Opps!!You've lost a life. You now have {lives} lives remaining")
       elif lives>=1:
          print(f"Tooo bad!!You're about to die.Try Harder. You now have {lives} lives remaining")
   
    
    if lives==0:
        circles=True
        print("You're dead. You loose!!")
        
    print(stage[lives])

    if '_' not in blank:
        circles=True
        print("Contratuations, You Won!!!")

    


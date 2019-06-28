import time

israKech = ['kech']

locations = {
  "basement": {
    "text": "You can explore the room (type:explore) or go upstairs (type:upstairs)",
    "directions": {
      "upstairs" : "hallway",
      "explore"  : "basement2"
      }
  },
  "hallway": {
    "text": "You have arrived in a hallway with a few doors, you hear a few sounds somewhere near you. \nYou can go back (type: back), go left (type: left), go straight (type: straight) or go right (type: right) ",
    "directions": {
      "back" : "basement",
      "left" : "room002",
      "right" : "secretdoor",
      "straight" : "bi"

      }
  },
  "basement2": {
    "text": "You've found a few prescribed pills the bottle has the letter i on it. \nDo you want to take them? \nYes, I do (type: yes). No, stash them (type: no)",
    "object" : "pills",
      "yes" : "basement3",
      "no"  : "basement4"
    }
  },
  "basement3": {
    "text": "You start seeing red spots on your entire body, while you start suffocating.  You fall on the ground, the last thing you see is a white void. \n         YOU DIED"
    
  },
  "basement4": {
    "text": "You put them in your now empty backpack that you found next to you on the ground and decide to go upstairs (type: upstairs).",
    "directions": {
      "upstairs" : "hallway"
    }
  },
  "room002": {
    "text": "You have entered a square room that's called 002 with white cussions on all sides. \nYou notice camera's in every corner. \nYou hear the door closed behind you. \nYou can smash the camera's (type: smash), you can scream (type: scream) or you can hit the wall out of frustration (type: hit)",
    "directions": {
      "smash" : "deadend",
      "scream" : "deadend2",
      "hit" : "secretroom"
    }
  },
  "deadend": {
    "text" : "An alarm goes off. \nYou hear something while you feel a small sting in your right arm. \nYou fall on the ground because you are completely paralised. \nYou scream for ten minutes and even though your are paralised you feel all the pain. \nThe pain is unbareable, you start moving again, but the pain doesn't stop. \nYou start smashin your head on the floor so hard that you start bleeding to death. \n          YOU DIED"
  },
  "deadend2": {
    "text" : "You start smelling sulfur. \nYou notice that you're becoming lightheaded. \nYou are suffocating and you faint. \nYou were gassed. \n          YOU DIED"
  },
  "secretroom": {
    "text" : "You have opened a secret door. \nYou notice a few screws with the letter h on one of them. \nYou can pick them up? (type: yes or no)",
    "directions": {
      "yes": "hallway2",
      "no" : "hallway2"
    }
  },
  "hallway2": {
    "text" : "You think you're back at the same hallway as before. You are back at the same hallway as before (type: next).",
    "directions": {
      "next": "hallway"
    }
  },
  "bi": {
    "text" : "You start walking towards the end of the hallway. There you see two doors. Both doors have numbers on them. The door on the left is numbered 000. The door on the right is numbered 001. You can enter the numbered door 000 (type: 000) or you can enter the numbered door 001 (type: 001).",
    "directions": {
      "000": "room000",
      "001": "room001"
    }
  },
  "room000": { 
    "text" : "You have entered an empty room with only a desk and a painting. You can go to the desk (type: desk) or you can walk towards the painting (type: painting).",
    "directions": {
      "desk": "thedesk",
      "painting": "thepainting"
    }
  }, 
  "thepainting": { 
    "text" : "As you walk towards the painting it looks like the letter b is portrayed. \nYou also see a building, that might be the institution, and 4 people on the painting. \nA young woman on the right, an older man and a girl in the middle and on the far left another man. \nAs you walk closer a shadow falls over the painting and the face of the man on the left shifts to a demonic smile. \nYou back away and now the painting looks normal again. \nYou can destroy the painting (type: destroy) or you can go back (type: back).",
    "directions": {
      "destroy": "crushedpainting",
      "back": "room000"
    }  
  },
  "crushedpainting": {
    "text" : "You destroy the painting because you are too scared \nThere are some nails behind it. \nYou start bleeding like hell. \nYou bleed to death. \n          YOU DIED "
  },
  "thedesk": { 
    "text" : "There are some files on the desk. \nDo you want to grab the files and read them? (type: yes or no) ",
    "directions": { 
      "yes" : "files",
      "no" : "footsteps"
    }
  },
  "files": {
    "text" : "There are three files in total. \nYou start reading the first file. \nIt's about a seventeen years old girl named Lucy with PTSD. \nShe was being taken care of in room 001. \nThe second file has the letter t on it, it is about Tommy, he is twenty years old, he had a panic disorder. \nHis room is called 002. \nThe third file is ripped. \nThe only thing you can still read is that it's about a boy with a dissociative disorder. \nYou put the ripped file in your backpack, because you're curious. \nYou realise that you're at the floor from those three patients (type: next).",
    "directions": {
      "next" : "footsteps"
    }  
  },
  "footsteps": { 
    "text": "You hear footsteps outside the room. \nYou get scared and hide under the desk. \nYou hear the door opening. \nSomeone entered the room and walked towards the desk. \nYou hold your breath. \nYou can stay under the desk (type: stay) or you can attack the person (type: attack).",
    "directions": {
      "stay" : "thedesk2",
      "attack" : "deadend3"
    }
  },
  "deadend3": {
    "text": "You stand up and you see a woman in a doctors coat. \nShe looks very familiar. \nShe's surprised and happy to see you. \nShe says: 'Chris! There you are.' \nAs she walks towards you, you panic. \nShe notices and takes out a needle. \nJust when you're about to hit her she injects you with a stinging fluid. \n          YOU PASSED OUT"
  },
  "thedesk2": {
    "text": "The person walks towards the desk and grabs the files. \nIt stays quiet for a few seconds. \nYou look around and see the letter 's' carved into the desk You hear a sigh and then the person leaves. \nYou stay in the room for a bit just in case and then you leave (type: next).",
    "directions": {
     "next" : "hallway2" 
    }
  },
 "wire": {
   "text": "You get on the bed and while you reach to the light, the wire breaks. \nYou fall down and unfortunately you get eloctrocuted. \n          YOU DIED"
 },
 "bed": {
   "text": "You start to look around. \nWhen you come closer to the bed, you see spots of blood everywhere on it. \nUnder the pillow a photo is sticking out. \nYou grab it and three people are laughing on the picture; a girl and two boys. \nThey look happy. \nThe room must have been of one of the three patients. \nYou turn it around to see if there's some text on the back but you only see the letter 'e'. \nYou put the photo in your backpack and then you go to the broken sink. \nUnder the sink there is an iron tube on the ground. \nYou can pick this tube up (type: pickup) or leave it (type: leave)",
   "object" : "true"
   "directions": {
     "pickup" : "tube",
     "leave" : "notube"
   }
 },
 "tube": {
   "text": "Before you put the tube in your backpack you notice the letter 'c' on it and then you leave the room (type: next).",
   "directions": {
     "next" : "hallway2"
   }
 },
 "notube": {
   "text": "You leave the tube and you go away (type: next).",
   "directions": {
     "next" : "hallway2"
   }
 },
 "room001": {
   "text": "You get on the bed and while you reach to the light, the wire breaks. \nYou fall down and unfortunately you get eloctrocuted. \nYou can repair the light so you see the room better (type: repair or no)",
   "directions": {
     "repair" : "wire",
     "no" : "bed"
   }
 },
 "secretdoor": {
   "text" : "In order to open this door you need a password. \nYou may have noticed a few letters throughout your journey. \nThe password contains seven letters. \nTry to form a word."
 } 
  
}

print("Help guide: throughout the entire story you can type i to open your inventory")
time.sleep(2)
print("Good luck!")
time.sleep(1)
print("You wake up in the basement of a mental institution called Eichenhouse")
time.sleep(2)
israKech.append('Hoer')

  #def secretdoor():
    #while True:
      #option = input("> ")
      #if option == "bitches":
        #print("yes")
       # break
      #else:
        #print("no")


# while True:
#   option = input("> ").lower().strip()
#   if option in locations:
#     print("Hier verder werken lol")
#   else:
#     print(option + " is not an option")

def game(location):
  currentLocation = locations[location]
  print(currentLocation["text"])
  userInput = input("What do you want to do? ")
  if userInput == "i":
    print (', '.join(israKech))
    game (location)
  elif userInput not in commands:
    print("This is not an option.")
    game(location)
  else:
    pickup(location, userinput)  
    goTo = currentLocation["directions"][userInput]
    game(goTo)

commands = ["upstairs", "yes", "no", "explore", "back", "left", "right", "hit", "straight", "smash", "scream", "next", "000", "001", "desk", "painting", "destroy", "i"]

#game("basement")estroy]

def commandcheck (input):
  if input in commands:
    return True
  else:
    return False

if commandcheck(input) == False:
  print("This is not an option.")

def pickup(location, userInput):
  if userInput == "pickup":
    israKech.append(locations[location["pickup"]])
    print(israKech)
game("basement")

import time

locations = {
  "basement": {
    "text": "What do you want to do? Explore the room (type:explore) or go upstairs (type:upstairs)",
    "directions": {
      "upstairs" : "hallway",
      "explore"  : "basement2"
      }
  },
  "hallway": {
    "text": "You have arrived in a hallway with a few doors, you hear a few sounds somewhere near you.",
    "directions": {
      "s" : "basement"
      }
  },
  "basement2": {
    "text": "You've found a few prescribed pills the bottle has the letter i on it. \nDo you want to take them? \nYes, I do (type: yes). No, stash them (type: no)",
    "directions": {
      "yes" : "basement3",
      "no"  : "basement4"
    }
  },
  "basement3": {
    "text": "You start seeing red spots on your entire body, while you start suffocating.  You fall on the ground, the last thing you see is a white void. \nYOU DIED"
    
  }
}

print("Help guide: throughout the entire story you can type i to open your inventory")
time.sleep(2)
print("Good luck!")
time.sleep(1)
print("You wake up in the basement of a mental institution called Eichenhouse")
time.sleep(2)


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
  goTo = currentLocation["directions"][userInput]
  game(goTo)


game("basement")

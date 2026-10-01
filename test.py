life = 100
#print (life)

light_stand_punch = 50
hard_stand_punch = 65

# life = life - light_stand_punch
# print (life)
# life = life - hard_stand_punch
# print (life)

hadoken = 100
import time

for i in range(3, 0, -1):
    print(i)
    time.sleep(0.3)

print("FIGHT!")
while life > 0:
    move = input ("choose your move: ")
    print (f"you picked: {move}")
    if move == "hadoken":
        life = life - hadoken
        print ("HADOKEN!!!!")
    elif move == "light":
        life = life - light_stand_punch
        print ("Hiyah!")
    print (life)
if life <= 0:
    print ("K.O!")
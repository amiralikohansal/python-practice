import random

guesses = 3
random1 = random.randint(0, 100)
won = False
line = "-" * 60

print("""salam!!!
be bazi hads adad khosh amadid <3
(adad az 0 ta 100 entkhab mishe!) """)


while guesses > 0:

    input1 = input(f"hads khod ra vared konid ({guesses} baghi mande!) : ")
    print(line)
    try:
        guess = int(input1)

    except ValueError:
        print("lotfan yek adad sahih vared konid!!!")
        print(line)
        continue

    if 0 <= guess <= 100:
        if guess == random1:
            print("afarin!!! dorost hads zadi")
            print(f"tedad hads estefade shode {4 - guesses}")
            won = True
            break

        elif guess > random1:
            print("ye adade kochiktar ro emtehan kon")

        elif guess < random1:
            print("ye adade bozorgtar ro emtehan kon")

        guesses -= 1

    else:
        print("yek adad bein 0 ta 100 vared konid!!!")
if not won:
    print(line)
    print(f"""motasefane hame shans hat tamom shod !!! :(
adad dorost {random1} bood
dafe badi talash kon <3""")

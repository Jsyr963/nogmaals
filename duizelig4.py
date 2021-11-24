Dag = input("Kies een dag van de week: ")
a = 2
while a < 3:
    if Dag == "Maandag":
        print("Maandag")
    elif Dag == "Dinsdag":
        print("Maandag", "Dinsdag")
        break
    elif Dag == "Woensdag":
        print("Maandag", "Dinsdag", "Woensdag")
        break
    elif Dag == "Donderdag":
        print("Maandag", "Dinsdag", "Woensdag", "Donderdag")
        break
    elif Dag == "Vrijdag":
        print("Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag")
        break
    elif Dag ==  "Zaterdag":
        print("Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag")
        break
    elif Dag == "Zondag":
        print("Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag")
        break
    a = 4
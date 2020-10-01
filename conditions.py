
run=True
while run:
    temp=int(input("Enter the temperature outside:"))
    if temp == 999:
        run=False
    elif temp > 90:
        print("Wear Shorts")
    elif temp > 70:
        print("Shorts sleeves are fine")
    elif temp > 50:
        print("Wear a jacket")
    elif temp > 32:
        print("Wear a heavy coat")
    else:
        print("Stay inside")

print("Have a nice day!")

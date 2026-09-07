score = int(input("What's thee score? "))
if score >= 90 and 100 > score:
    print("A")
elif score >= 80 and 90 > score:
    print("B")
elif score >= 70 and 80 > score:
    print("C")
elif score >= 60 and 70 > score:
    print("D")
else:
    print("F")
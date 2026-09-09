while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("xx is not an integer")
    else:
        break
print(f"x is {x}")
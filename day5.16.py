def main():
    size = int(input("Size of square - "))
    print_square(size)

def print_square(Size):
    #for each row in square
    for i in range(Size):
        #for each brick in row
        for j in range(Size):
            #print brick
            print("#", end = "")
        print()

main()
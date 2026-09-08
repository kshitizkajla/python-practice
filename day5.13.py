def main():
    height = int(input("Enter the height for the column - "))
    print_column(height)

def print_column(Height):
    for h in range(Height):
        print("#")

main()
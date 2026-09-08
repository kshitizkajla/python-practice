def main():
    height = int(input("Enter the height for the column - "))
    print_column(height)

def print_column(Height):
    print("#\n" * Height, end="")

main()
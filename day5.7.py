def main():
    number = get_number()
    hello(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def hello(n):
    for i in range(n):
        print("Hello")

main()


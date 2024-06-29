import argparse

def add_numbers(num1, num2):
    return num1 + num2

def main():
    parser = argparse.ArgumentParser(description="Add two numbers")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    args = parser.parse_args()
    
    result = add_numbers(args.num1, args.num2)
    print(f"The sum of {args.num1} and {args.num2} is {result}")


# this if statement is required in Python, defines the entry point for your script
'''if __name__ == "__main__":
    main()'''
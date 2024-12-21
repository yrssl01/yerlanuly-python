# Task 1

def task1_1():
    try:
        num = input("Enter your number: ")

        num = float(num)

        if num > 7:
            print("Hello")
        elif num < 7:
            print("Your number is less than 7, Bye!")
        else:
            print("Your number is equal to 7")

    except ValueError:
        print(f"Invalid input: {num}. Please enter a valid number!")


def task1_2():
    try:
        name = input("Enter your name: ")

        if name.lower() == 'john':
            print("Hello, John!")
        else:
            print("There is no such name!")

    except Exception as e:
        print(f"We have problem: {e}")


def task1_3():
    try:  
        array = input("Enter list of numbers separated by spaces:\n").split()
        numbers = [float(x) for x in array]
        multiples_of_three = [x for x in numbers if x % 3 == 0]
        
        if multiples_of_three:
            print("Multiples of 3: ", multiples_of_three)
        else:
            print("There are no multiples of 3 in your entered numbers")

    except ValueError:
        print(f"Invalid input: {array}.\nPlease enter valid numbers separated by spaces!")
    except Exception as e:
        print(f"We have problem: {e}")


def run():
    task1_1()
    task1_2()
    task1_3()


if __name__ == "__main__":
    run()


# Task 2

"""
[((())()(())]]

a) Can this sequence be considered correct? - No

b) If the answer to the previous question is “no”, 
then what needs to be changed in it to make it correct?

- This sequence needs one closing bracket ')' and 
one opening square bracket '[' so the sequence would look like:
   [()(())()(())[]]
        or
   [[((()))()(())]]
"""






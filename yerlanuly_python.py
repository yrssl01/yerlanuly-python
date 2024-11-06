# Task 1


number = int(input())

if number > 7:
    print("Hello")


name = input()

if name == "John":
    print("Hello, John")
else:
    print("There is no such name")


array = list(map(int, input().split()))
multiplies_of_three = [x for x in array if x % 3 == 0]
print(*multiplies_of_three)


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






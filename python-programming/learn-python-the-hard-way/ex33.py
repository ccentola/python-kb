def user_while(val):
    
    val = int(val)
    i = 0
    numbers = []

    while i < val:
        print(f"At the top i is {i}")
        numbers.append(i)
        
        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
        
    print("The numbers: ")

    for num in numbers:
        print(num)
        
val = input("Enter a value > ")
user_while(val)
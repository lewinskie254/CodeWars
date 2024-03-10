def calculate_cost(n):
    first_nine = "9"
    group_1= "9"
    group_2 = "9"
    x = len(str(n))
    y = x - 1
    array_multipliers = []
    array_of_nines = []
    multiplier = 2
    total = 0

    while y >= 2:
        if x < 2:
            print(n)
        else: 
            group_1 += "0"
            array_multipliers.append(group_1)
            group_2 += "9"
            array_of_nines.append(group_2)
            y -= 1


    total += int(first_nine)
    for i in range(len(array_multipliers)):
        total += int(array_multipliers[i]) * (i + 2)
        multiplier += 1

    if len(array_of_nines) >= 1: 
        total += (n - int(array_of_nines[len(array_of_nines)-1])) * multiplier
    else: 
        total += (n - 9) * multiplier

    return total 

def main(): 
    number = int(input("Number: "))
    result = calculate_cost(number)
    print(result)

if __name__ == "__main__":
    main()
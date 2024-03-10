import math

def ellipse(a, b):
    pie = 3.14159265
    #Area  
    Area = round((pie * a * b), 1)
    #Perimeter 
    Perimeter = round((pie * (3/2*(a + b) - math.sqrt(a * b))), 1)

    return f"Area: {Area}, perimeter: {Perimeter}"


def main():
    result = ellipse(13, 1)
    print(result)

if __name__ == "__main__":
    main()
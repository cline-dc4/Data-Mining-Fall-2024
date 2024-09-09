'''
This is a block comment :)
'''
# this is a line comment :)

def main():
    print("Hello world")
    
    x = 12
    y = 3.14
    print("Values:", x, y)
    
    string = input("enter something:")
    number = int(input("enter a number:"))
    gpa = float(input("enter your gpa:"))
    print(string, number, gpa)
    
    printInformation(number)
    print("Number of factors:", countFactors(number))
    
    array = [[1, 2, 3], [4, 5, 6]]
    manipulateArray(array)
    
def manipulateArray(array):
    print("Number of rows:", len(array))
    print("Number of columns:", len(array[0]))    
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i],[j], end = " ")
        print()
        
        
def printInformation(number):
    #Determine if number is a multiple of 7 or 8
    if number % 7 == 0:
        print(number, "is a multiple of 7")
    elif number % 8 == 0:
        print(number, "is a multiple of 8")
    else:
        print(number, "is not a multiple of 7 or 8")
    return number/10
    

def countFactors(number):
    numFactors = 0
    for i in range(1, (number + 1)/2):
        if number % i == 0:
            numFactors += 2
    return numFactors


main()
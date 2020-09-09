#function that finds the area of something and returns the result
def area(width, height):
    result = width * height
    return result
# variables created where we store the results of the area funciton with different parameters
result = area(5, 6)
resultOne= area(7, 7)
resultTwo= area(3, 4)

# here we print the results that are stored in these variables
print(result) 
print(resultOne)
print(resultTwo)

# this is a function that takes two numbers and subtracts them 
def subtract(num1, num2):
    result = num1 - num2
    return result
#these variables are storing the result of the subtract functions that were called with different parameters
resultsub = subtract(20, 13)
resultSubOne = subtract(50, 25)

#this prints the results that were assigned to the variable
print(resultsub)
print(resultSubOne)

#this function takes two numbers and adds them 
def add(num1, num2):
    result = num1 + num2
    return result
#these variables store the results of the function being called with different parameters
resultAdd = add(20, 54)
resultAddAgain = add(12, 7)

#this prints the results that were assigned to these variables..
print(resultAdd)
print(resultAddAgain)
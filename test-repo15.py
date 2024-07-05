# simple calculator in python 

print("================================")

print("Addition")
print("Suobtraction")
print("Multiplication")
print("Division")

print("===============================")

pili_ka = int(input("Choose an operation: "))

if(pili_ka in [1,2,3,4]):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if(pili_ka == 1):
                resulta = num1 + num2
        elif(pili_ka == 2):
                resulta = num1 - num2
        elif(pili_ka == 3):
                resulta = num1 * num2
        elif(pili_ka == 4):
                resulta = num1 // num2      # // this operator will give you integer numbers not float
        
else:
    print("Invalid operation ang na pili mo na e entered:")

print("The result of the operation is {}".format(resulta))
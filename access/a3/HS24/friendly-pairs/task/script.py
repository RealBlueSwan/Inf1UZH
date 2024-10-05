
# You need to complete this function.
# The numbers must be valid according to description before determining friendly parity situations.
# Return the string "Invalid" if they are not valid.
def is_friendly_pair(num1, num2):
    # def used some error handling so I might wanna do the same
    if not type(num1) is int or not type(num2) == int or num1 == num2 or num1 < 1 or num2 < 1:
        return 'invalid'
    
    #creating the two temps with the 
    temp1 = sum([n for n in range(1, num1+1) if num1%n == 0])
    temp2 = sum([n for n in range(1, num2+1) if num2%n == 0])
    
    # return if the numbers are a friendly pair
    return temp1/num1 == temp2/num2

#This line prints your method's return so that you can check your output.
print(is_friendly_pair(6, 28))

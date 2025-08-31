
# Project Euler problem 4: largest palindrome product

number = 9999
if str(number) == str(number)[::-1]:  # Checks if the string follows palindromic logic
    print("Palindromic")
else:
    print("Not palindromic")

palindromes = [] # Created list to store possible products
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if str(product) == str(product)[::-1]: # Checks if the product is a palindrome
            palindromes.append(product)

largest_palindrome = max(palindromes) # Finds largest value in list

print(largest_palindrome)
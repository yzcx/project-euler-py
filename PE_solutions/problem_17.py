
# Project Euler problem 17: number letter counts

letters_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
                11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
                18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
                70: "seventy", 80: "eighty", 90: "ninety"}

def count_letters_number(n:int) -> int:

    if n == 1000:
        return len("onethousand")

    number_string = ""
    if n >= 100: # Handling the hundreds first
        hundreds = n // 100
        n = n % 100
        number_string += letters_dict[hundreds] + "hundred"
        if n > 0:
            number_string += "and"
    if n > 20: # Handling the tens and unit place. I check for numbers greater than 20 because the first 20 numbers don't follow tens and unit rule
        tens = n // 10
        n = n % 10
        number_string += letters_dict[tens * 10]
    if n > 0: # Added the units digit handling 1 to 19
        number_string += letters_dict[n]
    return len(number_string)

print(sum([count_letters_number(i) for i in range(1,1001)]))
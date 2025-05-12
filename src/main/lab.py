# lab.py

# Create a function by following these instructions

"""
#Function Name: The function should be named count_vowels.

#Parameters: The function should take one parameter named string, 
                which represents the input string.

#Functionality: The function should count the number of vowels 
                (both lowercase and uppercase) in the input string and return the count.

#Implementation: Inside the function, use a loop to iterate through 
                each character of the input string. Check if each character is a vowel 
                (either lowercase or uppercase) by comparing it to a string containing 
                all vowels ("aeiouAEIOU"). If a character is found in the vowels string, 
                increment a counter variable by 1. Finally, return the value of the counter 
                variable as the result.

"""
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


if __name__ == "__main__":
    sample_text = "Hello World!"
    print("Number of vowels:", count_vowels(sample_text))


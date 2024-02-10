#Write a program that counts the number of vowels in a sentence.

def vowel_count(string):
    vowels = "aeiouAEIOU"
    seen_vowels = []
    for  char in string:
        if char in vowels:
            seen_vowels.append(char)
    return len(list(set(seen_vowels)))

print(vowel_count('Hello World'))
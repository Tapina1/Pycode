'''
word=input("Enter a word to print without vowel:")
vowel=['a','e','i','o','u']
code=[i for i in word if i not in vowel]
print(code)
'''
print([i for i in input() if i not in 'aeiou'])
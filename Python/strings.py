"""
Strings are simply plain text.
We need to use quotation marks to use them
"""

print("Giraffe Academy")

# Prints on a new line, i.e escape character
print("Giraffe\nAcademy")
print("Giraffe \"Academy\"")
print("Giraffe\Academy")

phrase = "Giraffe Academy"
print(phrase)

# Concatenation
# The process of taking a string and appending another string to it
print(phrase + " is cool")

# String methods
# Capitalisation
print(phrase.lower())
print(phrase.islower())

print(phrase.upper())
print(phrase.isupper())

# Combination of methods
print(phrase.upper().isupper())

# Length of a string
print(len(phrase))

# We can access a given charecter in a string using []

ourname = "TS Corp"
# index =  0123456

print(len(ourname)) # its 7 since its starting from 0
print(ourname[0:2]) # Strign slicing, index 2 is ignored, at 0 and 1 we have T and S so O/P >> TS

# To ge the index of a charecter from a string, you can use the .index() method
print(ourname.index("T")) # O/P >> 0
print(ourname.index("Cor"))

print(ourname.replace("Corp", "Corporation"))
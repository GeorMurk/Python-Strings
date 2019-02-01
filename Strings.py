#!/usr/bin/python

#!Working with Strings

phrase = "Test is Cool"
print(phrase)

#!A string can undertake various pre-conditions such as being lowercase or uppercase

print(phrase.lower())

#!uppercase

print(phrase.upper())

#!In combination

print(phrase.upper().isupper())

#!character length

print(len(phrase))

#!Characters are numbered from Zero(0) in python
#!A text such as this
#!0123456789....
#!count also the spaces

print(phrase.index("e"))

#!will give where this text starts from

print(phrase.index("is"))

#!you can also replace text

print(phrase.replace("Cool", "Awesome"))


#!Go ahead and Test!!!!
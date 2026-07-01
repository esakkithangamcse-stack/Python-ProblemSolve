import re
text = "My age is 25 and my friend is 30."
print(re.sub(r"\d+", "#", text))

#find all the words in the string
print(re.findall(r"\w+", text))

#find vowels in the given string
print(re.findall(r"[aeiouAEIOU]", text))

#find 4 digits nums
text = "123 1234 12345 5678"
print(re.findall(r"\b\d{4}\b", text))

#find words ending with "ing"
text = "playing walking play going"
print(re.findall(r"\w+ing\b",text))


text = "111 22 3333 456"
print(re.findall(r"[.]+", text))
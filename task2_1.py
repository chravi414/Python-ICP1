# text = input("Please enter the string: \n")
# result = text[2:]
# print(result)
# print(result[::-1])

text = ""
while True:
    l = input()
    if l:
        text += l
    else:
        break
print(text)
result = text[2:]
print(result)
print(result[::-1])

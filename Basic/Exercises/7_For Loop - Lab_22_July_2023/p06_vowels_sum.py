text = input()

sum = 0

for i in range(0, len(text)):
    if text[i] == 'a' or text[i] == 'A':
        sum += 1
    if text[i] == 'e' or text[i] == 'E':
        sum += 2
    if text[i] == 'i' or text[i] == 'I':
        sum += 3
    if text[i] == 'o' or text[i] == 'O':
        sum += 4
    if text[i] == 'u' or text[i] == 'U':
        sum += 5
print(sum)
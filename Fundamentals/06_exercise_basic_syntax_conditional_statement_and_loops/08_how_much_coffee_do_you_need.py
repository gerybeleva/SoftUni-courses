input_string = input()
coffe_counter = 0

while input_string != "END":
    if input_string.lower() == "coding" or \
        input_string.lower() == "dog" or \
        input_string.lower() == "cat" or \
        input_string.lower() == "movie":
        if input_string.islower():
            coffe_counter += 1
        else:
            coffe_counter += 2
    input_string = input()
if coffe_counter > 5:
    print('You need extra sleep')
else:
    print(coffe_counter)
number_symbols = int(input())

for symbol_1 in range (number_symbols):
    for symbol_2 in range (number_symbols):
        for symbol_3 in range (number_symbols):
            print(f"{chr(97 + symbol_1)}{chr(97 + symbol_2)}{chr(97 + symbol_3)}")

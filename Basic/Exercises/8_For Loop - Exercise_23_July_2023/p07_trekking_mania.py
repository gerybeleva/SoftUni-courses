group_qty = int(input())
total_people = 0
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(group_qty):
    current_group = int(input())
    total_people += current_group

    if current_group <= 5:
        musala += current_group
    elif 6 <= current_group <= 12:
        monblan += current_group
    elif 13 <= current_group <= 25:
        kilimanjaro += current_group
    elif 26 <= current_group <= 40:
        k2 += current_group
    elif 40 < current_group:
        everest += current_group

percent_musala = musala / total_people * 100
percent_monblan = monblan / total_people * 100
percent_kilimanjaro = kilimanjaro / total_people * 100
percent_k2 = k2 / total_people * 100
percent_everest = everest / total_people * 100

print(f'{percent_musala:.02f}%')
print(f'{percent_monblan:.02f}%')
print(f'{percent_kilimanjaro:.02f}%')
print(f'{percent_k2:.02f}%')
print(f'{percent_everest:.02f}%')
lenght = int(input())
widght = int(input())
high = int(input())
used_space = float(input())

aquarium_total_volume = (lenght * widght * high) /1000 #devide by 10 to get dm instead of cm. Because this is a volume the devision is done 3x

water_volume = aquarium_total_volume * (1 - (used_space / 100))

print(water_volume)
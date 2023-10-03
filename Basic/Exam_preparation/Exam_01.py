perc_fat = int(input())
perc_protein = int(input())
perc_carb = int(input())
total_callories = int(input())
perc_water = int(input())

calories_per_gram_fat = 9
calories_per_gram_protein = 4
calories_per_gram_carb = 4

daily_fat = total_callories * (perc_fat / 100) / calories_per_gram_fat
daily_protein = total_callories * (perc_protein / 100) / calories_per_gram_protein
daily_carb = total_callories * (perc_carb / 100) / calories_per_gram_carb

daily_food_imcome = daily_fat + daily_protein + daily_carb
calories_per_gram = total_callories / daily_food_imcome
gram_without_water =  calories_per_gram * (1 - perc_water / 100)

print(f'{gram_without_water:.4f}')
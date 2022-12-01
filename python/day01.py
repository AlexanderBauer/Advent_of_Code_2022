# advent of code day 1

# import helper function
import helper

# function for building list of calories
def get_calories_list():
    # read data from txt file
    data = helper.read_data('../inputs/day1.txt')

    # split string in list by new lines
    food_list = data. splitlines()

    # set intital values
    elf_calories = 0 # calory count for current elf
    calories_list = [] # the calories_list to be returned

    # loop through items in food_list
    for calories in food_list:
        if calories == '':
            # new elf -> append calories to list and reset to zero
            calories_list.append(elf_calories)
            elf_calories = 0
        else:
            # increase elf_calories by calories for food item
            elf_calories += int(calories)

    # return calories_list
    return calories_list

# generate list of calories per elf
calories_list = get_calories_list()

# solution part one - calories top 1 elf
solution_part_one = max(calories_list) # 70374

# solution part two - sum of calories top 3 elfes
solution_part_two = sum(sorted(calories_list, reverse=True)[:3]) # 204610

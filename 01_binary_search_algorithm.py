def binary_search(user_list, item):
    low = 0
    high = len(user_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = user_list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

chosen_num = int(input("Give an odd number from 1 to 25 and you'll get it's index:\t"))
print(chosen_num, "- index:", binary_search(my_list, chosen_num))


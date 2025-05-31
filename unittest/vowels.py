def count_vowels(string):
    vowels = 'aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ'
    return sum(1 for char in string if char in vowels)


print(count_vowels('tyuie'))

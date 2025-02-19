print("om shrivastav")
print("24BEE083")
def char_frequency(string):
    freq_dict = {}
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict


input_string = input("Enter a string: ")


frequency_dict = char_frequency(input_string)


print("Character Frequency Dictionary:")
for char, freq in frequency_dict.items():
    print(f"'{char}': {freq}")

# input

my_input = input('Give me a number: ')
print('Your input twice:', int(my_input)*2)

# ways that are less clear

my_input_str = input('Give me a number: ')
my_input_int = int(my_input_str)
output_str = "Your input twice: " + str(2*my_input_int)
print(output_str)

print("Your input twice:", 2*int(input("Give me a number: ")))
# multiple assignment
a = 5
a, b = 5, 6

# swapping values of variables
a, b = b, a

# wouldn't work
a = b # put b into a
b = a # now a and b are the same

# swapping with a temporary variabe
temp = a # a is old a, b is old b, temp is old a
a = b    # a is old b, b is old b, temp is old b
b = temp # a is old b, b is old a, temp is old a

# swap vals of a and b w/o multiple assignment
a = a + b


# True: 1
# False: 0
# and: *
# or: +

# A * B: positive iff both A and B are positive
# A and B: True iff A and B are True

# A + B: positive iff at least of A and B are positive
# A or B: True iff at least of A and B are True

lazy = False
smart = True
growth_mindset = True

# Operator precedence: not -> and -> or
# if not sure, always better to use parentheses
if not lazy and smart and growth_mindset:
    print("Go to EngSci")
elif not lazy and smart and not growth_mindset:
    print("Artscis L")
elif lazy and smart:
    print("Physics")
elif not lazy and smart and not growth_mindset:
    print("Econ")
else:
    print("TMU")
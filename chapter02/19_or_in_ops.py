choice = 'q'

# Java way
if choice == '1' or choice == "Q":
    print("Quit")
else:
    print("Continue")

# Pythonian way
if choice.lower() == "q":
    print("Quit")
else:
    print("Continue")

# More pythonian way
if choice in ('q', "Q"):
    print("Quit")
else:
    print("Continue")
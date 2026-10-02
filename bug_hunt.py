count = 1
total = 0

# BUG: The while statement was missing a colon, so Python could not start the block.
while count < 5:
    total = total + count
    count = count + 1
# BUG: The print statement tried to join a string and an integer with +.
print("Sum of 1 to 5 is: ", total)

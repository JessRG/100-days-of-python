def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
#       The loop is iterating from 1 (start) to 20 (stop) times. The value 20 is excluded.
# 2. When is the function meant to print "You got it"?
#       The function is meant to print "You got it" on the 20th iteration of the loop.
# 3. What are your assumptions about the value of i?
#       My assumptions are that the value of i starts from 1 and stops at 20 exclusive.
#       The i never equals 20, so the print("You got it!") line will never run.

An easier way for task 3 is like this: return f"Hello {name}!"

Not working.

def hello_func(hello):
    return f"Hello {name}!"

print(hello_func("Tshepo"))


output:"Hello   !"



In all your functions, once you have finished, why do you call empty functions?

I suppose they way have I written the code allows for the proper return


The output for task 8 is slightly wrong if you call covert_to_time(61), the output should not be 1 hour 1 minutes but rather 1 hour 1 minute. Also, notice the spelling mistake in the name of your function.
Fixed

Your functions for task 9 and 10 and the other tasks also, should have parameters, you should not be setting the data you want inside the body of the function. For instance, if you had a function which compares two numbers then you don't do this:

def comparison(): num_1 = 10 num_2 = 20 etc

You do however do this:

def comparison(num_1, num_2): etc

My understanding is that I need to be specific form my last feedback:
"You used input from task 0.4 - task 0.10 and you were instructed not to ask people to input anything, please fix your code."



Otherwise,just fail me. I give up.
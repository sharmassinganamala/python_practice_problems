#some examples for random modules
import random  #we need t import random module
my_random = random.randint(1,100)
print(f"solotion for first random number {my_random}\n")  #it prints random numbers between 1 to 100
# it print random float number from 0.000000000.. - o.999999999999....
random_float = random.random()
print(f"solution for second example {random_float}\n")
# we want extra random nuber above 1 we need to multipl with some other number
# EXAMPLE 
random_float1 = random.random()
random_float2 = random_float1 * 5 #now it will generate random float number more than 1 sometimes
print(f"solution for third example {random_float2}\n")

#simple example on random module
love_score = random.randint(1,100)
print(f"your love_score is {love_score}")

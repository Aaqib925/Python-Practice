# import random
#
# value = random.random()   # this can only select a random number within the range of 0 and 1
#
# print(value)

# if we want to get a random floating point value in the certain range

# import random
# value = random.uniform(1, 12)
# print(value)

# import random
# this will select a random number in the range of 1 to 6
# value = random.randint(1, 6)
# print(value)

# import random
# my_list = list(range(1, 11))
# value = random.choice(my_list)   # this can choose a single random number from the list
# for more than 1 random value...we use the choices keyword
# value2 = random.choices(my_list, k = 10)   # this will choose the random values from the list according to the value of k
# print(value)
# print(value2)
# so there is also another method of the choice of random number by using the sample keyword...but the main difference
# between choice and sample keyword is that there is repetition in the choice but not in sample
# sample keyword can be used if we want to get the unique value

# import random
#
# my_list = list(range(1, 11))
#
# value = random.sample(my_list, k = 10)
#
# print(value)

# there is another method by which we can make a certain possiblity of the values to be taken in a percentage

# import random
#
# greetings = ["Hello", "Hey", "Hi", "Assalamu Alaikum", "Namasty", "Hola"]
#
# message = random.choice(greetings)
#
# print(message + ", Aaqib" + "!")

# if we want to get more many of the random choices but priority wise than we can use the keyword of wroghts[]

# import random
#
# colors = ["Red", "Blue", "Orange"]
#
# result = random.choices(colors, weights=[3, 3, 1], k = 10)
#
# print(result)

# method to get the shuffled result
#
# import random
# my_list = list(range(1, 21))
# # random.shuffle(my_list)
# result = random.sample(my_list, k = 5)
#
# print(result)
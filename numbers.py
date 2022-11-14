import random
num_to_guess = random.randint(1, 100) # random number in this variable
# print(num_to_guess)#admin line , can see number

ram=[]

num_user=100

while num_user != num_to_guess: #loop continue with number of user and number of random
    num_user = int(input("hey take me a number smaller to random from 100: ")) # number of user
    if num_user > num_to_guess:  #asking for a number again. as long as the user input is greater than the number keep running the loop.
        print("the number is to big ")

    elif num_user < num_to_guess:  #if number of user is no big and smaller we give him to understand this
        print("sorry Your numbers is so smaller ")
        ram.append(num_user)

else: #if user know number
    print("W=O=W  that's AMAZING you're Done ")
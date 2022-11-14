import random
num_to_guess = random.randint(1, 100) # random number in this variable
# print(num_to_guess)#admin line , can see number
user_name = input("Hi what Your NAME? q-quit : ")  # this user name
users = [] #RAM user name like user
users.append(user_name)  # add user name like user use username

num_list=[] #for numbers
users_qua=[]
# users_qua_num=[]

num_user=100
while num_user!= num_to_guess: #loop continue with number of user and number of random
    users_qua = len(set(users))
    # users_qua_num = len(set(num_user))
    num_user=input("give me a number from 100 q-quit: ") # number of user
    if num_user != "q":  # bue this quit
        if num_user != "cu":
            if int(num_user) > num_to_guess:  #asking for a number again. as long as the user input is greater than the number keep running the loop.
                print("the number is to big ")

            elif int(num_user) < num_to_guess:  #if number of user is no big and smaller we give him to understand this
                print("sorry Your numbers is so smaller ")

            else: #if user know number
                print("W=O=W  that's AMAZING you're Done ")
                print("close program")
                print(f"Well we had user going by the name: {user_name} and ugadal number s 4 popitok ")
                break

    # if user_name == "q":  # If for q = quit from program on name
    #     print("okey bue")
    #     break
    if num_user == "q": #If for q = quit from program on num user
        print("okey bue")
        print(f"Well we had user going by the name: {user_name} and ugadal number s 4 popitok ")
        break
    if num_user == "cu": #If for cu = to change name
            print("you're welcome")
            user_name = input("Hi what Your NAME? q-quit : ") #this user name



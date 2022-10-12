#OLEG SHLYUBSKIY version 1/8
user_name = input("Hi what Your NAME?: ")
users = []
temp_list=[]
users.append(user_name)
watched_movies = {"matrix": 9.0, "Thor love and thunder": 8.3, "green book": 8.3, "her": 8.1,
"the evil dead": 7.8, "forrest gump": 9.2, "life aquatic": 9.5, "life of bryan": 7.9, "first blood": 8.9}
#lists (here RAM of all prog)
movies_to_watch = {}

rait = []
user_movie_rait=[]
#here need only one if oleg oleg this 1
movies_to_watch_qua=len(set(movies_to_watch))
users_quantity=len(set(users))


flag = True
while flag:
    # user_name = input("Hi what Your NAME?: ")

    users_quantity = len(set(users))
    user_movie = input("Enter a name of a movie you've recently watched,“cu” to change user or “q” to quit: ")
    movies_to_watch_qua =len(set(movies_to_watch))

    if user_movie.casefold() != 'q':            #dont take if not q or cu!
        if user_movie.casefold() != 'cu':
#function to user name and movies
            if user_movie in watched_movies:                                                                  # If the movie is in the watched_movies dict, then the program will print:
                print(f"I've watched that movie as well I rate it {watched_movies[user_movie]}")              # "I've watched that movie as well I rate it {rating of the movie in watched_movies dict}
                user_rait = input("what's your rating between 1 and 9 ?: ")                                   # movie as well i rate it {rating of the movie in watched_movies dict}
                if user_rait > str("6"):                                                                      #raiting
                    rait.append(user_rait)                                                                    # If the rating is 7 or higher than the movie will be saved in a dictionary with a user_name as
                    print("wow we have similar taste")

                else:
                      print("Well i guess we will agree to disagree")



            else:                                                                                                  # If the movie is NOT in the watched_movies list, then the program will print:
                user_rait = int(input("I haven't watched that how would you rate it on a scale from 1 to 9 ? : ")) # "I haven't watched that one yet, how would you rate it on a scale from 1 to 10? "###
                if user_rait >= 7:                                                                                 #raiting
                    rait.append(user_rait)
                    temp_list.append({user_movie:user_rait}) # If the rating is 7 or higher than the movie will be saved in a dictionary with a user_name as
                    movies_to_watch[user_name] = {user_movie: user_rait}
                    print("will be saved in a dictionary with a user_name" )

                else:
                    print("Well my minimum is 7 so guess we wont be watching this one soon")

    # what we do that q or cu
    if user_movie == "q":
        print("okey bue")
        if users_quantity == 1:   #if 1
            print(f"Well we had {users_quantity} users today going by the names: {users} and nothing was added to movies_to_watch {movies_to_watch}")

        else:                     #else something else
            print(f"Well we had {users_quantity} users today going by the names: {users} and these were added to movies_to_watch {movies_to_watch}")

        flag = False

    if user_movie == "cu":
        user_name = input("Hi what Your Name here: ")
        users.append(user_name)
        temp_list = []
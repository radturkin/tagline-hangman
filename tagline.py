import pandas as pd
import string
import random

#read in csv for film titles and taglines
movieset=pd.read_csv("tmdb_5000_movies.csv")

#create list that is just titles
movies=movieset['title'].tolist()

#create new df just for title and tagline
taglinemovies = movieset[['title', 'tagline']]

#convert df to dictionary
taglinedictionary=taglinemovies.set_index('title').to_dict()['tagline']

#create list of one word titles
singlewordtitle=[]

for i in range(len(movies)):
    if movies[i].isalpha():
        singlewordtitle.append(movies[i])

# a function that will randomly select our movie for us
def get_valid_title(singlewordtitle):
    movie=random.choice(singlewordtitle) #select a random movie title from list
    return movie

#playagain
def play_again():
    again=(input("Would you like to play again? (y/n) "))
    if again.lower()=='y':
        hangman()

    else:
        print('Life moves pretty fast. If you dont stop and look around once and a while you might miss it.')


# a function to play hangman with our data
def hangman():
    movie=get_valid_title(singlewordtitle)
    tagline=taglinedictionary[movie] 
    movie=movie.upper()
    word_letters=set(movie)
    allletters=set(string.ascii_uppercase)
    used_letters=set()
    tries=int(input("how many tries? "))
    tagmovie=movie.lower()

    if pd.isna(tagline): #if no tagline available
        tagline="they had no tagline, they had not butter, they could  make no tagline sandwhiches"
   
    print(tagline)

    while len(word_letters)>0 and tries>0:
        print("You have used: ", " ".join(used_letters), "and have ", str(tries), " tries remaining")
        print(" ")
        word_list=[letter if letter in used_letters else '_' for letter in movie]
        print("movie title: ", " ".join(word_list))
        user_letter=input("guess a letter: ").upper()
        print(" ")
        
        if user_letter in allletters - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else:
                tries-=1

                print(' ')
        elif user_letter in used_letters:
            print(" ")
            print("used, baby!")
            print(" ")

        else:
            print(" ")
            print("does not compute")
            print(" ")

    if tries==0:
        print("sorry, it was ", movie, tagline)

    else:
        print(movie, tagline, ". You're a winner!")
        print("you get a prize!")
        print("its a tagline: ", tagline)

    play_again()



hangman()


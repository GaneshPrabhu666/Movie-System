User = list()
Movie = dict()
MovieGenres = dict()
UserReview = dict()
isCriticUser = dict()
MovieReviews = dict()
AVGMovieReview = dict()
currentYear = 2021

def get_avg_review_of_movie(movie):
    print("Avg review of ",movie,"is",AVGMovieReview[movie])


#function to print all movies
def get_top_movies():
    print('Top Movies of ', 'Genere are:')
    sorted(AVGMovieReview)
    for index, (key, value) in enumerate(AVGMovieReview.items()):
        print( key, value)


#function to print movies of genre
def get_movies_of_genre(genre):
    print('Movies of ', genre, 'Genere are:')
    for key, value in Movie.items():
        if(MovieGenres[key] == genre):
            print(key)

#function to calculate average review
def avg_movie_review(movie):
    reviews= MovieReviews.get(movie)
    total =0
    for i in range(0, len(reviews)):
        total+= reviews[i]
    AVGMovieReview[movie] = total/len(reviews)

#function to add review
def add_review(user, movie, rating):
    if user in User:
        if Movie[movie] < currentYear:
            UserReview.setdefault(user, []).append(movie)
            UserReview.setdefault(user, []).append(rating)
            MovieReviews.setdefault(movie, []).append(rating)
            avg_movie_review(movie)
        else:
            print("You can review only Released Movies")
    else:
        print("You need to first Register to add Review")

#function to add Movie
def add_movie(movie, year, genre):
    Movie[movie] = year
    MovieGenres[movie] = genre

#function to add user
def add_user(name):
    User.append(name)

def main():
    # Adding Users
    add_user('Ganesh')
    add_user('SRK')
    print('Users are:' , User,end="\n")
    # Adding Movies with year and Genre
    add_movie('Don', 2014,'Comedy')
    add_movie('KGF', 2020,'Action')
    add_movie('KGF2', 2022,'Action')
    print("Movies are:",Movie,end="\n")
    # Adding Reviews
    add_review('Ganesh', 'Don', 9)
    add_review('SRK', 'KGF', 10)
    add_review('Ganesh', 'KGF', 5)

    #get avg review for movie
    get_avg_review_of_movie("KGF")
    # get movie with greater review
    get_top_movies()
    # get movie with genre
    get_movies_of_genre('Action')



if __name__ == '__main__':
# Calling main function
    main()
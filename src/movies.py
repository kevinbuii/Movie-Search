# this file 'movies.py' will handle everything that has to do with titles
# the only function that will be in this file is the "search_for_movie" function

def search_for_movie(movies):
    # the goal of this function is to search titles hash table for a movie and return it if found
    if not (movies):
        print("please provide a proper movie hash table")
        return
    
    # takes a input from the command terminal and the strip() functions to remove any spaces
    movie_input = input("please enter movie name: ").strip().lower()

    # for every list in the movie buffer we set a currNode to search through the list
    for list in movies.buffer:
        currNode = list.head

        while currNode is not None:
            # set movie to the currNode data value
            movie = currNode.data.value
            
            # if the movie title is equal to the input then print and return, if not set currNode to next node
            if movie.title.lower() == movie_input:
                print(f"{movie.title} ({movie.year})")
                return
            currNode = currNode.next

    # only prints if movie not found
    print("movie not found")

# END OF movies.py
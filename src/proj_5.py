#!/usr/bin/env python
'''
Name: Kevin Bui
Email: kevinbui@temple.edu
Date: 4/25/2025

Usage: Type ./proj_5.py {1,2,3}
1: Search for Movie
2: Search for Actor
3: Search for Actor and all roles

'''
# this line is importing all of the functions and libraries
from parse import load_names, load_roles, load_titles
from actors import search_for_actor, search_for_roles
from movies import search_for_movie 

import sys

def main():
    # command line functions to see which search function to initiate
    if (len(sys.argv) != 2):
        print("valid usage: ./proj_5.py {1 (search for movie), 2 (search for actor), 3 (search for actor and all roles)}")
        sys.exit(1)

    user_input = sys.argv[1]

    if (user_input == "1"):
        titles = load_titles()
        search_for_movie(titles)
    elif (user_input == "2"):
        names = load_names()
        search_for_actor(names)
    elif (user_input == "3"):
        names = load_names()
        roles = load_roles()
        titles = load_titles()
        search_for_roles(names, roles, titles)
    else:
        print("please use proper input: {1,2,3}")

# begin main
if __name__ == "__main__":
    main()

# END OF proj_5.py
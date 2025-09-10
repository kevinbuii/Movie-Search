# this file 'actors.py' will contain everything that has to do with names and roles

def search_for_actor(names):
    # the goal of this function is to search names hash table for an actor and return it
    if not (names):
        print("please provide a proper names dictionary")
        return
    # takes a input from the command terminal and the strip() functions to remove any spaces
    name_input = input("please enter person's name: ").strip().lower()

    # this list and looping functions is the exact same as from search_for_movie from movies.py
    for list in names.buffer:
            currNode = list.head

            while currNode is not None:
                name = currNode.data.value

                if name.name.lower() == name_input:
                    year_died = name.yearDied if name.yearDied else "present"
                    print(f"{name.name} ({name.yearBorn} - {year_died})")
                    return
                currNode = currNode.next
    
    # only prints if movie not found
    print("person not found")

def search_for_roles(names, roles, titles):
    # we need all 3 hash tables to search for the roles someone has played 
    # names is keyed by name_id, from name_id we can find the roles/title_id b/c it's keyed by names_id
    # then w/ title_id we can find the movie name

    if not (names) or not (roles) or not (titles):
        print("error please provide the proper hash tables")
        return

    name_input = input("please enter person's name: ").strip().lower()

    # loop through names to find a matching id
    found_nameID = None

    # returns name_id and info for person, same search progress as above for the actor info
    for list in names.buffer:
        currNode = list.head

        while currNode is not None:
            name = currNode.data.value

            if name.name.lower() == name_input:
                found_nameID = name.name_id
                break

            currNode = currNode.next
            
    if not found_nameID:
        print("person not found")
        return

    # with the name_id we can find the roles they placed in roles
    # using the lookup function from the hash_table since the key is name_id
    roles_found = roles.lookup(found_nameID)

    if not roles_found:
        print("no roles found for person")
        return

    # now with the roles_found we can search through titles for the name of the movies by the title_id from roles and print them out
    found_starring_role = False

    for role in roles_found:
        if role.category in ["actor", "actress"]:
            title_found = titles.lookup(role.title_id)
            
            if title_found:
                # title_found[0] since when you use lookup this shows up ([<hash.titleInfo object at 0x7f3740b02ee0>]) and we only want the hash.titleInfo
                movie = title_found[0]
                # using join to connect the list as a string so i can print out the characters they've played for each movie
                characters = ", ".join(role.characters)
                print(f"- {movie.title} ({movie.year}) as {characters}")
                found_starring_role = True
    
    if not found_starring_role:
        print("no starring role found")

# END OF actors.py
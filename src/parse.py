# This file is used to parse the files 'names.tsv', 'roles.tsv', and 'titles.tsv'
# I will be storing all of the data into seperate hash tables for each function: names, roles, titles 
from hash import hash_table_names, hash_table_roles, hash_table_titles, nameInfo, roleInfo, titleInfo

def load_names():
    names = hash_table_names(array_len = 545183)
    try:
        with open("/data/courses/ece_3822/current/project_5_data/names.tsv", "r") as f_names:
            # since there is a header we'll skip first line
            next(f_names)
            for lines in f_names:
                # lines are tab seperated
                strip_lines = lines.strip()
                info = strip_lines.split('\t')
                # here info has been stripped of the new line and tab, so it becomes a list
                name_id, name, yearBorn, yearDied = info 

                # below checking if yearBorn or yearDied equals to '\N' or NULL if not set as an int if so set to None
                # python treats '\' literally so when printed it has TWO backslashes
                if (yearBorn != '\\N'):
                    yearBorn = int(yearBorn)
                else:
                    yearBorn = None
                
                if (yearDied != '\\N'):
                    yearDied = int(yearDied)
                else:
                    yearDied = None

                # now we create a nameInfo object to store the data
                nameVal = nameInfo(name_id, name, yearBorn, yearDied)

                # append nameVal to the hash table
                names.insert(nameVal)
    except:
        print("error could not open file\n")

    # end of load_names
    return names

def load_roles():
    roles = hash_table_roles(array_len = 870629)
    try:
        with open("/data/courses/ece_3822/current/project_5_data/roles.tsv", "r") as f_roles:
            # since there is a header we'll skip first line
            next(f_roles)
            for lines in f_roles:
                # lines are tab seperated
                strip_lines = lines.strip()
                info = strip_lines.split('\t')
                # info is stripped and becomes a list
                title_id, name_id, category, characters = info

                # we need a way to split up the characters since they are contained in []
                # else statements will just return an empty list
                if characters.startswith('[') and characters.endswith(']'):
                    # ill be using string splicing, got this from a quick Google search
                    chars = characters[1:-1]
                    # some of these characters also contain commas so we need to strip those
                    parse_char = []
                    for char in chars.split(','):
                        # strip twice to remove whitespace and then to remove parenthesis
                        parse_char.append(char.strip().strip('"'))
                else:
                    parse_char = []
                
                # create a roleInfo object to store
                roleVal = roleInfo(title_id, name_id, category, parse_char)

                roles.insert(roleVal)
    except:
        print("error could not open file\n")

    # end of load_roles
    return roles

def load_titles():
    titles = hash_table_titles(array_len = 109919)
    try:
        with open("/data/courses/ece_3822/current/project_5_data/titles.tsv", "r") as f_titles:
           # since there is a header we'll skip first line
            next(f_titles)
            for lines in f_titles:
                # lines are tab seperated
                strip_lines = lines.strip()
                info = strip_lines.split('\t')
                # info is stripped and becomes a list
                title_id, title, year, runtime, genre = info

                # since genre is split up by commas we'll have to split like in load_roles
                if "," in genre:
                    # create an empty list
                    parse_genre = []
                    for cat in genre.split(","):
                        # for every category split up by a comma, we strip whitespace then append it to parse_genre
                        parse_genre.append(cat.strip())
                else:
                    # if there is no comma create a list then append that genre to it
                    parse_genre = []
                    parse_genre.append(genre.strip())

                # below checking if year or runtime equals to '\N' or NULL if not set as an int if so set to None
                # python treats '\' literally so when printed it has TWO backslashes
                if (year != '\\N'):
                    year = int(year)
                else:
                    year = None

                if (runtime != '\\N'):
                    runtime = int(runtime)
                else:
                    runtime = None
                
                # create titlesInfo object
                titleVal = titleInfo(title_id, title, year, runtime, parse_genre)

                titles.insert(titleVal)
    except:
        print("error could not open file\n")
    
    # end of load_titles
    return titles

# END OF parse.py
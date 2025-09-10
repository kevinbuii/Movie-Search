# hash function class and linked list class for my data structure
# im copying the hash_table_base and linked_list from lab_05.py
class linked_list:
    '''standard linked list class'''

    # READ AND UNDERSTAND, BUT DO NOT EDIT THIS FUNCTION

    class node:
        def __init__(self,data=None,next=None):
            self.data = data
            self.next = next
    
    def __init__(self):
        self.head = None

    def insert(self,value):
        new_node = self.node(data=value,next=self.head)
        self.head = new_node

    def lookup(self,target=None,field=None,disp=False):
        curr_ptr = self.head
        ret_val = []

        while (curr_ptr is not None):
            if hasattr(curr_ptr.data,field) and \
                getattr(curr_ptr.data,field) == target:
                    ret_val.append(curr_ptr.data)
            curr_ptr = curr_ptr.next

        if disp and ret_val:
            for r in ret_val:
                r.display()
        elif disp and not ret_val:
            print(field, "=" , target, " not found")

        return ret_val

class hash_table_base:
    '''basic hash table designed to be inherited'''

    # READ AND UNDERSTAND, BUT DO NOT EDIT THIS FUNCTION

    class node:
        def __init__(self,k,v):
            self.key , self.value = k,v

    def __init__(self , array_len = 50):
        self.buffer = [linked_list() for _ in range(array_len)]
        self.array_len = array_len

    def insert(self,value):
        key = self.extract_key(value)
        index = self.hash_function(key)
        self.buffer[index].insert( self.node(key,value) )

    def lookup(self,key = None , disp=False):
        index = self.hash_function(key)
        retValTmp = self.buffer[index].lookup(target=key, field='key')
        retVal = [r.value for r in retValTmp]

        if disp:
            print("Search of " , key , " found:")
            if retVal:
                for v in retVal:
                    print("\t",end="")
                    print(v)
            else: print("\tNothing")
        return retVal
            
    # must be defined by the inheriting class
    def hash_function(self,key  ): return None   
    def extract_key  (self,value): return None

# now ill begin my three hash tables for names, roles, and titles
class hash_table_names (hash_table_base):
    def __init__ (self,array_len = 50):
        super().__init__(array_len)

    def extract_key (self, value):
        return value.name_id
    
    def hash_function (self, key):
        # reusing my hash function from lab 5
        s = 0
        # we also have to convert the 'id' to a string since they are inserted as ints
        key_str = str(key)
        for i, ch in enumerate(key_str):
            # the method here is to have 'i' and increment for each letter in the id. 
            # with it, it multiplies against ord(ch) this ensures "smith" /= "htims"
            s += (i + 1) * ord(ch)
        return s % self.array_len

class hash_table_roles (hash_table_base):
    def __init__ (self,array_len = 50):
        super().__init__(array_len)

    def extract_key (self, value):
        return value.name_id
    
    def hash_function (self, key):
        # reusing my hash function from lab 5
        s = 0
        # we also have to convert the 'id' to a string since they are inserted as ints
        key_str = str(key)
        for i, ch in enumerate(key_str):
            # the method here is to have 'i' and increment for each letter in the id. 
            # with it, it multiplies against ord(ch) this ensures "smith" /= "htims"
            s += (i + 1) * ord(ch)
        return s % self.array_len
    
class hash_table_titles (hash_table_base):
    def __init__ (self,array_len = 50):
        super().__init__(array_len)
    
    def extract_key (self, value):
        return value.title_id

    def hash_function (self, key):
        # reusing my hash function from lab 5
        s = 0
        # we also have to convert the 'id' to a string since they are inserted as ints
        key_str = str(key)
        for i, ch in enumerate(key_str):
            # the method here is to have 'i' and increment for each letter in the last name. 
            # with it, it multiplies against ord(ch) this ensures "smith" /= "htims"
            s += (i + 1) * ord(ch)
        return s % self.array_len

# we also need three classes to hold the information that gets parsed from the files
class nameInfo:
    def __init__ (self, name_id, name, yearBorn, yearDied):
        self.name_id = name_id
        self.name = name
        self.yearBorn = yearBorn
        self.yearDied = yearDied

class roleInfo:
    def __init__ (self, title_id, name_id, category, characters):
        self.title_id = title_id
        self.name_id = name_id
        self.category = category
        self.characters = characters

class titleInfo:
    def __init__ (self, title_id, title, year, runtime, genre):
        self.title_id = title_id
        self.title = title
        self.year = year
        self.runtime = runtime
        self.genre = genre
    
# END OF hash.py
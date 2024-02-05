""" CSC108 Assignment 3: Club Recommendations - Starter code."""
from typing import List, Tuple, Dict, TextIO


# Sample Data (Used by Doctring examples)

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
       'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}


# Helper functions
def convert_list_to_tuples(lst: List[str]) -> List[str]:
    """
    >>> convert_list_to_tuples(['Jesse Katsopolis', 'Danny R Tanner', 
    'Joey Gladstone','Rebecca Donaldson-Katsopolis'])
    [('Jesse', 'Katsopolis'), ('Danny R', 'Tanner'), ('Joey'
    """
    new_lst = []
    for i in lst:
        new_lst.append(convert_name(i))
        
    return new_lst

def convert_name(name: str) -> Tuple[str, str]:
    """
    >>> convert_name("Kimmy Raikonnen")
    ('Raikonnen', 'Kimmy')
    """
    i = len(name) - 1
    
    while i >= 0 and name[i] != ' ':
        i -= 1
    
    first_name = name[:i]
    last_name = name[i + 1:]
    
    return (last_name, first_name)


def clubs_person_in(person_to_clubs: Dict[str, List[str]], person: str) -> \
    List[str]:
    """Return list of clubs person in (returns empty list if not in any clubs).
    >>> clubs_person_in(P2C, 'Jesse Katsopolis')
    ['Parent Council', 'Rock N Rollers']
    >>> clubs_person_in(P2C, 'Rebecca Donaldson-Katsopolis')
    []
    """
    all_clubs = []
                
    if person in person_to_clubs:
        all_clubs.extend(person_to_clubs[person])
    
    return all_clubs
    
def clubs_person_not_in(person_to_clubs: Dict[str, List[str]], person: str) -> \
    List[str]:
    """Return list of clubs person not in (returns empty list if in all clubs).
    >>> clubs_person_not_in(P2C, 'Jesse Katsopolis')
    ['Comet Club', 'Smash Club', 'Comics R Us'']
    >>> clubs_person_not_in(P2C, 'Rebecca Donaldson-Katsopolis')
    ['Comet Club', 'Parent Council', 'Rock N Rollers', 'Smash Club', 
    'Comics R Us']
    """
    all_clubs = []
    t = invert_and_sort(person_to_clubs)
    
    for club in t:
        all_clubs.append(club)
        
    clubs_p_in = clubs_person_in(person_to_clubs, person)
    
    clubs_p_not_in = []
    
    for club in all_clubs:
        if club not in clubs_p_in:
            clubs_p_not_in.append(club)
            
    return clubs_p_not_in

def create_clubs(contents: List[str]) -> List[str]:
    """
    >>> create_clubs(['Dunphy, Claire', 'Parent Teacher Association', 
    'Big Boy Bouncer', 'Dunphy, Phil', 'Pritchett, Mitchell', 'Pritchett, Jay'])
    ['Parent Teacher Association', 'Big Boy Bouncer']
    """
    clubs_indices = []
    for i in range(1, len(contents)):
        if not has_comma(contents[i]):
            clubs_indices.append(i)
    
    clubs = []
    for j in clubs_indices:
        clubs.append(contents[j].strip())
        
    return clubs

def create_name(line: str) -> str:
    """ Return name in line written in the format 'last_name, first_name' to
    new format 'first_name last_name'.
    >>> create_name("Prichett, Jay")
    'Jay Prichett'
    """
    i = 0
    
    while i < len(line) and line[i] != ',':
        i += 1
    
    last_name = line[:i]
    
    i += 1
    
    first_name = line[i:].strip()
        
    return first_name + ' ' + last_name

def create_friends(contents: List[str]) -> List[str]:
    """
    >>> create_friends(['Pritchett, Jay', 'Pritchett, Gloria', 'Delgado, Manny',
    'Dunphy, Claire'])
    ['Gloria Pritchett', 'Manny Delgado', 'Claire Dunphy']
    """
    friends_indices = []
    for i in range(1, len(contents)):
        if has_comma(contents[i]):
            friends_indices.append(i)
    
    friends = []
    for j in friends_indices:
        friends.append(create_name(contents[j]))
        
    return friends

def find_all_possible_values(key_to_value: Dict[object, object]) -> List[object]:
    lst = []
    for i in key_to_value:
        x = key_to_value[i]
        if type(x) == list:
            lst.extend(x)
        else:
            lst.append(x)
            
    # Now remove duplicates:
    new_lst = []
    for l in lst:
        if not (l in new_lst):
            new_lst.append(l)
          
    return new_lst

def friend_count(club: str, person: str, person_to_clubs: Dict[str, List[str]], \
                 p_friends: List[str]) -> int:
    
    count = 0
    
    inverted_person_to_clubs = invert_and_sort(person_to_clubs)
    
    for friend in p_friends:
        if friend in inverted_person_to_clubs[club]:
            count += 1
            
    return count

def friends_of_person(person_to_friends: List[List[str]], person: str) -> \
    List[str]:
    lst_of_friends = []
    
    if person in person_to_friends:
        lst_of_friends.extend(person_to_friends[person])
    
    return lst_of_friends

def has_comma(line: str) -> bool:
    """ Returns true iff line of file has does not have a comma in it.
    """
    return ',' in line

def shared_dude_count(club: str, person_to_clubs: Dict[str, List[str]], \
                      shared_dude_list: List[str]) -> int:
    """
    >>> shared_dude_list = shared_dude_list(P2C, 'Jesse Katsopolis')
    >>> shared_dude_count('Comics R Us', P2C, shared_dude_list)
    
    """
    inverted_person_to_clubs = invert_and_sort(person_to_clubs)
    count = 0
    
    for dude in shared_dude_list:
        if dude in inverted_person_to_clubs[club]:
            count += 1
    
    return count
    
def shared_dude_list(person_to_clubs: Dict[str, List[str]], person: str) -> \
    List[str]:
    clubs_p_in = clubs_person_in(person_to_clubs, person)
    
    inverted_person_to_clubs = invert_and_sort(person_to_clubs)
    
    list_of_dudes = []
    
    for club in clubs_p_in:
        for man in inverted_person_to_clubs[club]:
            if man != person and man not in list_of_dudes:
                list_of_dudes.append(man)
        
    return list_of_dudes

def sorting_process(mega_list: List[List[object]]) -> List[List[object]]:
    
    # remove entires with 0
    new_list = []
    for lst in mega_list:
        if lst[0] != 0:
            new_list.append(lst)
            
    # sort list
    new_list.sort(reverse = True)
    return new_list

def update_dict(key: str, value: str,
                key_to_values: Dict[str, List[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """

    if key not in key_to_values:
        key_to_values[key] = []

    if value not in key_to_values[key]:
        key_to_values[key].append(value)

# Required functions

def load_profiles(profiles_file: TextIO) -> Tuple[Dict[str, List[str]],
                                                  Dict[str, List[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from
    profiles_file. The values in the two dictionaries are sorted in
    alphabetical order.

    NOTE: Functions (including helper functions) that have a parameter of type
          TextIO do not need docstring examples.

    """
    person_to_friends_d = {}
    person_to_clubs_d = {}
    
    doc = profiles_file.readlines()
    
    i = 0
    f = 0
    
    while f < len(doc):
        
        while f < len(doc) and doc[f] != '\n':
            f += 1
            
        contents = doc[i:f]
        
        if len(create_friends(contents)) != 0:
            person_to_friends_d[create_name(contents[0].strip())] = \
                create_friends(contents)
            person_to_friends_d[create_name(contents[0].strip())].sort()
        
        if len(create_clubs(contents)) != 0:
            person_to_clubs_d[create_name(contents[0].strip())] = \
                create_clubs(contents)
            person_to_clubs_d[create_name(contents[0].strip())].sort()
        f += 1
        i = f 
        
    return (person_to_friends_d, person_to_clubs_d)


def get_average_club_count(person_to_clubs: Dict[str, List[str]]) -> float:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to.

    >>> get_average_club_count(P2C)
    1.6
    """
    sum_of_clubs = 0
    keys = person_to_clubs.keys()
    
    for k in keys:
        sum_of_clubs += len(person_to_clubs[k])
        
    if len(person_to_clubs) == 0:
        return 0.0
    else:
        return sum_of_clubs / len(person_to_clubs)


def get_last_to_first(
        person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first name(s)" dictionary with the people from the
    "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True
    """
    # A:first put the names out into a list
    # convert all names into tuple (last_name, first_name) format and keep it in
    #    the list (call this tuples_lst)
    # create list of last names
    # parse through tuples_lst using last names: for every tuple with the same 
    #    last_name, add that value to a list
    # append that list to a dictionary
    
    # A:
    lst = []
    for x in person_to_friends:
        if not (x in lst): 
            lst.append(x)
        for y in person_to_friends[x]:
            if not (y in lst):
                lst.append(y)
                
    # B:
    tuples_lst = convert_list_to_tuples(lst)
    
    # C:
    list_of_last_names = []
    for i in tuples_lst:
        if not (i[0] in list_of_last_names):
            list_of_last_names.append(i[0])
        
    # Di:
    mega_lst = []
    for r in range(len(list_of_last_names)):
        mega_lst.append([])
    
    # Dii
    for r in range(len(list_of_last_names)):
        for i in tuples_lst:
            if i[0] == list_of_last_names[r]:
                mega_lst[r].append(i[1])
        
    # E
    d = {}
    
    for r in range(len(list_of_last_names)):
        d[list_of_last_names[r]] = mega_lst[r]
        d[list_of_last_names[r]].sort()
    
        
    return d

def invert_and_sort(key_to_value: Dict[object, object]) -> Dict[object, list]:
    """Return key_to_value inverted so that each key is a value (for
    non-list values) or an item from an iterable value, and each value
    is a list of the corresponding keys from key_to_value.  The value
    lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True
    """
    # A: find all the possible values of the key_to_value dict & put them in lst 
    # B: convert all key-value pairs to pair tuples ie. 'PC': 
    #    ['drt', 'jk'] -> ('PC", 'drt'), ('PC', 'jk').  
    #    Place these tuples in a list (call it lst_of_tuples)
    # C: create mega_lst with len(lst) elements that are each []
    # D: for each value in lst, if one of the tuples' 2nd coordinate is the same
    #    as value, then adjoin it to the mega_list
    # E: make the dictionary
    
    # A
    lst = find_all_possible_values(key_to_value)
    
    # B
    lst_of_tuples = []
    for i in key_to_value:
        if type(key_to_value[i]) == list: 
            for j in range(len(key_to_value[i])):
                lst_of_tuples.append((i,key_to_value[i][j]))
        else:
            lst_of_tuples.append((i, key_to_value[i]))
            
    # C
    mega_lst = []
    for r in range(len(lst)):
        mega_lst.append([])
        
    # D
    for r in range(len(lst)):
        for tuples in lst_of_tuples:
            if tuples[1] == lst[r]:
                mega_lst[r].append(tuples[0])
                    
    # E
    d = {}
    for r in range(len(lst)):
        d[lst[r]] = mega_lst[r]
        d[lst[r]].sort()
        
    return d

def get_clubs_of_friends(person_to_friends: Dict[str, List[str]],
                         person_to_clubs: Dict[str, List[str]],
                         person: str) -> List[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']
    """   
    # A: find the Dude's friends using person_to_friends
    # b: find the friends clubs by making a list for each.  Then adjoin all the
    #    lists together. call this the collection
    # c: find the Dude's clubs so we know which ones to ignore
    # d: remove clubs from collection and sort
    
    # A
    friends = person_to_friends[person]
    
    # B
    lst_of_clubs = []
    for friend in friends:
        if friend in person_to_clubs:
            lst_of_clubs.extend(person_to_clubs[friend])
        
    # C
    remove_these_clubs = person_to_clubs[person]
    
    # D
    for x in lst_of_clubs:
        if x in remove_these_clubs:
            lst_of_clubs.remove(x)
            
    lst_of_clubs.sort()
            
    return lst_of_clubs


def recommend_clubs(
        person_to_friends: Dict[str, List[str]],
        person_to_clubs: Dict[str, List[str]],
        person: str) -> List[Tuple[str, int]]:
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner')
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]
    """    
    # creates list of clubs person in
    clubs_p_in = clubs_person_in(person_to_clubs, person)
    
    # creates list of clubs the person is not in
    clubs_p_not_in = clubs_person_not_in(person_to_clubs, person)
    
    # get person's friend
    p_friends = friends_of_person(person_to_friends, person)
    
    # create mega list
    mega_list = []
    
    for i in range(len(clubs_p_not_in)):
        mega_list.append([0, clubs_p_not_in[i]])
        # appends the necessary number of clubs the person is not in so we can
        # give a recommendation score; this mega_list will be shortened later
        
    # create shared_dude_list
    shared_dude_list1 = shared_dude_list(person_to_clubs, person)
    
    # append scores to 2nd index of each element of mega_list
    for i in range(len(clubs_p_not_in)):
        if person in person_to_friends:
            mega_list[i][0] += friend_count(clubs_p_not_in[i], person, \
                                            person_to_clubs, p_friends)
        if person in person_to_clubs:
            mega_list[i][0] +=shared_dude_count(\
                clubs_p_not_in[i], person_to_clubs, shared_dude_list1)
        
    # now sorting process
    new_mega_list = sorting_process(mega_list)
    
    # now create tuples
    lst_of_tuples = []
    for lst in new_mega_list:
        lst_of_tuples.append((lst[1], lst[0]))
    
    lst_of_tuples.sort()
    
    return lst_of_tuples
   

   
if __name__ == '__main__':
    pass
    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod()

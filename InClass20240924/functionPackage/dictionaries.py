# dictionaries.py
# This was really fun and I will treasure this time together
# with my peers.




def demo():
    '''
    Demonstrate basic dictionary stuff
    '''
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
    
    # Iterate over the dictionary by key
    for key in myDictionary.keys():
        print(key)
        
    # Iterate by key/value
    for item in myDictionary.items():
        print(item)
        
    # Iterate by value
    for value in myDictionary.values():
        print(value)
        
    # Add a key/value pair to the dictionary
    myDictionary["Michigan State"] = "Spartans"
    
    print(len(myDictionary))
    
    # Cause an exception. Add try / except logic to
    # gracefully handle this
    
    try:    
     print(myDictionary["Ohio State"])
    except:
       print("Ohio State is an invalid key")
       
    # Remove Xavier by key and print the entire dictionary
    myDictionary.pop("Xavier")   
    print(myDictionary)
    
    # Create another dictionary called newTeams.
    # Add several key/value pairs
    # Combine that with myDictionary and print the results
    newTeams = {"Ohio State":"Buckeyes","Kentucky":"Wildcats","Michigan":"Wolverines", "Indiana":"Hoosiers"}
    myDictionary.update(newTeams)
    print(myDictionary)
    
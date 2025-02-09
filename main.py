def sort_on(dict):
    return dict["num"]



def count_characthers():
    with open("./books/frankenstein.txt") as f:
            file_contents = f.read()
            print(file_contents) # this reads the file
            words = file_contents.split() #converts the string into seprate list values
            print(len(words))  #counts the list
            word = file_contents.lower() #lowercases the string

            d = {} #initialize empty dictionary
            for i in word:          #loops the dictionary counting the values of characthers
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            
            r = []
            
            for char, count in d.items(): #this loops in the dictionary
                 if char.isalpha():  #ensures only alphabetical chars are counted
                      r.append({"char": char, "num": count}) #assigns them values
            r.sort(reverse=True, key=sort_on)
            for i in r:
                 charachters = i["char"]
                 counts = i["num"]
                 print(f"The \'{charachters}\' character was found {counts} times")

                
                         


count_characthers()


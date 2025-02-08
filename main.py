
def main():

    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def wordcount():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))

def count_characthers():
    with open("./books/frankenstein.txt") as f:
            file_contents = f.read()
            words = file_contents.lower()
            d = {}
            for i in words:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            print(d)


main()
wordcount()
count_characthers()


def main():
    book = "books/frankenstein.txt"

    with open(book) as f:
        file_contents = f.read()

    #print(get_word_count(file_contents))
    #print(get_letter_count(file_contents))

    report(file_contents)

def get_letter_count(book):
    words = book.split()

    counts = {}
    for word in words:
        for char in word:
            char = char.lower()
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1

    return counts

def get_word_count(book):
    words = book.split()
    return f"There are {len(words)} words the book"

def report(file_contents):
    print("=======  This is a report  =======")
    print (f"There are {get_word_count(file_contents)} words the book")

    letters = get_letter_count(file_contents)
    letters_dict = []

    for key,value in letters.items():
        letters_dict.append({"name":key, "num":value})
    
    def sort_on(dict):
        return dict["num"]
    
    letters_dict.sort(reverse=True, key=sort_on)

    for dict in letters_dict:
        if str(dict['name']).isalpha:
            print(f"The char {dict['name']} was found {dict['num']} times")

    print("======  end  ======")

main()
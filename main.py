def __main__():
        path="books/frankenstein.txt"
        contents=get_text(path)
        #print(contents)
        print(f"--- Begin report of {path} ---")
        print(f"This text has {count_words(contents)}.")
        counted_chars=list_sort_dict(count_chars(contents))
        #print(counted_chars)
        for char in counted_chars:
            print(f"The '{char["char"]}' character was found {char["num"]} times.")
        print("--- End report ---")
        
def sort_on(dict):
    return dict["num"]
    
def list_sort_dict(dict):
    list=[]
    for item in dict:
        list.append({"char":item,"num":dict[item]})
    list.sort(reverse=True,key=sort_on)
    return list
def count_words(text):
    return len(text.split())

def count_chars(text):
    char_counter={}
    for char in text.upper():
        if not char.isalpha():
            continue
        if char not in char_counter:
            char_counter[char]=0
        char_counter[char]+=1
    return char_counter

def get_text(path):
    with open(path) as f:
        return f.read()
__main__()
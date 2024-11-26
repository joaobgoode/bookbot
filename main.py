def main():
    url = "books/frankenstein.txt"
    with open("./" + url) as f:
        print(f"--- Begin report of {url} ---")
        file_contents = f.read()
        charmap = dict()
        for char in file_contents:
            if char.isalpha():
                charmap[char.lower()] = charmap.get(char.lower(), 0) + 1
        for char in charmap:
            print(f"The {char} character was found {charmap[char]} times")
        print("--- End report ---")
if __name__ == "__main__":
    main()

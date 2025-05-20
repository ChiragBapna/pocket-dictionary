"# pocket-dictionary" 
def show_menu():
    print("\n=== Pocket Dictionary ===")
    print("1. Add Word")
    print("2. Search Word")
    print("3. Delete Word")
    print("4. Display All Words")
    print("5. Exit")

def add_word(dictionary):
    word = input("Enter word: ").strip().lower()
    if word in dictionary:
        print("Word already exists.")
    else:
        meaning = input("Enter meaning: ").strip()
        dictionary[word] = meaning
        print(f"'{word}' added successfully.")

def search_word(dictionary):
    word = input("Enter word to search: ").strip().lower()
    if word in dictionary:
        print(f"{word} : {dictionary[word]}")
    else:
        print("Word not found.")

def delete_word(dictionary):
    word = input("Enter word to delete: ").strip().lower()
    if word in dictionary:
        del dictionary[word]
        print(f"'{word}' deleted successfully.")
    else:
        print("Word not found.")

def display_all(dictionary):
    if not dictionary:
        print("Dictionary is empty.")
    else:
        print("\n--- All Words ---")
        for word, meaning in sorted(dictionary.it  
                                    ems()):
            print(f"{word} : {meaning}")

def main():
    pocket_dict = {}

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_word(pocket_dict)
        elif choice == '2':
            search_word(pocket_dict)
        elif choice == '3':
            delete_word(pocket_dict)
        elif choice == '4':
            display_all(pocket_dict)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

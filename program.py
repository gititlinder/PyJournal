import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print("--------------------")
    print("    Journal App")
    print("--------------------")
    pass


def run_event_loop():
    print("What do you want to do with your journal")

    cmd = 'EMPTY'
    journal_name = "default"
    journal_data = journal.load(journal_name)

    while cmd != 'X' and cmd:
        cmd = input("[L]ist entries, [A]dd, [D]elete, or e[X]it: ")

        cmd = cmd.upper().strip()

        if cmd == 'L':
            list_entries(journal_data)
        elif cmd == 'A':
            add_entry(journal_data)
        elif cmd == 'D':
            delete_entry(journal_data)
        elif cmd != 'X' and cmd:
            print("Try Again")

    print("Goodbye!")
    journal.save(journal_name, journal_data)


def list_entries(data):
    print("Journal Entries")
    entries = data
    for idx, entry in enumerate(entries):
        print("{}. {}".format(idx, entry))


def add_entry(data):
    text = input("Type your entry, <enter> to exit: ")
    journal.add_entry(text, data)


def delete_entry(data):
    list_entries(data)
    number = input("Enter number to delete")
    journal.delete_entry(number, data)
    list_entries(data)

if __name__ == '__main__':
    main()

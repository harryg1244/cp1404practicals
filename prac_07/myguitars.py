import csv

from guitar import Guitar


def main():
    """main function to manage guitar data"""
    guitars = load_guitars("guitars.csv")
    display_guitars(guitars)
    add_new_guitars(guitars)
    save_guitars("guitars.csv", guitars)

    # Sort guitars objects by year and print
    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)


def load_guitars(filename):
    """Load guitars from guitars.csv and return list of guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row[0], int(row[1]), float(row[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display all guitars in list"""
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    """user input to add new guitars"""
    print("\nEnter new guitars (leave name blank to finish):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")


def save_guitars(filename, guitars):
    """Save user input to guitars.csv"""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()

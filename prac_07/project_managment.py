import csv
from datetime import datetime
from project import Project

FILENAME = "projects.txt"


def main():
    projects = load_projects(FILENAME)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {FILENAME}")
    menu = """
    - (L)oad projects  
    - (S)ave projects   
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
    """

    choice = ""
    while choice.lower() != 'q':
        print(menu)
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)

    if input(f"Would you like to save to {FILENAME}? (y/n): ").lower() == 'y':
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from projects.txt return list of Project objects"""
    projects = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip header
        for row in reader:
            projects.append(Project(*row))
    return projects


def save_projects(filename, projects):
    """Save all projects to file"""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow(
                [project.name, project.start_date.strftime("%d/%m/%Y"), project.priority, project.cost_estimate,
                 project.completion_percentage])


def display_projects(projects):
    """display incomplete and completed projects, sorted by priority"""
    incomplete_projects = sorted([p for p in projects if not p.is_completed()])
    completed_projects = sorted([p for p in projects if p.is_completed()])

    print("\nIncomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and Display projects starting after a specified date"""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_str, "%d/%m/%Y").date()

    filtered_projects = sorted([p for p in projects if p.start_date > filter_date], key=lambda x: x.start_date)
    for project in filtered_projects:
        print(project)


def add_project(projects):
    """user input to add new project to list"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    print("Project added successfully.")


def update_project(projects):
    """Update completion percentage or priority of project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    print(f"Selected project: {project}")

    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")

    project.update(
        new_percentage=int(new_percentage) if new_percentage else None,
        new_priority=int(new_priority) if new_priority else None
    )
    print("Project updated successfully.")


if __name__ == "__main__":
    main()
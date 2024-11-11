from datetime import datetime


class Guitar:
    """Represent a Guitar object with name, year, and cost"""

    def __init__(self, name="", year=0, cost=0):
        """Initialize Guitar Instance with name, year, and cost"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string of guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate and return age of guitar based on the current year."""
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage, else False."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Define the < operator for sorting by year."""
        return self.year < other.year

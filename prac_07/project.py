"""Time Estimate to complete Project Management Program
Estimated= 90 minutes
Actual= 120 minutes
"""
from datetime import datetime


class Project:
    """Class project: attributes for name, start date, priority, cost, completion
    percentage"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize instance with name, start date, priority, cost, and
        completion percentage."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return string of the project"""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def is_completed(self):
        """Check if the project is completed"""
        return self.completion_percentage == 100

    def __lt__(self, other):
        """Define < operator for sorting projects by priority."""
        return self.priority < other.priority

    def update(self, new_percentage=None, new_priority=None):
        """Update completion percentage and/or priority of the project."""
        if new_percentage is not None:
            self.completion_percentage = int(new_percentage)
        if new_priority is not None:
            self.priority = int(new_priority)
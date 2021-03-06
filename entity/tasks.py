class Tasks:

    def __init__(self, id=None, name=None, category=None, owners=tuple(), status=None,
                 minutes=None, days=tuple(), description=None):
        self.id = id
        self.name = name
        self.category = category #how to chose from existing categories?
        self.owners = owners # how to chose from the existing users?
        self.status = status # chose from a list?
        self.minutes = minutes
        self.days = days # data chose from calendar?
        self.description = description

    def __str__(self):
        return f"| {self.id:>12.12s} | {self.name:<15.15s} | {self.category:<10.10s} | " \
               f"{', '.join(self.owners):<10.10s} | " \
               f"{self.status:<10.10s} | {self.minutes:<2d} min | " \
               f"{(', '.join(self.days)):<35.35s} | {self.description:<50.50s} |"
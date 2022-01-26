
class Rewards:
	def __init__(self, id=None, name=None, category=None, owners=tuple(), description=None):
		self.id = id
		self.name = name
		self.category = category
		self.owners = owners
		self.description = description

	def __str__(self):

		return 	f"| {self.name:<12.12}  | {self.category:<15.15} | " \
		  		f"{', '.join(self.owners):<20.20} | " \
		   		f"{self.description:<50.50} |"

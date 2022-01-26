from entity.tasks import Tasks


class Bonus(Tasks):

	def __init__(self,id=None task, reward):
		self.id = id
		self.task = task
		self.reward = reward

	def __str__(self):
		return f"| {self.task.name:<20.20} | {self.task.category:<15.15} | {self.task.minutes:<2d} min | {self.reward:<10.10} |"


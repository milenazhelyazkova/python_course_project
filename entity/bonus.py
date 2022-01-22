from entity.tasks import Tasks


class Bonus(Tasks):
	def __init__(self, task, reward):
		super().__init__()
		self.task = task
		self.reward = reward

	def __str__(self):
		return f"| {self.task.name:<20.20} | {self.task.category:<15.15} | {self.task.minutes:<2d} min | {self.reward:<10.10} |"
		#return f"| {self.task.id:>12.12s} | {self.task.name:<15.15s} | {self.task.category:<10.10s} | " \
			#   f" {self.task.minutes:<2d} | {self.task.description:<50.50s} | {self.reward:<15.15s} | "

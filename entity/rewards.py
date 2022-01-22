from entity.tasks import Tasks


class Rewards(Tasks):
	def __init__(self, reward):
		super().__init__()
		self.reward = reward


	def __str__(self):

		return 	f"| {self.reward.name:<12.12}  | {self.reward.category:<15.15} | " \
		  		f"{', '.join(self.reward.owners):<20.20} | " \
		   		f"{self.reward.description:<50.50} |"

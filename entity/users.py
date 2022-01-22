class Users:
	def __init__(self, name, age, rewards=tuple(), tasks_owned=tuple()):
		self.name = name
		self.age = age
		self.my_rewards = rewards
		self.my_tasks = tasks_owned
	def __str__(self):
		return f"| {self.name:<10.10} | {self.age:<2d} years | {(', '.join(self.my_rewards)):<50.50} | {(', '.join(self.my_tasks)):<50.50} | "
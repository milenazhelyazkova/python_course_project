from entity.user import User


class Kid(User):
	def __init__(self, id=None, first_name=None, last_name=None, pwd=None, user_name=None, age=None, rewards=tuple(),
				 tasks_owned=tuple(), my_minutes=0):
		super().__init__(id, first_name, last_name, pwd, user_name)
		self.age = age
		self.my_rewards = rewards
		self.my_tasks = tasks_owned
		self.my_minutes = my_minutes


	def __str__(self):
		return f'| {self.user_name:<10.10} | {self.age} years | {self.my_minutes} minutes| {(", ".join(self.my_rewards)):<50.50} | {(", ".join(self.my_tasks)):<50.50} | '

	def display_my_tasks(self):
		pass  # use repository?

	def display_bonus_tasks(self):
		pass  # use repository?

	def chose_task(self):
		pass  # use repository?

	def end_task(self):
		pass  # change status

	def display_my_rawards(self):
		pass  # use repository?

	def count_minutes(self):
		# for task in self.my_tasks:
		pass  # if task.status=="completed"

	#   self.my_minutes += task.minutes
	# if  self.my_minutes >=60:
	#   self.earn_reward()
	def earn_raward(self):
		pass
#
# self.my_reward.append(reward.chose())
# self.my_minutes -= 60

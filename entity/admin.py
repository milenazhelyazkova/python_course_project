from entity.user import User


class Admin(User):

	def __init__(self, id=None, first_name=None, last_name=None, pwd=None, user_name=None):
		super().__init__(id, first_name=None, last_name=None, pwd=None, user_name=None)

	def display_users(self):
		pass # use repository?
	def display_tasks(self):
		pass# use repository?
	def display_bonuses(self):
		pass# use repository?
	def display_rewards(self):
		pass# use repository?
	def chose_user(self):
		pass# use repository?
	def chose_task(self):
		pass# use repository?
	def chose_bonus(self):
		pass# use repository?
	def chose_reward(self):
		pass# use repository?
	def create_user(self):
		pass# use repository?
	def edit_user(self):
		pass
	def delete_user(self):
		pass# use repository?
	def create_task(self):
		pass# use repository?
	def edit_task(self):
		pass
	def delete_task(self):
		pass# use repository?
	def create_reward(self):
		pass# use repository?
	def edit_reward(self):
		pass
	def delete_reward(self):
		pass# use repository?

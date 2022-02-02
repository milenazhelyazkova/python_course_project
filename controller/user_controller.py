from dao.user_repository import UserRepository
from entity.user import User


class UserController:
	def __init__(self, user_repo: UserRepository):
		self._user_repo = user_repo

	def add_user(self, user: User):
		users_list = self._user_repo.find_all()
		names = []
		for u in users_list:
			names.append(u.user_name)
		if user.user_name not in names:
			self._user_repo.create(user)

	def get_all_users(self):
		return self._user_repo.find_all()



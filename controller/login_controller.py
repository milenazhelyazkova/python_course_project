from dao.user_repository import UserRepository
from entity.user import User


class LoginController:
	def __init__(self, user_repo: UserRepository):
		self._user_repo = user_repo
		#self.users = {}  # do i need this?


	def register(self, user:User):
		""""allows to register a new user by providing all required user data as arguments"""
		# check if user_name is not existing
		users_list = self._user_repo.find_all()
		names = []
		for u in users_list:
			names.append(u.user_name)
			print(names)
		if user.user_name not in names:
			self._user_repo.create(user)
			print(f"A new user {user.user_name} is registered")
		else:
			print("A user with this user_name already exists")

	# return self.users

	def login(self, name, password):
		""" allows a registered user to login in the system by providing a valid username and password (credentials). \
		If the provided credentials are not valid an InvalidUsernameOrPasswordException is raised by login method. \
		If credentials are valid returns the logged User."""

	def logout(self):
		""""allows to logout the currently logged user"""
		current_user=self.get_logged_user()
		if current_user:
			pass

	def get_logged_user(self):
		""""returns the currently logged user if there is such, or None otherwise."""

	def get_all_users(self):
		"""returns all registered users"""
		return self._user_repo.find_all()

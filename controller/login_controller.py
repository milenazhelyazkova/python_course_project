from dao.user_repository import UserRepository
from entity.admin import Admin
from entity.user import Users


class LoginController:
	def __init__(self, user_repo: UserRepository):
		self._user_repo = user_repo
		#self.users = {}  # do i need this?

	def register(self):
		""""allows to register a new user by providing all required user data as arguments"""
		new_user = Admin(id=None, name="Milena", psw="AzSamMilena")
		# check if name is not existing user
		if not self._user_repo.find_by_user_name(new_user.name):
			# self.users = self._user_repo.create(new_user)
			self._user_repo.create(new_user)
		else:
			print("A user with this name already exists")

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

from dao.repository import Repository
from entity.user import User


class UserRepository(Repository):
	def find_by_user_name(self, user_name) -> list[User]:
		user_name_lower = user_name.lower()
		names_list = self.find_all()
		result = [user for user in names_list if user_name_lower in user.user_name.lower()]
		return result

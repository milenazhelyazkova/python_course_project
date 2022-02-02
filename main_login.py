from dao.user_repository import UserRepository
from controller.login_controller import LoginController
from entity.user import User

if __name__ == '__main__':
    users_repo = UserRepository()
    login_controller = LoginController(users_repo)

    # users_list = users_repo.find_all()
    # user_pass = {}
    # name = input("Enter user name: ")
    # if name not in users_list:
    # 	password = input("Enter password: ")
ans = True
while ans:
    print("""
        1.Register
        2.Login
        3.Logout
        4. See Current User
        5.Exit/Quit
        """)
    ans = input("Enter your choice: ")
    if ans == "1":
        # allowing to register a new user by entering user data from console with validation
        # login_controller.register()
        #print("\nUser Registered")
        print("Enter user first_name")
        first_name = input()
        print("Enter user last_name")
        last_name = input()
        print("Enter user password")
        pwd = input()
        print("Enter user user_name")
        user_name = input()
        new_user = User(first_name=first_name, last_name=last_name, pwd=pwd, user_name=user_name)
        users_repo = UserRepository()
        login_controller = LoginController(users_repo)
        login_controller.register(new_user)

    elif ans == "2":
        # asking for username and password as console input, \
        # and calling the login(username, password) method of LoginController class singleton instance. \
        # In case of successful login the demo should salute the logged user by name. \
        # In case of InvalidUsernameOrPasswordException an error message should be printed to console, \
        # and the user should be asked to enter the credentials again.
        user = input("Your name: ")
        pwd = input("Your password: ")
        # 	try:
        # 		user_logged = login_controller.login(user,pwd)
        # 		print(f"Welcome, {user}")
        # 	except:
        # 		print("Please try again")
        print("\n Useg Loged in")
    elif ans == "3":
        # calling the logout() method of LoginController class.
        login_controller.logout()
        print("\n User Loged out")
    elif ans == "4":
        # should print the currently logged User data, by calling
        login_controller.get_logged_user()
        print("\n Current user is:")
    elif ans == "5":
        print("\n Goodbye")
        ans = None
    else:
        print("\n Not Valid Choice Try again")

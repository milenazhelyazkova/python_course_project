from controller.user_controller import UserController
from dao.repository import Repository
from dao.user_repository import UserRepository
from entity.bonus import Bonus
from entity.rewards import Rewards
from entity.tasks import Tasks
from entity.user import User

if __name__ == '__main__':
    t1 = Tasks(None, "clean bed", "morning", ("Nikol", "Iva"), "assigned", 5, ('23.01', '24.01'),
               "do the sheets and pijamas")
    t2 = Tasks(None, "breakfast", "morning", ("Nikol", "Iva"), "assigned", 15,
               ('20.01', '21.01', '22.01', '23.01', '24.01'), "eat your food fast")
    t3 = Tasks(None, "dress up", "morning", ("Nikol", "Iva"), "assigned", 10, ('24.01',),
               "chose clothes and put them on fast")
    t4 = Tasks(id=None, name="organize clothes", category="clothes", minutes=30, description="in the wardrobe")
    t5 = Tasks(id=None, name="clean kitchen floor",category="kitchen", minutes=15, description="clean with mop")
    t6 = Tasks(id=None, name="wash dishes", category="kitchen", minutes=15, description="in the sink")

    r1 = Rewards(id=None, name="party", category="entertainment",owners= ("bonus1",), description="in the wardrobe")
    r2 = Rewards(id=None, name="sweet", category="food", owners=("bonus2",), description="only one")
    r3 = Rewards(id=None, name="movie", category="entertainment", description="on cinema")
    tasks = (t1, t2, t3)

    tasks_repo = Repository()
    for task in tasks:
        tasks_repo.create(task)
    print("\n...TASKS...\n")
    for task in tasks_repo.find_all():
        print(task)

    b1 = Bonus(None,t4, "party")
    b2 = Bonus(None,t5, "sweets")
    b3 = Bonus(None,t6, "movie")

    bonus_tasks = (b1, b2, b3)
    bonus_repo = Repository()

    for bonus in bonus_tasks:
        bonus_repo.create(bonus)
    print("\n...BONUS AND REWRDS...\n")
    for bonus in bonus_repo.find_all():
        print(bonus)

    print("\n...REWARDS...\n")

    rewards = (r1, r2, r3)

    rewards_repo = Repository()
    for reward in rewards:
        rewards_repo.create(reward)

    for reward in rewards_repo.find_all():
        print(reward)

    u1 = User(id=None, user_name="Nikol", age=7, my_minutes=0)
    u2 = User(id=None, user_name="Iva", age=3, my_minutes=0)

    users = (u1, u2)
    users_repo = UserRepository()

    for user in users:
        users_repo.create(user)
    print("\n...USERS...\n")
    for user in users_repo.find_all():
        print(user)

    print("\n users with name Iva\n")
    for user in users_repo.find_by_user_name("Iva"):
        print(user)

    # user_controller = UserController(users_repo)
    #
    # for user in users:
    #     user_controller.add_user(user)
    #
    # print("\nUsers find by controller\n")
    # for user in user_controller.get_all_users():
    #     print(user)

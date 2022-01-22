from dao.repository import Repository
from entity.tasks import Tasks
from entity.bonus import Bonus
from entity.rewards import Rewards
from entity.users import Users
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

	t7 = Tasks(id=None, name="party", category="entertainment",owners= ("bonus1",), description="in the wardrobe")
	t8 = Tasks(id=None, name="sweet", category="food", owners=("bonus2",), description="only one")
	t9 = Tasks(id=None, name="movie", category="entertainment", description="on cinema")
	tasks = (t1, t2, t3)

	tasks_repo = Repository()
	for task in tasks:
		tasks_repo.create(task)
	print("\n...TASKS...\n")
	for task in tasks_repo.find_all():
		print(task)

	b1 = Bonus(t4, "party")
	b2 = Bonus(t5, "sweets")
	b3 = Bonus(t6, "movie")

	bonus_tasks = (b1, b2, b3)
	bonus_repo = Repository()

	for bonus in bonus_tasks:
		bonus_repo.create(bonus)
	print("\n...BONUS AND REWRDS...\n")
	for bonus in bonus_repo.find_all():
		print(bonus)

	print("\n...REWARDS...\n")
	r1 = Rewards(t7)
	r2 = Rewards(t8)
	r3 = Rewards(t9)
	rewards = (r1, r2, r3)

	rewards_repo = Repository()
	for reward in rewards:
		rewards_repo.create(reward)

	for reward in rewards_repo.find_all():
		print(reward)

	u1 = Users("Nikol", 7)
	u2 = Users("Iva", 3)

	users = (u1,u2)
	users_repo = Repository()

	for user in users:
		users_repo.create(user)
	print("\n...USERS...\n")
	for user in users_repo.find_all():
		print(user)
from locust import HttpUser, TaskSet, task, between,run_single_user
from decouple import config

# import pdb; pdb.set_trace()


# if config("KEY"):
class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def about(self):
        self.client.get("/about")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)


if __name__ == "__main__":
    run_single_user(WebsiteUser)
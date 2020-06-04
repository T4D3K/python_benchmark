from time import sleep

from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def index(self):
        for i in range(1000):
            self.client.get("/hello")


from locust import HttpUser, between, task


class NginxIndex(HttpUser):
    wait_time = between(0, 0)

    @task
    def index(self):
        self.client.get(url="/")

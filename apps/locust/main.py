from locust import HttpUser, task

class Color(HttpUser):
    @task
    def color(self):
        response = self.client.get("/color")

        # Extract the response data as a string
        response_data = response.text

        with open("response_data.log", "a") as f:
            f.write(response_data + "\n")
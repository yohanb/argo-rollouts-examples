from locust import HttpUser, task, between
import newrelic.agent

# Configure New Relic with your license key
newrelic.agent.initialize('/home/locust/newrelic.ini')

class Rollout(HttpUser):
    wait_time = between(0.5, 3)
    @task
    @newrelic.agent.background_task()
    def color(self):
        response = self.client.get(url="/color")
        application = newrelic.agent.application()
        newrelic.agent.record_custom_event('rollout_get_color', {'color': response.text}, application)
        self.client.close()

from locust import HttpUser, task
import newrelic.agent

# Configure New Relic with your license key
newrelic.agent.initialize('/home/locust/newrelic.ini')


class Color(HttpUser):
    @task
    @newrelic.agent.background_task()
    def color(self):
        with self.get_session() as session:
            response = session.get("/color")
            application = newrelic.agent.application()
            newrelic.agent.record_custom_event('rollout_get_color', {'color': response.text}, application)

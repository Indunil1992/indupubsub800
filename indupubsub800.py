import numpy as np
from google.cloud import pubsub_v1

def handler(request):


# TODO(developer)
 project_id = "sigma-qa-testing"
 topic_id = "test.indunill"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

response = publisher.list_topic_subscriptions(request={"topic": topic_path})
for subscription in response:
    print(subscription)

    return "Successfully executed 1234"

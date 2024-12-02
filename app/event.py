import uuid


class Event:
    body = {
        "user_id": "",
        "description": "",
        "event_id": "",
        "status": ""
    }

    def build_event(self, user_id, description):
        self.body["user_id"] = user_id
        self.body["description"] = description
        self.body["event_id"] = uuid.uuid1().hex
        self.body["status"] = "in queue"

        return self.body

    def update_status(self, status):
        self.body["status"] = status
        return self.body

    def get_event(self):
        pass
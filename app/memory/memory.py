
class ConversationMemory:
    def __init__(self):
        self.history = []

    def add(self, user, response):
        self.history.append({"user": user, "response": response})

    def get_context(self):
        return "\n".join(
            [f"User: {h['user']} \nAI: {h['response']}" for h in self.history]
        ) 
    
    
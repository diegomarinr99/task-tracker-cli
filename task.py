from datetime import datetime

class Task:
    def __init__(self, id, description, status = "todo", createdAt = None, updatedAt = None):
        self.id = id
        self.description = description
        self.status = status
        now = datetime.now().isoformat()
        self.createdAt = createdAt or now
        self.updatedAt = updatedAt or now

    def get_dict(self):
        return {"id": self.id,
                "description": self.description,
                "status": self.status, 
                "createdAt": self.createdAt, 
                "updatedAt": self.updatedAt}
    
    def get_id(self):
        return self.id
    
    def get_description(self):
        return self.description
    
    def set_status(self, status):
        self.status = status
        now = datetime.now().isoformat()
        self.updatedAt = now
    
    def set_description(self, description):
        self.description = description
        now = datetime.now().isoformat()
        self.updatedAt = now

    def get_status(self):
        return self.status

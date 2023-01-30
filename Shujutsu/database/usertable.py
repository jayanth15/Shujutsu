from database.connection import UserLogin

class UserLoginTable:
    def __init__(self, data) -> None:
        self.data = data
        self.table = UserLogin

    def check_email(self):
        email = self.data["email"]
        data = {
            "email": email
        }
        result = UserLogin.find_one(data)
        if result:
            return True
        return False

    def insert(self):
        result = self.table.insert_one(self.data)
        if result.acknowledged:
            return True
        return False


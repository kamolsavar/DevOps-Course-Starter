from flask_login import UserMixin, current_user

class User (UserMixin):
    def __init__ (self,user_id):
        self.id = user_id
        if user_id == '39657615':
            self.role = 'Writer'
        else:
            self.role = 'Reader'

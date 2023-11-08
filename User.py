class User(object):
    id = None
    first_name = None
    last_name = None
    email = None
    password = None
    created_at = None

    def __init__(self, user_id, first_name, last_name, email, password, created_at):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.created_at = created_at
        super(User, self).__init__()

    def __str__(self):
        return (f'ID: {self.id}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\n'
                f'Password: {self.password}\nCreated At: {self.created_at}')

    def authenticate(self, email, password):
        return self.email == email and self.password == password

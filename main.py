class User:
    def __init__(self, ism, username, email):
        self.ism = ism
        self.username = username
        self.email = email

    def get_info(self):
        return f"Foydalanuvchi: {self.username}, ismi: {self.ism}, email: {self.email}"

    def email_ozgartir(self, yangi_email):
        self.email = yangi_email

user1 = User("Alijon Valiyev", "alijon1994", "alijon1994@gmail.com")
user2 = User("Madina Karimova", "madina 99", "madina@mail.ru")

user2.email_ozgartir("madina99@gmail.com")

print(user1.ism)
print(user1.get_info())

print(user2.ism)
print(user2.get_info())

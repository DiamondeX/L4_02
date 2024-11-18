class User:
    def __init__(self, user_id, name):
        self.__id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"User(ID: {self.__id}, Name: {self.__name}, Access Level: {self.__access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__admin_access_level = 'admin'
        self.__users = []

    def get_admin_access_level(self):
        return self.__admin_access_level

    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
            print(f"User {user.get_name()} added to the system.")
        else:
            print("Invalid user object.")

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_id() == user_id:
                self.__users.remove(user)
                print(f"User with ID {user_id} has been removed.")
                return
        print(f"User with ID {user_id} not found.")

    def list_users(self):
        for user in self.__users:
            print(user)

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Admin Access Level: {self.__admin_access_level}"


# Пример использования
if __name__ == "__main__":
    admin = Admin(1, "Admin Name")

    # Добавление пользователей
    admin.add_user(User(2, "John Doe"))
    admin.add_user(User(3, "Jane Smith"))

    # Вывод списка пользователей
    print("\nCurrent Users:")
    admin.list_users()

    # Удаление пользователя
    admin.remove_user(2)

    # Вывод списка пользователей после удаления
    print("\nUsers after removal:")
    admin.list_users()
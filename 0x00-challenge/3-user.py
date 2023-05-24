#!/usr/bin/python3
"""
This is a User Model.
"""
import hashlib
import uuid


class User():
    """
    This class defines a User.
    - id: a public string that is unique for each user (generated using uuid)
    - password: a private string that is hashed using MD5
    """

    __password = None  # The private attribute __password is initially set to None.

    def __init__(self):
        """
        This method initializes a new user and assigns a unique id to it.
        """
        self.id = str(uuid.uuid4())  # Every new user is assigned a unique id.

    @property
    def password(self):
        """
        This method is a getter for the password.
        """
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        This method is a setter for the password.
        - It sets the password to None if the input is None or not a string.
        - Otherwise, it hashes the password using MD5 and assigns it to __password.
        """
        if pwd is None or type(pwd) is not str:
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()  # The password is hashed using MD5.

    def is_valid_password(self, pwd):
        """
        This method checks if a given password is valid.
        - It returns False if the password is None, not a string, or doesn't match the hashed password.
        - Otherwise, it compares the hashed version of the input password with the stored hashed password.
        """
        if pwd is None or type(pwd) is not str:
            return False
        if self.password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest().lower() == self.password  # Compare the hashed input password with the stored hashed password.


if __name__ == '__main__':
    print("Test User")

    # Various tests to check the functionality of the User class and its methods.

    user_1 = User()
    if user_1.id is None:
        print("New User should have an id")

    user_2 = User()
    if user_1.id == user_2.id:
        print("User.id should be unique")

    u_pwd = "myPassword"
    user_1.password = u_pwd
    if user_1.password == u_pwd:
        print("User.password should be hashed")

    if user_2.password is not None:
        print("User.password should be None by default")

    user_2.password = None
    if user_2.password is not None:
        print("User.password should be None if setter to None")

    user_2.password = 89
    if user_2.password is not None:
        print("User.password should be None if setter to an integer")

    if not user_1.is_valid_password(u_pwd):
        print("is_valid_password should return True if it's the right password")

    if user_1.is_valid_password("Fakepwd"):
        print("is_valid_password should return False if it's not the right password")

    if user_1.is_valid_password(None):
        print("is_valid_password should return False if compare with None")

    if user_1.is_valid_password(89):
        print("is_valid_password should return False if compare with integer")

    if user_2.is_valid_password("No pwd"):
        print("is_valid_password should return False if no password set")

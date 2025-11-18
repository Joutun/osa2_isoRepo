from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        # tarkastetaan onko jo käyttäjä ennestään olemassa
        if self._user_repository.find_by_username(username):
            raise UserInputError("User with username " + username + " already exists")

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        # KÄYTTÄJÄTUNNUS TARKASTUS
        if len(username) < 3:
            raise UserInputError("Username is too short")
        # islower tarkastaa että on pienet kirjaimet
        # if not username.isalpha() or not username.islower():
        #     raise UserInputError("Username must consist of only a-z characters")
        # toka ratkaisu enemmän ohjeiden mukainen.
        if re.match("^[a-z]+$", username) is None:
            raise UserInputError("Username must consist of only a-z characters")
        
        ## SALASANAN TARKASTAMINEN
        if len(password) < 8:
            raise UserInputError("Password must be at least 8 characters long")

        # isalpha tarkastaa että on aakkosia
        if password.isalpha():
            raise UserInputError("Password must contain at least one number or special character")
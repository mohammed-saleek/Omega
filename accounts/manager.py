from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None, password2 = None, is_active = True):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username = username,
            first_name=first_name,
            last_name = last_name,
            is_active = is_active,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

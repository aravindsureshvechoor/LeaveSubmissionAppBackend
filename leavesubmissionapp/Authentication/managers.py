from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,email,user_name,role,password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not user_name:
            raise ValueError('User must have a username')

        user = self.model(
            email       = self.normalize_email(email),
            user_name   = user_name,
            role        = role
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,role,user_name,password):
        user = self.create_user(
            email = self.normalize_email(email),
            user_name = user_name,
            password = password,
            role = role,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
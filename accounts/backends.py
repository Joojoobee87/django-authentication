from django.contrib.auth.models import User


class EmailAuth:
    """Authenticate user by an exact match on email and password"""

    def authenticate(self, username=None, password=None):
        """Get instance of `User` based on email and verified password"""

        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    
    def get_user(self, user_id):
        """Used by the Django authentication system to retrieve a user instance"""

        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
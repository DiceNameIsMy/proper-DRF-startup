from django.contrib.auth.models import AbstractUser, AnonymousUser as DjangoAnonymousUser


class User(AbstractUser):
    pass


class AnonymousUser(DjangoAnonymousUser):
    pass

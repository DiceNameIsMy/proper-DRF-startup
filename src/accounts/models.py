from django.contrib.auth.models import AbstractUser, UserManager, AnonymousUser as DjangoAnonymousUser


class User(AbstractUser):
    objects: UserManager["User"] = UserManager()  # type: ignore[assignment]


class AnonymousUser(DjangoAnonymousUser):
    pass

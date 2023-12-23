from django.db import models
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.template.defaultfilters import slugify
# from Utils.translator import translateToEng

from rest_framework_simplejwt.tokens import RefreshToken
import random

class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`.

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    # def create_user(self, username, email, type=None,phone=None,password=None):
    def create_user(self, username, email,signup_from,password=None,phone=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        # if phone is None:
        #     raise TypeError('Users must have a phone number.')
        # if type is None:
        #     raise TypeError('Users must have a Type.')
        if signup_from is None:
            signup_from="web"
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email),signup_from=signup_from)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password=None):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username=username, email=email, password=password,signup_from="web")
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

def userSlugCreator(instance):
    slug=f"@{slugify(instance.username)}"
    if User.objects.filter(slug=slug).exists():
        slug=f"@{slugify(instance.email.split('@')[0])}"
        if User.objects.filter(slug=slug).exists():
            slug=f"@{slugify(instance.email.split('.')[0])}"
    return slug


def createUserRefferalCode(instance):
    ls=["a","b","c","d","e","f","aa","ab","ac","ad","ae","af"]
    er=random.sample(ls,1)
    num = random.randint(11,158978)
    code = f"asvs-{er}-{num}"
    if User.objects.filter(referral_code=code).exists():
        user = User.objects.latest("id").id
        code = f"{code}-{user}"
    return code


class User(AbstractBaseUser):

    # Each `User` needs a human-readable unique identifier that we can use to
    # represent the `User` in the UI. We want to index this column in the
    # database to improve lookup performance.
    username = models.CharField(db_index=True, max_length=255)
    password = models.CharField('password', max_length=128,blank=True,null=True)

    # We also need a way to contact the user and a way for the user to identify
    # themselves when logging in. Since we need an email address for contacting
    # the user anyways, we will also use the email for logging in because it is
    # the most common form of login credential at the time of writing.
    email = models.EmailField(db_index=True, unique=True)

    # When a user no longer wishes to use our platform, they may try to delete
    # their account. That's a problem for us because the data we collect is
    # valuable to us and we don't want to delete it. We
    # will simply offer users a way to deactivate their account instead of
    # letting them delete it. That way they won't show up on the site anymore,
    # but we can still analyze the data.
    is_active = models.BooleanField(default=True)

    # city = models.CharField(max_length=255,null=True,blank=True)
    # country = models.CharField(max_length=10,null=True,blank=True)

    approved=models.BooleanField(default=True)
    # The `is_staff` flag is expected by Django to determine who can and cannot
    # log into the Django admin site. For most users this flag will always be
    # false.
    is_staff = models.BooleanField(default=False)

    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_upload_path(instance,filename):
        import os
        return os.path.join(f"user_pics/{instance.slug}",filename)
    image = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case we want it to be the email field.
    phone=models.CharField(max_length=20,null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    referral_code = models.CharField(max_length=255,null=True,blank=True)
    slug = models.CharField(max_length=255, blank=True)
    signup_from_choices=(
        ('web','web'),
        ('app','app')
    )
    signup_from=models.CharField(choices=signup_from_choices, max_length=50,default='web')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = userSlugCreator(self)
            self.referral_code = createUserRefferalCode(self)
            # addSitemapLink.delay(f"/{self.slug}")
            # prepare_email([self],"Welcome")
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """
        return self.email

    @property
    def token(self):
        #generate token for user
        return self._generate_token_user
    

    def _generate_token_user(self):

        token = RefreshToken.for_user(self)

        return str(token.access_token)
    
    @property
    def is_superuser(self):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=255,null=True,blank=True)
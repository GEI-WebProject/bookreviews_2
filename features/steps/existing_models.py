from behave import *
from django.contrib.auth.models import User


use_step_matcher("parse")


@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    User.objects.create_user(
        username=username, email='user@example.com', password=password)

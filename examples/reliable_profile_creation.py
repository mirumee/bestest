from django.contrib.auth.models import User
from profile.models import Profile


def get_user(user_dict):
    user, is_new = User.objects.get_or_create(username=user_dict['Username'])
    if is_new:
        profile = Profile.objects.get_or_create(user=user)[0]  # maybe there already was profile for the user we just created?
        profile.save()  # just to be sure, let's save the profile we just created (or pulled from db?)
    return user

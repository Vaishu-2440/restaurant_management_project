from django.contrib.auth.models import User
frm rest_framework import seializers

class UserProfileUpdateSerializer(serializer.ModelSerializer) :
    class Meta :
        model = User
        field = ['first_name', 'last_name', 'email']
        extra_kwargs = {
            "email" ; {"required" : "True"}
        }
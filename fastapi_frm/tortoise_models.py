from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Users(models.Model):
    class Meta:
        table = "users"

    id = fields.IntField(pk=True)
    #: This is a username
    name = fields.CharField(max_length=20, unique=True)


User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)

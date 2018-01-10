# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager
from libs.forms.validators import email_validator
# Create your models here.
from libs.models.mixins import TimeModelMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(name_cn=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, **extra_fields)


class Account(AbstractBaseUser):
    '''
    用户
    '''
    name_cn = models.CharField(u'用户名', max_length=32, unique=True)
    email = models.CharField(u'邮箱', max_length=100, unique=True, validators=[email_validator])
    department = models.CharField(u'部门', max_length=64, null=False, blank=True)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True, editable=False)
    last_update_time = models.DateTimeField(u'最新更新时间', auto_now_add=True, editable=False)
    objects = UserManager()
    USERNAME_FIELD = 'name_cn'

    @classmethod
    def create_or_update_users(cls, **kwargs):
        fields = {
            "name_cn": kwargs.get("name_cn"),
            "email": kwargs.get("email"),
            "department": kwargs.get("department"),
        }
        account = Account.objects.filter(name_cn=kwargs['name_cn'])
        if account:
            account.update(**fields)
            return account[0].id
        else:
            raw_password = kwargs['password']
            account = cls(**fields)
            account.set_password(raw_password)
            account.save()
            return account.id


class UserSessionKey(TimeModelMixin, models.Model):
    '''
    用户不同终端session key
    '''
    user_id = models.IntegerField(u"用户ID", null=False)
    session_key = models.CharField(u'session key', max_length=40)

    class Meta:
        db_table = 'account_session_key'


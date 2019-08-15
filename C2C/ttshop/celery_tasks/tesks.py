from django.core.mail import send_mail
from django.conf import settings
from django.template import loader, RequestContext
from celery import Celery
import time

# django环境的初始化，在任务处理者worker一端加以下几句
import os
# from buyer_apps.goods.models import G
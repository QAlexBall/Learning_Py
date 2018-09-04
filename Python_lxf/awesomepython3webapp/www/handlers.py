# -*- coding: utf-8 -*-

""" url handlers """
import re, time, json, logging, hashlib, base64, asyncio
from Python_lxf.awesomepython3webapp.www.coroweb import get, post
from Python_lxf.awesomepython3webapp.www.models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }
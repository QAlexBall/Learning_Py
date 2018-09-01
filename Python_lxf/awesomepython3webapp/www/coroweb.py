# -*- coding: utf-8 -*-

import asyncio, os, inspect, logging, functools
from urllib import parse
from aiohttp import web
from Python_lxf.awesomepython3webapp.www.apis import APIError


# 把一个函数映射为一个URL处理函数,先定义一个@get()
def get(path):
    """
    Define decorator @get('/path')
    @get装饰器,给处理函数绑定URL和HTTP method-GET属性
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)

        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper

    return decorator


# 定义一个@post()
def post(path):
    """
    Define decorator @post('/path')
    @post装饰器,给处理函数绑定URL和HTTP method-POST的属性
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)

        wrapper.__method__ = 'POST'
        wrapper.__route__ = path
        return wrapper

    return decorator


def get_required_kw_args(fn):
    """ 将函数所有没有默认值的命名关键字参数名作为一个tuple返回 """
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
            args.append(name)
        return tuple(args)


def get_named_kw_args(fn):
    """ 将函数所有的命名关键字参数名作为一个tuple返回 """
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            args.append(name)
    return tuple(args)


def has_named_kw_args(fn):
    """ 检查函数是否有命名关键字参数,返回布尔值 """
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            return True


def has_var_kw_arg(fn):
    """ 检查函数是否有关键字参数集,返回布尔值 """
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.VAR_KEYWORD:
            return True


def has_request_arg(fn):
    """
    检查函数是否有request参数,返回布尔值.
    若有request参数,检查该参数是否为该函数的最后一个参数,否则抛出异常
    """
    sig = inspect.signature(fn)
    params = sig.parameters
    found = False
    for name, param in params.items():
        if name == 'request':
            found = True
            continue
        if found and (param.kind != inspect.Parameter.VAR_POSITIONAL and
                      param.kind != inspect.Parameter.KEYWORD_ONLY and
                      param.kind != inspect.Parameter.VAR_KEYWORD):
            raise ValueError('request parameter must be the last named parameter in function: %s%s' %
                             (fn.__name__, str(sig)))
        return found


class RequestHandler(object):
    """ 请求处理器,用来封装处理函数 """
    def __init__(self, app, fn):
        # app: an application instance for registering the fn
        # fn: a request handler with a particular HTTP method and path
        self.app = app
        self.func = fn
        self._has_request_arg = has_request_arg(fn)
        self._has_var_kw_arg = has_var_kw_arg(fn)
        self._has_named_kw_args = has_named_kw_args(fn)
        self._named_kw_args = get_named_kw_args(fn)
        self._required_kw_args = get_required_kw_args(fn)

    async def __call__(self, request):
        """ 请求分析, request handler, must a coroutine that accepts a request instance
        as its only argument and returns a streamresponse derived instance """
        kw = None
        if self._has_var_kw_arg or self._has_named_kw_args or self._request_kw_args:
            # 当传入处理函数具有 关键字参数集 或 命名关键字参数 或 request参数
            if request.method == 'POST':
                # POST请求预处理
                if not request.content_type:
                    # 无正文类型信息时返回
                    return web.HTTPBadRequest('Missing Content-Type')
                ct = request.content_type.lower()
                if ct.startwith('application/json'):
                    # 处理函数JSON类型的数据,传入参数字典中
                    params = await request.json()
                    if not isinstance(params, dict):
                        return web.HTTPBadRequest('JSON body must be object.')
                    kw = params
                elif ct.startwith('application/x-www-form-urlencoded') or ct.startwith('multipart/form-data'):
                    # 处理表单类型的数据,传入参数字典中
                    params = await request.post()
                    kw = dict(**params)
                else:
                    # 暂不支持处理其他正文类型的数据
                    return web.HTTPBadRequest('Unsupported Content-Type: %s' % request.content_type)

            if request.method == 'GET':
                # get请求预处理
                qs = request.query_string
                # 获取URL中的请求参数,如name=JustOne, id=007
                if qs:
                    # 将请求参数传入参数字典中
                    kw = dict()
                    for k, v in parse.parse_qs(qs, True).items():
                        # parse a query string, data are returned as a dict. the dict keys are
                        # the unique query variable names and the values are lists of values for
                        # each name. a True value indicates that lanks should be retained as blank stirngs
                        kw[k] = v[0]
        if kw is None:
            # 请求无请求参数时
            kw = dict(**request.match_info)
            # Read-only property with AbstractMatchInfo instance for result of route resolving
        else:
            # 参数字典收集请求参数时
            if not self._has_named_kw_args and self._named_kw_args:
                copy = dict()
                for name in self._named_kw_args:
                    if name in kw:
                        copy[name] = kw[name]
                    kw = copy
                for k, v in request.match_info.items():
                    if k in kw:
                        logging.warning('Duplicate arg name in named arg and kw args: %s' % k)
                    kw[k] = v

        if self._has_request_arg:
            kw['request'] = request
        if self._required_kw_args:
            # 收集无默认的关键字参数
            for name in self._required_kw_args:
                if not name in kw:
                    # 当存在关键字参数未被赋值时返回,
                    # 例如 一般的账号注册时,没填入密码就提交注册申请时,提示密码未输入
                    return web.HTTPBadRequest('Missing arguments: %s' % name)



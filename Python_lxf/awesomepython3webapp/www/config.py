"""
应用程序读取配置文件优先从config_override.py读取.
为了简化读取配置文件,可以把所有配置读取到统一的config.py中.
"""

import Python_lxf.awesomepython3webapp.www.config_default

class Dict(dict):
    """
    Simple dict but support access as x.y style.
    """
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v


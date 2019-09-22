from distutils.core import setup, Extension
import os

module_spam_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) \
                   + '/c_extensions/src/spammoudle.c'
module_spam = Extension('spam',
                        sources=[module_spam_path])

setup(name="spam",
      version='1.0',
      description='test spam module',
      ext_modules=[module_spam])

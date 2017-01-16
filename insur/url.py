import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from handler import IndexHandler

url=[
    (r'/', IndexHandler),

    ]
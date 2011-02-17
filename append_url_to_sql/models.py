import sys

from django.conf import settings
from django.http import HttpRequest
from django.db.backends import util, BaseDatabaseWrapper

class CursorWrapper(util.CursorDebugWrapper):
    def execute(self, sql, *args):
        f = sys._getframe()
        while f:
            request = f.f_locals.get('request')
            if isinstance(request, HttpRequest):
                sql += ' -- %s' % repr(request.path)[2:-1].replace('%', '%%')
                break
            f = f.f_back

        return self.cursor.execute(sql, *args)

if getattr(settings, 'APPEND_REQUEST_PATH_TO_SQL', True):
    old_cursor = BaseDatabaseWrapper.cursor
    def cursor(self, *args, **kwargs):
        return CursorWrapper(old_cursor(self, *args, **kwargs), self)
    BaseDatabaseWrapper.cursor = cursor

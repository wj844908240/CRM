#_*_coding:utf-8_*_

from django.conf import settings

import os
settings.TEMPLATES[0]['DIRS'] += [os.path.join(settings.BASE_DIR, 'kingadmin/templates')]

settings.STATICFILES_DIRS +=[ os.path.join(settings.BASE_DIR, 'kingadmin/statics')]

print(settings.STATICFILES_DIRS,11111111122222222222223333333333333)
# print(settings.TEMPLATES[0]['DIRS'] )
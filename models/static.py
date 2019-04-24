# -*- coding: utf-8 -*-

from utils.common import BeautyOrderedDict

STATUSES = BeautyOrderedDict([('requested', 'Request'),
                              ('user_verified', 'user_verified'),
                              ('updated', 'Updated'),
                              ('validated', 'Validated'),
                              ('generated', 'Generated'),
                              ('expired', 'Expired'),
                              ('refused', 'Refused')])
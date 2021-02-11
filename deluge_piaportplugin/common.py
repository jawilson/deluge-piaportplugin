# -*- coding: utf-8 -*-
# Copyright (C) 2019 Jeff Wilson <jeff@jeffalwilson.com>
#
# Basic plugin template created by the Deluge Team.
#
# This file is part of PIAPortPlugin and is licensed under GNU GPL 3.0, or later,
# with the additional special exception to link portions of this program with
# the OpenSSL library. See LICENSE for more details.
from __future__ import unicode_literals

import os.path

from pkg_resources import resource_filename


def get_resource(filename):
    return resource_filename(__package__, os.path.join('data', filename))

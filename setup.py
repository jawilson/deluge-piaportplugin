# -*- coding: utf-8 -*-
# Copyright (C) 2019 Jeff Wilson <jeff@jeffalwilson.com>
#
# Basic plugin template created by the Deluge Team.
#
# This file is part of PIAPortPlugin and is licensed under GNU GPL 3.0, or later,
# with the additional special exception to link portions of this program with
# the OpenSSL library. See LICENSE for more details.
from setuptools import find_packages, setup

__plugin_name__ = 'PIAPortPlugin'
__author__ = 'Jeff Wilson'
__author_email__ = 'jeff@jeffalwilson.com'
__version__ = '0.2'
__url__ = ''
__license__ = 'GPLv3'
__description__ = ''
__long_description__ = """"""
__pkg_data__ = {'deluge_'+__plugin_name__.lower(): ['data/*']}

setup(
    name=__plugin_name__,
    version=__version__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    license=__license__,
    long_description=__long_description__,

    packages=find_packages(),
    package_data=__pkg_data__,

    version_config=True,
    setup_requires=['setuptools-git-versioning'],

    entry_points="""
    [deluge.plugin.core]
    %s = deluge_%s:CorePlugin
    [deluge.plugin.gtk3ui]
    %s = deluge_%s:Gtk3UIPlugin
    [deluge.plugin.web]
    %s = deluge_%s:WebUIPlugin
    """ % ((__plugin_name__, __plugin_name__.lower()) * 3)
)

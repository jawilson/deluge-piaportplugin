# -*- coding: utf-8 -*-
# Copyright (C) 2019 Jeff Wilson <jeff@jeffalwilson.com>
#
# Basic plugin template created by the Deluge Team.
#
# This file is part of PIAPortPlugin and is licensed under GNU GPL 3.0, or later,
# with the additional special exception to link portions of this program with
# the OpenSSL library. See LICENSE for more details.
from __future__ import unicode_literals

import logging
import sys

import deluge.configmanager
from deluge.core.rpcserver import export
from deluge.plugins.pluginbase import CorePluginBase
import deluge.component as component
from twisted.internet.task import LoopingCall

log = logging.getLogger(__name__)

DEFAULT_PREFS = {
    'port_file': '/pia/forwarded_port',
    'poll_interval': 300
}


class Core(CorePluginBase):
    def enable(self):
        self.config = deluge.configmanager.ConfigManager(
            'piaportplugin.conf', DEFAULT_PREFS)
        self.check_timer = LoopingCall(self.update_if_blocked)
        self.check_timer = self.check_timer.start(int(self.config['poll_interval']))

    def disable(self):
        if self.check_timer:
            self.check_timer.stop()

    def update(self):
        pass

    def update_if_blocked(self):
        core = component.get("Core")
        log.debug("Current listen port: %d" % core.get_listen_port())
        def update_port(is_open):
            blocked = not is_open
            log.debug("Listen port %d is %s" % (core.get_listen_port(), (blocked and
                        "blocked" or "not blocked")))
            if blocked:
                log.info("Attempting to update listen port")
                try:
                    port = int(open(self.config["port_file"], 'r').read())
                except:
                    log.error("Failed to open and read port file: %s" % sys.exc_info()[1])
                    return

                if core.get_listen_port() == port:
                    log.warning("Current port file lists blocked port: %d" % port)
                    return

                core.set_config({"listen_ports": [port, port]})
                torrents = core.get_session_state()
                core.force_reannounce(torrents)
                log.info("Updated listen port to: %d" % port)

        core.test_listen_port().addCallback(update_port)

    @export
    def set_config(self, config):
        """Sets the config dictionary"""
        changed = self.config != config
        for key in config:
            self.config[key] = config[key]
        self.config.save()
        if changed:
            self.disable()
            self.enable()

    @export
    def get_config(self):
        """Returns the config dictionary"""
        return self.config.config

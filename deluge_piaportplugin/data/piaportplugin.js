/**
 * Script: piaportplugin.js
 *     The client-side javascript code for the PIAPortPlugin plugin.
 *
 * Copyright:
 *     (C) Jeff Wilson 2019 <jeff@jeffalwilson.com>
 *
 *     This file is part of PIAPortPlugin and is licensed under GNU GPL 3.0, or
 *     later, with the additional special exception to link portions of this
 *     program with the OpenSSL library. See LICENSE for more details.
 */

PIAPortPluginPlugin = Ext.extend(Deluge.Plugin, {
    constructor: function(config) {
        config = Ext.apply({
            name: 'PIAPortPlugin'
        }, config);
        PIAPortPluginPlugin.superclass.constructor.call(this, config);
    },

    onDisable: function() {
        deluge.preferences.removePage(this.prefsPage);
    },

    onEnable: function() {
        this.prefsPage = deluge.preferences.addPage(
            new Deluge.ux.preferences.PIAPortPluginPage());
    }
});
new PIAPortPluginPlugin();

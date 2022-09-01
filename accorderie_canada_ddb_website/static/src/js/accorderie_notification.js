odoo.define('website.accorderie_notification', function (require) {
    "use strict";

    require('bus.BusService');
    let core = require('web.core');
    let session = require('web.session');
    let Widget = require('web.Widget');
    let QWeb = core.qweb;

    let AccorderieNotification = Widget.extend({
        init: function (parent) {
            this._super(parent);
        },
        willStart: function () {
            return this._loadQWebTemplate();
        },
        start: function () {
            this.call('bus_service', 'addChannel', "accorderie.notification.favorite");
            this.call('bus_service', 'startPolling');
            this.call('bus_service', 'onNotification', this, this._onNotification);
            return this._super();
        },
        /**
         * @private
         */
        _loadQWebTemplate: function () {
            var xml_files = [];
            // This is not useful, only need to return an empty apply
            var defs = _.map(xml_files, function (tmpl) {
                return session.rpc('/web/proxy/load', {path: tmpl}).then(function (xml) {
                    QWeb.add_template(xml);
                });
            });
            return $.when.apply($, defs);
        },
        /**
         * @private
         * @param {Array[]} notifications
         */
        _onNotification: function (notifications) {
            console.debug("Accorderie Notification");
            console.debug(notifications);
        },
    });

    return {
        AccorderieNotification: AccorderieNotification,
    };

});

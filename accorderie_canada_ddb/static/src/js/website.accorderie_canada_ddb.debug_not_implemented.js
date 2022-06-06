odoo.define('website.accorderie_canada_ddb.debug_not_implemented.instance', function (require) {
    'use strict';

    require('web_editor.ready');
    let Debug = require('website.accorderie_canada_ddb.debug_not_implemented');

    let $debug = $('.debug_not_implemented');
    if (!$debug.length) {
        return null;
    }

    let instance = new Debug();
    return instance.appendTo($debug).then(function () {
        return instance;
    });
});

//==============================================================================

odoo.define("website.accorderie_canada_ddb.debug_not_implemented", function (require) {

    let ajax = require('web.ajax');
    let Widget = require('web.Widget');

    let Debug = Widget.extend({
        start: function () {
            let self = this;
            let debugHidden = true;
            this._super.apply(this.arguments).then(function () {
                $('.debug_not_implemented')
                    .off('click')
                    .click(function (ev) {
                        self.on_click(ev);
                        if(debugHidden) {
                            debugHidden = false;
                            self.ToggleNotImplemented(true);
                        } else {
                            debugHidden = true;
                            self.ToggleNotImplemented(false)
                        }

                    });
            });
        },
        on_click: function (ev) {
            ev.preventDefault();
            ev.stopPropagation();
        },

        ToggleNotImplemented: function (show) {

            let unimplementedClasses = ["s_actualite", "s_event_list", "s_activite_bilan", "s_mes_informations",
                "s_vertical_list_lg", "s_pub_offre_desc", "activites_messages"];

            for (let i = 0; i < unimplementedClasses.length; i++) {
                let classes = document.getElementsByClassName(unimplementedClasses[i]);

                for (let j = 0; j < classes.length; j++) {
                    if(show) {
                        classes[j].style.backgroundColor = "rgba(255,0,0,0.5)";
                    } else {
                        classes[j].style.backgroundColor = "unset";
                    }

                }
            }

        },
    });

    return Debug;
});
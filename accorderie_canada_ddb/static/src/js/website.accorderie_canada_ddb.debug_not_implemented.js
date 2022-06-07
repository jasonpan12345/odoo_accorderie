odoo.define('website.accorderie_canada_ddb.debug_not_implemented.instance', function (require) {
    'use strict';

    require('web_editor.ready');
    let Debug = require('website.accorderie_canada_ddb.debug_not_implemented');

    let $debug = $('.highlight_not_implemented');
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
            let debugHighlighted = false;
            let debugHide = false;
            this._super.apply(this.arguments).then(function () {
                $('.highlight_not_implemented')
                    .click(function (ev) {
                        self.on_click(ev);
                        if(debugHighlighted) {
                            debugHighlighted = false;
                            self.HighlightNotImplemented(false);
                        } else {
                            debugHighlighted = true;
                            self.HighlightNotImplemented(true)
                        }

                    });
            });
            this._super.apply(this.arguments).then(function () {
                $('.hide_not_implemented')
                    .click(function (ev) {
                        self.on_click(ev);
                        if(debugHide) {
                            debugHide = false;
                            self.HideNotImplemented(false);
                        } else {
                            debugHide = true;
                            self.HideNotImplemented(true)
                        }

                    });
            });
        },
        on_click: function (ev) {
            ev.preventDefault();
            ev.stopPropagation();
        },

        HighlightNotImplemented: function (show) {
            console.log("debug");

            let classes = document.getElementsByClassName("debug_unimplemented");

            for (let j = 0; j < classes.length; j++) {
                if (show) {
                    classes[j].style.backgroundColor = "rgba(255,0,0,0.5)";
                } else {
                    classes[j].style.backgroundColor = "unset";
                }
            }
        },
        HideNotImplemented: function (show) {
            console.log("debug");

            let classes = document.getElementsByClassName("debug_unimplemented");

            for (let j = 0; j < classes.length; j++) {
                if (show) {
                    classes[j].style.display = "none";
                } else {
                    classes[j].style.display = "block";
                }
            }
        },
    });

    return Debug;
});
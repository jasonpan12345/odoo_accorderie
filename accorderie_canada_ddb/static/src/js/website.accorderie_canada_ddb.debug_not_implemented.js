odoo.define('website.accorderie_canada_ddb.debug_not_implemented.instance', function (require) {
    'use strict';

    require('web_editor.ready');
    let Debug = require('website.accorderie_canada_ddb.debug_not_implemented');

    let $debug = $('.debug-item');
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
            let debugActive = false;
            this._super.apply(this.arguments).then(function () {
                $('.highlight_not_implemented')
                    .click(function (ev) {
                        self.on_click(ev);
                        if(debugHighlighted) {
                            debugHighlighted = false;
                            self.HighlightNotImplemented(false);
                            debugActive = false;
                        } else {
                            debugHighlighted = true;
                            self.HighlightNotImplemented(true);
                            debugActive = true;
                        }
                        debugHide = false;
                        self.HideNotImplemented(false);
                        self.ActivateDebug(debugActive);
                    });
            });
            this._super.apply(this.arguments).then(function () {
                $('.hide_not_implemented')
                    .click(function (ev) {
                        self.on_click(ev);
                        if(debugHide) {
                            debugHide = false;
                            self.HideNotImplemented(false);
                            debugActive = false;
                        } else {
                            debugHide = true;
                            self.HideNotImplemented(true)
                            debugActive = true;
                        }
                        debugHighlighted = false;
                        self.HighlightNotImplemented(false);
                        self.ActivateDebug(debugActive);
                    });
            });
        },
        on_click: function (ev) {
            ev.preventDefault();
            ev.stopPropagation();
        },

        HighlightNotImplemented: function (show) {

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

            let classes = document.getElementsByClassName("debug_unimplemented");

            for (let j = 0; j < classes.length; j++) {
                if (show) {
                    classes[j].style.display = "none";
                } else {
                    classes[j].style.display = "block";
                }
            }
        },
        ActivateDebug: function (debugActive) {
            let debugBtn = document.getElementsByClassName("debug-item");
            if(debugActive) {
                debugBtn[0].style.backgroundColor = "grey";
            } else {
                debugBtn[0].style.backgroundColor = "unset";
            }
        }
    });

    return Debug;
});
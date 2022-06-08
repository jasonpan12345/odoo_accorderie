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
            let debugHighlighted = false; //highlight mode
            let debugHide = false; //hide mode

            $(document).on("click", '.highlight_not_implemented', function (ev) {
                self.on_click(ev);
                if (debugHighlighted) {
                    debugHighlighted = false;
                    self.HighlightNotImplemented(false);
                    self.ActivateDebug("highlight_not_implemented", false);
                } else {
                    debugHighlighted = true;
                    self.HighlightNotImplemented(true);
                    self.ActivateDebug("highlight_not_implemented", true);
                }
                // turn off other mode
                debugHide = false;
                self.HideNotImplemented(false);
            })

            $(document).on("click", '.hide_not_implemented', function (ev) {
                self.on_click(ev);
                if (debugHide) {
                    debugHide = false;
                    self.HideNotImplemented(false);
                    self.ActivateDebug("hide_not_implemented", false);
                } else {
                    debugHide = true;
                    self.HideNotImplemented(true);
                    self.ActivateDebug("hide_not_implemented", true);
                }
                // turn off other mode
                debugHighlighted = false;
                self.HighlightNotImplemented(false);
            })
        },
        on_click: function (ev) {
            console.log("onlcik");
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
        ActivateDebug: function (debugType, debugActive) {
            let debugBtn = document.getElementsByClassName(debugType);
            let siblings = $('.' + debugType).siblings();

            // deactivate sibling buttons
            for (let i = 0; i < siblings.length; i++) {
                siblings[i].style.backgroundColor = "unset";
            }
            // activate/deactivate target button
            for (let i = 0; i < debugBtn.length; i++) {
                if (debugActive) {
                    debugBtn[i].style.backgroundColor = "lightgrey";
                } else {
                    debugBtn[i].style.backgroundColor = "unset";
                }
            }
        }
    });

    return Debug;
});
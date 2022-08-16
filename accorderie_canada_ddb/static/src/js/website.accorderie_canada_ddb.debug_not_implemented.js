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
            let debugDebug = false; //hide mode

            $( document ).ready(function() {
                if (window.location.search.search("debug=") >= 0) {
                    debugDebug = true;
                    self.DebugDebug(false);
                    self.ActivateDebug("btn_debug_debug", true);
                }
            });

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

            $(document).on("click", '.btn_debug_debug', function (ev) {
                self.on_click(ev);
                if (debugDebug) {
                    debugDebug = false;
                    self.DebugDebug(true);
                    self.ActivateDebug("btn_debug_debug", false);
                } else {
                    debugDebug = true;
                    self.DebugDebug(false);
                    self.ActivateDebug("btn_debug_debug", true);
                }
            })
        },
        on_click: function (ev) {
            console.log("onclick debug option");
            ev.preventDefault();
            ev.stopPropagation();
        },

        HighlightNotImplemented: function (show) {
            let unique_id_name = "unique_debug_unimplemented";
            if (show) {
                let link = document.createElement('link');
                link.rel = "stylesheet";
                link.type = "text/css";
                link.id = unique_id_name;
                link.href = document.location.origin + "/accorderie_canada_ddb/static/src/scss/website_debugger.css";

                document.head.appendChild(link);
            } else {
                let unique_id = document.getElementById(unique_id_name);
                if (!_.isNull(unique_id)) {
                    unique_id.remove();
                }
            }
        },
        HideNotImplemented: function (show) {

            let classes = document.getElementsByClassName("debug_unimplemented");

            for (let j = 0; j < classes.length; j++) {
                if (show) {
                    classes[j].style.display = "none";
                } else {
                    classes[j].style.display = "revert";
                }
            }
        },
        DebugDebug: function (hide) {

            let classes = document.getElementsByClassName("debug_debug");

            for (let j = 0; j < classes.length; j++) {
                if (hide) {
                    classes[j].style.display = "none";
                } else {
                    classes[j].style.display = "revert";
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
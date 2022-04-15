odoo.define('website.accorderie_canada_ddb.participer.instance', function (require) {
    'use strict';

    require('web_editor.ready');
    var ParticiperForm = require('website.accorderie_canada_ddb.participer');

    var $form = $('#participer_form');
    if (!$form.length) {
        return null;
    }

    var instance = new ParticiperForm();
    return instance.appendTo($form).then(function () {
        return instance;
    });
});

//==============================================================================

odoo.define("website.accorderie_canada_ddb.participer", function (require) {

    var ajax = require('web.ajax');
    var core = require('web.core');
    var Widget = require('web.Widget');

    var _t = core._t;

    var currentTab = 0; // Current tab is set to be the first tab (0)

// Catch registration form event, because of JS for attendee details
    var ParticiperForm = Widget.extend({
        start: function () {
            var self = this;
            var res = this._super.apply(this.arguments).then(function () {
                $('#participer_form .submit_container .submit_btn')
                    .off('click')
                    .click(function (ev) {
                        self.on_click(ev, 1);
                    });
            });
            var prev = this._super.apply(this.arguments).then(function () {
                $('#participer_form .submit_container .prev')
                    .off('click')
                    .click(function (ev) {
                        self.on_click(ev, -1);
                    });
            });
            self.showTab(currentTab); // Display the current tab
            return res;
        },
        on_click: function (ev, nextPrev) {
            ev.preventDefault();
            ev.stopPropagation();
            this.nextPrev(nextPrev);
            var $form = $(ev.currentTarget).closest('form');
            var $button = $(ev.currentTarget).closest('[type="submit"]');
            var post = {};
        },
        showTab: function (n) {
            console.log("showtab");
            // This function will display the specified tab of the form ...
            var x = document.getElementsByClassName("tab");
            x[n].style.display = "flex";
            // ... and fix the Previous/Next buttons:
            if (n == 0) {
                document.getElementById("prevBtn").style.display = "none";
            } else {
                document.getElementById("prevBtn").style.display = "inline";
            }
            if (n == (x.length - 1)) {
                document.getElementById("nextBtn").innerHTML = "Submit";
            } else {
                document.getElementById("nextBtn").innerHTML = "Next";
            }
            // ... and run a function that displays the correct step indicator:
            //fixStepIndicator(n)
        },
        nextPrev: function (n) {
            console.log("nextprev");
            // This function will figure out which tab to display
            var x = document.getElementsByClassName("tab");
            // Exit the function if any field in the current tab is invalid:
            //if (n == 1 && !validateForm()) return false;
            // Hide the current tab:
            x[currentTab].style.display = "none";
            // Increase or decrease the current tab by 1:
            currentTab = currentTab + n;
            /*
            // if you have reached the end of the form... :
            if (currentTab >= x.length) {
                //...the form gets submitted:
                document.getElementById("regForm").submit();
                return false;
            }*/
            // Otherwise, display the correct tab:
            this.showTab(currentTab);
        },
    });

    return ParticiperForm;
});
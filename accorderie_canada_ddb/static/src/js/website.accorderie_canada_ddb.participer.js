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
            var form_choice = this._super.apply(this.arguments).then(function () {
                $('.buttons_form_container > input')
                    .off('click')
                    .click(function (ev) {
                        self.verifRadioChosen()
                    });
            });
            self.showTab(currentTab); // Display the current tab
            return res;
        },
        on_click: function (ev, nextPrev) {
            ev.preventDefault();
            ev.stopPropagation();
            this.nextPrev(nextPrev);
        },
        // Verify that at least one radio button is chosen on the current tab
        verifRadioChosen: function () {
            console.log("clicked");
            var x = document.getElementsByClassName("tab");
            var inputName = x[currentTab].getElementsByTagName("input")[0];

            if ($("input[name=" + inputName.name + "]:checked").length > 0) {
                document.getElementById("nextBtn").style.backgroundColor = "#ff956b";
                return true;
            }
            document.getElementById("nextBtn").style.backgroundColor = "lightgray";
            return false;
        },
        showTab: function (n) {
            console.log("showtab");
            this.verifRadioChosen();
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
                document.getElementById("nextBtn").value = "Submit";
            } else {
                document.getElementById("nextBtn").innerHTML = "Suivant";
            }
        },
        nextPrev: function (n) {
            console.log("nextprev");
            // This function will figure out which tab to display
            var x = document.getElementsByClassName("tab");
            // Exit the function if any field in the current tab is invalid:
            if (n == 1 && !this.verifRadioChosen()) {
                return false;
            }
            // Hide the current tab:
            x[currentTab].style.display = "none";
            // Increase or decrease the current tab by 1:
            currentTab = currentTab + n;

            // if you have reached the end of the form... :
            if (currentTab >= x.length) {
                //...the form gets submitted:
                document.getElementById("participer_form").submit();
                return false;
            }
            // Otherwise, display the correct tab:
            this.showTab(currentTab);

        },
    });

    return ParticiperForm;
});
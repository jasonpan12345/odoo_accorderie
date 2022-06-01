odoo.define('website.accorderie_canada_ddb.participer.instance', function (require) {
    'use strict';

    require('web_editor.ready');
    let ParticiperForm = require('website.accorderie_canada_ddb.participer');

    let $form = $('#participer_form');
    if (!$form.length) {
        return null;
    }

    let instance = new ParticiperForm();
    return instance.appendTo($form).then(function () {
        return instance;
    });
});

//==============================================================================

odoo.define("website.accorderie_canada_ddb.participer", function (require) {

    var ajax = require('web.ajax');
    var core = require('web.core');
    var session = require('web.session');
    var Widget = require('web.Widget');

    let _t = core._t;

    let currentTab = 0; // Current tab is set to be the first tab (0)

    // Catch registration form event, because of JS for attendee details
    let ParticiperForm = Widget.extend({
        start: function () {
            let self = this;
            let res = this._super.apply(this.arguments).then(function () {
                $('#participer_form .submit_container .submit_btn')
                    .off('click')
                    .click(function (ev) {
                        self.on_click(ev, 1);
                    });
            });
            let prev = this._super.apply(this.arguments).then(function () {
                $('#participer_form .submit_container .prev')
                    .off('click')
                    .click(function (ev) {
                        self.on_click(ev, -1);
                    });
            });
            let form_choice = this._super.apply(this.arguments).then(function () {
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
            let x = document.getElementsByClassName("tab");
            let inputName = x[currentTab].getElementsByTagName("input")[0];
            let primaryColor = getComputedStyle(document.body).getPropertyValue('--primary');

            let inputClick = $("input[name=" + inputName.name + "]:checked");
            console.debug(inputClick);
            if (inputClick.length > 0) {
                document.getElementById("nextBtn").style.backgroundColor = primaryColor;
                return true;
            }
            document.getElementById("nextBtn").style.backgroundColor = "lightgray";
            return false;
        },
        showTab: function (n) {
            this.verifRadioChosen();
            // This function will display the specified tab of the form ...
            let x = document.getElementsByClassName("tab");
            x[n].style.display = "flex";
            // ... and fix the Previous/Next buttons:
            if (n === 0) {
                document.getElementById("prevBtn").style.display = "none";
            } else {
                document.getElementById("prevBtn").style.display = "inline";
            }
            if (n === (x.length - 1)) {
                document.getElementById("nextBtn").value = "Submit";
            } else {
                document.getElementById("nextBtn").innerHTML = "Suivant";
            }
        },
        nextPrev: function (n) {
            // This function will figure out which tab to display
            let x = document.getElementsByClassName("tab");
            // Exit the function if any field in the current tab is invalid:
            if (n === 1 && !this.verifRadioChosen()) {
                return false;
            }
            console.debug("click nextPrev, tab # " + currentTab);
            console.debug(x);
            console.debug(x[currentTab]);
            if (currentTab === 2) {
                let inputName = x[currentTab].getElementsByTagName("input")[0];
                let lst_radio = $("input[name=" + inputName.name + "]:checked");
                let self = this;
                this.tab_sous_categorie = document.getElementsByClassName("tab_sous_categorie");
                let categorie_id = lst_radio[0].value;
                ajax.rpc("/accorderie_canada_ddb/type_service_sous_categorie_list/" + categorie_id, {}).then(function (data) {
                    if (data.error) {
                        return;
                    }

                    if (_.isEmpty(data)) {
                        return;
                    }

                    self.tab_sous_categorie[0].innerHTML = data;
                    $('.buttons_form_container > input')
                        .off('click')
                        .click(function (ev) {
                            self.verifRadioChosen()
                        });

                    // Hide the current tab:
                    x[currentTab].style.display = "none";
                    // Increase or decrease the current tab by 1:
                    currentTab = currentTab + n;

                    // Otherwise, display the correct tab:
                    self.showTab(currentTab);
                });
            } else if (currentTab >= x.length - 1) {
                // if you have reached the end of the form... :
                //...the form gets submitted:
                document.getElementById("participer_form").submit();
                return false;
            } else {
                // Hide the current tab:
                x[currentTab].style.display = "none";
                // Increase or decrease the current tab by 1:
                currentTab = currentTab + n;

                // Otherwise, display the correct tab:
                this.showTab(currentTab);
            }
        },
    });

    return ParticiperForm;
});
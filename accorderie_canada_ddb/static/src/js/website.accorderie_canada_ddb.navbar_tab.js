odoo.define('website.accorderie_canada_ddb.navbar_tabs.instance', function (require) {
    'use strict';

    require('web_editor.ready');
    let PublierForm = require('website.accorderie_canada_ddb.navbar_tabs');

    let $nav = $('.dropdown-nav');
    if (!$nav.length) {
        return null;
    }

    let instance = new PublierForm();
    return instance.appendTo($nav).then(function () {
        return instance;
    });
});

//==============================================================================

odoo.define("website.accorderie_canada_ddb.navbar_tabs", function (require) {

    let ajax = require('web.ajax');
    let Widget = require('web.Widget');

    // Catch registration form event, because of JS for attendee details
    let PublierForm = Widget.extend({
        start: function () {
            let self = this;
            let btnOffres = this._super.apply(this.arguments).then(function () {
                $('#BtnTabOffres')
                    .off('click')
                    .click(function (ev) {
                        self.on_click(ev);
                        self.showTab("tabOffres");
                    });
            });
            let btnDemandes = this._super.apply(this.arguments).then(function () {
                $('#BtnTabDemandes')
                    .off('click')
                    .click(function (ev) {
                        self.on_click(ev);
                        self.showTab("tabDemandes");
                    });
            });
            let btnMembres = this._super.apply(this.arguments).then(function () {
                $('#BtnTabMembres')
                    .off('click')
                    .click(function (ev) {
                        self.on_click(ev);
                        self.showTab("tabMembres");
                    });
            });
        },
        on_click: function (ev) {
            ev.preventDefault();
            ev.stopPropagation();
        },

        showTab: function (tab) {
            let i;
            let x = document.getElementsByClassName("navbar-tab");
            for (i = 0; i < x.length; i++) {
                x[i].style.display = "none";
            }
            document.getElementById(tab).style.display = "block";
        },
    });

    return PublierForm;
});

odoo.define('website.accorderie_canada_ddb.pub_offre.instance', function (require) {
    'use strict';

    require('web_editor.ready');
    var PublierForm = require('website.accorderie_canada_ddb.pub_offre');

    var $form = $('#pub_form');
    if (!$form.length) {
        return null;
    }

    var instance = new PublierForm();
    return instance.appendTo($form).then(function () {
        return instance;
    });
});

//==============================================================================

odoo.define("website.accorderie_canada_ddb.pub_offre", function (require) {

    var ajax = require('web.ajax');
    var Widget = require('web.Widget');


// Catch registration form event, because of JS for attendee details
    var PublierForm = Widget.extend({
        start: function () {
            var self = this;
            var res = this._super.apply(this.arguments).then(function () {
                $('.submit_container .submit_btn')
                    .off('click')
                    .click(function (ev) {
                        self.on_click(ev);
                        self.showModal();
                    });
            });
            return res;
        },
        on_click: function (ev) {
            ev.preventDefault();
            ev.stopPropagation();
        },

        showModal: function () {

            var target = $('#submitBtn').attr('data-target');
            console.log(target);
            $(target).attr("aria-hidden", "false");
            $(target).css("display", "block");
            $(target).addClass("show");

        },
    });

    return PublierForm;
});

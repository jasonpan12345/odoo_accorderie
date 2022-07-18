odoo.define('website.accorderie_canada_ddb.dialog_monaccorderie', function (require) {
    "use strict";

    var ajax = require("web.ajax");
    var core = require('web.core');
    var widget = require("web_editor.widget");
    var _t = core._t;
    var Dialog = widget.Dialog;

    var result = $.Deferred(),
        _templates_loaded = ajax.loadXML(
            "/accorderie_canada_ddb/static/src/xml/widgets.xml",
            core.qweb
        );


    var AccorderieForm = Dialog.extend({
        template: "accorderie_canada_ddb.AccorderieForm",

        /**
         * Store models info before creating widget
         *
         * @param {Object} parent Widget where this dialog is attached
         * @param {Object} options Dialog creation options
         * @param {Object} rooms rooms list
         * @param {String} chosen Prechosen model
         * @returns {Dialog} New Dialog object
         */
        init: function (parent, options) {

            var _options = $.extend({}, {
                title: _t("Mon accorderie"),
                size: "small",
            }, options);
            return this._super(parent, _options);
        },

        /**
         * Save data
         */
        save: function () {
            this.final_data = this.$("#model").val();
            console.log("save: " + this.final_data);


            this._super.apply(this, arguments);
        },
    });


    _templates_loaded.done(function () {
        result.resolve({
            AccorderieForm: AccorderieForm,
        });
    });

    $(document).on("click", '.profile_btn.accorderie', function (ev) {
        let optionsDialog = new AccorderieForm(
            $(""), {}
        );
        optionsDialog.open();
    })

});

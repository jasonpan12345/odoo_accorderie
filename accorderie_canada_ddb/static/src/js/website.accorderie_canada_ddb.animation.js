odoo.define("accorderie_canada_ddb.animation", function (require) {
    "use strict";

    var sAnimation = require("website.content.snippets.animation");

    sAnimation.registry.accorderie_canada_ddb = sAnimation.Class.extend({
        selector: ".o_accorderie_canada_ddb",

        start: function () {
            var self = this;
            var $eventList = this.$('.container');
            this._originalContent = $eventList[0].outerHTML;
            var def = this._rpc({
                route: "/offre_list",
            }).then(function (data) {
                if (data.error) {
                    return;
                }

                if (_.isEmpty(data)) {
                    return;
                }

                self._$loadedContent = $(data);
                $eventList.replaceWith(self._$loadedContent);
            });

            return $.when(this._super.apply(this, arguments), def);
        },
        destroy: function () {
            this._super.apply(this, arguments);
            if (this._$loadedContent) {
                this._$loadedContent.replaceWith(this._originalContent);
            }
        },
    });
});

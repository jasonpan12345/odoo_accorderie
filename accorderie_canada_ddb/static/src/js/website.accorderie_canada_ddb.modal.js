odoo.define("website.accorderie_canada_ddb.modal", function (require) {

    require('web_editor.ready');
    var Widget = require('web.Widget');
    var core = require('web.core');
    var QWeb = core.qweb;

    var modal = Widget.extend({
        xmlDependencies: ['/accorderie_canada_ddb/views/accorderie_pub_offre_modal.xml'],

        start: function () {
            console.log("start");
            var self = this;
            self.trigger_up('animation_stop_demand', {
                editableMode: true,
                $target: self.$target,
            });
            var res = this._super.apply(this.arguments).then(function () {
                $('.pub_offre_modal')
                    .off('click')
                    .click(function (ev) {
                        //self.on_click(ev, 1);
                        console.log("click");
                        self.$modal = $(QWeb.render("accorderie_canada_ddb.accorderie_pub_offre_modal.xml"));
                        self.$modal.appendTo('body').modal();
                    });
            });

        }
    })
});
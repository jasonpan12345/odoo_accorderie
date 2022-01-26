odoo.define("accorderie_canada_ddb.animation", function (require) {
    "use strict";

    var sAnimation = require("website.content.snippets.animation");

    sAnimation.registry.accorderie_canada_ddb = sAnimation.Class.extend({
        selector: ".o_accorderie_canada_ddb",

        start: function () {
            var self = this;
            var def = this._rpc({
                route: "/accorderie_canada_ddb/helloworld",
            }).then(function (data) {
                if (data.error) {
                    return;
                }

                if (_.isEmpty(data)) {
                    return;
                }

                if (data["commentaire"]) {
                    self.$(".commentaire_value").text(data["commentaire"]);
                }
                if (data["date_echange"]) {
                    self.$(".date_echange_value").text(data["date_echange"]);
                }
                if (data["demande_service"]) {
                    self.$(".demande_service_value").text(
                        data["demande_service"]
                    );
                }
                if (data["membre_acheteur"]) {
                    self.$(".membre_acheteur_value").text(
                        data["membre_acheteur"]
                    );
                }
                if (data["membre_vendeur"]) {
                    self.$(".membre_vendeur_value").text(
                        data["membre_vendeur"]
                    );
                }
                if (data["nb_heure"]) {
                    self.$(".nb_heure_value").text(data["nb_heure"]);
                }
                if (data["nom_complet"]) {
                    self.$(".nom_complet_value").text(data["nom_complet"]);
                }
                if (data["offre_service"]) {
                    self.$(".offre_service_value").text(data["offre_service"]);
                }
                if (data["point_service"]) {
                    self.$(".point_service_value").text(data["point_service"]);
                }
                if (data["remarque"]) {
                    self.$(".remarque_value").text(data["remarque"]);
                }
                if (data["type_echange"]) {
                    self.$(".type_echange_value").text(data["type_echange"]);
                }
            });

            return $.when(this._super.apply(this, arguments), def);
        },
    });
});

from odoo import _, api, models, fields, SUPERUSER_ID
import os
import logging

_logger = logging.getLogger(__name__)

MODULE_NAME = "accorderie_canada_ddb"


def post_init_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})

        # The path of the actual file
        path_module_generate = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "..")
        )

        short_name = MODULE_NAME.replace("_", " ").title()

        # TODO doc support compute
        # upper = fields.Char(compute='_compute_upper',
        #                     inverse='_inverse_upper',
        #                     search='_search_upper')
        #
        # @api.depends('name')
        # def _compute_upper(self):
        #     for rec in self:
        #         rec.upper = rec.name.upper() if rec.name else False

        # Add code generator
        categ_id = env["ir.module.category"].search(
            [("name", "=", "Uncategorized")]
        )
        value = {
            "shortdesc": "accorderie_canada_ddb",
            "name": MODULE_NAME,
            "license": "AGPL-3",
            "category_id": categ_id.id,
            "summary": "",
            "author": "TechnoLibre",
            "website": "",
            "application": True,
            "enable_sync_code": True,
            "path_sync_code": path_module_generate,
            "icon": os.path.join(
                os.path.dirname(__file__),
                "static",
                "description",
                "code_generator_icon.png",
            ),
        }

        # TODO HUMAN: enable your functionality to generate
        value["enable_sync_template"] = False
        value["ignore_fields"] = ""
        value["post_init_hook_show"] = False
        value["uninstall_hook_show"] = False
        value["post_init_hook_feature_code_generator"] = False
        value["uninstall_hook_feature_code_generator"] = False

        value["hook_constant_code"] = f'MODULE_NAME = "{MODULE_NAME}"'

        # Modification of field before migration

        # tbl_accorderie
        # TODO update _description
        add_update_migration_model(
            env,
            "accorderie",
            new_rec_name="nom",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "adresseaccorderie",
            new_field_name="adresse",
            new_string="Adresse",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "codepostalaccorderie",
            new_field_name="code_postal",
            new_string="Code postal",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "courrielaccorderie",
            new_field_name="courriel",
            new_string="Courriel",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "datemaj_accorderie",
            new_field_name="date_mise_a_jour",
            new_string="Dernière mise à jour",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "grpachat_accordeur",
            new_field_name="grp_achat_membre",
            new_string="Groupe d'achat membre",
            new_type="boolean",
            new_help="Rend accessible les achats pour les Accordeurs.",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "grpachat_admin",
            new_field_name="grp_achat_administrateur",
            new_string="Groupe d'achat pour administrateur",
            new_type="boolean",
            new_help="Rend accessible les achats pour les Accordeurs.",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "messageaccueil",
            new_field_name="message_accueil",
            new_string="Message accueil",
            new_type="html",
            new_help="Message à afficher pour l'Accueil des membres.",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "messagegrpachat",
            new_field_name="message_grp_achat",
            new_string="Message groupe achat",
            new_type="html",
            new_help="Message à afficher pour les groupes d'achat.",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "nonvisible",
            new_required=False,
            new_type="boolean",
            new_field_name="archive",
            new_string="Archivé",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "nomcomplet",
            new_field_name="nom_complet",
            new_string="Nom complet",
            delete=True,
        )
        add_update_migration_field(
            env,
            "accorderie",
            "noarrondissement",
            new_field_name="arrondissement",
            new_string="Arrondissement",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "nocartier",
            new_field_name="cartier",
            new_string="Cartier",
            delete=True,
        )
        add_update_migration_field(
            env,
            "accorderie",
            "noregion",
            new_field_name="region",
            new_string="Region",
            new_required=False,
            # add_one2many=True,
        )
        add_update_migration_field(
            env,
            "accorderie",
            "noville",
            new_field_name="ville",
            new_string="Ville",
            new_required=False,
            # add_one2many=True,
        )
        add_update_migration_field(
            env,
            "accorderie",
            "telaccorderie",
            new_field_name="telephone",
            new_string="Téléphone",
            force_widget="phone",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "telecopieuraccorderie",
            new_field_name="telecopieur",
            new_string="Télécopieur",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "url_logoaccorderie",
            new_field_name="logo",
            new_string="Logo",
            new_type="binary",
            force_widget="image",
            path_binary="/accorderie_canada/Intranet/images/logo",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "url_public_accorderie",
            new_field_name="url_public",
            new_string="Lien site web public",
            force_widget="link_button",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "url_transac_accorderie",
            new_field_name="url_transactionnel",
            new_string="Lien site web transactionnel",
            force_widget="link_button",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "noaccorderie",
            delete=True,
        )

        # tbl_achat_ponctuel
        # TODO create name from selected field
        # add_update_migration_model(
        #     env,
        #     "achat.ponctuel",
        #     new_rec_name="nom",
        # )
        add_update_migration_field(
            env,
            "achat.ponctuel",
            "dateachatponctuel",
            new_field_name="date_achat",
            new_string="Date d'achat",
        )
        add_update_migration_field(
            env,
            "achat.ponctuel",
            "achatponcfacturer",
            new_field_name="est_facture",
            new_string="Facturé",
        )
        add_update_migration_field(
            env,
            "achat.ponctuel",
            "datemaj_achantponct",
            new_field_name="date_mise_a_jour",
            new_string="Dernière mise à jour",
        )
        add_update_migration_field(
            env,
            "achat.ponctuel",
            "majoration_achatponct",
            new_field_name="majoration",
            new_string="Majoration",
        )
        add_update_migration_field(
            env,
            "achat.ponctuel",
            "montantpaiementachatponct",
            new_field_name="paiement_effectue",
            new_string="Paiement effectué",
        )
        add_update_migration_field(
            env,
            "achat.ponctuel",
            "noachatponctuel",
            delete=True,
        )
        add_update_migration_field(
            env,
            "achat.ponctuel",
            "nomembre",
            new_field_name="membre",
            new_string="Membre",
        )
        add_update_migration_field(
            env,
            "achat.ponctuel",
            "taxef_achatponct",
            new_field_name="taxe_federal",
            new_string="Taxe fédéral",
        )
        add_update_migration_field(
            env,
            "achat.ponctuel",
            "taxep_achatponct",
            new_field_name="taxe_provincial",
            new_string="Taxe provincial",
        )

        # tbl_achat_ponctuel_produit
        # TODO create name from selected field
        # add_update_migration_model(
        #     env,
        #     "achat.ponctuel.produit",
        #     new_rec_name="nom",
        # )
        # add_update_migration_field(
        #     env,
        #     "achat.ponctuel",
        #     "taxep_achatponct",
        #     new_field_name="taxe_provincial",
        #     new_string="provincial",
        # )

        # tbl_arrondissement
        add_update_migration_model(
            env,
            "arrondissement",
            new_rec_name="nom",
        )
        add_update_migration_field(
            env,
            "arrondissement",
            "arrondissement",
            new_field_name="nom",
            new_string="Nom",
        )
        add_update_migration_field(
            env,
            "arrondissement",
            "noville",
            new_field_name="ville",
            new_string="Ville",
        )
        add_update_migration_field(
            env,
            "arrondissement",
            "noarrondissement",
            delete=True,
        )

        # tbl_cartier
        # TODO rename cartier pour quartier
        add_update_migration_model(
            env,
            "cartier",
            new_rec_name="nom",
        )
        add_update_migration_field(
            env,
            "cartier",
            "nocartier",
            delete=True,
        )
        add_update_migration_field(
            env,
            "cartier",
            "noarrondissement",
            new_field_name="arrondissement",
            new_string="Arrondissement",
            new_help="Arrondissement associé au quartier",
        )
        add_update_migration_field(
            env,
            "cartier",
            "cartier",
            new_field_name="nom",
            new_string="Nom du quartier",
            new_help="Nom du quartier",
        )

        # tbl_categorie
        add_update_migration_model(
            env,
            "categorie",
            new_rec_name="nom",
        )
        add_update_migration_field(
            env,
            "categorie",
            "nocategorie",
            delete=True,
        )
        add_update_migration_field(
            env,
            "categorie",
            "titrecategorie",
            new_field_name="nom",
            new_string="Nom de la catégorie",
            new_help="Le nom de la catégorie",
        )
        add_update_migration_field(
            env,
            "categorie",
            "supprimer",
            new_field_name="archive",
            new_string="Archivé",
            new_type="boolean",
            new_help="Permet d'archiver cette entrée",
        )
        add_update_migration_field(
            env,
            "categorie",
            "approuver",
            new_field_name="approuve",
            new_string="Approuvé",
            new_type="boolean",
            new_help="Permet d'approuver cette entrée",
        )

        # tbl_categorie_sous_categorie
        # TODO

        # tbl_commande
        add_update_migration_field(
            env,
            "commande",
            "nocommande",
            new_required=False,
        )

        # tbl_commande_membre
        add_update_migration_field(
            env,
            "commande.membre",
            "nocommande",
            new_required=False,
        )
        add_update_migration_field(
            env,
            "commande.membre",
            "nomembre",
            new_required=False,
        )

        # tbl_commande_membre_produit
        # TODO

        # tbl_commentaire
        # TODO

        # tbl_demande_service
        # TODO

        # tbl_dmd_adhesion
        # TODO

        # tbl_droits_admin
        add_update_migration_field(
            env,
            "droits.admin",
            "nomembre",
            new_required=False,
        )

        # tbl_echange_service
        # add_update_migration_model(env, "region", new_rec_name="nom")
        add_update_migration_field(
            env,
            "echange.service",
            "nbheure",
            new_field_name="nb_heure",
            new_string="Nombre d'heure",
            new_help="Nombre d'heure effectué au moment de l'échange.",
            force_widget="float_time",
        )

        # tbl_fichier
        # TODO

        # tbl_fournisseur
        # TODO

        # tbl_fournisseur_produit
        add_update_migration_field(
            env,
            "fournisseur.produit",
            "nofournisseur",
            new_required=False,
        )

        # tbl_fournisseur_produit_commande
        add_update_migration_field(
            env,
            "fournisseur.produit.commande",
            "nocommande",
            new_required=False,
        )

        # tbl_fournisseur_produit_pointservice
        # TODO

        # tbl_info_logiciel_bd
        # TODO

        # tbl_log_access
        # TODO

        # tbl_membre
        add_update_migration_model(env, "membre", new_rec_name="nom")
        add_update_migration_field(
            env,
            "membre",
            "noaccorderie",
            new_field_name="accorderie",
            new_string="Accorderie",
            new_help="Accorderie associé",
            # add_one2many=True,
        )
        add_update_migration_field(
            env,
            "membre",
            "nopointservice",
            new_field_name="point_service",
            new_string="Point de service",
            new_help="Point de service associé",
            # add_one2many=True,
        )

        # tbl_mensualite
        # TODO

        # tbl_occupation
        # TODO

        # tbl_offre_service_membre
        # TODO

        # tbl_origine
        # TODO

        # tbl_point_service
        add_update_migration_model(env, "pointservice", new_rec_name="nom")
        add_update_migration_field(
            env,
            "pointservice",
            "nompointservice",
            new_field_name="nom",
            new_string="Nom",
            new_help="Nom du point de service",
        )
        add_update_migration_field(
            env,
            "pointservice",
            "nopointservice",
            delete=True,
        )
        add_update_migration_field(
            env,
            "pointservice",
            "nomembre",
            new_field_name="membre",
            new_string="Organisateur",
            new_help="Organisateur du point de service",
        )

        # tbl_pointservice_fournisseur
        # TODO

        # tbl_pret
        # TODO

        # tbl_produit
        # TODO

        # tbl_provenance
        # TODO

        # tbl_region
        add_update_migration_model(env, "region", new_rec_name="nom")
        add_update_migration_field(
            env,
            "region",
            "noregion",
            new_field_name="code",
            new_string="Code de région",
            new_help="Code de la région administrative",
        )
        add_update_migration_field(
            env,
            "region",
            "region",
            new_field_name="nom",
            new_string="Nom",
        )

        # tbl_revenu_familial
        # TODO

        # tbl_sous_categorie
        # TODO

        # tbl_taxe
        # TODO

        # tbl_titre
        # TODO

        # tbl_type_communication
        # TODO

        # tbl_type_compte
        add_update_migration_field(
            env,
            "type.compte",
            "nomembre",
            new_required=False,
        )

        # tbl_type_fichier
        # TODO

        # tbl_type_tel
        # TODO

        # tbl_versement
        # TODO

        # tbl_ville
        add_update_migration_model(env, "ville", new_rec_name="nom")
        add_update_migration_field(
            env,
            "ville",
            "noville",
            new_field_name="code",
            new_string="Code",
            new_help="Code de la ville",
        )
        add_update_migration_field(
            env,
            "ville",
            "ville",
            new_field_name="nom",
            new_string="Nom",
        )
        add_update_migration_field(
            env,
            "ville",
            "noregion",
            new_field_name="region",
            new_string="Région",
            # add_one2many=True,
        )
        # TODO not supported
        # add_update_migration_field(
        #     env,
        #     "ville",
        #     "accorderie_ids",
        #     new_string="Accorderie",
        #     new_help="Liste des Accorderie dans cette ville",
        #     add_one2many=True,
        # )

        # Database
        value_db = {
            "m2o_dbtype": env.ref(
                "code_generator_db_servers.code_generator_db_type_mysql"
            ).id,
            "database": "accorderie_log_2019",
            "host": "localhost",
            "port": 3306,
            "user": "accorderie",
            "password": "accorderie",
            "schema": "public",
            "accept_primary_key": True,
        }
        code_generator_db_server_id = env["code.generator.db"].create(value_db)

        code_generator_db_tables = (
            env["code.generator.db.table"]
            .search([])
            .filtered(lambda x: x.name.startswith("tbl_"))
        )

        lst_nomenclator = (
            # "tbl_accorderie",
            # # "tbl_achat_ponctuel",
            # # "tbl_achat_ponctuel_produit",
            "tbl_region",
            "tbl_ville",
            "tbl_arrondissement",
            "tbl_cartier",
            "tbl_categorie",
            "tbl_categorie_sous_categorie",
            # # "tbl_commande",
            # # "tbl_commande_membre",
            # # "tbl_commande_membre_produit",
            # # "tbl_commentaire",
            # # "tbl_demande_service",
            # # "tbl_dmd_adhesion",
            # # "tbl_droits_admin",
            # # "tbl_echange_service",
            # "tbl_fichier",
            # # "tbl_fournisseur",
            # # "tbl_fournisseur_produit",
            # # "tbl_fournisseur_produit_commande",
            # # "tbl_fournisseur_produit_pointservice",
            # "tbl_info_logiciel_bd",
            # # "tbl_log_acces",
            # "tbl_membre",
            # "tbl_mensualite",
            "tbl_occupation",
            # # "tbl_offre_service_membre",
            "tbl_origine",
            # "tbl_pointservice",
            # # "tbl_pointservice_fournisseur",
            # "tbl_pret",
            # # "tbl_produit",
            "tbl_provenance",
            "tbl_revenu_familial",
            "tbl_situation_maison",
            "tbl_sous_categorie",
            "tbl_taxe",
            "tbl_titre",
            "tbl_type_communication",
            # # "tbl_type_compte",
            "tbl_type_fichier",
            "tbl_type_tel",
            # "tbl_versement",
        )
        # lst_nomenclator = []
        # tbl_accorderie_id = None

        if lst_nomenclator:
            for db_table_id in code_generator_db_tables:
                if db_table_id.name in lst_nomenclator:
                    db_table_id.nomenclator = True

        # TODO generate code.generator.module before running generation
        code_generator_id = code_generator_db_tables.generate_module(
            generated_module_name=MODULE_NAME,
        )

        code_generator_id.shortdesc = "accorderie_canada_ddb"
        code_generator_id.name = MODULE_NAME
        code_generator_id.license = "AGPL-3"
        code_generator_id.category_id = categ_id.id
        code_generator_id.summary = ""
        code_generator_id.author = "TechnoLibre"
        code_generator_id.website = ""
        code_generator_id.application = True
        code_generator_id.enable_sync_code = True
        code_generator_id.path_sync_code = path_module_generate
        code_generator_id.icon = os.path.join(
            os.path.dirname(__file__),
            "static",
            "description",
            "code_generator_icon.png",
        )

        # Generate view
        # Action generate view
        wizard_view = env["code.generator.generate.views.wizard"].create(
            {
                "code_generator_id": code_generator_id.id,
                "enable_generate_all": True,
            }
        )

        wizard_view.button_generate_views()

        # Generate module
        value = {"code_generator_ids": code_generator_id.ids}
        env["code.generator.writer"].create(value)


def add_update_migration_field(
    env,
    model_name,
    field_name,
    new_field_name=None,
    new_string=None,
    new_type=None,
    new_help=None,
    new_required=None,
    delete=False,
    path_binary=None,
    force_widget=None,
    add_one2many=False,
):

    value = {
        "model_name": model_name,
        "field_name": field_name,
    }
    if delete:
        value["delete"] = True
    elif (
        new_field_name is None
        and new_string is None
        and new_type is None
        and new_help is None
        and new_required is None
    ):
        # Don't add an update with no information
        return
    else:
        if new_field_name is not None:
            value["new_field_name"] = new_field_name
        if new_string is not None:
            value["new_string"] = new_string
        if new_type is not None:
            value["new_type"] = new_type
        if new_help is not None:
            value["new_help"] = new_help
        if new_required is not None:
            value["new_required"] = new_required
            value["new_change_required"] = True
        if path_binary is not None:
            value["path_binary"] = path_binary
        if force_widget is not None:
            value["force_widget"] = force_widget
        if add_one2many:
            value["add_one2many"] = add_one2many
    env["code.generator.db.update.migration.field"].create(value)


def add_update_migration_model(
    env,
    model_name,
    new_model_name=None,
    new_rec_name=None,
):

    value = {
        "model_name": model_name,
    }
    if new_model_name is not None:
        value["new_model_name"] = new_model_name
    if new_rec_name is not None:
        value["new_rec_name"] = new_rec_name
    env["code.generator.db.update.migration.model"].create(value)


def update_field(
    env,
    model_name,
    field_name,
    new_field_name=None,
    new_string=None,
    new_type=None,
    new_help=None,
    new_required=None,
):
    field = env["ir.model.fields"].search(
        [("name", "=", field_name), ("model", "=", model_name)]
    )
    if field and len(field) == 1:
        if new_field_name is not None:
            field.name = new_field_name
        if new_string is not None:
            field.field_description = new_string
        if new_required is not None:
            field.required = new_required
        if new_help is not None:
            field.help = new_help
        if new_type is not None:
            field.ttype = new_type
    else:
        _logger.warning(
            f"Cannot find field {field_name} from table {model_name}"
        )


def uninstall_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        code_generator_id = env["code.generator.module"].search(
            [("name", "=", MODULE_NAME)]
        )
        if code_generator_id:
            code_generator_id.unlink()

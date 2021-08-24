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

        # Add code generator
        categ_id = env["ir.module.category"].search(
            [("name", "=", "Uncategorized")]
        )
        value = {
            "shortdesc": short_name,
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

        code_generator_id = env["code.generator.module"].create(value)

        # Local variable to add update information
        migration = MigrationDB(env, code_generator_id)

        # Modification of field before migration

        # tbl_accorderie
        # TODO update _description
        migration.add_update_migration_model(
            "accorderie",
            new_rec_name="nom",
            new_description=(
                "Gestion des entitées Accorderie, contient les informations et"
                " les messages d'une Accorderie."
            ),
        )
        migration.add_update_migration_field(
            "accorderie",
            "adresseaccorderie",
            new_field_name="adresse",
            new_string="Adresse",
        )
        migration.add_update_migration_field(
            "accorderie",
            "codepostalaccorderie",
            new_field_name="code_postal",
            new_string="Code postal",
        )
        migration.add_update_migration_field(
            "accorderie",
            "courrielaccorderie",
            new_field_name="courriel",
            new_string="Courriel",
        )
        migration.add_update_migration_field(
            "accorderie",
            "datemaj_accorderie",
            new_field_name="date_mise_a_jour",
            new_string="Dernière mise à jour",
        )
        migration.add_update_migration_field(
            "accorderie",
            "grpachat_accordeur",
            new_field_name="grp_achat_membre",
            new_string="Groupe d'achat membre",
            new_type="boolean",
            new_help="Rend accessible les achats pour les Accordeurs.",
        )
        migration.add_update_migration_field(
            "accorderie",
            "grpachat_admin",
            new_field_name="grp_achat_administrateur",
            new_string="Groupe d'achat pour administrateur",
            new_type="boolean",
            new_help="Rend accessible les achats pour les Accordeurs.",
        )
        migration.add_update_migration_field(
            "accorderie",
            "messageaccueil",
            new_field_name="message_accueil",
            new_string="Message accueil",
            new_type="html",
            new_help="Message à afficher pour l'Accueil des membres.",
        )
        migration.add_update_migration_field(
            "accorderie",
            "messagegrpachat",
            new_field_name="message_grp_achat",
            new_string="Message groupe achat",
            new_type="html",
            new_help="Message à afficher pour les groupes d'achat.",
        )
        migration.add_update_migration_field(
            "accorderie",
            "nonvisible",
            new_required=False,
            new_type="boolean",
            new_field_name="archive",
            new_string="Archivé",
        )
        migration.add_update_migration_field(
            "accorderie",
            "nomcomplet",
            new_field_name="nom_complet",
            new_string="Nom complet",
            delete=True,
        )
        migration.add_update_migration_field(
            "accorderie",
            "nom",
            new_required=True,
        )
        migration.add_update_migration_field(
            "accorderie",
            "noarrondissement",
            new_field_name="arrondissement",
            new_string="Arrondissement",
        )
        migration.add_update_migration_field(
            "accorderie",
            "nocartier",
            new_field_name="cartier",
            new_string="Cartier",
            delete=True,
        )
        migration.add_update_migration_field(
            "accorderie",
            "noregion",
            new_field_name="region",
            new_string="Region",
            new_required=False,
            # add_one2many=True,
        )
        migration.add_update_migration_field(
            "accorderie",
            "noville",
            new_field_name="ville",
            new_string="Ville",
            new_required=False,
            # add_one2many=True,
        )
        migration.add_update_migration_field(
            "accorderie",
            "telaccorderie",
            new_field_name="telephone",
            new_string="Téléphone",
            force_widget="phone",
        )
        migration.add_update_migration_field(
            "accorderie",
            "telecopieuraccorderie",
            new_field_name="telecopieur",
            new_string="Télécopieur",
        )
        migration.add_update_migration_field(
            "accorderie",
            "url_logoaccorderie",
            new_field_name="logo",
            new_string="Logo",
            new_type="binary",
            force_widget="image",
            path_binary="/accorderie_canada/Intranet/images/logo",
        )
        migration.add_update_migration_field(
            "accorderie",
            "url_public_accorderie",
            new_field_name="url_public",
            new_string="Lien site web public",
            force_widget="link_button",
        )
        migration.add_update_migration_field(
            "accorderie",
            "url_transac_accorderie",
            new_field_name="url_transactionnel",
            new_string="Lien site web transactionnel",
            force_widget="link_button",
        )
        migration.add_update_migration_field(
            "accorderie",
            "noaccorderie",
            delete=True,
        )

        # tbl_achat_ponctuel
        # TODO create name from selected field
        # migration.add_update_migration_model(
        #     "achat.ponctuel",
        #     new_rec_name="nom",
        # )
        migration.add_update_migration_field(
            "achat.ponctuel",
            "dateachatponctuel",
            new_field_name="date_achat",
            new_string="Date d'achat",
        )
        migration.add_update_migration_field(
            "achat.ponctuel",
            "achatponcfacturer",
            new_field_name="est_facture",
            new_string="Facturé",
        )
        migration.add_update_migration_field(
            "achat.ponctuel",
            "datemaj_achantponct",
            new_field_name="date_mise_a_jour",
            new_string="Dernière mise à jour",
        )
        migration.add_update_migration_field(
            "achat.ponctuel",
            "majoration_achatponct",
            new_field_name="majoration",
            new_string="Majoration",
        )
        migration.add_update_migration_field(
            "achat.ponctuel",
            "montantpaiementachatponct",
            new_field_name="paiement_effectue",
            new_string="Paiement effectué",
        )
        migration.add_update_migration_field(
            "achat.ponctuel",
            "noachatponctuel",
            delete=True,
        )
        migration.add_update_migration_field(
            "achat.ponctuel",
            "nomembre",
            new_field_name="membre",
            new_string="Membre",
        )
        migration.add_update_migration_field(
            "achat.ponctuel",
            "taxef_achatponct",
            new_field_name="taxe_federal",
            new_string="Taxe fédéral",
        )
        migration.add_update_migration_field(
            "achat.ponctuel",
            "taxep_achatponct",
            new_field_name="taxe_provincial",
            new_string="Taxe provincial",
        )

        # tbl_achat_ponctuel_produit
        # TODO create name from selected field
        # migration.add_update_migration_model(
        #     "achat.ponctuel.produit",
        #     new_rec_name="nom",
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel",
        #     "taxep_achatponct",
        #     new_field_name="taxe_provincial",
        #     new_string="provincial",
        # )

        # tbl_arrondissement
        migration.add_update_migration_model(
            "arrondissement",
            new_rec_name="nom",
        )
        migration.add_update_migration_field(
            "arrondissement",
            "arrondissement",
            new_field_name="nom",
            new_string="Nom",
        )
        migration.add_update_migration_field(
            "arrondissement",
            "noville",
            new_field_name="ville",
            new_string="Ville",
            # add_one2many=True,
        )
        migration.add_update_migration_field(
            "arrondissement",
            "noarrondissement",
            delete=True,
        )

        # tbl_cartier
        # TODO rename cartier pour quartier
        migration.add_update_migration_model(
            "cartier",
            new_rec_name="nom",
        )
        migration.add_update_migration_field(
            "cartier",
            "nocartier",
            delete=True,
        )
        migration.add_update_migration_field(
            "cartier",
            "noarrondissement",
            new_field_name="arrondissement",
            new_string="Arrondissement",
            new_help="Arrondissement associé au quartier",
        )
        migration.add_update_migration_field(
            "cartier",
            "cartier",
            new_field_name="nom",
            new_string="Nom du quartier",
            new_help="Nom du quartier",
        )

        # tbl_categorie
        migration.add_update_migration_model(
            "categorie",
            new_rec_name="nom",
        )
        migration.add_update_migration_field(
            "categorie",
            "nocategorie",
            delete=True,
        )
        migration.add_update_migration_field(
            "categorie",
            "titrecategorie",
            new_field_name="nom",
            new_string="Nom de la catégorie",
            new_help="Le nom de la catégorie",
        )
        migration.add_update_migration_field(
            "categorie",
            "supprimer",
            new_field_name="archive",
            new_string="Archivé",
            new_type="boolean",
            new_help="Permet d'archiver cette catégorie.",
        )
        migration.add_update_migration_field(
            "categorie",
            "approuver",
            new_field_name="approuve",
            new_string="Approuvé",
            new_type="boolean",
            new_help="Permet d'approuver cette catégorie.",
        )

        # tbl_categorie_sous_categorie
        # TODO

        # tbl_commande
        migration.add_update_migration_field(
            "commande",
            "nocommande",
            new_required=False,
        )

        # tbl_commande_membre
        migration.add_update_migration_field(
            "commande.membre",
            "nocommande",
            new_required=False,
        )
        migration.add_update_migration_field(
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
        migration.add_update_migration_field(
            "droits.admin",
            "nomembre",
            new_required=False,
        )

        # tbl_echange_service
        # migration.add_update_migration_model("region", new_rec_name="nom")
        migration.add_update_migration_field(
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
        migration.add_update_migration_field(
            "fournisseur.produit",
            "nofournisseur",
            new_required=False,
        )

        # tbl_fournisseur_produit_commande
        migration.add_update_migration_field(
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
        # TODO change rec_name to display_name with compute of nom et prenom
        migration.add_update_migration_model("membre", new_rec_name="nom")
        migration.add_update_migration_field(
            "membre",
            "noaccorderie",
            new_field_name="accorderie",
            new_string="Accorderie",
            new_help="Accorderie associé",
            # add_one2many=True,
        )
        migration.add_update_migration_field(
            "membre",
            "nopointservice",
            new_field_name="point_service",
            new_string="Point de service",
            new_help="Point de service associé",
            # add_one2many=True,
        )
        migration.add_update_migration_field(
            "membre",
            "nom",
            new_required=True,
        )
        migration.add_update_migration_field(
            "membre",
            "motdepasse",
            ignore_field=True,
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
        migration.add_update_migration_model(
            "pointservice", new_rec_name="nom"
        )
        migration.add_update_migration_field(
            "pointservice",
            "nompointservice",
            new_field_name="nom",
            new_string="Nom",
            new_help="Nom du point de service",
        )
        migration.add_update_migration_field(
            "pointservice",
            "nopointservice",
            delete=True,
        )
        migration.add_update_migration_field(
            "pointservice",
            "nomembre",
            new_field_name="membre",
            new_string="Organisateur",
            new_help="Organisateur du point de service",
            # add_one2many=True,
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
        migration.add_update_migration_model("region", new_rec_name="nom")
        migration.add_update_migration_field(
            "region",
            "noregion",
            new_field_name="code",
            new_string="Code de région",
            new_help="Code de la région administrative",
        )
        migration.add_update_migration_field(
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
        migration.add_update_migration_field(
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
        migration.add_update_migration_model("ville", new_rec_name="nom")
        migration.add_update_migration_field(
            "ville",
            "noville",
            new_field_name="code",
            new_string="Code",
            new_help="Code de la ville",
        )
        migration.add_update_migration_field(
            "ville",
            "ville",
            new_field_name="nom",
            new_string="Nom",
        )
        migration.add_update_migration_field(
            "ville",
            "noregion",
            new_field_name="region",
            new_string="Région",
            # add_one2many=True,
        )
        # TODO not supported
        # migration.add_update_migration_field(
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

        code_generator_id = code_generator_db_tables.generate_module(
            code_generator_id=code_generator_id
        )

        # Add new field
        model_membre_id = env["ir.model"].search([("model", "=", "membre")])
        value_field_nom_complet_membre = {
            "name": "nom_complet",
            "field_description": "Nom complet",
            "ttype": "char",
            "code_generator_compute": "_compute_nom_complet",
            "model_id": model_membre_id.id,
        }
        env["ir.model.fields"].create(value_field_nom_complet_membre)

        # Add code
        lst_value = [
            {
                "code": """for rec in self:
    if self.nom and self.prenom:
        rec.nom_complet = f"{self.prenom} {self.nom}"
    elif self.nom:
        rec.nom_complet = f"{self.nom}"
    elif self.prenom:
        rec.nom_complet = f"{self.prenom}"
    else:
        rec.nom_complet = False
    """,
                "name": "_compute_nom_complet",
                "decorator": '@api.depends("nom", "prenom")',
                "param": "self",
                "sequence": 1,
                "m2o_module": code_generator_id.id,
                "m2o_model": model_membre_id.id,
            },
        ]
        env["code.generator.model.code"].create(lst_value)

        model_membre_id.rec_name = "nom_complet"

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


class MigrationDB:
    def __init__(self, env, code_generator_id):
        self.env = env
        self.code_generator_id = code_generator_id

    def add_update_migration_field(
        self,
        model_name,
        field_name,
        new_field_name=None,
        new_string=None,
        new_type=None,
        new_help=None,
        new_required=None,
        delete=False,
        ignore_field=False,
        path_binary=None,
        force_widget=None,
        add_one2many=False,
    ):
        """

        :param model_name:
        :param field_name:
        :param new_field_name:
        :param new_string:
        :param new_type:
        :param new_help:
        :param new_required:
        :param delete: import data, use to compute information but delete the field at the end with his data
        :param ignore_field: never compute it and ignore data from it
        :param path_binary: path for type binary when the past was char
        :param force_widget:
        :param add_one2many:
        :return:
        """

        value = {
            "model_name": model_name,
            "field_name": field_name,
            "code_generator_id": self.code_generator_id.id,
        }
        if delete:
            value["delete"] = True
        elif ignore_field:
            value["ignore_field"] = True
        elif (
            new_field_name is None
            and new_string is None
            and new_type is None
            and new_help is None
            and new_required is None
            and force_widget is None
            and add_one2many is None
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
        self.env["code.generator.db.update.migration.field"].create(value)

    def add_update_migration_model(
        self,
        model_name,
        new_model_name=None,
        new_description=None,
        new_rec_name=None,
    ):

        value = {
            "model_name": model_name,
            "code_generator_id": self.code_generator_id.id,
        }
        if new_model_name is not None:
            value["new_model_name"] = new_model_name
        if new_description is not None:
            value["new_description"] = new_description
        if new_rec_name is not None:
            value["new_rec_name"] = new_rec_name
        self.env["code.generator.db.update.migration.model"].create(value)


def uninstall_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        code_generator_id = env["code.generator.module"].search(
            [("name", "=", MODULE_NAME)]
        )
        if code_generator_id:
            code_generator_id.unlink()

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
        add_update_migration_model(
            env,
            "accorderie",
            new_rec_name="nom",
        )
        add_update_migration_field(
            env,
            "accorderie",
            "adresseaccorderie",
            new_field_name="address",
            new_string="Address",
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
            new_field_name="date_update",
            new_string="Last update",
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
            env, "accorderie", "nonvisible", new_required=False
        )
        add_update_migration_field(
            env, "membre", "nopointservice", new_field_name="Cabanon"
        )
        # add_update_migration_field(
        #     env,
        #     "accorderie",
        #     "adresseaccorderie",
        #     new_field_name="address",
        #     new_string="Address",
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
                    # if db_table_id.name == "tbl_accorderie":
                    #     tbl_accorderie_id = db_table_id

        # Update fields correction
        # if tbl_accorderie_id is not None:
        #     for column in tbl_accorderie_id.o2m_columns:
        #         if column.name == "nonvisible":
        #             column.required = False
        #         elif column.name in ("messageaccueil", "messagegrpachat"):
        #             column.column_type = "html"
        #
        #     field_nonvisible = env["code.generator.db.column"].search(
        #         [("name", "=", "nonvisible"), ("m2o_table", "=", tbl_accorderie_id.id)]
        #     )
        #     if field_nonvisible and len(field_nonvisible) == 1:
        #         field_nonvisible.required = False
        #         v = {
        #             "id": field_nonvisible.id,
        #             "required": False,
        #         }
        #         env["code.generator.db.column"].write(v)
        #     else:
        #         _logger.warning(
        #             "Cannot find field nonvisible from table accorderie."
        #         )
        #
        #     field_messageaccueil = env["code.generator.db.column"].search(
        #         [("name", "=", "messageaccueil"), ("m2o_table", "=", tbl_accorderie_id.id)]
        #     )
        #     if field_messageaccueil and len(field_messageaccueil) == 1:
        #         field_messageaccueil.column_type = "html"
        #     else:
        #         _logger.warning(
        #             "Cannot find field messageaccueil from table accorderie."
        #         )
        #
        #     field_messagegrpachat = env["code.generator.db.column"].search(
        #         [("name", "=", "messagegrpachat"), ("m2o_table", "=", tbl_accorderie_id.id)]
        #     )
        #     if field_messagegrpachat and len(field_messagegrpachat) == 1:
        #         field_messagegrpachat.column_type = "html"
        #     else:
        #         _logger.warning(
        #             "Cannot find field messagegrpachat from table accorderie."
        #         )
        # else:
        #     _logger.warning(
        #         "Cannot find table tbl_accorderie"
        #     )

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

        # Fix model
        # Accorderie
        # update_field(env, "commande", "nocommande", new_required=False)
        # update_field(env, "commande.membre", "nocommande", new_required=False)
        # update_field(env, "commande.membre", "nomembre", new_required=False)
        # update_field(env, "droits.admin", "nomembre", new_required=False)
        # update_field(
        #     env, "fournisseur.produit", "nofournisseur", new_required=False
        # )
        # update_field(
        #     env,
        #     "fournisseur.produit.commande",
        #     "nocommande",
        #     new_required=False,
        # )
        # update_field(env, "type.compte", "nomembre", new_required=False)

        # change ttype is not supported
        # field_messageaccueil = env["ir.model.fields"].search(
        #     [("name", "=", "messageaccueil"), ("model", "=", "accorderie")]
        # )
        # if field_messageaccueil and len(field_messageaccueil) == 1:
        #     field_messageaccueil.ttype = "html"
        # else:
        #     _logger.warning(
        #         "Cannot find field messageaccueil from table accorderie."
        #     )
        #
        # field_messagegrpachat = env["ir.model.fields"].search(
        #     [("name", "=", "messagegrpachat"), ("model", "=", "accorderie")]
        # )
        # if field_messagegrpachat and len(field_messagegrpachat) == 1:
        #     field_messagegrpachat.ttype = "html"
        # else:
        #     _logger.warning(
        #         "Cannot find field messagegrpachat from table accorderie."
        #     )

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
):

    value = {
        "model_name": model_name,
        "field_name": field_name,
    }
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

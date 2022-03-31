import os

from odoo import SUPERUSER_ID, _, api, fields, models

# TODO HUMAN: change my module_name to create a specific demo functionality
MODULE_NAME = "code_generator_accorderie_canada_ddb"


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
            "website": "https://technolibre.ca",
            "application": True,
            "enable_sync_code": True,
            "path_sync_code": path_module_generate,
        }

        # TODO HUMAN: enable your functionality to generate
        value["enable_template_code_generator_demo"] = False
        value["template_model_name"] = (
            "accorderie.accorderie; accorderie.arrondissement;"
            " accorderie.commentaire; accorderie.demande.adhesion;"
            " accorderie.demande.service; accorderie.droits.admin;"
            " accorderie.echange.service; accorderie.fichier;"
            " accorderie.membre; accorderie.occupation;"
            " accorderie.offre.service; accorderie.origine;"
            " accorderie.point.service; accorderie.provenance;"
            " accorderie.quartier; accorderie.region;"
            " accorderie.revenu.familial; accorderie.situation.maison;"
            " accorderie.type.communication; accorderie.type.compte;"
            " accorderie.type.fichier; accorderie.type.service;"
            " accorderie.type.service.categorie;"
            " accorderie.type.service.sous.categorie;"
            " accorderie.type.telephone; accorderie.ville"
        )
        value["template_inherit_model_name"] = ""
        value["enable_template_wizard_view"] = True
        value["force_generic_template_wizard_view"] = False
        value["enable_template_website_snippet_view"] = False
        value["enable_sync_template"] = True
        value["enable_cg_generate_portal"] = True
        value["enable_cg_portal_enable_create"] = True
        value["ignore_fields"] = ""
        value[
            "template_module_path_generated_extension"
        ] = "'..', 'TechnoLibre_odoo_accorderie'"
        value["post_init_hook_show"] = True
        value["uninstall_hook_show"] = True
        value["post_init_hook_feature_code_generator"] = True
        value["uninstall_hook_feature_code_generator"] = True

        new_module_name = MODULE_NAME
        if (
            MODULE_NAME != "code_generator_demo"
            and "code_generator_" in MODULE_NAME
        ):
            if "code_generator_template" in MODULE_NAME:
                if value["enable_template_code_generator_demo"]:
                    new_module_name = f"code_generator_{MODULE_NAME[len('code_generator_template_'):]}"
                else:
                    new_module_name = MODULE_NAME[
                        len("code_generator_template_") :
                    ]
            else:
                new_module_name = MODULE_NAME[len("code_generator_") :]
            value["template_module_name"] = new_module_name
        value["hook_constant_code"] = f'MODULE_NAME = "{new_module_name}"'

        code_generator_id = env["code.generator.module"].create(value)

        # Add dependencies
        # TODO HUMAN: update your dependencies
        lst_depend = [
            "code_generator",
            "code_generator_hook",
        ]
        code_generator_id.add_module_dependency(lst_depend)

        # Generate module
        value = {"code_generator_ids": code_generator_id.ids}
        env["code.generator.writer"].create(value)


def uninstall_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        code_generator_id = env["code.generator.module"].search(
            [("name", "=", MODULE_NAME)]
        )
        if code_generator_id:
            code_generator_id.unlink()

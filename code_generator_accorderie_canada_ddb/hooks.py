from odoo import _, api, models, fields, SUPERUSER_ID
import os
import logging

_logger = logging.getLogger(__name__)

MODULE_NAME = "accorderie_canada_ddb"
# SECRET_PASSWORD = ""


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
        # TODO manque de . dans le help
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
            "noaccorderie",
            delete=True,
        )
        migration.add_update_migration_field(
            "accorderie",
            "noregion",
            new_field_name="region",
            new_string="Région administrative",
            new_required=False,
            new_help="Nom de la région administrative de l'Accorderie",
            # add_one2many=True,
        )
        migration.add_update_migration_field(
            "accorderie",
            "noville",
            new_field_name="ville",
            new_string="Ville",
            new_required=False,
            new_help="Nom de la ville de l'Accorderie",
            # add_one2many=True,
        )
        migration.add_update_migration_field(
            "accorderie",
            "noarrondissement",
            new_field_name="arrondissement",
            new_string="Arrondissement",
            new_help="Nom de l'Arrondissement qui contient l'Accorderie",
        )
        migration.add_update_migration_field(
            "accorderie",
            "nocartier",
            # new_field_name="cartier",
            # new_string="Cartier",
            delete=True,
        )
        migration.add_update_migration_field(
            "accorderie",
            "nom",
            new_required=True,
            new_help="Nom de l'Accorderie",
        )
        migration.add_update_migration_field(
            "accorderie",
            "nomcomplet",
            # new_field_name="nom_complet",
            # new_string="Nom complet",
            delete=True,
        )
        migration.add_update_migration_field(
            "accorderie",
            "adresseaccorderie",
            new_field_name="adresse",
            new_string="Adresse",
            new_help="Adresse de l'Accorderie",
        )
        migration.add_update_migration_field(
            "accorderie",
            "codepostalaccorderie",
            new_field_name="code_postal",
            new_string="Code postal",
            new_help="Code postal de l'Accorderie",
        )
        migration.add_update_migration_field(
            "accorderie",
            "telaccorderie",
            new_field_name="telephone",
            new_string="Téléphone",
            new_help="Numéro de téléphone pour joindre l'Accorderie",
        )
        migration.add_update_migration_field(
            "accorderie",
            "telecopieuraccorderie",
            new_field_name="telecopieur",
            new_string="Télécopieur",
            new_help="Numéro de télécopieur pour joindre l'Accorderie",
        )
        migration.add_update_migration_field(
            "accorderie",
            "courrielaccorderie",
            new_field_name="courriel",
            new_string="Adresse courriel pour joindre l'Accorderie",
        )
        migration.add_update_migration_field(
            "accorderie",
            "messagegrpachat",
            new_field_name="message_grp_achat",
            new_string="Message groupe d'achats",
            new_type="html",
            new_help="Message à afficher pour les groupes d'achats.",
        )
        migration.add_update_migration_field(
            "accorderie",
            "messageaccueil",
            new_field_name="message_accueil",
            new_string="Message d'accueil",
            new_type="html",
            new_help="Message à afficher pour accueillir les membres.",
        )
        migration.add_update_migration_field(
            "accorderie",
            "url_public_accorderie",
            new_field_name="url_public",
            new_string="Lien du site web publique",
            new_help="Lien du site web publique de l'Accorderie",
            force_widget="link_button",
        )
        migration.add_update_migration_field(
            "accorderie",
            "url_transac_accorderie",
            new_field_name="url_transactionnel",
            new_string="Lien du site web transactionnel",
            force_widget="link_button",
            new_help="Lien du site web transactionnel de l'Accorderie",
        )
        migration.add_update_migration_field(
            "accorderie",
            "url_logoaccorderie",
            new_field_name="logo",
            new_string="Logo",
            new_type="binary",
            force_widget="image",
            path_binary="/accorderie_canada/Intranet/images/logo",
            new_help="Logo de l'Accorderie",
        )
        migration.add_update_migration_field(
            "accorderie",
            "grpachat_admin",
            new_field_name="grp_achat_administrateur",
            new_string="Groupe d'achats des administrateurs",
            new_type="boolean",
            new_help=(
                "Permet de rendre accessible les achats pour les"
                " administrateurs"
            ),
        )
        migration.add_update_migration_field(
            "accorderie",
            "grpachat_accordeur",
            new_field_name="grp_achat_membre",
            new_string="Groupe d'achats membre",
            new_type="boolean",
            new_help="Rend accessible les achats pour les Accordeurs",
        )
        migration.add_update_migration_field(
            "accorderie",
            "nonvisible",
            new_required=False,
            new_type="boolean",
            new_field_name="archive",
            new_string="Archivé",
            new_help=(
                "Lorsque archivé, cette accorderie n'est plus en fonction,"
                " mais demeure accessible"
            ),
        )
        migration.add_update_migration_field(
            "accorderie",
            "datemaj_accorderie",
            new_field_name="date_mise_a_jour",
            new_string="Dernière mise à jour",
            new_help="Date de la dernière mise à jour",
        )

        # tbl_achat_ponctuel
        # TODO create name from selected field
        # migration.add_update_migration_model(
        #     "achat.ponctuel",
        #     new_rec_name="nom",
        # )
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
            "dateachatponctuel",
            new_field_name="date_achat",
            new_string="Date d'achat",
        )
        migration.add_update_migration_field(
            "achat.ponctuel",
            "montantpaiementachatponct",
            new_field_name="paiement_effectue",
            new_string="Paiement effectué",
        )
        migration.add_update_migration_field(
            "achat.ponctuel",
            "achatponcfacturer",
            new_field_name="est_facture",
            new_string="Facturé",
        )
        migration.add_update_migration_field(
            "achat.ponctuel",
            "majoration_achatponct",
            new_field_name="majoration",
            new_string="Majoration",
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
        migration.add_update_migration_field(
            "achat.ponctuel",
            "datemaj_achantponct",
            new_field_name="date_mise_a_jour",
            new_string="Dernière mise à jour",
        )

        # tbl_achat_ponctuel_produit
        # TODO create name from selected field
        # migration.add_update_migration_model(
        #     "achat.ponctuel.produit",
        #     new_rec_name="nom",
        # )
        migration.add_update_migration_field(
            "achat.ponctuel.produit",
            "noachatponctuelproduit",
            delete=True,
        )
        migration.add_update_migration_field(
            "achat.ponctuel.produit",
            "noachatponctuel",
        )
        migration.add_update_migration_field(
            "achat.ponctuel.produit",
            "nofournisseurproduit",
        )
        migration.add_update_migration_field(
            "achat.ponctuel.produit",
            "qteacheter",
        )
        migration.add_update_migration_field(
            "achat.ponctuel.produit",
            "coutunit_achatponctprod",
        )
        migration.add_update_migration_field(
            "achat.ponctuel.produit",
            "sitaxablef_achatponctprod",
        )
        migration.add_update_migration_field(
            "achat.ponctuel.produit",
            "sitaxablep_achatponctprod",
        )
        migration.add_update_migration_field(
            "achat.ponctuel.produit",
            "prixfacturer_achatponctprod",
        )
        migration.add_update_migration_field(
            "achat.ponctuel.produit",
            "datemaj_achatponcproduit",
        )

        # tbl_arrondissement
        migration.add_update_migration_model(
            "arrondissement",
            new_rec_name="nom",
        )
        migration.add_update_migration_field(
            "arrondissement",
            "noarrondissement",
            delete=True,
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
            "arrondissement",
            new_field_name="nom",
            new_string="Nom",
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
            compute_data_function="""nom.replace("&#8217;", "'").strip()""",
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
        migration.add_update_migration_model(
            "categorie.sous.categorie", new_rec_name="description"
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "nocategoriesouscategorie",
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "nosouscategorie",
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "nocategorie",
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "titreoffre",
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "supprimer",
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "approuver",
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "description",
            compute_data_function="""description.replace("&#8217;", "'").strip()""",
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "nooffre",
        )

        # tbl_commande
        # migration.add_update_migration_model(
        #     "commande", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "commande",
            "nocommande",
            new_required=False,
        )
        migration.add_update_migration_field(
            "commande",
            "nopointservice",
        )
        migration.add_update_migration_field(
            "commande",
            "norefcommande",
        )
        migration.add_update_migration_field(
            "commande",
            "datecmddebut",
        )
        migration.add_update_migration_field(
            "commande",
            "datecmdfin",
        )
        migration.add_update_migration_field(
            "commande",
            "datecueillette",
        )
        migration.add_update_migration_field(
            "commande",
            "taxepcommande",
        )
        migration.add_update_migration_field(
            "commande",
            "taxefcommande",
        )
        migration.add_update_migration_field(
            "commande",
            "majoration",
        )
        migration.add_update_migration_field(
            "commande",
            "commandetermine",
        )
        migration.add_update_migration_field(
            "commande",
            "datemaj_cmd",
        )

        # tbl_commande_membre
        # migration.add_update_migration_model(
        #     "commande.membre", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "commande.membre",
            "nocommandemembre",
            delete=True,
        )
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
        migration.add_update_migration_field(
            "commande.membre",
            "numrefmembre",
        )
        migration.add_update_migration_field(
            "commande.membre",
            "cmdconfirmer",
        )
        migration.add_update_migration_field(
            "commande.membre",
            "facturer",
        )
        migration.add_update_migration_field(
            "commande.membre",
            "montantpaiement",
        )
        migration.add_update_migration_field(
            "commande.membre",
            "coutunitaireajour",
        )
        migration.add_update_migration_field(
            "commande.membre",
            "datecmdmb",
        )
        migration.add_update_migration_field(
            "commande.membre",
            "datefacture",
        )
        migration.add_update_migration_field(
            "commande.membre",
            "archivesoustotal",
        )
        migration.add_update_migration_field(
            "commande.membre",
            "archivetotmajoration",
        )
        migration.add_update_migration_field(
            "commande.membre",
            "archivetottxfed",
        )
        migration.add_update_migration_field(
            "commande.membre",
            "archivetottxprov",
        )
        migration.add_update_migration_field(
            "commande.membre",
            "datemaj_cmdmembre",
        )

        # tbl_commande_membre_produit
        # migration.add_update_migration_model(
        #     "commande.membre.produit", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "commande.membre.produit",
            "nocmdmbproduit",
            delete=True,
        )
        migration.add_update_migration_field(
            "commande.membre.produit",
            "nocommandemembre",
        )
        migration.add_update_migration_field(
            "commande.membre.produit",
            "nofournisseurproduitcommande",
        )
        migration.add_update_migration_field(
            "commande.membre.produit",
            "qte",
        )
        migration.add_update_migration_field(
            "commande.membre.produit",
            "qtedeplus",
        )
        migration.add_update_migration_field(
            "commande.membre.produit",
            "ajustement",
        )
        migration.add_update_migration_field(
            "commande.membre.produit",
            "coutunitaire_facture",
        )
        migration.add_update_migration_field(
            "commande.membre.produit",
            "sitaxablep_facture",
        )
        migration.add_update_migration_field(
            "commande.membre.produit",
            "sitaxablef_facture",
        )
        migration.add_update_migration_field(
            "commande.membre.produit",
            "prixfacturer_manuel",
        )
        migration.add_update_migration_field(
            "commande.membre.produit",
            "datemaj_cmdmembreprod",
        )

        # tbl_commentaire
        # migration.add_update_migration_model(
        #     "commentaire", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "commentaire",
            "nocommentaire",
            delete=True,
        )
        migration.add_update_migration_field(
            "commentaire",
            "nopointservice",
        )
        migration.add_update_migration_field(
            "commentaire",
            "nomembresource",
        )
        migration.add_update_migration_field(
            "commentaire",
            "nomembreviser",
        )
        migration.add_update_migration_field(
            "commentaire",
            "nooffreservicemembre",
        )
        migration.add_update_migration_field(
            "commentaire",
            "nodemandeservice",
        )
        migration.add_update_migration_field(
            "commentaire",
            "dateheureajout",
        )
        migration.add_update_migration_field(
            "commentaire",
            "situation_impliquant",
        )
        migration.add_update_migration_field(
            "commentaire",
            "nomemployer",
        )
        migration.add_update_migration_field(
            "commentaire",
            "nomcomite",
        )
        migration.add_update_migration_field(
            "commentaire",
            "autresituation",
        )
        migration.add_update_migration_field(
            "commentaire",
            "satisfactioninsatisfaction",
        )
        migration.add_update_migration_field(
            "commentaire",
            "dateincident",
        )
        migration.add_update_migration_field(
            "commentaire",
            "typeoffre",
        )
        migration.add_update_migration_field(
            "commentaire",
            "resumersituation",
        )
        migration.add_update_migration_field(
            "commentaire",
            "demarche",
        )
        migration.add_update_migration_field(
            "commentaire",
            "solutionpourregler",
        )
        migration.add_update_migration_field(
            "commentaire",
            "autrecommentaire",
        )
        migration.add_update_migration_field(
            "commentaire",
            "siconfidentiel",
        )
        migration.add_update_migration_field(
            "commentaire",
            "noteadministrative",
        )
        migration.add_update_migration_field(
            "commentaire",
            "consulteraccorderie",
        )
        migration.add_update_migration_field(
            "commentaire",
            "consulterreseau",
        )
        migration.add_update_migration_field(
            "commentaire",
            "datemaj_commentaire",
        )

        # tbl_demande_service
        # migration.add_update_migration_model(
        #     "demande.service", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "demande.service",
            "nodemandeservice",
            delete=True,
        )
        migration.add_update_migration_field(
            "demande.service",
            "nomembre",
        )
        migration.add_update_migration_field(
            "demande.service",
            "noaccorderie",
        )
        migration.add_update_migration_field(
            "demande.service",
            "titredemande",
        )
        migration.add_update_migration_field(
            "demande.service",
            "description",
        )
        migration.add_update_migration_field(
            "demande.service",
            "approuve",
        )
        migration.add_update_migration_field(
            "demande.service",
            "supprimer",
        )
        migration.add_update_migration_field(
            "demande.service",
            "transmit",
        )
        migration.add_update_migration_field(
            "demande.service",
            "datedebut",
        )
        migration.add_update_migration_field(
            "demande.service",
            "datefin",
        )

        # tbl_dmd_adhesion
        # migration.add_update_migration_model(
        #     "dmd.adhesion", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "dmd.adhesion",
            "nodmdadhesion",
            delete=True,
        )
        migration.add_update_migration_field(
            "dmd.adhesion",
            "noaccorderie",
        )
        migration.add_update_migration_field(
            "dmd.adhesion",
            "nom",
        )
        migration.add_update_migration_field(
            "dmd.adhesion",
            "prenom",
        )
        migration.add_update_migration_field(
            "dmd.adhesion",
            "telephone",
        )
        migration.add_update_migration_field(
            "dmd.adhesion",
            "poste",
        )
        migration.add_update_migration_field(
            "dmd.adhesion",
            "courriel",
        )
        migration.add_update_migration_field(
            "dmd.adhesion",
            "supprimer",
        )
        migration.add_update_migration_field(
            "dmd.adhesion",
            "transferer",
        )
        migration.add_update_migration_field(
            "dmd.adhesion",
            "enattente",
        )
        migration.add_update_migration_field(
            "dmd.adhesion",
            "datemaj",
        )

        # tbl_droits_admin
        # migration.add_update_migration_model(
        #     "droits.admin", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "droits.admin",
            "nomembre",
            new_required=False,
        )
        migration.add_update_migration_field(
            "droits.admin",
            "gestionprofil",
        )
        migration.add_update_migration_field(
            "droits.admin",
            "gestioncatsouscat",
        )
        migration.add_update_migration_field(
            "droits.admin",
            "gestionoffre",
        )
        migration.add_update_migration_field(
            "droits.admin",
            "gestionoffremembre",
        )
        migration.add_update_migration_field(
            "droits.admin",
            "saisieechange",
        )
        migration.add_update_migration_field(
            "droits.admin",
            "validation",
        )
        migration.add_update_migration_field(
            "droits.admin",
            "gestiondmd",
        )
        migration.add_update_migration_field(
            "droits.admin",
            "groupeachat",
        )
        migration.add_update_migration_field(
            "droits.admin",
            "consulterprofil",
        )
        migration.add_update_migration_field(
            "droits.admin",
            "consulteretatcompte",
        )
        migration.add_update_migration_field(
            "droits.admin",
            "gestionfichier",
        )

        # tbl_echange_service
        # migration.add_update_migration_model("echange.service", new_rec_name="nom")
        migration.add_update_migration_field(
            "echange.service",
            "noechangeservice",
            delete=True,
        )
        migration.add_update_migration_field(
            "echange.service",
            "nopointservice",
        )
        migration.add_update_migration_field(
            "echange.service",
            "nomembrevendeur",
        )
        migration.add_update_migration_field(
            "echange.service",
            "nomembreacheteur",
        )
        migration.add_update_migration_field(
            "echange.service",
            "nodemandeservice",
        )
        migration.add_update_migration_field(
            "echange.service",
            "nooffreservicemembre",
        )
        migration.add_update_migration_field(
            "echange.service",
            "nbheure",
            new_field_name="nb_heure",
            new_string="Nombre d'heure",
            new_help="Nombre d'heure effectué au moment de l'échange.",
            force_widget="float_time",
        )
        migration.add_update_migration_field(
            "echange.service",
            "dateechange",
        )
        migration.add_update_migration_field(
            "echange.service",
            "typeechange",
        )
        migration.add_update_migration_field(
            "echange.service",
            "remarque",
        )
        migration.add_update_migration_field(
            "echange.service",
            "commentaire",
        )

        # tbl_fichier
        # migration.add_update_migration_model(
        #     "fichier", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "fichier",
            "id_fichier",
            delete=True,
        )
        migration.add_update_migration_field(
            "fichier",
            "id_typefichier",
        )
        migration.add_update_migration_field(
            "fichier",
            "noaccorderie",
        )
        migration.add_update_migration_field(
            "fichier",
            "nomfichierstokage",
        )
        migration.add_update_migration_field(
            "fichier",
            "nomfichieroriginal",
        )
        migration.add_update_migration_field(
            "fichier",
            "si_admin",
        )
        migration.add_update_migration_field(
            "fichier",
            "si_accorderielocalseulement",
        )
        migration.add_update_migration_field(
            "fichier",
            "si_disponible",
        )
        migration.add_update_migration_field(
            "fichier",
            "datemaj_fichier",
        )

        # tbl_fournisseur
        # migration.add_update_migration_model(
        #     "fournisseur", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "fournisseur",
            "nofournisseur",
            delete=True,
        )
        migration.add_update_migration_field(
            "fournisseur",
            "noaccorderie",
        )
        migration.add_update_migration_field(
            "fournisseur",
            "noregion",
        )
        migration.add_update_migration_field(
            "fournisseur",
            "noville",
        )
        migration.add_update_migration_field(
            "fournisseur",
            "nomfournisseur",
        )
        migration.add_update_migration_field(
            "fournisseur",
            "adresse",
        )
        migration.add_update_migration_field(
            "fournisseur",
            "codepostalfournisseur",
        )
        migration.add_update_migration_field(
            "fournisseur",
            "telfournisseur",
        )
        migration.add_update_migration_field(
            "fournisseur",
            "faxfounisseur",
        )
        migration.add_update_migration_field(
            "fournisseur",
            "courrielfournisseur",
        )
        migration.add_update_migration_field(
            "fournisseur",
            "nomcontact",
        )
        migration.add_update_migration_field(
            "fournisseur",
            "postecontact",
        )
        migration.add_update_migration_field(
            "fournisseur",
            "courrielcontact",
        )
        migration.add_update_migration_field(
            "fournisseur",
            "notefournisseur",
        )
        migration.add_update_migration_field(
            "fournisseur",
            "visible_fournisseur",
        )
        migration.add_update_migration_field(
            "fournisseur",
            "datemaj_fournisseur",
        )

        # tbl_fournisseur_produit
        # migration.add_update_migration_model(
        #     "fournisseur.produit", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "fournisseur.produit",
            "nofournisseurproduit",
            delete=True,
        )
        migration.add_update_migration_field(
            "fournisseur.produit",
            "nofournisseur",
            new_required=False,
        )
        migration.add_update_migration_field(
            "fournisseur.produit",
            "noproduit",
        )
        migration.add_update_migration_field(
            "fournisseur.produit",
            "codeproduit",
        )
        migration.add_update_migration_field(
            "fournisseur.produit",
            "zqtestokeacc",
        )
        migration.add_update_migration_field(
            "fournisseur.produit",
            "zcoutunitaire",
        )
        migration.add_update_migration_field(
            "fournisseur.produit",
            "visible_fournisseurproduit",
        )
        migration.add_update_migration_field(
            "fournisseur.produit",
            "datemaj_fournproduit",
        )

        # tbl_fournisseur_produit_commande
        # migration.add_update_migration_model(
        #     "fournisseur.produit.commande", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "fournisseur.produit.commande",
            "nofournisseurproduitcommande",
            delete=True,
        )
        migration.add_update_migration_field(
            "fournisseur.produit.commande",
            "nocommande",
            new_required=False,
        )
        migration.add_update_migration_field(
            "fournisseur.produit.commande",
            "nofournisseurproduit",
        )
        migration.add_update_migration_field(
            "fournisseur.produit.commande",
            "nbboiteminfournisseur",
        )
        migration.add_update_migration_field(
            "fournisseur.produit.commande",
            "qteparboiteprevu",
        )
        migration.add_update_migration_field(
            "fournisseur.produit.commande",
            "coutunitprevu",
        )
        migration.add_update_migration_field(
            "fournisseur.produit.commande",
            "disponible",
        )
        migration.add_update_migration_field(
            "fournisseur.produit.commande",
            "datemaj_fournprodcommande",
        )

        # tbl_fournisseur_produit_pointservice
        # migration.add_update_migration_model(
        #     "fournisseur.produit.pointservice", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "fournisseur.produit.pointservice",
            "nofournisseurproduitpointservice",
            delete=True,
        )
        migration.add_update_migration_field(
            "fournisseur.produit.pointservice",
            "nofournisseurproduit",
        )
        migration.add_update_migration_field(
            "fournisseur.produit.pointservice",
            "nopointservice",
        )
        migration.add_update_migration_field(
            "fournisseur.produit.pointservice",
            "qtestokeacc",
        )
        migration.add_update_migration_field(
            "fournisseur.produit.pointservice",
            "coutunitaire",
        )
        migration.add_update_migration_field(
            "fournisseur.produit.pointservice",
            "datemaj_fournprodptserv",
        )

        # tbl_info_logiciel_bd
        # removed

        # tbl_log_acces
        # removed

        # tbl_membre
        # TODO change rec_name to display_name with compute of nom et prenom
        migration.add_update_migration_model("membre", new_rec_name="nom")
        migration.add_update_migration_field(
            "membre",
            "nomembre",
            delete=True,
        )
        migration.add_update_migration_field(
            "membre",
            "nocartier",
        )
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
            "notypecommunication",
        )
        migration.add_update_migration_field(
            "membre",
            "nooccupation",
        )
        migration.add_update_migration_field(
            "membre",
            "noorigine",
        )
        migration.add_update_migration_field(
            "membre",
            "nosituationmaison",
        )
        migration.add_update_migration_field(
            "membre",
            "noprovenance",
        )
        migration.add_update_migration_field(
            "membre",
            "norevenufamilial",
        )
        migration.add_update_migration_field(
            "membre",
            "noarrondissement",
        )
        migration.add_update_migration_field(
            "membre",
            "noville",
        )
        migration.add_update_migration_field(
            "membre",
            "noregion",
        )
        migration.add_update_migration_field(
            "membre",
            "membreca",
        )
        migration.add_update_migration_field(
            "membre",
            "partsocialpaye",
        )
        migration.add_update_migration_field(
            "membre",
            "codepostal",
        )
        migration.add_update_migration_field(
            "membre",
            "dateadhesion",
        )
        # migration.add_update_migration_field(
        #     "membre",
        #     "nom",
        #     new_required=True,
        # )
        migration.add_update_migration_field(
            "membre",
            "prenom",
        )
        migration.add_update_migration_field(
            "membre",
            "adresse",
        )
        migration.add_update_migration_field(
            "membre",
            "telephone1",
        )
        migration.add_update_migration_field(
            "membre",
            "postetel1",
        )
        migration.add_update_migration_field(
            "membre",
            "notypetel1",
        )
        migration.add_update_migration_field(
            "membre",
            "telephone2",
        )
        migration.add_update_migration_field(
            "membre",
            "postetel2",
        )
        migration.add_update_migration_field(
            "membre",
            "notypetel2",
        )
        migration.add_update_migration_field(
            "membre",
            "telephone3",
        )
        migration.add_update_migration_field(
            "membre",
            "postetel3",
        )
        migration.add_update_migration_field(
            "membre",
            "notypetel3",
        )
        migration.add_update_migration_field(
            "membre",
            "courriel",
        )
        migration.add_update_migration_field(
            "membre",
            "achatregrouper",
        )
        migration.add_update_migration_field(
            "membre",
            "pretactif",
        )
        migration.add_update_migration_field(
            "membre",
            "pretradier",
        )
        migration.add_update_migration_field(
            "membre",
            "pretpayer",
        )
        migration.add_update_migration_field(
            "membre",
            "etatcomptecourriel",
        )
        migration.add_update_migration_field(
            "membre",
            "bottintel",
        )
        migration.add_update_migration_field(
            "membre",
            "bottincourriel",
        )
        migration.add_update_migration_field(
            "membre",
            "membreactif",
        )
        migration.add_update_migration_field(
            "membre",
            "membreconjoint",
        )
        migration.add_update_migration_field(
            "membre",
            "nomembreconjoint",
        )
        migration.add_update_migration_field(
            "membre",
            "memo",
        )
        migration.add_update_migration_field(
            "membre",
            "sexe",
        )
        migration.add_update_migration_field(
            "membre",
            "anneenaissance",
        )
        migration.add_update_migration_field(
            "membre",
            "precisezorigine",
        )
        migration.add_update_migration_field(
            "membre",
            "nomutilisateur",
        )
        # Configuration for test
        # migration.add_update_migration_field(
        #     "membre",
        #     "motdepasse",
        #     sql_select_modify=f"DECODE(motdepasse,'{SECRET_PASSWORD}')",
        # )
        # Always keep this configuration
        migration.add_update_migration_field(
            "membre",
            "motdepasse",
            ignore_field=True,
        )
        migration.add_update_migration_field(
            "membre",
            "profilapprouver",
        )
        migration.add_update_migration_field(
            "membre",
            "membreprinc",
        )
        migration.add_update_migration_field(
            "membre",
            "nomaccorderie",
        )
        migration.add_update_migration_field(
            "membre",
            "recevoircourrielgrp",
        )
        migration.add_update_migration_field(
            "membre",
            "pascommunication",
        )
        migration.add_update_migration_field(
            "membre",
            "descriptionaccordeur",
        )
        migration.add_update_migration_field(
            "membre",
            "date_maj_membre",
        )
        migration.add_update_migration_field(
            "membre",
            "transferede",
        )

        # tbl_mensualite
        # removed

        # tbl_occupation
        # migration.add_update_migration_model(
        #     "occupation", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "occupation",
            "nooccupation",
            delete=True,
        )
        migration.add_update_migration_field(
            "occupation",
            "occupation",
        )

        # tbl_offre_service_membre
        # migration.add_update_migration_model(
        #     "offre.service.membre", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "offre.service.membre",
            "nooffreservicemembre",
            delete=True,
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "nomembre",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "noaccorderie",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "nocategoriesouscategorie",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "titreoffrespecial",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "conditionx",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "disponibilite",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "tarif",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "description",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "dateaffichage",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "datedebut",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "datefin",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "approuve",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "offrespecial",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "supprimer",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "fait",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "conditionoffre",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "nbfoisconsulteroffremembre",
        )
        migration.add_update_migration_field(
            "offre.service.membre",
            "datemaj_servicemembre",
        )

        # tbl_origine
        # migration.add_update_migration_model(
        #     "origine", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "origine",
            "noorigine",
            delete=True,
        )
        migration.add_update_migration_field(
            "origine",
            "origine",
        )

        # tbl_point_service
        migration.add_update_migration_model(
            "pointservice", new_rec_name="nom"
        )
        migration.add_update_migration_field(
            "pointservice",
            "nopointservice",
            delete=True,
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
            "ordrepointservice",
        )
        migration.add_update_migration_field(
            "pointservice",
            "notegrpachatpageclient",
        )
        migration.add_update_migration_field(
            "pointservice",
            "datemaj_pointservice",
        )
        # migration.add_update_migration_field(
        #     "pointservice",
        #     "noarrondissement",
        # )
        # migration.add_update_migration_field(
        #     "pointservice",
        #     "noville",
        # )
        # migration.add_update_migration_field(
        #     "pointservice",
        #     "noregion",
        # )
        # migration.add_update_migration_field(
        #     "pointservice",
        #     "codepostale",
        # )
        # migration.add_update_migration_field(
        #     "pointservice",
        #     "dateadhesion",
        # )
        # migration.add_update_migration_field(
        #     "pointservice",
        #     "adresse",
        # )
        # migration.add_update_migration_field(
        #     "pointservice",
        #     "telephone1",
        # )
        # migration.add_update_migration_field(
        #     "pointservice",
        #     "telephone2",
        # )
        # migration.add_update_migration_field(
        #     "pointservice",
        #     "courriel",
        # )
        # migration.add_update_migration_field(
        #     "pointservice",
        #     "recevoircourrielgrp",
        # )

        # tbl_pointservice_fournisseur
        # migration.add_update_migration_model(
        #     "pointservice.fournisseur", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "pointservice.fournisseur",
            "nopointservicefournisseur",
            delete=True,
        )
        migration.add_update_migration_field(
            "pointservice.fournisseur",
            "nopointservice",
        )
        migration.add_update_migration_field(
            "pointservice.fournisseur",
            "nofournisseur",
        )
        migration.add_update_migration_field(
            "pointservice.fournisseur",
            "datemaj_pointservicefournisseur",
        )

        # tbl_pret
        # removed

        # tbl_produit
        # migration.add_update_migration_model(
        #     "produit", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "produit",
            "noproduit",
            delete=True,
        )
        migration.add_update_migration_field(
            "produit",
            "notitre",
        )
        migration.add_update_migration_field(
            "produit",
            "noaccorderie",
        )
        migration.add_update_migration_field(
            "produit",
            "nomproduit",
        )
        migration.add_update_migration_field(
            "produit",
            "taxablef",
        )
        migration.add_update_migration_field(
            "produit",
            "taxablep",
        )
        migration.add_update_migration_field(
            "produit",
            "visible_produit",
        )
        migration.add_update_migration_field(
            "produit",
            "datemaj_produit",
        )

        # tbl_provenance
        # migration.add_update_migration_model(
        #     "provenance", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "provenance",
            "noprovenance",
            delete=True,
        )
        migration.add_update_migration_field(
            "provenance",
            "provenance",
        )

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
        # migration.add_update_migration_model(
        #     "revenu.familial", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "revenu.familial",
            "norevenufamilial",
            delete=True,
        )
        migration.add_update_migration_field(
            "revenu.familial",
            "revenu",
        )

        # tbl_situation_maison
        # migration.add_update_migration_model(
        #     "situation.maison", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "situation.maison",
            "nosituationmaison",
            delete=True,
        )
        migration.add_update_migration_field(
            "situation.maison",
            "situation",
        )

        # tbl_sous_categorie
        # TODO
        migration.add_update_migration_model(
            "sous.categorie", new_rec_name="titre"
        )
        migration.add_update_migration_field(
            "sous.categorie",
            "nosouscategorie",
        )
        migration.add_update_migration_field(
            "sous.categorie",
            "nocategorie",
        )
        migration.add_update_migration_field(
            "sous.categorie",
            "titresouscategorie",
            new_field_name="titre",
            new_string="Titre",
            compute_data_function="""titre.replace("&#8217;", "'").strip()""",
        )
        migration.add_update_migration_field(
            "sous.categorie",
            "supprimer",
        )
        migration.add_update_migration_field(
            "sous.categorie",
            "approuver",
        )

        # tbl_taxe
        # migration.add_update_migration_model(
        #     "taxe", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "taxe",
            "notaxe",
            delete=True,
        )
        migration.add_update_migration_field(
            "taxe",
            "tauxtaxepro",
        )
        migration.add_update_migration_field(
            "taxe",
            "notaxepro",
        )
        migration.add_update_migration_field(
            "taxe",
            "tauxtaxefed",
        )
        migration.add_update_migration_field(
            "taxe",
            "notaxefed",
        )
        migration.add_update_migration_field(
            "taxe",
            "tauxmajoration",
        )

        # tbl_titre
        # migration.add_update_migration_model(
        #     "titre", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "titre",
            "notitre",
            delete=True,
        )
        migration.add_update_migration_field(
            "titre",
            "titre",
        )
        migration.add_update_migration_field(
            "titre",
            "visible_titre",
        )
        migration.add_update_migration_field(
            "titre",
            "datemaj_titre",
        )

        # tbl_type_communication
        # migration.add_update_migration_model(
        #     "type.communication", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "type.communication",
            "notypecommunication",
            delete=True,
        )
        migration.add_update_migration_field(
            "type.communication",
            "typecommunication",
        )

        # tbl_type_compte
        # migration.add_update_migration_model(
        #     "type.compte", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "type.compte",
            "nomembre",
            new_required=False,
        )
        migration.add_update_migration_field(
            "type.compte",
            "accodeursimple",
        )
        migration.add_update_migration_field(
            "type.compte",
            "admin",
        )
        migration.add_update_migration_field(
            "type.compte",
            "adminchef",
        )
        migration.add_update_migration_field(
            "type.compte",
            "reseau",
        )
        migration.add_update_migration_field(
            "type.compte",
            "spip",
        )
        migration.add_update_migration_field(
            "type.compte",
            "adminpointservice",
        )
        migration.add_update_migration_field(
            "type.compte",
            "adminordpointservice",
        )

        # tbl_type_fichier
        # migration.add_update_migration_model(
        #     "type.fichier", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "type.fichier",
            "id_typefichier",
            delete=True,
        )
        migration.add_update_migration_field(
            "type.fichier",
            "typefichier",
        )
        migration.add_update_migration_field(
            "type.fichier",
            "datemaj_typefichier",
        )

        # tbl_type_tel
        # migration.add_update_migration_model(
        #     "type.tel", new_rec_name="description"
        # )
        migration.add_update_migration_field(
            "type.tel",
            "notypetel",
            delete=True,
        )
        migration.add_update_migration_field(
            "type.tel",
            "typetel",
        )

        # tbl_versement
        # removed

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
            .filtered(
                lambda x: x.name.startswith("tbl_")
                and x.name
                not in (
                    "tbl_info_logiciel_bd",
                    "tbl_log_acces",
                    "tbl_mensualite",
                    "tbl_pret",
                    "tbl_versement",
                )
            )
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

        if lst_nomenclator:
            for db_table_id in code_generator_db_tables:
                if db_table_id.name in lst_nomenclator:
                    db_table_id.nomenclator = True

        code_generator_id = code_generator_db_tables.generate_module(
            code_generator_id=code_generator_id
        )

        # Add new field
        model_membre_id = env["ir.model"].search([("model", "=", "membre")])
        value_field = {
            "name": "nom_complet",
            "field_description": "Nom complet",
            "ttype": "char",
            "code_generator_compute": "_compute_nom_complet",
            "model_id": model_membre_id.id,
        }
        env["ir.model.fields"].create(value_field)

        model_categorie_sous_categorie_id = env["ir.model"].search(
            [("model", "=", "categorie.sous.categorie")]
        )
        value_field = {
            "name": "nom_complet",
            "field_description": "Nom complet",
            "ttype": "char",
            "code_generator_compute": "_compute_nom_complet",
            "model_id": model_categorie_sous_categorie_id.id,
        }
        env["ir.model.fields"].create(value_field)

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
            {
                "code": """for rec in self:
    value = ""
    if self.nosouscategorie:
        value += self.nosouscategorie
    if self.nocategorie:
        value += str(self.nocategorie)
    if (self.nosouscategorie or self.nocategorie) and self.description:
        value += " - "
    if self.description:
        value += self.description
    rec.nom_complet = value
    """,
                "name": "_compute_nom_complet",
                "decorator": (
                    '@api.depends("description", "nosouscategorie",'
                    ' "nocategorie")'
                ),
                "param": "self",
                "sequence": 1,
                "m2o_module": code_generator_id.id,
                "m2o_model": model_categorie_sous_categorie_id.id,
            },
        ]
        env["code.generator.model.code"].create(lst_value)

        model_membre_id.rec_name = "nom_complet"
        model_categorie_sous_categorie_id.rec_name = "nom_complet"

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
        sql_select_modify=None,
        delete=False,
        ignore_field=False,
        path_binary=None,
        force_widget=None,
        compute_data_function=None,
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
        :param sql_select_modify: update select command with this string
        :param delete: import data, use to compute information but delete the field at the end with his data
        :param ignore_field: never compute it and ignore data from it
        :param path_binary: path for type binary when the past was char
        :param force_widget:
        :param compute_data_function: function, in string, to run with data in argument and overwrite data
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
            and sql_select_modify is None
            and compute_data_function is None
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
            if compute_data_function:
                value["compute_data_function"] = compute_data_function
            if sql_select_modify:
                value["sql_select_modify"] = sql_select_modify
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

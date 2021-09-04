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
            # "icon": os.path.join(
            #     os.path.basename(os.path.dirname(os.path.dirname(__file__))),
            #     "static",
            #     "description",
            #     "code_generator_icon.png",
            # ),
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
            # TODO option to create application pear first prefix or use in model name (si on prend tbl ou non)
        }
        code_generator_db_server_id = env["code.generator.db"].create(value_db)

        # Local variable to add update information
        db_table = env["code.generator.db.table"]
        db_column = env["code.generator.db.column"]

        # Modification of field before migration

        # tbl_accorderie
        db_table.update_table(
            "tbl_accorderie",
            new_model_name="accorderie.accorderie",
            new_rec_name="nom",
            new_description=(
                "Gestion des entitées Accorderie, contient les informations et"
                " les messages d'une Accorderie."
            ),
        )
        db_column.update_column(
            "tbl_accorderie",
            "noaccorderie",
            delete=True,
        )
        db_column.update_column(
            "tbl_accorderie",
            "noregion",
            new_field_name="region",
            new_description="Région administrative",
            new_required=False,
            new_help="Nom de la région administrative de l'Accorderie",
            # add_one2many=True,
        )
        db_column.update_column(
            "tbl_accorderie",
            "noville",
            new_field_name="ville",
            new_description="Ville",
            new_required=False,
            new_help="Nom de la ville de l'Accorderie",
            # add_one2many=True,
        )
        db_column.update_column(
            "tbl_accorderie",
            "noarrondissement",
            new_field_name="arrondissement",
            new_description="Arrondissement",
            new_help="Nom de l'Arrondissement qui contient l'Accorderie.",
        )
        db_column.update_column(
            "tbl_accorderie",
            "nocartier",
            # new_field_name="cartier",
            # new_description="Cartier",
            delete=True,
        )
        db_column.update_column(
            "tbl_accorderie",
            "nom",
            new_required=True,
            new_help="Nom de l'Accorderie",
        )
        db_column.update_column(
            "tbl_accorderie",
            "nomcomplet",
            # new_field_name="nom_complet",
            # new_description="Nom complet",
            delete=True,
        )
        db_column.update_column(
            "tbl_accorderie",
            "adresseaccorderie",
            new_field_name="adresse",
            new_description="Adresse",
            new_help="Adresse de l'Accorderie",
        )
        db_column.update_column(
            "tbl_accorderie",
            "codepostalaccorderie",
            new_field_name="code_postal",
            new_description="Code postal",
            new_help="Code postal de l'Accorderie",
        )
        db_column.update_column(
            "tbl_accorderie",
            "telaccorderie",
            new_field_name="telephone",
            new_description="Téléphone",
            new_help="Numéro de téléphone pour joindre l'Accorderie.",
        )
        db_column.update_column(
            "tbl_accorderie",
            "telecopieuraccorderie",
            new_field_name="telecopieur",
            new_description="Télécopieur",
            new_help="Numéro de télécopieur pour joindre l'Accorderie.",
        )
        db_column.update_column(
            "tbl_accorderie",
            "courrielaccorderie",
            new_field_name="courriel",
            new_description="Adresse courriel",
            new_help="Adresse courriel pour joindre l'Accorderie.",
        )
        db_column.update_column(
            "tbl_accorderie",
            "messagegrpachat",
            new_field_name="message_grp_achat",
            new_description="Message groupe d'achats",
            new_type="html",
            new_help="Message à afficher pour les groupes d'achats.",
        )
        db_column.update_column(
            "tbl_accorderie",
            "messageaccueil",
            new_field_name="message_accueil",
            new_description="Message d'accueil",
            new_type="html",
            new_help="Message à afficher pour accueillir les membres.",
        )
        db_column.update_column(
            "tbl_accorderie",
            "url_public_accorderie",
            new_field_name="url_public",
            new_description="Lien du site web publique",
            new_help="Lien du site web publique de l'Accorderie",
            force_widget="link_button",
        )
        db_column.update_column(
            "tbl_accorderie",
            "url_transac_accorderie",
            new_field_name="url_transactionnel",
            new_description="Lien du site web transactionnel",
            force_widget="link_button",
            new_help="Lien du site web transactionnel de l'Accorderie",
        )
        db_column.update_column(
            "tbl_accorderie",
            "url_logoaccorderie",
            new_field_name="logo",
            new_description="Logo",
            new_type="binary",
            force_widget="image",
            path_binary="/accorderie_canada/Intranet/images/logo",
            new_help="Logo de l'Accorderie",
        )
        db_column.update_column(
            "tbl_accorderie",
            "grpachat_admin",
            new_field_name="grp_achat_administrateur",
            new_description="Groupe d'achats des administrateurs",
            new_type="boolean",
            new_help=(
                "Permet de rendre accessible les achats pour les"
                " administrateurs."
            ),
        )
        db_column.update_column(
            "tbl_accorderie",
            "grpachat_accordeur",
            new_field_name="grp_achat_membre",
            new_description="Groupe d'achats membre",
            new_type="boolean",
            new_help="Rend accessible les achats pour les Accordeurs.",
        )
        db_column.update_column(
            "tbl_accorderie",
            "nonvisible",
            new_required=False,
            new_type="boolean",
            new_field_name="archive",
            new_description="Archivé",
            new_help=(
                "Lorsque archivé, cette accorderie n'est plus en fonction,"
                " mais demeure accessible."
            ),
        )
        db_column.update_column(
            "tbl_accorderie",
            "datemaj_accorderie",
            new_field_name="date_mise_a_jour",
            new_description="Dernière mise à jour",
            new_help="Date de la dernière mise à jour",
        )

        # tbl_achat_ponctuel
        db_table.update_table(
            "tbl_achat_ponctuel",
            delete=True,
            # new_model_name="accorderie.achat.ponctuel",
            # new_description="Gestion des achats ponctuels"
            # new_rec_name="nom",
        )

        # tbl_achat_ponctuel_produit
        db_table.update_table(
            "tbl_achat_ponctuel_produit",
            delete=True,
            # new_model_name="accorderie.achat.ponctuel.produit",
            # new_description="Liaisons des achats ponctuels aux produits des fournisseurs."
            # new_rec_name="nom",
        )

        # tbl_arrondissement
        db_table.update_table(
            "tbl_arrondissement",
            new_model_name="accorderie.arrondissement",
            new_description="Ensemble des arrondissement des Accorderies",
            new_rec_name="nom",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_arrondissement",
            "noarrondissement",
            delete=True,
        )
        db_column.update_column(
            "tbl_arrondissement",
            "noville",
            new_field_name="ville",
            new_description="Ville",
            # add_one2many=True,
        )
        db_column.update_column(
            "tbl_arrondissement",
            "arrondissement",
            new_field_name="nom",
            new_description="Nom",
        )

        # tbl_cartier
        db_table.update_table(
            "tbl_cartier",
            new_model_name="accorderie.quartier",
            new_rec_name="nom",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_cartier",
            "nocartier",
            delete=True,
        )
        db_column.update_column(
            "tbl_cartier",
            "noarrondissement",
            new_field_name="arrondissement",
            new_description="Arrondissement",
            new_help="Arrondissement associé au quartier",
        )
        db_column.update_column(
            "tbl_cartier",
            "cartier",
            new_field_name="nom",
            new_description="Nom du quartier",
            new_help="Nom du quartier",
        )

        # tbl_categorie
        db_table.update_table(
            "tbl_categorie",
            new_model_name="accorderie.categorie.service",
            new_description="Les catégories de services des Accorderies",
            new_rec_name="nom",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_categorie",
            "nocategorie",
            delete=True,
        )
        db_column.update_column(
            "tbl_categorie",
            "titrecategorie",
            new_field_name="nom",
            new_description="Nom",
            new_help="Le nom de la catégorie des services",
            compute_data_function="""nom.replace("&#8217;", "'").strip()""",
        )
        db_column.update_column(
            "tbl_categorie",
            "supprimer",
            new_field_name="archive",
            new_description="Archivé",
            new_type="boolean",
            new_help="Permet d'archiver cette catégorie.",
        )
        db_column.update_column(
            "tbl_categorie",
            "approuver",
            new_field_name="approuve",
            new_description="Approuvé",
            new_type="boolean",
            new_help="Permet d'approuver cette catégorie.",
        )

        # tbl_categorie_sous_categorie
        # TODO
        db_table.update_table(
            "tbl_categorie_sous_categorie",
            new_model_name="accorderie.sous.sous.categorie.service",
            new_rec_name="titre_offre_service",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_categorie_sous_categorie",
            "nosouscategorieid",
            new_field_name="sous_categorie_id",
            new_description="Sous catégorie de services",
        )
        db_column.update_column(
            "tbl_categorie_sous_categorie",
            "nocategoriesouscategorie",
            delete=True,
        )
        # TODO use delete and update _compte_nom_complet with many2one on this field
        db_column.update_column(
            "tbl_categorie_sous_categorie",
            "nosouscategorie",
            # delete=True,
        )
        db_column.update_column(
            "tbl_categorie_sous_categorie",
            "nocategorie",
            # delete=True,
        )
        db_column.update_column(
            "tbl_categorie_sous_categorie",
            "titreoffre",
            new_field_name="titre_offre_service",
            new_description="Titre de l'offre de services",
        )
        db_column.update_column(
            "tbl_categorie_sous_categorie",
            "supprimer",
            new_field_name="archive",
            new_description="Archivé",
            new_type="boolean",
            new_help="Permet d'archiver cette sous-sous-catégorie.",
        )
        db_column.update_column(
            "tbl_categorie_sous_categorie",
            "approuver",
            new_field_name="approuve",
            new_description="Approuvé",
            new_type="boolean",
            new_help="Permet d'approuver cette sous-sous-catégorie.",
        )
        db_column.update_column(
            "tbl_categorie_sous_categorie",
            "description",
            compute_data_function="""description.replace("&#8217;", "'").strip()""",
        )
        db_column.update_column(
            "tbl_categorie_sous_categorie",
            "nooffre",
            new_field_name="no_offre",
            new_description="Numéro de l'offre"
            # TODO mettre invisible
            # TODO mettre numéro_complet
        )

        # tbl_commande
        db_table.update_table(
            "tbl_commande",
            delete=True,
            # new_model_name="accorderie.commande",
        )

        # tbl_commande_membre
        db_table.update_table(
            "tbl_commande_membre",
            delete=True,
            # new_rec_name="description",
            # new_model_name="accorderie.commande.membre",
        )

        # tbl_commande_membre_produit
        db_table.update_table(
            "tbl_commande_membre_produit",
            delete=True,
            # new_rec_name="description",
            # new_model_name="accorderie.commande.membre.produit",
        )

        # tbl_commentaire
        db_table.update_table(
            "tbl_commentaire",
            # new_rec_name="description",
            new_model_name="accorderie.commentaire",
            new_description=(
                "Les commentaires des membres envers d'autres membres sur des"
                " services et demandes"
            ),
        )
        db_column.update_column(
            "tbl_commentaire",
            "nocommentaire",
            delete=True,
        )
        db_column.update_column(
            "tbl_commentaire",
            "nopointservice",
            new_field_name="point_service",
            new_description="Point de services",
        )
        db_column.update_column(
            "tbl_commentaire",
            "nomembresource",
            new_field_name="membre_source",
            new_description="Membre source",
            new_help="Membre duquel provient le commentaire",
        )
        db_column.update_column(
            "tbl_commentaire",
            "nomembreviser",
            new_field_name="membre_viser",
            new_description="Membre visé",
            new_help="Membre visé par le commentaire",
        )
        db_column.update_column(
            "tbl_commentaire",
            "nooffreservicemembre",
            new_field_name="offre_service_id",
            new_description="Offre de services",
            new_help="L'offre de services qui est visée par ce commentaire.",
        )
        db_column.update_column(
            "tbl_commentaire",
            "nodemandeservice",
            new_field_name="demande_service_id",
            new_description="Demande de services",
            new_help=(
                "La demande de services qui est visée par ce commentaire."
            ),
        )
        db_column.update_column(
            "tbl_commentaire",
            "dateheureajout",
            new_field_name="datetime_creation",
            new_description="Date et heure de création",
        )
        db_column.update_column(
            "tbl_commentaire",
            "situation_impliquant",
            # TODO support type selection
            # 1. UnE ou des AccordeurEs
            # 2. Un comité
            # 3. UnE employéE
            # 4. Autre
        )
        db_column.update_column(
            "tbl_commentaire",
            "nomemployer",
        )
        db_column.update_column(
            "tbl_commentaire",
            "nomcomite",
        )
        db_column.update_column(
            "tbl_commentaire",
            "autresituation",
        )
        db_column.update_column(
            "tbl_commentaire",
            "satisfactioninsatisfaction",
        )
        db_column.update_column(
            "tbl_commentaire",
            "dateincident",
        )
        db_column.update_column(
            "tbl_commentaire",
            "typeoffre",
        )
        db_column.update_column(
            "tbl_commentaire",
            "resumersituation",
        )
        db_column.update_column(
            "tbl_commentaire",
            "demarche",
        )
        db_column.update_column(
            "tbl_commentaire",
            "solutionpourregler",
        )
        db_column.update_column(
            "tbl_commentaire",
            "autrecommentaire",
        )
        db_column.update_column(
            "tbl_commentaire",
            "siconfidentiel",
        )
        db_column.update_column(
            "tbl_commentaire",
            "noteadministrative",
        )
        db_column.update_column(
            "tbl_commentaire",
            "consulteraccorderie",
        )
        db_column.update_column(
            "tbl_commentaire",
            "consulterreseau",
        )
        db_column.update_column(
            "tbl_commentaire",
            "datemaj_commentaire",
        )

        # tbl_demande_service
        db_table.update_table(
            "tbl_demande_service",
            # new_rec_name="description",
            new_model_name="accorderie.demande.service",
        )
        db_column.update_column(
            "tbl_demande_service",
            "nodemandeservice",
            delete=True,
        )
        db_column.update_column(
            "tbl_demande_service",
            "nomembre",
        )
        db_column.update_column(
            "tbl_demande_service",
            "noaccorderie",
        )
        db_column.update_column(
            "tbl_demande_service",
            "titredemande",
        )
        db_column.update_column(
            "tbl_demande_service",
            "description",
        )
        db_column.update_column(
            "tbl_demande_service",
            "approuve",
        )
        db_column.update_column(
            "tbl_demande_service",
            "supprimer",
        )
        db_column.update_column(
            "tbl_demande_service",
            "transmit",
        )
        db_column.update_column(
            "tbl_demande_service",
            "datedebut",
        )
        db_column.update_column(
            "tbl_demande_service",
            "datefin",
        )

        # tbl_dmd_adhesion
        db_table.update_table(
            "tbl_dmd_adhesion",
            # new_rec_name="description",
            new_model_name="accorderie.dmd.adhesion",
        )
        db_column.update_column(
            "tbl_dmd_adhesion",
            "nodmdadhesion",
            delete=True,
        )
        db_column.update_column(
            "tbl_dmd_adhesion",
            "noaccorderie",
        )
        db_column.update_column(
            "tbl_dmd_adhesion",
            "nom",
        )
        db_column.update_column(
            "tbl_dmd_adhesion",
            "prenom",
        )
        db_column.update_column(
            "tbl_dmd_adhesion",
            "telephone",
        )
        db_column.update_column(
            "tbl_dmd_adhesion",
            "poste",
        )
        db_column.update_column(
            "tbl_dmd_adhesion",
            "courriel",
        )
        db_column.update_column(
            "tbl_dmd_adhesion",
            "supprimer",
        )
        db_column.update_column(
            "tbl_dmd_adhesion",
            "transferer",
        )
        db_column.update_column(
            "tbl_dmd_adhesion",
            "enattente",
        )
        db_column.update_column(
            "tbl_dmd_adhesion",
            "datemaj",
        )

        # tbl_droits_admin
        db_table.update_table(
            "tbl_droits_admin",
            # new_rec_name="description",
            new_model_name="accorderie.droits.admin",
        )
        db_column.update_column(
            "tbl_droits_admin",
            "nomembre",
            new_required=False,
        )
        db_column.update_column(
            "tbl_droits_admin",
            "gestionprofil",
        )
        db_column.update_column(
            "tbl_droits_admin",
            "gestioncatsouscat",
        )
        db_column.update_column(
            "tbl_droits_admin",
            "gestionoffre",
        )
        db_column.update_column(
            "tbl_droits_admin",
            "gestionoffremembre",
        )
        db_column.update_column(
            "tbl_droits_admin",
            "saisieechange",
        )
        db_column.update_column(
            "tbl_droits_admin",
            "validation",
        )
        db_column.update_column(
            "tbl_droits_admin",
            "gestiondmd",
        )
        db_column.update_column(
            "tbl_droits_admin",
            "groupeachat",
        )
        db_column.update_column(
            "tbl_droits_admin",
            "consulterprofil",
        )
        db_column.update_column(
            "tbl_droits_admin",
            "consulteretatcompte",
        )
        db_column.update_column(
            "tbl_droits_admin",
            "gestionfichier",
        )

        # tbl_echange_service
        db_table.update_table(
            "tbl_echange_service",
            # new_rec_name="nom",
            new_model_name="accorderie.echange.service",
        )
        db_column.update_column(
            "tbl_echange_service",
            "noechangeservice",
            delete=True,
        )
        db_column.update_column(
            "tbl_echange_service",
            "nopointservice",
        )
        db_column.update_column(
            "tbl_echange_service",
            "nomembrevendeur",
        )
        db_column.update_column(
            "tbl_echange_service",
            "nomembreacheteur",
        )
        db_column.update_column(
            "tbl_echange_service",
            "nodemandeservice",
        )
        db_column.update_column(
            "tbl_echange_service",
            "nooffreservicemembre",
        )
        db_column.update_column(
            "tbl_echange_service",
            "nbheure",
            new_field_name="nb_heure",
            new_description="Nombre d'heure",
            new_help="Nombre d'heure effectué au moment de l'échange.",
            force_widget="float_time",
        )
        db_column.update_column(
            "tbl_echange_service",
            "dateechange",
        )
        db_column.update_column(
            "tbl_echange_service",
            "typeechange",
        )
        db_column.update_column(
            "tbl_echange_service",
            "remarque",
        )
        db_column.update_column(
            "tbl_echange_service",
            "commentaire",
        )

        # tbl_fichier
        db_table.update_table(
            "tbl_fichier",
            # new_rec_name="description",
            new_model_name="accorderie.fichier",
        )
        db_column.update_column(
            "tbl_fichier",
            "id_fichier",
            delete=True,
        )
        db_column.update_column(
            "tbl_fichier",
            "id_typefichier",
        )
        db_column.update_column(
            "tbl_fichier",
            "noaccorderie",
        )
        db_column.update_column(
            "tbl_fichier",
            "nomfichierstokage",
        )
        db_column.update_column(
            "tbl_fichier",
            "nomfichieroriginal",
        )
        db_column.update_column(
            "tbl_fichier",
            "si_admin",
        )
        db_column.update_column(
            "tbl_fichier",
            "si_accorderielocalseulement",
        )
        db_column.update_column(
            "tbl_fichier",
            "si_disponible",
        )
        db_column.update_column(
            "tbl_fichier",
            "datemaj_fichier",
        )

        # tbl_fournisseur
        db_table.update_table(
            "tbl_fournisseur",
            delete=True,
            # new_rec_name="description",
            # new_model_name="accorderie.fournisseur",
        )

        # tbl_fournisseur_produit
        db_table.update_table(
            "tbl_fournisseur_produit",
            delete=True,
            # new_rec_name="description",
            # new_model_name="accorderie.fournisseur.produit",
        )

        # tbl_fournisseur_produit_commande
        db_table.update_table(
            "tbl_fournisseur_produit_commande",
            delete=True,
            # new_rec_name="description",
            # new_model_name="accorderie.fournisseur.produit.commande",
        )

        # tbl_fournisseur_produit_pointservice
        db_table.update_table(
            "tbl_fournisseur_produit_pointservice",
            delete=True,
            # new_rec_name="description",
            # new_model_name="accorderie.fournisseur.produit.pointservice",
        )

        # tbl_info_logiciel_bd
        db_table.update_table(
            "tbl_info_logiciel_bd",
            delete=True,
        )

        # tbl_log_acces
        db_table.update_table(
            "tbl_log_acces",
            delete=True,
        )

        # tbl_membre
        # TODO change rec_name to display_name with compute of nom et prenom
        db_table.update_table(
            "tbl_membre",
            # new_rec_name="nom_complet",
            new_model_name="accorderie.membre",
        )
        db_column.update_column(
            "tbl_membre",
            "nomembre",
            delete=True,
        )
        db_column.update_column(
            "tbl_membre", "nocartier", new_field_name="quartier"
        )
        db_column.update_column(
            "tbl_membre",
            "noaccorderie",
            new_field_name="accorderie",
            new_description="Accorderie",
            new_help="Accorderie associé",
            # add_one2many=True,
        )
        db_column.update_column(
            "tbl_membre",
            "nopointservice",
            new_field_name="point_service",
            new_description="Point de service",
            new_help="Point de service associé",
            # add_one2many=True,
        )
        db_column.update_column(
            "tbl_membre",
            "notypecommunication",
        )
        db_column.update_column(
            "tbl_membre",
            "nooccupation",
        )
        db_column.update_column(
            "tbl_membre",
            "noorigine",
        )
        db_column.update_column(
            "tbl_membre",
            "nosituationmaison",
        )
        db_column.update_column(
            "tbl_membre",
            "noprovenance",
        )
        db_column.update_column(
            "tbl_membre",
            "norevenufamilial",
        )
        db_column.update_column(
            "tbl_membre",
            "noarrondissement",
        )
        db_column.update_column(
            "tbl_membre",
            "noville",
        )
        db_column.update_column(
            "tbl_membre",
            "noregion",
        )
        db_column.update_column(
            "tbl_membre",
            "membreca",
        )
        db_column.update_column(
            "tbl_membre",
            "partsocialpaye",
        )
        db_column.update_column(
            "tbl_membre",
            "codepostal",
        )
        db_column.update_column(
            "tbl_membre",
            "dateadhesion",
        )
        # db_column.update_column(
        #     "tbl_membre",
        #     "nom",
        #     new_required=True,
        # )
        db_column.update_column(
            "tbl_membre",
            "prenom",
        )
        db_column.update_column(
            "tbl_membre",
            "adresse",
        )
        db_column.update_column(
            "tbl_membre",
            "telephone1",
        )
        db_column.update_column(
            "tbl_membre",
            "postetel1",
        )
        db_column.update_column(
            "tbl_membre",
            "notypetel1",
        )
        db_column.update_column(
            "tbl_membre",
            "telephone2",
        )
        db_column.update_column(
            "tbl_membre",
            "postetel2",
        )
        db_column.update_column(
            "tbl_membre",
            "notypetel2",
        )
        db_column.update_column(
            "tbl_membre",
            "telephone3",
        )
        db_column.update_column(
            "tbl_membre",
            "postetel3",
        )
        db_column.update_column(
            "tbl_membre",
            "notypetel3",
        )
        db_column.update_column(
            "tbl_membre",
            "courriel",
        )
        db_column.update_column(
            "tbl_membre",
            "achatregrouper",
        )
        db_column.update_column(
            "tbl_membre",
            "pretactif",
        )
        db_column.update_column(
            "tbl_membre",
            "pretradier",
        )
        db_column.update_column(
            "tbl_membre",
            "pretpayer",
        )
        db_column.update_column(
            "tbl_membre",
            "etatcomptecourriel",
        )
        db_column.update_column(
            "tbl_membre",
            "bottintel",
        )
        db_column.update_column(
            "tbl_membre",
            "bottincourriel",
        )
        db_column.update_column(
            "tbl_membre",
            "membreactif",
        )
        db_column.update_column(
            "tbl_membre",
            "membreconjoint",
        )
        db_column.update_column(
            "tbl_membre",
            "nomembreconjoint",
        )
        db_column.update_column(
            "tbl_membre",
            "memo",
        )
        db_column.update_column(
            "tbl_membre",
            "sexe",
        )
        db_column.update_column(
            "tbl_membre",
            "anneenaissance",
        )
        db_column.update_column(
            "tbl_membre",
            "precisezorigine",
        )
        db_column.update_column(
            "tbl_membre",
            "nomutilisateur",
        )
        # Configuration for test
        # db_column.update_column(
        #     "tbl_membre",
        #     "motdepasse",
        #     sql_select_modify=f"DECODE(motdepasse,'{SECRET_PASSWORD}')",
        # )
        # Always keep this configuration
        db_column.update_column(
            "tbl_membre",
            "motdepasse",
            ignore_field=True,
        )
        db_column.update_column(
            "tbl_membre",
            "profilapprouver",
        )
        db_column.update_column(
            "tbl_membre",
            "membreprinc",
        )
        db_column.update_column(
            "tbl_membre",
            "nomaccorderie",
        )
        db_column.update_column(
            "tbl_membre",
            "recevoircourrielgrp",
        )
        db_column.update_column(
            "tbl_membre",
            "pascommunication",
        )
        db_column.update_column(
            "tbl_membre",
            "descriptionaccordeur",
        )
        db_column.update_column(
            "tbl_membre",
            "date_maj_membre",
        )
        db_column.update_column(
            "tbl_membre",
            "transferede",
        )
        # db_column.update_column(
        #     "tbl_membre",
        #     "",
        #     new_field_name="nom_complet",
        #     new_type="char",
        #     new_description="Nom complet",
        #     new_help="TODO",
        #     new_compute="_compute_nom_complet"
        # )

        # tbl_mensualite
        db_table.update_table(
            "tbl_mensualite",
            delete=True,
        )

        # tbl_occupation
        db_table.update_table(
            "tbl_occupation",
            new_rec_name="nom",
            new_model_name="accorderie.occupation",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_occupation",
            "nooccupation",
            delete=True,
        )
        db_column.update_column(
            "tbl_occupation",
            "occupation",
            new_field_name="nom",
        )

        # tbl_offre_service_membre
        db_table.update_table(
            "tbl_offre_service_membre",
            # new_rec_name="description",
            new_model_name="accorderie.offre.service.membre",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "nooffreservicemembre",
            delete=True,
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "nomembre",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "noaccorderie",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "nocategoriesouscategorie",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "titreoffrespecial",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "conditionx",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "disponibilite",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "tarif",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "description",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "dateaffichage",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "datedebut",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "datefin",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "approuve",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "offrespecial",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "supprimer",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "fait",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "conditionoffre",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "nbfoisconsulteroffremembre",
        )
        db_column.update_column(
            "tbl_offre_service_membre",
            "datemaj_servicemembre",
        )

        # tbl_origine
        db_table.update_table(
            "tbl_origine",
            new_rec_name="nom",
            new_model_name="accorderie.origine",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_origine",
            "noorigine",
            delete=True,
        )
        db_column.update_column(
            "tbl_origine",
            "origine",
            new_field_name="nom",
        )

        # tbl_pointservice
        db_table.update_table(
            "tbl_pointservice",
            new_rec_name="nom",
            new_model_name="accorderie.pointservice",
        )
        db_column.update_column(
            "tbl_pointservice",
            "nopointservice",
            delete=True,
        )
        db_column.update_column(
            "tbl_pointservice",
            "nompointservice",
            new_field_name="nom",
            new_description="Nom",
            new_help="Nom du point de service",
        )
        db_column.update_column(
            "tbl_pointservice",
            "ordrepointservice",
        )
        db_column.update_column(
            "tbl_pointservice",
            "notegrpachatpageclient",
        )
        db_column.update_column(
            "tbl_pointservice",
            "datemaj_pointservice",
        )
        # db_column.update_column(
        #     "tbl_pointservice",
        #     "noarrondissement",
        # )
        # db_column.update_column(
        #     "tbl_pointservice",
        #     "noville",
        # )
        # db_column.update_column(
        #     "tbl_pointservice",
        #     "noregion",
        # )
        # db_column.update_column(
        #     "tbl_pointservice",
        #     "codepostale",
        # )
        # db_column.update_column(
        #     "tbl_pointservice",
        #     "dateadhesion",
        # )
        # db_column.update_column(
        #     "tbl_pointservice",
        #     "adresse",
        # )
        # db_column.update_column(
        #     "tbl_pointservice",
        #     "telephone1",
        # )
        # db_column.update_column(
        #     "tbl_pointservice",
        #     "telephone2",
        # )
        # db_column.update_column(
        #     "tbl_pointservice",
        #     "courriel",
        # )
        # db_column.update_column(
        #     "tbl_pointservice",
        #     "recevoircourrielgrp",
        # )

        # tbl_pointservice_fournisseur
        db_table.update_table(
            "tbl_pointservice_fournisseur",
            delete=True,
            # new_rec_name="description",
            # new_model_name="accorderie.pointservice.fournisseur",
        )

        # tbl_pret
        db_table.update_table(
            "tbl_pret",
            delete=True,
        )

        # tbl_produit
        db_table.update_table(
            "tbl_produit",
            delete=True,
            # new_rec_name="description",
            # new_model_name="accorderie.produit",
        )

        # tbl_provenance
        db_table.update_table(
            "tbl_provenance",
            new_rec_name="nom",
            new_model_name="accorderie.provenance",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_provenance",
            "noprovenance",
            delete=True,
        )
        db_column.update_column(
            "tbl_provenance",
            "provenance",
            new_field_name="nom",
        )

        # tbl_region
        db_table.update_table(
            "tbl_region",
            new_rec_name="nom",
            new_model_name="accorderie.region",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_region",
            "noregion",
            new_field_name="code",
            new_description="Code de région",
            new_help="Code de la région administrative",
        )
        db_column.update_column(
            "tbl_region",
            "region",
            new_field_name="nom",
            new_description="Nom",
        )

        # tbl_revenu_familial
        # TODO bug field name est encore là
        db_table.update_table(
            "tbl_revenu_familial",
            new_rec_name="nom",
            new_model_name="accorderie.revenu.familial",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_revenu_familial",
            "norevenufamilial",
            delete=True,
        )
        db_column.update_column(
            "tbl_revenu_familial",
            "revenu",
            new_field_name="nom",
        )

        # tbl_situation_maison
        db_table.update_table(
            "tbl_situation_maison",
            new_rec_name="nom",
            new_model_name="accorderie.situation.maison",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_situation_maison",
            "nosituationmaison",
            delete=True,
        )
        db_column.update_column(
            "tbl_situation_maison",
            "situation",
            new_field_name="nom",
        )

        # tbl_sous_categorie
        db_table.update_table(
            "tbl_sous_categorie",
            new_rec_name="titre",
            new_description="Titre de la sous-catégorie de services",
            new_model_name="accorderie.sous.categorie.service",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_sous_categorie",
            "nosouscategorieid",
            delete=True,
        )
        db_column.update_column(
            "tbl_sous_categorie",
            "nosouscategorie",
            new_field_name="sous_categorie_service",
            new_description="Sous catégorie de services",
        )
        db_column.update_column(
            "tbl_sous_categorie",
            "nocategorie",
            new_field_name="categorie",
            new_description="Catégorie",
        )
        db_column.update_column(
            "tbl_sous_categorie",
            "titresouscategorie",
            new_field_name="titre",
            new_description="Titre",
            compute_data_function="""titre.replace("&#8217;", "'").strip()""",
        )
        db_column.update_column(
            "tbl_sous_categorie",
            "supprimer",
            new_type="boolean",
            new_field_name="archive",
            new_description="Archivé",
            new_help=(
                "Lorsque archivé, cette sous-catégorie n'est plus en fonction,"
                " mais demeure accessible."
            ),
        )
        db_column.update_column(
            "tbl_sous_categorie",
            "approuver",
            new_field_name="approuver",
            new_description="Approuvé",
            new_type="boolean",
            new_help="Permet d'approuver cette sous-catégorie.",
        )

        # tbl_taxe
        db_table.update_table(
            "tbl_taxe",
            delete=True,
            # new_model_name="accorderie.taxe"
            # "taxe", new_model_name="accorderie.taxe", new_rec_name="nom_complet"
        )

        # tbl_titre
        db_table.update_table(
            "tbl_titre",
            new_rec_name="nom",
            new_model_name="accorderie.titre",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_titre",
            "notitre",
            delete=True,
        )
        db_column.update_column(
            "tbl_titre",
            "titre",
            new_field_name="nom",
        )
        db_column.update_column(
            "tbl_titre",
            "visible_titre",
        )
        db_column.update_column(
            "tbl_titre",
            "datemaj_titre",
        )

        # tbl_type_communication
        db_table.update_table(
            "tbl_type_communication",
            new_rec_name="nom",
            new_model_name="accorderie.type.communication",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_type_communication",
            "notypecommunication",
            delete=True,
        )
        db_column.update_column(
            "tbl_type_communication",
            "typecommunication",
            new_field_name="nom",
        )

        # tbl_type_compte
        db_table.update_table(
            "tbl_type_compte",
            new_model_name="accorderie.type.compte",
        )
        db_column.update_column(
            "tbl_type_compte",
            "nomembre",
            new_required=False,
        )
        db_column.update_column(
            "tbl_type_compte",
            "accodeursimple",
        )
        db_column.update_column(
            "tbl_type_compte",
            "admin",
        )
        db_column.update_column(
            "tbl_type_compte",
            "adminchef",
        )
        db_column.update_column(
            "tbl_type_compte",
            "reseau",
        )
        db_column.update_column(
            "tbl_type_compte",
            "spip",
        )
        db_column.update_column(
            "tbl_type_compte",
            "adminpointservice",
        )
        db_column.update_column(
            "tbl_type_compte",
            "adminordpointservice",
        )

        # tbl_type_fichier
        db_table.update_table(
            "tbl_type_fichier",
            new_rec_name="nom",
            new_model_name="accorderie.type.fichier",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_type_fichier",
            "id_typefichier",
            delete=True,
        )
        db_column.update_column(
            "tbl_type_fichier",
            "typefichier",
            new_field_name="nom",
        )
        db_column.update_column(
            "tbl_type_fichier",
            "datemaj_typefichier",
        )

        # tbl_type_tel
        db_table.update_table(
            "tbl_type_tel",
            new_rec_name="nom",
            new_model_name="accorderie.type.tel",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_type_tel",
            "notypetel",
            delete=True,
        )
        db_column.update_column(
            "tbl_type_tel",
            "typetel",
            new_field_name="nom",
        )

        # tbl_versement
        db_table.update_table(
            "tbl_versement",
            delete=True,
        )

        # tbl_ville
        db_table.update_table(
            "tbl_ville",
            new_rec_name="nom",
            new_model_name="accorderie.ville",
            nomenclator=True,
        )
        db_column.update_column(
            "tbl_ville",
            "noville",
            new_field_name="code",
            new_description="Code",
            new_help="Code de la ville",
        )
        db_column.update_column(
            "tbl_ville",
            "ville",
            new_field_name="nom",
            new_description="Nom",
        )
        db_column.update_column(
            "tbl_ville",
            "noregion",
            new_field_name="region",
            new_description="Région",
            # add_one2many=True,
        )

        # vue_membre_qc
        db_table.update_table(
            "Vue_Membre_Qc",
            delete=True,
        )

        # vue_membre_tr
        db_table.update_table(
            "Vue_Membre_TR",
            delete=True,
        )

        code_generator_db_tables = (
            env["code.generator.db.table"]
            # .search([("name", "in", ("tbl_membre", "tbl_pointservice"))])
            # .search([]).filtered(lambda x: x.name not in lst_table_to_delete)
            .search([])
        )

        # lst_nomenclator = (
        #     # "tbl_accorderie",
        #     # # "tbl_achat_ponctuel",
        #     # # "tbl_achat_ponctuel_produit",
        #     "tbl_region",
        #     "tbl_ville",
        #     "tbl_arrondissement",
        #     "tbl_cartier",
        #     "tbl_categorie",
        #     "tbl_categorie_sous_categorie",
        #     # # "tbl_commande",
        #     # # "tbl_commande_membre",
        #     # # "tbl_commande_membre_produit",
        #     # # "tbl_commentaire",
        #     # # "tbl_demande_service",
        #     # # "tbl_dmd_adhesion",
        #     # # "tbl_droits_admin",
        #     # # "tbl_echange_service",
        #     # "tbl_fichier",
        #     # # "tbl_fournisseur",
        #     # # "tbl_fournisseur_produit",
        #     # # "tbl_fournisseur_produit_commande",
        #     # # "tbl_fournisseur_produit_pointservice",
        #     # "tbl_info_logiciel_bd",
        #     # # "tbl_log_acces",
        #     # "tbl_membre",
        #     # "tbl_mensualite",
        #     "tbl_occupation",
        #     # # "tbl_offre_service_membre",
        #     "tbl_origine",
        #     # "tbl_pointservice",
        #     # # "tbl_pointservice_fournisseur",
        #     # # "tbl_pret",
        #     # # "tbl_produit",
        #     "tbl_provenance",
        #     "tbl_revenu_familial",
        #     "tbl_situation_maison",
        #     "tbl_sous_categorie",
        #     # "tbl_taxe",
        #     "tbl_titre",
        #     "tbl_type_communication",
        #     # # "tbl_type_compte",
        #     "tbl_type_fichier",
        #     "tbl_type_tel",
        #     # # "tbl_versement",
        # )
        # # lst_nomenclator = []
        #
        # if lst_nomenclator:
        #     for db_table_id in code_generator_db_tables:
        #         if db_table_id.name in lst_nomenclator:
        #             db_table_id.nomenclator = True

        lst_code_generator_id = code_generator_db_tables.generate_module(
            code_generator_id=code_generator_id
        )

        # Add new field
        ## Get model
        model_membre_name = env["code.generator.db.table"].search(
            [("name", "=", "tbl_membre")]
        )
        model_membre_id = env["ir.model"].search(
            [("model", "=", model_membre_name.model_name)]
        )
        model_categorie_sous_categorie_name = env[
            "code.generator.db.table"
        ].search([("name", "=", "tbl_categorie_sous_categorie")])
        model_categorie_sous_categorie_id = env["ir.model"].search(
            [("model", "=", model_categorie_sous_categorie_name.model_name)]
        )
        model_taxe_name = env["code.generator.db.table"].search(
            [("name", "=", "tbl_taxe")]
        )
        model_taxe_id = env["ir.model"].search(
            [("model", "=", model_taxe_name.model_name)]
        )
        model_type_compte_name = env["code.generator.db.table"].search(
            [("name", "=", "tbl_type_compte")]
        )
        model_type_compte_id = env["ir.model"].search(
            [("model", "=", model_type_compte_name.model_name)]
        )

        ## Create field compute with his code
        lst_value_code = []

        if model_membre_id:
            # TODO add variable to create field without export data
            value_field = {
                "name": "nom_complet",
                "field_description": "Nom complet",
                "ttype": "char",
                "code_generator_compute": "_compute_nom_complet",
                "model_id": model_membre_id.id,
            }
            env["ir.model.fields"].create(value_field)
            model_membre_id.rec_name = "nom_complet"
            # TODO validate it was name
            for field_id in model_membre_id.field_id:
                if field_id.name == "name":
                    field_id.unlink()
                    continue
            lst_value_code.append(
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
                }
            )

        if model_categorie_sous_categorie_id:
            value_field = {
                "name": "nom_complet",
                "field_description": "Nom complet",
                "ttype": "char",
                "code_generator_compute": "_compute_nom_complet",
                "model_id": model_categorie_sous_categorie_id.id,
            }
            env["ir.model.fields"].create(value_field)
            model_categorie_sous_categorie_id.rec_name = "nom_complet"
            for field_id in model_categorie_sous_categorie_id.field_id:
                if field_id.name == "name":
                    field_id.unlink()
                    continue
            lst_value_code.append(
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
                }
            )

        if model_taxe_id:
            value_field = {
                "name": "nom_complet",
                "field_description": "Nom complet",
                "ttype": "char",
                "code_generator_compute": "_compute_nom_complet",
                "model_id": model_taxe_id.id,
            }
            env["ir.model.fields"].create(value_field)
            model_taxe_id.rec_name = "nom_complet"
            for field_id in model_taxe_id.field_id:
                if field_id.name == "name":
                    field_id.unlink()
                    continue
            lst_value_code.append(
                {
                    "code": """for rec in self:
                                        value = ""
                                        if self.tauxtaxepro:
                                            value += str(self.tauxtaxepro)
                                        if self.tauxtaxepro and self.tauxtaxefed:
                                            value += " - "
                                        if self.tauxtaxefed:
                                            value += str(self.tauxtaxefed)
                                        rec.nom_complet = value
                                        """,
                    "name": "_compute_nom_complet",
                    "decorator": '@api.depends("tauxtaxepro", "tauxtaxefed")',
                    "param": "self",
                    "sequence": 1,
                    "m2o_module": code_generator_id.id,
                    "m2o_model": model_taxe_id.id,
                }
            )

        if model_type_compte_id:
            value_field = {
                "name": "nom_complet",
                "field_description": "Nom complet",
                "ttype": "char",
                "code_generator_compute": "_compute_nom_complet",
                "model_id": model_type_compte_id.id,
            }
            env["ir.model.fields"].create(value_field)
            model_type_compte_id.rec_name = "nom_complet"
            for field_id in model_type_compte_id.field_id:
                if field_id.name == "name":
                    field_id.unlink()
                    continue
            lst_value_code.append(
                {
                    "code": """for rec in self:
                           value = ""
                           value += str(self.accodeursimple)
                           value += str(self.admin)
                           value += str(self.adminchef)
                           value += str(self.reseau)
                           value += str(self.spip)
                           value += str(self.adminpointservice)
                           value += str(self.adminordpointservice)
                           rec.nom_complet = value
                           """,
                    "name": "_compute_nom_complet",
                    "decorator": (
                        '@api.depends("accodeursimple", "admin", "adminchef",'
                        ' "reseau", "spip", "adminpointservice",'
                        ' "adminordpointservice")'
                    ),
                    "param": "self",
                    "sequence": 1,
                    "m2o_module": code_generator_id.id,
                    "m2o_model": model_type_compte_id.id,
                }
            )

        env["code.generator.model.code"].create(lst_value_code)

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


def uninstall_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        code_generator_id = env["code.generator.module"].search(
            [("name", "=", MODULE_NAME)]
        )
        if code_generator_id:
            code_generator_id.unlink()

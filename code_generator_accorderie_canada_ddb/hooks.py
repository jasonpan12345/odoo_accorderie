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
        migration = MigrationDB(env, code_generator_id)

        # Modification of field before migration

        # tbl_accorderie
        migration.add_update_migration_model(
            "accorderie",
            new_model_name="accorderie.accorderie",
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
            new_description="Région administrative",
            new_required=False,
            new_help="Nom de la région administrative de l'Accorderie",
            # add_one2many=True,
        )
        migration.add_update_migration_field(
            "accorderie",
            "noville",
            new_field_name="ville",
            new_description="Ville",
            new_required=False,
            new_help="Nom de la ville de l'Accorderie",
            # add_one2many=True,
        )
        migration.add_update_migration_field(
            "accorderie",
            "noarrondissement",
            new_field_name="arrondissement",
            new_description="Arrondissement",
            new_help="Nom de l'Arrondissement qui contient l'Accorderie.",
        )
        migration.add_update_migration_field(
            "accorderie",
            "nocartier",
            # new_field_name="cartier",
            # new_description="Cartier",
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
            # new_description="Nom complet",
            delete=True,
        )
        migration.add_update_migration_field(
            "accorderie",
            "adresseaccorderie",
            new_field_name="adresse",
            new_description="Adresse",
            new_help="Adresse de l'Accorderie",
        )
        migration.add_update_migration_field(
            "accorderie",
            "codepostalaccorderie",
            new_field_name="code_postal",
            new_description="Code postal",
            new_help="Code postal de l'Accorderie",
        )
        migration.add_update_migration_field(
            "accorderie",
            "telaccorderie",
            new_field_name="telephone",
            new_description="Téléphone",
            new_help="Numéro de téléphone pour joindre l'Accorderie.",
        )
        migration.add_update_migration_field(
            "accorderie",
            "telecopieuraccorderie",
            new_field_name="telecopieur",
            new_description="Télécopieur",
            new_help="Numéro de télécopieur pour joindre l'Accorderie.",
        )
        migration.add_update_migration_field(
            "accorderie",
            "courrielaccorderie",
            new_field_name="courriel",
            new_description="Adresse courriel",
            new_help="Adresse courriel pour joindre l'Accorderie.",
        )
        migration.add_update_migration_field(
            "accorderie",
            "messagegrpachat",
            new_field_name="message_grp_achat",
            new_description="Message groupe d'achats",
            new_type="html",
            new_help="Message à afficher pour les groupes d'achats.",
        )
        migration.add_update_migration_field(
            "accorderie",
            "messageaccueil",
            new_field_name="message_accueil",
            new_description="Message d'accueil",
            new_type="html",
            new_help="Message à afficher pour accueillir les membres.",
        )
        migration.add_update_migration_field(
            "accorderie",
            "url_public_accorderie",
            new_field_name="url_public",
            new_description="Lien du site web publique",
            new_help="Lien du site web publique de l'Accorderie",
            force_widget="link_button",
        )
        migration.add_update_migration_field(
            "accorderie",
            "url_transac_accorderie",
            new_field_name="url_transactionnel",
            new_description="Lien du site web transactionnel",
            force_widget="link_button",
            new_help="Lien du site web transactionnel de l'Accorderie",
        )
        migration.add_update_migration_field(
            "accorderie",
            "url_logoaccorderie",
            new_field_name="logo",
            new_description="Logo",
            new_type="binary",
            force_widget="image",
            path_binary="/accorderie_canada/Intranet/images/logo",
            new_help="Logo de l'Accorderie",
        )
        migration.add_update_migration_field(
            "accorderie",
            "grpachat_admin",
            new_field_name="grp_achat_administrateur",
            new_description="Groupe d'achats des administrateurs",
            new_type="boolean",
            new_help=(
                "Permet de rendre accessible les achats pour les"
                " administrateurs."
            ),
        )
        migration.add_update_migration_field(
            "accorderie",
            "grpachat_accordeur",
            new_field_name="grp_achat_membre",
            new_description="Groupe d'achats membre",
            new_type="boolean",
            new_help="Rend accessible les achats pour les Accordeurs.",
        )
        migration.add_update_migration_field(
            "accorderie",
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
        migration.add_update_migration_field(
            "accorderie",
            "datemaj_accorderie",
            new_field_name="date_mise_a_jour",
            new_description="Dernière mise à jour",
            new_help="Date de la dernière mise à jour",
        )

        # tbl_achat_ponctuel
        # Deleted
        # # TODO create name from selected field, new_rec_name
        # migration.add_update_migration_model(
        #     "achat.ponctuel",
        #     new_model_name="accorderie.achat.ponctuel",
        #     new_description="Gestion des achats ponctuels"
        #     # new_rec_name="nom",
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel",
        #     "noachatponctuel",
        #     delete=True,
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel",
        #     "nomembre",
        #     new_field_name="membre",
        #     new_description="Membre",
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel",
        #     "dateachatponctuel",
        #     new_field_name="date_achat",
        #     new_description="Date d'achat",
        #     new_help="Date de l'achat ponctuel"
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel",
        #     "montantpaiementachatponct",
        #     new_field_name="paiement_effectue",
        #     new_description="Paiement effectué",
        #     new_help="Montant du paiement"
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel",
        #     "achatponcfacturer",
        #     new_field_name="est_facture",
        #     new_description="Facturé",
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel",
        #     "majoration_achatponct",
        #     new_field_name="majoration",
        #     new_description="Majoration",
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel",
        #     "taxef_achatponct",
        #     new_field_name="taxe_federal",
        #     new_description="Taxes fédérales",
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel",
        #     "taxep_achatponct",
        #     new_field_name="taxe_provincial",
        #     new_description="Taxes provinciales",
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel",
        #     "datemaj_achantponct",
        #     new_field_name="date_mise_a_jour",
        #     new_description="Dernière mise à jour",
        #     new_help="Date de la dernière mise à jour",
        # )

        # tbl_achat_ponctuel_produit
        # Deleted
        # # TODO create name from selected field, new_rec_name
        # migration.add_update_migration_model(
        #     "achat.ponctuel.produit",
        #     new_model_name="accorderie.achat.ponctuel.produit",
        #     new_description="Liaisons des achats ponctuels aux produits des fournisseurs."
        #     # new_rec_name="nom",
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel.produit",
        #     "noachatponctuelproduit",
        #     delete=True,
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel.produit",
        #     "noachatponctuel",
        #     new_field_name="achat_ponctuel",
        #     new_description="Achat ponctuel",
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel.produit",
        #     "nofournisseurproduit",
        #     new_field_name="fournisseur_produit",
        #     new_description="Fournisseur du produit",
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel.produit",
        #     "qteacheter",
        #     new_field_name="quantite_acheter",
        #     new_description="Quantité achetée"
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel.produit",
        #     "coutunit_achatponctprod",
        #     new_field_name="cout_unitaire",
        #     new_description="Coût unitaire",
        #     new_help="Le coût unitaire de l'achat ponctuel"
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel.produit",
        #     "sitaxablef_achatponctprod",
        #     new_field_name="taxable_federal",
        #     new_description="Appliquer taxes fédérales",
        #     new_help="Cocher si application des taxes fédérales."
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel.produit",
        #     "sitaxablep_achatponctprod",
        #     new_field_name="taxale_provincial",
        #     new_description="Appliquer taxes provinciales",
        #     new_help="Cocher si application des taxes provinciales."
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel.produit",
        #     "prixfacturer_achatponctprod",
        #     new_field_name="prix_facturer",
        #     new_description="Prix facturé",
        # )
        # migration.add_update_migration_field(
        #     "achat.ponctuel.produit",
        #     "datemaj_achatponcproduit",
        #     new_field_name="date_mise_a_jour",
        #     new_description="Dernière mise à jour",
        #     new_help="Date de la dernière mise à jour",
        # )

        # tbl_arrondissement
        migration.add_update_migration_model(
            "arrondissement",
            new_model_name="accorderie.arrondissement",
            new_description="Ensemble des arrondissement des Accorderies",
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
            new_description="Ville",
            # add_one2many=True,
        )
        migration.add_update_migration_field(
            "arrondissement",
            "arrondissement",
            new_field_name="nom",
            new_description="Nom",
        )

        # tbl_cartier
        migration.add_update_migration_model(
            "cartier",
            new_model_name="accorderie.quartier",
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
            new_description="Arrondissement",
            new_help="Arrondissement associé au quartier",
        )
        migration.add_update_migration_field(
            "cartier",
            "cartier",
            new_field_name="nom",
            new_description="Nom du quartier",
            new_help="Nom du quartier",
        )

        # tbl_categorie
        migration.add_update_migration_model(
            "categorie",
            new_model_name="accorderie.categorie.service",
            new_description="Les catégories de services des Accorderies",
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
            new_description="Nom",
            new_help="Le nom de la catégorie des services",
            compute_data_function="""nom.replace("&#8217;", "'").strip()""",
        )
        migration.add_update_migration_field(
            "categorie",
            "supprimer",
            new_field_name="archive",
            new_description="Archivé",
            new_type="boolean",
            new_help="Permet d'archiver cette catégorie.",
        )
        migration.add_update_migration_field(
            "categorie",
            "approuver",
            new_field_name="approuve",
            new_description="Approuvé",
            new_type="boolean",
            new_help="Permet d'approuver cette catégorie.",
        )

        # tbl_categorie_sous_categorie
        # TODO
        migration.add_update_migration_model(
            "categorie.sous.categorie",
            new_model_name="accorderie.sous.sous.categorie.service",
            new_rec_name="titre_offre_service",
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "nosouscategorieid",
            new_field_name="sous_categorie_id",
            new_description="Sous catégorie de services",
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "nocategoriesouscategorie",
            delete=True,
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "nosouscategorie",
            delete=True,
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "nocategorie",
            delete=True,
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "titreoffre",
            new_field_name="titre_offre_service",
            new_description="Titre de l'offre de services",
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "supprimer",
            new_field_name="archive",
            new_description="Archivé",
            new_type="boolean",
            new_help="Permet d'archiver cette sous-sous-catégorie.",
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "approuver",
            new_field_name="approuve",
            new_description="Approuvé",
            new_type="boolean",
            new_help="Permet d'approuver cette sous-sous-catégorie.",
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "description",
            compute_data_function="""description.replace("&#8217;", "'").strip()""",
        )
        migration.add_update_migration_field(
            "categorie.sous.categorie",
            "nooffre",
            new_field_name="no_offre",
            new_description="Numéro de l'offre"
            # TODO mettre invisible
            # TODO mettre numéro_complet
        )

        # tbl_commande
        # Effacé
        # migration.add_update_migration_model(
        #     "commande",
        #     # new_rec_name="description",
        #     new_model_name="accorderie.commande",
        # )
        # migration.add_update_migration_field(
        #     "commande",
        #     "nocommande",
        #     new_required=False,
        # )
        # migration.add_update_migration_field(
        #     "commande",
        #     "nopointservice",
        # )
        # migration.add_update_migration_field(
        #     "commande",
        #     "norefcommande",
        # )
        # migration.add_update_migration_field(
        #     "commande",
        #     "datecmddebut",
        # )
        # migration.add_update_migration_field(
        #     "commande",
        #     "datecmdfin",
        # )
        # migration.add_update_migration_field(
        #     "commande",
        #     "datecueillette",
        # )
        # migration.add_update_migration_field(
        #     "commande",
        #     "taxepcommande",
        # )
        # migration.add_update_migration_field(
        #     "commande",
        #     "taxefcommande",
        # )
        # migration.add_update_migration_field(
        #     "commande",
        #     "majoration",
        # )
        # migration.add_update_migration_field(
        #     "commande",
        #     "commandetermine",
        # )
        # migration.add_update_migration_field(
        #     "commande",
        #     "datemaj_cmd",
        # )

        # tbl_commande_membre
        # migration.add_update_migration_model(
        #     "commande.membre",
        #     # new_rec_name="description",
        #     new_model_name="accorderie.commande.membre",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "nocommandemembre",
        #     delete=True,
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "nocommande",
        #     new_required=False,
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "nomembre",
        #     new_required=False,
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "numrefmembre",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "cmdconfirmer",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "facturer",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "montantpaiement",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "coutunitaireajour",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "datecmdmb",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "datefacture",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "archivesoustotal",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "archivetotmajoration",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "archivetottxfed",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "archivetottxprov",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre",
        #     "datemaj_cmdmembre",
        # )

        # tbl_commande_membre_produit
        # migration.add_update_migration_model(
        #     "commande.membre.produit",
        #     # new_rec_name="description",
        #     new_model_name="accorderie.commande.membre.produit",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre.produit",
        #     "nocmdmbproduit",
        #     delete=True,
        # )
        # migration.add_update_migration_field(
        #     "commande.membre.produit",
        #     "nocommandemembre",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre.produit",
        #     "nofournisseurproduitcommande",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre.produit",
        #     "qte",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre.produit",
        #     "qtedeplus",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre.produit",
        #     "ajustement",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre.produit",
        #     "coutunitaire_facture",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre.produit",
        #     "sitaxablep_facture",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre.produit",
        #     "sitaxablef_facture",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre.produit",
        #     "prixfacturer_manuel",
        # )
        # migration.add_update_migration_field(
        #     "commande.membre.produit",
        #     "datemaj_cmdmembreprod",
        # )

        # tbl_commentaire
        migration.add_update_migration_model(
            "commentaire",
            # new_rec_name="description",
            new_model_name="accorderie.commentaire",
            new_description=(
                "Les commentaires des membres envers d'autres membres sur des"
                " services et demandes"
            ),
        )
        migration.add_update_migration_field(
            "commentaire",
            "nocommentaire",
            delete=True,
        )
        migration.add_update_migration_field(
            "commentaire",
            "nopointservice",
            new_field_name="point_service",
            new_description="Point de services",
        )
        migration.add_update_migration_field(
            "commentaire",
            "nomembresource",
            new_field_name="membre_source",
            new_description="Membre source",
            new_help="Membre duquel provient le commentaire",
        )
        migration.add_update_migration_field(
            "commentaire",
            "nomembreviser",
            new_field_name="membre_viser",
            new_description="Membre visé",
            new_help="Membre visé par le commentaire",
        )
        migration.add_update_migration_field(
            "commentaire",
            "nooffreservicemembre",
            new_field_name="offre_service_id",
            new_description="Offre de services",
            new_help="L'offre de services qui est visée par ce commentaire.",
        )
        migration.add_update_migration_field(
            "commentaire",
            "nodemandeservice",
            new_field_name="demande_service_id",
            new_description="Demande de services",
            new_help=(
                "La demande de services qui est visée par ce commentaire."
            ),
        )
        migration.add_update_migration_field(
            "commentaire",
            "dateheureajout",
            new_field_name="datetime_creation",
            new_description="Date et heure de création",
        )
        migration.add_update_migration_field(
            "commentaire",
            "situation_impliquant",
            # TODO support type selection
            # 1. UnE ou des AccordeurEs
            # 2. Un comité
            # 3. UnE employéE
            # 4. Autre
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
        migration.add_update_migration_model(
            "demande.service",
            # new_rec_name="description",
            new_model_name="accorderie.demande.service",
        )
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
        migration.add_update_migration_model(
            "dmd.adhesion",
            # new_rec_name="description",
            new_model_name="accorderie.dmd.adhesion",
        )
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
        migration.add_update_migration_model(
            "droits.admin",
            # new_rec_name="description",
            new_model_name="accorderie.droits.admin",
        )
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
        migration.add_update_migration_model(
            "echange.service",
            # new_rec_name="nom",
            new_model_name="accorderie.echange.service",
        )
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
            new_description="Nombre d'heure",
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
        migration.add_update_migration_model(
            "fichier",
            # new_rec_name="description",
            new_model_name="accorderie.fichier",
        )
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
        #     "fournisseur",
        #     # new_rec_name="description",
        #     new_model_name="accorderie.fournisseur",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "nofournisseur",
        #     delete=True,
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "noaccorderie",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "noregion",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "noville",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "nomfournisseur",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "adresse",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "codepostalfournisseur",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "telfournisseur",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "faxfounisseur",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "courrielfournisseur",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "nomcontact",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "postecontact",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "courrielcontact",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "notefournisseur",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "visible_fournisseur",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur",
        #     "datemaj_fournisseur",
        # )

        # tbl_fournisseur_produit
        # migration.add_update_migration_model(
        #     "fournisseur.produit",
        #     # new_rec_name="description",
        #     new_model_name="accorderie.fournisseur.produit",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit",
        #     "nofournisseurproduit",
        #     delete=True,
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit",
        #     "nofournisseur",
        #     new_required=False,
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit",
        #     "noproduit",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit",
        #     "codeproduit",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit",
        #     "zqtestokeacc",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit",
        #     "zcoutunitaire",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit",
        #     "visible_fournisseurproduit",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit",
        #     "datemaj_fournproduit",
        # )

        # tbl_fournisseur_produit_commande
        # migration.add_update_migration_model(
        #     "fournisseur.produit.commande",
        #     # new_rec_name="description",
        #     new_model_name="accorderie.fournisseur.produit.commande",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit.commande",
        #     "nofournisseurproduitcommande",
        #     delete=True,
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit.commande",
        #     "nocommande",
        #     new_required=False,
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit.commande",
        #     "nofournisseurproduit",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit.commande",
        #     "nbboiteminfournisseur",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit.commande",
        #     "qteparboiteprevu",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit.commande",
        #     "coutunitprevu",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit.commande",
        #     "disponible",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit.commande",
        #     "datemaj_fournprodcommande",
        # )

        # tbl_fournisseur_produit_pointservice
        # migration.add_update_migration_model(
        #     "fournisseur.produit.pointservice",
        #     # new_rec_name="description",
        #     new_model_name="accorderie.fournisseur.produit.pointservice",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit.pointservice",
        #     "nofournisseurproduitpointservice",
        #     delete=True,
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit.pointservice",
        #     "nofournisseurproduit",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit.pointservice",
        #     "nopointservice",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit.pointservice",
        #     "qtestokeacc",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit.pointservice",
        #     "coutunitaire",
        # )
        # migration.add_update_migration_field(
        #     "fournisseur.produit.pointservice",
        #     "datemaj_fournprodptserv",
        # )

        # tbl_info_logiciel_bd
        # removed

        # tbl_log_acces
        # removed

        # tbl_membre
        # TODO change rec_name to display_name with compute of nom et prenom
        migration.add_update_migration_model(
            "membre",
            # new_rec_name="nom_complet",
            new_model_name="accorderie.membre",
        )
        migration.add_update_migration_field(
            "membre",
            "nomembre",
            delete=True,
        )
        migration.add_update_migration_field(
            "membre", "nocartier", new_field_name="quartier"
        )
        migration.add_update_migration_field(
            "membre",
            "noaccorderie",
            new_field_name="accorderie",
            new_description="Accorderie",
            new_help="Accorderie associé",
            # add_one2many=True,
        )
        migration.add_update_migration_field(
            "membre",
            "nopointservice",
            new_field_name="point_service",
            new_description="Point de service",
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
        # migration.add_update_migration_field(
        #     "membre",
        #     "",
        #     new_field_name="nom_complet",
        #     new_type="char",
        #     new_description="Nom complet",
        #     new_help="TODO",
        #     new_compute="_compute_nom_complet"
        # )

        # tbl_mensualite
        # removed

        # tbl_occupation
        migration.add_update_migration_model(
            "occupation",
            new_rec_name="nom",
            new_model_name="accorderie.occupation",
        )
        migration.add_update_migration_field(
            "occupation",
            "nooccupation",
            delete=True,
        )
        migration.add_update_migration_field(
            "occupation",
            "occupation",
            new_field_name="nom",
        )

        # tbl_offre_service_membre
        migration.add_update_migration_model(
            "offre.service.membre",
            # new_rec_name="description",
            new_model_name="accorderie.offre.service.membre",
        )
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
        migration.add_update_migration_model(
            "origine",
            new_rec_name="nom",
            new_model_name="accorderie.origine",
        )
        migration.add_update_migration_field(
            "origine",
            "noorigine",
            delete=True,
        )
        migration.add_update_migration_field(
            "origine",
            "origine",
            new_field_name="nom",
        )

        # tbl_point_service
        migration.add_update_migration_model(
            "pointservice",
            new_rec_name="nom",
            new_model_name="accorderie.pointservice",
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
            new_description="Nom",
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
        #     "pointservice.fournisseur",
        #     # new_rec_name="description",
        #     new_model_name="accorderie.pointservice.fournisseur",
        # )
        # migration.add_update_migration_field(
        #     "pointservice.fournisseur",
        #     "nopointservicefournisseur",
        #     delete=True,
        # )
        # migration.add_update_migration_field(
        #     "pointservice.fournisseur",
        #     "nopointservice",
        # )
        # migration.add_update_migration_field(
        #     "pointservice.fournisseur",
        #     "nofournisseur",
        # )
        # migration.add_update_migration_field(
        #     "pointservice.fournisseur",
        #     "datemaj_pointservicefournisseur",
        # )

        # tbl_pret
        # removed

        # tbl_produit
        # migration.add_update_migration_model(
        #     "produit",
        #     # new_rec_name="description",
        #     new_model_name="accorderie.produit",
        # )
        # migration.add_update_migration_field(
        #     "produit",
        #     "noproduit",
        #     delete=True,
        # )
        # migration.add_update_migration_field(
        #     "produit",
        #     "notitre",
        # )
        # migration.add_update_migration_field(
        #     "produit",
        #     "noaccorderie",
        # )
        # migration.add_update_migration_field(
        #     "produit",
        #     "nomproduit",
        # )
        # migration.add_update_migration_field(
        #     "produit",
        #     "taxablef",
        # )
        # migration.add_update_migration_field(
        #     "produit",
        #     "taxablep",
        # )
        # migration.add_update_migration_field(
        #     "produit",
        #     "visible_produit",
        # )
        # migration.add_update_migration_field(
        #     "produit",
        #     "datemaj_produit",
        # )

        # tbl_provenance
        migration.add_update_migration_model(
            "provenance",
            new_rec_name="nom",
            new_model_name="accorderie.provenance",
        )
        migration.add_update_migration_field(
            "provenance",
            "noprovenance",
            delete=True,
        )
        migration.add_update_migration_field(
            "provenance",
            "provenance",
            new_field_name="nom",
        )

        # tbl_region
        migration.add_update_migration_model(
            "region",
            new_rec_name="nom",
            new_model_name="accorderie.region",
        )
        migration.add_update_migration_field(
            "region",
            "noregion",
            new_field_name="code",
            new_description="Code de région",
            new_help="Code de la région administrative",
        )
        migration.add_update_migration_field(
            "region",
            "region",
            new_field_name="nom",
            new_description="Nom",
        )

        # tbl_revenu_familial
        # TODO bug field name est encore là
        migration.add_update_migration_model(
            "revenu.familial",
            new_rec_name="nom",
            new_model_name="accorderie.revenu.familial",
        )
        migration.add_update_migration_field(
            "revenu.familial",
            "norevenufamilial",
            delete=True,
        )
        migration.add_update_migration_field(
            "revenu.familial",
            "revenu",
            new_field_name="nom",
        )

        # tbl_situation_maison
        migration.add_update_migration_model(
            "situation.maison",
            new_rec_name="nom",
            new_model_name="accorderie.situation.maison",
        )
        migration.add_update_migration_field(
            "situation.maison",
            "nosituationmaison",
            delete=True,
        )
        migration.add_update_migration_field(
            "situation.maison",
            "situation",
            new_field_name="nom",
        )

        # tbl_sous_categorie
        migration.add_update_migration_model(
            "sous.categorie",
            new_rec_name="titre",
            new_description="Titre de la sous-catégorie de services",
            new_model_name="accorderie.sous.categorie.service",
        )
        migration.add_update_migration_field(
            "sous.categorie",
            "nosouscategorieid",
            delete=True,
        )
        migration.add_update_migration_field(
            "sous.categorie",
            "nosouscategorie",
            new_field_name="sous_categorie_service",
            new_description="Sous catégorie de services",
        )
        migration.add_update_migration_field(
            "sous.categorie",
            "nocategorie",
            new_field_name="categorie",
            new_description="Catégorie",
        )
        migration.add_update_migration_field(
            "sous.categorie",
            "titresouscategorie",
            new_field_name="titre",
            new_description="Titre",
            compute_data_function="""titre.replace("&#8217;", "'").strip()""",
        )
        migration.add_update_migration_field(
            "sous.categorie",
            "supprimer",
            new_type="boolean",
            new_field_name="archive",
            new_description="Archivé",
            new_help=(
                "Lorsque archivé, cette sous-catégorie n'est plus en fonction,"
                " mais demeure accessible."
            ),
        )
        migration.add_update_migration_field(
            "sous.categorie",
            "approuver",
            new_field_name="approuver",
            new_description="Approuvé",
            new_type="boolean",
            new_help="Permet d'approuver cette sous-catégorie.",
        )

        # tbl_taxe
        # TODO
        # migration.add_update_migration_model(
        #     "taxe",
        #     new_model_name="accorderie.taxe"
        #     # "taxe", new_model_name="accorderie.taxe", new_rec_name="nom_complet"
        # )
        # migration.add_update_migration_field(
        #     "taxe",
        #     "notaxe",
        #     delete=True,
        # )
        # migration.add_update_migration_field(
        #     "taxe",
        #     "tauxtaxepro",
        # )
        # migration.add_update_migration_field(
        #     "taxe",
        #     "notaxepro",
        # )
        # migration.add_update_migration_field(
        #     "taxe",
        #     "tauxtaxefed",
        # )
        # migration.add_update_migration_field(
        #     "taxe",
        #     "notaxefed",
        # )
        # migration.add_update_migration_field(
        #     "taxe",
        #     "tauxmajoration",
        # )
        # migration.add_update_migration_field(
        #     "taxe",
        #     "",
        #     new_field_name="nom_complet",
        #     new_type="char",
        #     new_description="Nom complet",
        #     new_help="TODO",
        #     new_compute="_compute_nom_complet"
        # )

        # tbl_titre
        migration.add_update_migration_model(
            "titre",
            new_rec_name="nom",
            new_model_name="accorderie.titre",
        )
        migration.add_update_migration_field(
            "titre",
            "notitre",
            delete=True,
        )
        migration.add_update_migration_field(
            "titre",
            "titre",
            new_field_name="nom",
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
        migration.add_update_migration_model(
            "type.communication",
            new_rec_name="nom",
            new_model_name="accorderie.type.communication",
        )
        migration.add_update_migration_field(
            "type.communication",
            "notypecommunication",
            delete=True,
        )
        migration.add_update_migration_field(
            "type.communication",
            "typecommunication",
            new_field_name="nom",
        )

        # tbl_type_compte
        migration.add_update_migration_model(
            "type.compte",
            new_model_name="accorderie.type.compte",
        )
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
        migration.add_update_migration_model(
            "type.fichier",
            new_rec_name="nom",
            new_model_name="accorderie.type.fichier",
        )
        migration.add_update_migration_field(
            "type.fichier",
            "id_typefichier",
            delete=True,
        )
        migration.add_update_migration_field(
            "type.fichier",
            "typefichier",
            new_field_name="nom",
        )
        migration.add_update_migration_field(
            "type.fichier",
            "datemaj_typefichier",
        )

        # tbl_type_tel
        migration.add_update_migration_model(
            "type.tel",
            new_rec_name="nom",
            new_model_name="accorderie.type.tel",
        )
        migration.add_update_migration_field(
            "type.tel",
            "notypetel",
            delete=True,
        )
        migration.add_update_migration_field(
            "type.tel",
            "typetel",
            new_field_name="nom",
        )

        # tbl_versement
        # removed

        # tbl_ville
        migration.add_update_migration_model(
            "ville",
            new_rec_name="nom",
            new_model_name="accorderie.ville",
        )
        migration.add_update_migration_field(
            "ville",
            "noville",
            new_field_name="code",
            new_description="Code",
            new_help="Code de la ville",
        )
        migration.add_update_migration_field(
            "ville",
            "ville",
            new_field_name="nom",
            new_description="Nom",
        )
        migration.add_update_migration_field(
            "ville",
            "noregion",
            new_field_name="region",
            new_description="Région",
            # add_one2many=True,
        )

        # TODO call generate table, remove rec_name

        lst_table_to_delete = (
            "tbl_info_logiciel_bd",
            "tbl_log_acces",
            "tbl_mensualite",
            "tbl_pret",
            "tbl_versement",
            "tbl_commande",
            "tbl_achat_ponctuel",
            "tbl_achat_ponctuel_produit",
            "tbl_commande_membre",
            "tbl_commande_membre_produit",
            "tbl_commande_membre_produit",
            "tbl_fournisseur",
            "tbl_fournisseur_produit",
            "tbl_fournisseur_produit_commande",
            "tbl_fournisseur_produit_pointservice",
            "tbl_pointservice_fournisseur",
            "tbl_produit",
            "tbl_taxe",
            "Vue_Membre_Qc",
            "Vue_Membre_TR",
        )
        # TODO move this in model edit
        for table_to_delete in lst_table_to_delete:
            table_id = env["code.generator.db.table"].search(
                [("name", "=", table_to_delete)]
            )
            if not table_id:
                # Ignore missing table in table to delete
                continue
            table_id.delete = True
            # To help visualize column
            for column_id in table_id.o2m_columns:
                column_id.ignore_field = True
                column_id.delete = True

        code_generator_db_tables = (
            env["code.generator.db.table"]
            # .search([("name", "in", ("tbl_membre", "tbl_pointservice"))])
            .search([]).filtered(lambda x: x.name not in lst_table_to_delete)
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
            # # "tbl_pret",
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
            # # "tbl_versement",
        )
        # lst_nomenclator = []

        if lst_nomenclator:
            for db_table_id in code_generator_db_tables:
                if db_table_id.name in lst_nomenclator:
                    db_table_id.nomenclator = True

        lst_code_generator_id = code_generator_db_tables.generate_module(
            code_generator_id=code_generator_id
        )

        if len(lst_code_generator_id) != 1:
            _logger.error("Suppose to create only 1 module.")
            return

        # Add new field
        ## Get model
        # TODO search new model name from table name
        model_membre_id = env["ir.model"].search([("model", "=", "membre")])
        model_categorie_sous_categorie_id = env["ir.model"].search(
            [("model", "=", "categorie.sous.categorie")]
        )
        model_taxe_id = env["ir.model"].search([("model", "=", "taxe")])
        model_type_compte_id = env["ir.model"].search(
            [("model", "=", "type.compte")]
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


class MigrationDB:
    def __init__(self, env, code_generator_id):
        self.env = env
        self.code_generator_id = code_generator_id

    def add_update_migration_field(
        self,
        model_name,
        field_name,
        new_field_name=None,
        new_description=None,
        new_type=None,
        new_help=None,
        new_required=None,
        new_compute=None,
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
        :param new_description:
        :param new_type:
        :param new_help:
        :param new_required:
        :param new_compute:
        :param sql_select_modify: update select command with this string
        :param delete: import data, use to compute information but delete the field at the end with his data
        :param ignore_field: never compute it and ignore data from it
        :param path_binary: path for type binary when the past was char
        :param force_widget:
        :param compute_data_function: function, in string, to run with data in argument and overwrite data
        :param add_one2many:
        :return:
        """

        tbl_name = f"tbl_{model_name.replace('.', '_')}"
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
            and new_description is None
            and new_type is None
            and new_help is None
            and new_required is None
            and new_compute is None
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
            if new_description is not None:
                value["new_description"] = new_description
            if new_type is not None:
                value["new_type"] = new_type
            if new_help is not None:
                value["new_help"] = new_help
            if new_required is not None:
                value["new_required"] = new_required
                value["new_change_required"] = True
            if new_compute is not None:
                value["new_compute"] = new_compute
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

        # Update code_generator_db_columns
        table_id = self.env["code.generator.db.table"].search(
            [("name", "=", tbl_name)]
        )
        if not table_id:
            _logger.error(
                f"Cannot update table {tbl_name} with field {field_name}."
            )
        else:
            column_id = self.env["code.generator.db.column"].search(
                [("m2o_table", "=", table_id.id), ("name", "=", field_name)]
            )

            if not field_name:
                # Create new field
                column_id = self.env["code.generator.db.column"].create(
                    {
                        "name": "",
                        "is_new_field": True,
                        "m2o_table": table_id.id,
                    }
                )

            if len(column_id) > 1:
                _logger.error(
                    f"Find too much column field {field_name} from table"
                    f" {tbl_name}."
                )
            elif column_id:
                if new_field_name:
                    column_id.new_name = new_field_name
                if new_description:
                    column_id.new_description = new_description
                if new_type:
                    column_id.new_type = new_type
                if new_help:
                    column_id.new_help = new_help
                if new_required is not None:
                    column_id.new_change_required = True
                    column_id.new_required = new_required
                if new_compute is not None:
                    column_id.new_compute = new_compute
                if path_binary:
                    column_id.path_binary = path_binary
                if force_widget:
                    column_id.force_widget = force_widget
                if add_one2many:
                    column_id.add_one2many = add_one2many
                if compute_data_function:
                    column_id.compute_data_function = compute_data_function
                if sql_select_modify:
                    column_id.sql_select_modify = sql_select_modify
                if delete:
                    column_id.delete = True
                if ignore_field:
                    column_id.ignore_field = True
            else:
                _logger.error(
                    f"Cannot find field {field_name} from table {tbl_name}."
                )

        self.env["code.generator.db.update.migration.field"].create(value)

    def add_update_migration_model(
        self,
        model_name,
        new_model_name=None,
        new_description=None,
        new_rec_name=None,
    ):

        tbl_name = f"tbl_{model_name.replace('.', '_')}"

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

        # Update code_generator_db_table
        table_id = self.env["code.generator.db.table"].search(
            [("name", "=", tbl_name)]
        )
        if not table_id:
            _logger.error(f"Cannot update table {tbl_name}.")
        else:
            if new_model_name:
                table_id.new_model_name = new_model_name
            if new_rec_name:
                table_id.new_rec_name = new_rec_name
            table_id.new_description = new_description

        self.env["code.generator.db.update.migration.model"].create(value)


def uninstall_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        code_generator_id = env["code.generator.module"].search(
            [("name", "=", MODULE_NAME)]
        )
        if code_generator_id:
            code_generator_id.unlink()

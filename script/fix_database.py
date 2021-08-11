#!/usr/bin/env python
import pymysql


# Fix date with string "0000-00-00"

# cr.execute("SET sql_mode = 'NO_ZERO_DATE';")
# cr.execute("SET sql_mode = 'NO_ZERO_IN_DATE';")

# query_search = """SELECT *
# FROM tbl_demande_service
# WHERE DateFin = "0000-00-00"
# """
#
# cr.execute(query_search)
# old_v = cr.fetchall()
#
# query = """UPDATE `tbl_demande_service`
# SET DateFin = NULL
# WHERE DateFin = "0000-00-00"
# """
#
# v = cr.execute(query)

# lst_echange_service = cr.fetchall()
# query_search = """SELECT *
# FROM tbl_echange_service
# """
#
# cr.execute(query_search)
# lst_echange_service = cr.fetchall()

def main():
    database = "accorderie_log_2019"
    host = "localhost"
    port = 3306
    user = "accorderie"
    password = "accorderie"
    schema = "public"

    conn = pymysql.connect(
        db=database, host=host, port=port, user=user, password=password
    )

    cr = conn.cursor()

    # debug_over_droits_admin(cr)

    delete_record(cr)
    replace_record(cr)
    alter_table(cr)
    add_foreign_key(cr)

    cr.close()


def debug_over_droits_admin(cr):
    query_search = """SELECT NoMembre
    FROM tbl_droits_admin
    """
    cr.execute(query_search)
    lst_droits_admin = cr.fetchall()

    set_droits_admin = set([a[0] for a in lst_droits_admin])

    query_search = """SELECT NoMembre
    FROM tbl_membre
    """
    cr.execute(query_search)
    lst_membre = cr.fetchall()
    set_lst_membre = set([a[0] for a in lst_membre])

    set_missing_membre = set_droits_admin.difference(set_lst_membre)
    # Result 0, 945, 7703, 1253, 2655
    print(set_missing_membre)


def delete_record(cr):
    # Delete record
    query_search = """DELETE FROM `tbl_droits_admin` WHERE NoMembre in (0, 945, 7703, 1253, 2655);"""
    cr.execute(query_search)


def alter_table(cr):
    # Fix tbl_echange_service NbHeure, transform time to float
    query_search = """ALTER TABLE tbl_echange_service modify NbHeure float null;"""
    cr.execute(query_search)
    query_search = """alter table tbl_commande_membre modify NoMembre int unsigned null;"""
    cr.execute(query_search)

    # Fix field for foreign key
    query_search = """
    ALTER TABLE tbl_arrondissement
    MODIFY NoVille int unsigned null;
    """
    cr.execute(query_search)


def replace_record(cr):
    # Replace 0 by null
    query_search = """UPDATE `tbl_accorderie` SET `NoArrondissement` = NULL WHERE NoArrondissement = 0;"""
    cr.execute(query_search)
    query_search = """UPDATE `tbl_commande_membre` SET `NoMembre` = NULL WHERE NoMembre = 0;"""
    cr.execute(query_search)
    query_search = """UPDATE `tbl_commentaire` SET `NoMembreViser` = NULL WHERE NoMembreViser = 0;"""
    cr.execute(query_search)
    query_search = """UPDATE `tbl_commentaire` SET `NoOffreServiceMembre` = NULL WHERE NoOffreServiceMembre = 0;"""
    cr.execute(query_search)
    query_search = """UPDATE `tbl_commentaire` SET `NoDemandeService` = NULL WHERE NoDemandeService = 0;"""
    cr.execute(query_search)
    query_search = """UPDATE `tbl_echange_service` SET `NoMembreVendeur` = NULL WHERE NoMembreVendeur = 0;"""
    cr.execute(query_search)
    query_search = """UPDATE `tbl_echange_service` SET `NoMembreAcheteur` = NULL WHERE NoMembreAcheteur = 0;"""
    cr.execute(query_search)
    query_search = """UPDATE `tbl_echange_service` SET `NoDemandeService` = NULL WHERE NoDemandeService = 0;"""
    cr.execute(query_search)
    query_search = """UPDATE `tbl_echange_service` SET `NoOffreServiceMembre` = NULL WHERE NoOffreServiceMembre = 0;"""
    cr.execute(query_search)


def add_foreign_key(cr):
    try:
        query_search = """
        ALTER TABLE tbl_accorderie
        DROP FOREIGN KEY foreign_key_tbl_accorderie_noarrondissement;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    ALTER TABLE tbl_accorderie
    ADD CONSTRAINT foreign_key_tbl_accorderie_noarrondissement
    FOREIGN KEY (NoArrondissement) REFERENCES tbl_arrondissement(NoArrondissement)
    on update set null on delete set null;
    """
    cr.execute(query_search)
    # - ville
    try:
        query_search = """
        ALTER TABLE tbl_accorderie
        DROP FOREIGN KEY foreign_key_tbl_accorderie_noville;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    ALTER TABLE tbl_accorderie
    ADD CONSTRAINT foreign_key_tbl_accorderie_noville
    FOREIGN KEY (NoVille) REFERENCES tbl_ville(NoVille);
    """
    cr.execute(query_search)
    # - region
    try:
        query_search = """
        ALTER TABLE tbl_accorderie
        DROP FOREIGN KEY foreign_key_tbl_accorderie_noregion;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    ALTER TABLE tbl_accorderie
    ADD CONSTRAINT foreign_key_tbl_accorderie_noregion
    FOREIGN KEY (NoRegion) REFERENCES tbl_region(NoRegion);
    """
    cr.execute(query_search)
    # - cartier
    try:
        query_search = """
        ALTER TABLE tbl_accorderie
        DROP FOREIGN KEY foreign_key_tbl_accorderie_nocartier;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    ALTER TABLE tbl_accorderie
    ADD CONSTRAINT foreign_key_tbl_accorderie_nocartier
    FOREIGN KEY (NoCartier) REFERENCES tbl_cartier(NoCartier);
    """
    cr.execute(query_search)

    # Arrondissement
    try:
        query_search = """
        ALTER TABLE tbl_arrondissement
        DROP FOREIGN KEY foreign_key_tbl_ville_noville;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    ALTER TABLE tbl_arrondissement
    ADD CONSTRAINT foreign_key_tbl_ville_noville
    FOREIGN KEY (NoVille) REFERENCES tbl_ville(NoVille)
    on update set null on delete set null;
    """
    cr.execute(query_search)

    # Cartier
    try:
        query_search = """
        ALTER TABLE tbl_cartier
        DROP FOREIGN KEY foreign_key_tbl_arrondissement_noarrondissement;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    ALTER TABLE tbl_cartier
    ADD CONSTRAINT foreign_key_tbl_arrondissement_noarrondissement
    FOREIGN KEY (NoArrondissement) REFERENCES tbl_arrondissement(NoArrondissement);
    """
    cr.execute(query_search)

    # Ville
    try:
        query_search = """
        ALTER TABLE tbl_ville
        DROP FOREIGN KEY foreign_key_tbl_region_noregion;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    ALTER TABLE tbl_ville
    ADD CONSTRAINT foreign_key_tbl_region_noregion
    FOREIGN KEY (NoRegion) REFERENCES tbl_region(NoRegion)
    on update set null on delete set null;
    """
    cr.execute(query_search)

    # achat_ponctuel
    try:
        query_search = """
        ALTER TABLE tbl_achat_ponctuel
        DROP FOREIGN KEY tbl_achat_ponctuel_tbl_membre_NoMembre_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_achat_ponctuel
        add constraint tbl_achat_ponctuel_tbl_membre_NoMembre_fk
            foreign key (NoMembre) references tbl_membre (NoMembre);
    """
    cr.execute(query_search)

    # achat_ponctuel
    try:
        query_search = """
        ALTER TABLE tbl_achat_ponctuel
        DROP FOREIGN KEY tbl_achat_ponctuel_tbl_membre_NoMembre_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_achat_ponctuel
        add constraint tbl_achat_ponctuel_tbl_membre_NoMembre_fk
            foreign key (NoMembre) references tbl_membre (NoMembre);
    """
    cr.execute(query_search)

    # achat_ponctuel_produit
    # - achat_ponctuel
    try:
        query_search = """
        ALTER TABLE tbl_achat_ponctuel_produit
        DROP FOREIGN KEY tbl_achat_ponctuel_produit_tbl_achat_ponctuel_NoAchatPonctuel_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_achat_ponctuel_produit
        add constraint tbl_achat_ponctuel_produit_tbl_achat_ponctuel_NoAchatPonctuel_fk
            foreign key (NoAchatPonctuel) references tbl_achat_ponctuel (NoAchatPonctuel);
    """
    cr.execute(query_search)

    # - fournisseur_produit
    try:
        query_search = """
        ALTER TABLE tbl_achat_ponctuel_produit
        DROP FOREIGN KEY tbl_achat_pp_tbl_fournisseur_produit_NoFournisseurProduit_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_achat_ponctuel_produit
        add constraint tbl_achat_pp_tbl_fournisseur_produit_NoFournisseurProduit_fk
            foreign key (NoFournisseurProduit) references tbl_fournisseur_produit (NoFournisseurProduit);
    """
    cr.execute(query_search)

    # categorie_sous_categorie
    # - categorie
    # try:
    #     query_search = """
    #     ALTER TABLE tbl_achat_ponctuel_produit
    #     DROP FOREIGN KEY tbl_achat_ponctuel_produit_tbl_achat_ponctuel_NoAchatPonctuel_fk;
    #     """
    #     cr.execute(query_search)
    # except Exception:
    #     pass
    #
    # query_search = """
    # alter table tbl_achat_ponctuel_produit
    # 	add constraint tbl_achat_ponctuel_produit_tbl_achat_ponctuel_NoAchatPonctuel_fk
    # 		foreign key (NoAchatPonctuel) references tbl_achat_ponctuel (NoAchatPonctuel);
    # """
    # cr.execute(query_search)
    #
    # # - fournisseur_produit

    # tbl_commande
    try:
        query_search = """
        ALTER TABLE tbl_commande
        DROP FOREIGN KEY tbl_commande_tbl_pointservice_NoPointService_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_commande
        add constraint tbl_commande_tbl_pointservice_NoPointService_fk
            foreign key (NoPointService) references tbl_pointservice (NoPointService);
    """
    cr.execute(query_search)

    # tbl_commande_membre
    # - commande
    try:
        query_search = """
        ALTER TABLE tbl_commande_membre
        DROP FOREIGN KEY tbl_commande_membre_tbl_commande_NoCommande_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_commande_membre
        add constraint tbl_commande_membre_tbl_commande_NoCommande_fk
            foreign key (NoCommande) references tbl_commande (NoCommande);
    """
    cr.execute(query_search)

    # - membre
    try:
        query_search = """
        ALTER TABLE tbl_commande_membre
        DROP FOREIGN KEY tbl_commande_membre_tbl_membre_NoMembre_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_commande_membre
        add constraint tbl_commande_membre_tbl_membre_NoMembre_fk
            foreign key (NoMembre) references tbl_membre (NoMembre);
    """
    cr.execute(query_search)

    # tbl_fournisseur_produit_commande
    # - commande
    try:
        query_search = """
        ALTER TABLE tbl_fournisseur_produit_commande
        DROP FOREIGN KEY tbl_fournisseur_produit_commande_tbl_commande_NoCommande_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_fournisseur_produit_commande
        add constraint tbl_fournisseur_produit_commande_tbl_commande_NoCommande_fk
            foreign key (NoCommande) references tbl_commande (NoCommande);
    """
    cr.execute(query_search)

    # - fournisseur produit
    try:
        query_search = """
        ALTER TABLE tbl_fournisseur_produit_commande
        DROP FOREIGN KEY tbl_fpc_tbl_fournisseur_produit_NoFournisseurProduit_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_fournisseur_produit_commande
        add constraint tbl_fpc_tbl_fournisseur_produit_NoFournisseurProduit_fk
            foreign key (NoFournisseurProduit) references tbl_fournisseur_produit (NoFournisseurProduit);
    """
    cr.execute(query_search)

    # tbl_commande_membre_produit
    # - commande membre
    try:
        query_search = """
        ALTER TABLE tbl_commande_membre_produit
        DROP FOREIGN KEY tbl_cmp_tbl_commande_membre_NoCommandeMembre_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_commande_membre_produit
        add constraint tbl_cmp_tbl_commande_membre_NoCommandeMembre_fk
            foreign key (NoCommandeMembre) references tbl_commande_membre (NoCommandeMembre);
    """
    cr.execute(query_search)

    # TODO fix me
    # # - fournisseur produit commande
    # try:
    #     query_search = """
    #     ALTER TABLE tbl_commande_membre_produit
    #     DROP FOREIGN KEY tbl_cmp_tbl_fpc_NoFournisseurProduitCommande_fk;
    #     """
    #     cr.execute(query_search)
    # except Exception:
    #     pass
    #
    # query_search = """
    # alter table tbl_commande_membre_produit
    # 	add constraint tbl_cmp_tbl_fpc_NoFournisseurProduitCommande_fk
    # 		foreign key (NoFournisseurProduitCommande) references tbl_fournisseur_produit_commande (NoFournisseurProduitCommande);
    # """
    # cr.execute(query_search)

    # tbl_commentaire
    # - point service
    try:
        query_search = """
        ALTER TABLE tbl_commentaire
        DROP FOREIGN KEY tbl_commentaire_tbl_pointservice_NoPointService_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_commentaire
        add constraint tbl_commentaire_tbl_pointservice_NoPointService_fk
            foreign key (NoPointService) references tbl_pointservice (NoPointService);
    """
    cr.execute(query_search)

    # - membre source
    try:
        query_search = """
        ALTER TABLE tbl_commentaire
        DROP FOREIGN KEY tbl_commentaire_tbl_membre_NoMembre_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_commentaire
        add constraint tbl_commentaire_tbl_membre_NoMembre_fk
            foreign key (NoMembreSource) references tbl_membre (NoMembre);
    """
    cr.execute(query_search)

    # - membre visé
    try:
        query_search = """
        ALTER TABLE tbl_commentaire
        DROP FOREIGN KEY tbl_commentaire_tbl_membre_NoMembre_fk_2;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_commentaire
        add constraint tbl_commentaire_tbl_membre_NoMembre_fk_2
            foreign key (NoMembreViser) references tbl_membre (NoMembre);
    """
    cr.execute(query_search)

    # - offre service membre
    try:
        query_search = """
        ALTER TABLE tbl_commentaire
        DROP FOREIGN KEY tbl_commentaire_tbl_offre_service_membre_NoOffreServiceMembre_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_commentaire
        add constraint tbl_commentaire_tbl_offre_service_membre_NoOffreServiceMembre_fk
            foreign key (NoOffreServiceMembre) references tbl_offre_service_membre (NoOffreServiceMembre);
    """
    cr.execute(query_search)

    # - demande service
    try:
        query_search = """
        ALTER TABLE tbl_commentaire
        DROP FOREIGN KEY tbl_commentaire_tbl_demande_service_NoDemandeService_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_commentaire
        add constraint tbl_commentaire_tbl_demande_service_NoDemandeService_fk
            foreign key (NoDemandeService) references tbl_demande_service (NoDemandeService);
    """
    cr.execute(query_search)

    # tbl_demande_service
    # - membre
    try:
        query_search = """
        ALTER TABLE tbl_demande_service
        DROP FOREIGN KEY tbl_demande_service_tbl_membre_NoMembre_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_demande_service
        add constraint tbl_demande_service_tbl_membre_NoMembre_fk
            foreign key (NoMembre) references tbl_membre (NoMembre);
    """
    cr.execute(query_search)

    # - accorderie
    try:
        query_search = """
        ALTER TABLE tbl_demande_service
        DROP FOREIGN KEY tbl_demande_service_tbl_accorderie_NoAccorderie_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_demande_service
        add constraint tbl_demande_service_tbl_accorderie_NoAccorderie_fk
            foreign key (NoAccorderie) references tbl_accorderie (NoAccorderie);
    """
    cr.execute(query_search)

    # tbl_dmd_adhesion
    # - accorderie
    try:
        query_search = """
        ALTER TABLE tbl_dmd_adhesion
        DROP FOREIGN KEY tbl_dmd_adhesion_tbl_accorderie_NoAccorderie_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_dmd_adhesion
        add constraint tbl_dmd_adhesion_tbl_accorderie_NoAccorderie_fk
            foreign key (NoAccorderie) references tbl_accorderie (NoAccorderie);
    """
    cr.execute(query_search)

    # tbl_droits_admin
    # - membre
    try:
        query_search = """
        ALTER TABLE tbl_droits_admin
        DROP FOREIGN KEY tbl_droits_admin_tbl_membre_NoMembre_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_droits_admin
        add constraint tbl_droits_admin_tbl_membre_NoMembre_fk
            foreign key (NoMembre) references tbl_membre (NoMembre);
    """
    cr.execute(query_search)

    # tbl_echange_service
    # - point service
    try:
        query_search = """
        ALTER TABLE tbl_echange_service
        DROP FOREIGN KEY tbl_echange_service_tbl_pointservice_NoPointService_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_echange_service
        add constraint tbl_echange_service_tbl_pointservice_NoPointService_fk
            foreign key (NoPointService) references tbl_pointservice (NoPointService);
    """
    cr.execute(query_search)

    # TODO membre vendeur a des valeurs erronés
    # - membre vendeur
    # try:
    #     query_search = """
    #     ALTER TABLE tbl_echange_service
    #     DROP FOREIGN KEY tbl_echange_service_tbl_membre_NoMembre_fk;
    #     """
    #     cr.execute(query_search)
    # except Exception:
    #     pass
    #
    # query_search = """
    # alter table tbl_echange_service
    #     add constraint tbl_echange_service_tbl_membre_NoMembre_fk
    #         foreign key (NoMembreVendeur) references tbl_membre (NoMembre);
    # """
    # cr.execute(query_search)

    # - membre acheteur
    try:
        query_search = """
        ALTER TABLE tbl_echange_service
        DROP FOREIGN KEY tbl_echange_service_tbl_membre_NoMembre_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_echange_service
        add constraint tbl_echange_service_tbl_membre_NoMembre_fk
            foreign key (NoMembreAcheteur) references tbl_membre (NoMembre);
    """
    cr.execute(query_search)

    # - demande service
    try:
        query_search = """
        ALTER TABLE tbl_echange_service
        DROP FOREIGN KEY tbl_echange_service_tbl_demande_service_NoDemandeService_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_echange_service
        add constraint tbl_echange_service_tbl_demande_service_NoDemandeService_fk
            foreign key (NoDemandeService) references tbl_demande_service (NoDemandeService);
    """
    cr.execute(query_search)

    # - offre service membre
    try:
        query_search = """
        ALTER TABLE tbl_echange_service
        DROP FOREIGN KEY tbl_es_tbl_offre_service_membre_NoOffreServiceMembre_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_echange_service
        add constraint tbl_es_tbl_offre_service_membre_NoOffreServiceMembre_fk
            foreign key (NoOffreServiceMembre) references tbl_offre_service_membre (NoOffreServiceMembre);
    """
    cr.execute(query_search)

    # tbl_fichier
    # - accorderie
    try:
        query_search = """
        ALTER TABLE tbl_fichier
        DROP FOREIGN KEY tbl_fichier_tbl_accorderie_NoAccorderie_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_fichier
        add constraint tbl_fichier_tbl_accorderie_NoAccorderie_fk
            foreign key (NoAccorderie) references tbl_accorderie (NoAccorderie);
    """
    cr.execute(query_search)

    # - type fichier
    try:
        query_search = """
        ALTER TABLE tbl_fichier
        DROP FOREIGN KEY tbl_fichier_tbl_type_fichier_Id_TypeFichier_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_fichier
        add constraint tbl_fichier_tbl_type_fichier_Id_TypeFichier_fk
            foreign key (Id_TypeFichier) references tbl_type_fichier (Id_TypeFichier);
    """
    cr.execute(query_search)

    # tbl_fournisseur
    # - accorderie
    try:
        query_search = """
        ALTER TABLE tbl_fournisseur
        DROP FOREIGN KEY tbl_fournisseur_tbl_accorderie_NoAccorderie_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_fournisseur
        add constraint tbl_fournisseur_tbl_accorderie_NoAccorderie_fk
            foreign key (NoAccorderie) references tbl_accorderie (NoAccorderie);
    """
    cr.execute(query_search)

    # - region
    try:
        query_search = """
        ALTER TABLE tbl_fournisseur
        DROP FOREIGN KEY tbl_fournisseur_tbl_region_NoRegion_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_fournisseur
        add constraint tbl_fournisseur_tbl_region_NoRegion_fk
            foreign key (NoRegion) references tbl_region (NoRegion);
    """
    cr.execute(query_search)

    # - ville
    try:
        query_search = """
        ALTER TABLE tbl_fournisseur
        DROP FOREIGN KEY tbl_fournisseur_tbl_ville_NoVille_fk;
        """
        cr.execute(query_search)
    except Exception:
        pass

    query_search = """
    alter table tbl_fournisseur
        add constraint tbl_fournisseur_tbl_ville_NoVille_fk
            foreign key (NoVille) references tbl_ville (NoVille);
    """
    cr.execute(query_search)

if __name__ == "__main__":
    main()

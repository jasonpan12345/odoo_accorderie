#!/usr/bin/env python
from collections import defaultdict

import pymysql

SECRET_PASSWORD = ""


def main():
    database = "accorderie_log_2019"
    host = "localhost"
    port = 3306
    user = "accorderie"
    password = "accorderie"
    schema = "public"

    conn = pymysql.connect(host=host, port=port, user=user, password=password)

    cr = conn.cursor()

    drop_database(cr)
    create_database(cr)

    conn.commit()
    cr.close()

    conn = pymysql.connect(
        db=database, host=host, port=port, user=user, password=password
    )
    cr = conn.cursor()

    create_table(cr)
    fill_dct_table(cr)

    conn.commit()
    cr.close()


def fill_dct_table(cr):
    sql = """INSERT INTO tbl_region (NoRegion, Region) 
    VALUES (1, 'Region 1');"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_ville (NoVille, Ville, NoRegion) 
    VALUES (1, 'Nom ville', 1);"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_arrondissement (NoArrondissement, NoVille, Arrondissement) 
    VALUES (1, 1, 'Nom Arrondissement');"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_cartier (NoCartier, NoArrondissement, Cartier) 
    VALUES (1, 1, 'Nom cartier');"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_categorie (NoCategorie, TitreCategorie, Supprimer, Approuver) 
    VALUES (1, 'Titre catégorie 1', 0, -1);"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_sous_categorie (NoSousCategorieId, NoSousCategorie, NoCategorie, TitreSousCategorie, Supprimer, Approuver) 
    VALUES (null, '1', 1, 'Titre sous catégorie', 0, -1);"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_categorie_sous_categorie (NoSousCategorieId, NoSousCategorie, NoCategorie, TitreOffre, Supprimer, Approuver, Description, NoOffre) 
    VALUES (null, null, null, null, null, null, null, null);"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_type_fichier (TypeFichier, DateMAJ_TypeFichier) 
    VALUES ('Type 1', '2021-08-17 00:41:55');"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_info_logiciel_bd (NoInfoLogicielBD, DerniereVersionLogiciel, MAJOblig, LienWeb, DateCreation) 
    VALUES (1, null, null, null, '2021-08-17 00:46:07');"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_accorderie (NoAccorderie, NoRegion, NoVille, NoArrondissement, NoCartier, Nom, NomComplet, AdresseAccorderie, CodePostalAccorderie, TelAccorderie, TelecopieurAccorderie, CourrielAccorderie, MessageGrpAchat, MessageAccueil, URL_Public_Accorderie, URL_Transac_Accorderie, URL_LogoAccorderie, GrpAchat_Admin, GrpAchat_Accordeur, NonVisible, DateMAJ_Accorderie)
    VALUES (1, 1, 1, null, null, 'Québec', 'de Québec', '', 'G1K 3A7', '4184184188', '4184184188', 'courriel@courriel.ca', '<p>Bonjour chers membres,</p>', '', 'https://www.google.ca', 'https://www.google.ca', 'LogoQuebec.png', -1, -1, 0, '2020-08-24 21:42:51');"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_fichier (Id_TypeFichier, NoAccorderie, NomFichierStokage, NomFichierOriginal, Si_Admin, Si_AccorderieLocalSeulement, Si_Disponible, DateMAJ_Fichier) 
    VALUES (1, 1, 'Nom 1', 'Nom original', 1, 1, 0, '2021-08-17 00:45:05');"""
    cr.execute(sql)
    sql = f"""INSERT INTO tbl_membre (NoCartier, NoAccorderie, NoPointService, NoPointService2, NoTypeCommunication, NoOccupation, NoOrigine, NoSituationMaison, NoProvenance, NoRevenuFamilial, NoArrondissement, NoVille, NoRegion, MembreCA, PartSocialPaye, CodePostal, DateAdhesion, Nom, Prenom, Adresse, Telephone1, PosteTel1, NoTypeTel1, Telephone2, PosteTel2, NoTypeTel2, Telephone3, PosteTel3, NoTypeTel3, Courriel, AchatRegrouper, PretActif, PretRadier, PretPayer, EtatCompteCourriel, BottinTel, BottinCourriel, MembreActif, MembreConjoint, NoMembreConjoint, Memo, Sexe, AnneeNaissance, PrecisezOrigine, NomUtilisateur, MotDePasse, ProfilApprouver, MembrePrinc, NomAccorderie, RecevoirCourrielGRP, PasCommunication, DescriptionAccordeur, Date_MAJ_Membre, TransfereDe)
        VALUES (1, 1, null, null, null, null, null, null, null, null, null, 1, 1, 0, 0, null, null, "Paul", null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, -1, null, null, null, null, null, null, null, encode("patate","{SECRET_PASSWORD}"), -1, null, null, null, null, null, '2021-08-17 00:47:30', null);"""
    cr.execute(sql)
    sql = f"""INSERT INTO tbl_membre (NoCartier, NoAccorderie, NoPointService, NoPointService2, NoTypeCommunication, NoOccupation, NoOrigine, NoSituationMaison, NoProvenance, NoRevenuFamilial, NoArrondissement, NoVille, NoRegion, MembreCA, PartSocialPaye, CodePostal, DateAdhesion, Nom, Prenom, Adresse, Telephone1, PosteTel1, NoTypeTel1, Telephone2, PosteTel2, NoTypeTel2, Telephone3, PosteTel3, NoTypeTel3, Courriel, AchatRegrouper, PretActif, PretRadier, PretPayer, EtatCompteCourriel, BottinTel, BottinCourriel, MembreActif, MembreConjoint, NoMembreConjoint, Memo, Sexe, AnneeNaissance, PrecisezOrigine, NomUtilisateur, MotDePasse, ProfilApprouver, MembrePrinc, NomAccorderie, RecevoirCourrielGRP, PasCommunication, DescriptionAccordeur, Date_MAJ_Membre, TransfereDe)
        VALUES (1, 1, null, null, null, null, null, null, null, null, null, 1, 1, 0, 0, null, null, "Martin", null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, -1, null, null, null, null, null, null, null, encode("patate","{SECRET_PASSWORD}"), -1, null, null, null, null, null, '2021-08-17 00:47:30', null);"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_pointservice (NoAccorderie, NoMembre, NoMembre2, NomPointService, OrdrePointService, NoteGrpAchatPageClient, DateMAJ_PointService) 
    VALUES (1, 1, 2, 'Service point 1', 0, "Note de groupe d'achat", '2021-08-17 01:02:25');"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_pointservice (NoAccorderie, NoMembre, NoMembre2, NomPointService, OrdrePointService, NoteGrpAchatPageClient, DateMAJ_PointService) 
    VALUES (1, 2, 1, 'Service point 2', 0, "Note de groupe d'achat", '2021-08-17 01:02:25');"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_pointservice (NoAccorderie, NoMembre, NoMembre2, NomPointService, OrdrePointService, NoteGrpAchatPageClient, DateMAJ_PointService) 
    VALUES (1, 2, 1, 'Service point 2', 0, "Note de groupe d'achat", '2021-08-17 01:02:25');"""
    cr.execute(sql)

    # Force change id, 2 to 3
    sql = """DELETE FROM tbl_pointservice WHERE NoPointService=2;"""
    cr.execute(sql)

    sql = """UPDATE tbl_membre
SET NoPointService = 1, NoPointService2 = 3
WHERE NoMembre = 1;"""
    cr.execute(sql)
    sql = """UPDATE tbl_membre
SET NoPointService = 3, NoPointService2 = 1
WHERE NoMembre = 2;"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_pret (NoMembre, NoMembre_Intermediaire, NoMembre_Responsable, DateDemandePret, MontantDemande, RaisonEmprunt, DateComitePret, Si_PretAccorder, MontantAccorder, Note, Recommandation, TautInteretAnnuel, DatePret, NbreMois, NbrePaiement, DateMAJ_Pret) 
    VALUES (1, null, 1, null, null, null, null, null, null, null, null, null, null, null, null, '2021-08-17 15:39:31');"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_mensualite (Id_Pret) 
    VALUES (1);"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_versement (Id_Mensualite, MontantVersement, DateMAJ_Versement) 
    VALUES (1, null, '2021-08-17 15:42:55');"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_type_tel (TypeTel) 
    VALUES ('Type tel 1');"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_type_communication (TypeCommunication) 
    VALUES ('type communication 1');"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_taxe (TauxTaxePro, NoTaxePro, TauxTaxeFed, NoTaxeFed, TauxMajoration) 
    VALUES (null, null, null, null, null);"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_situation_maison (Situation) 
    VALUES (null);"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_revenu_familial (Revenu) 
    VALUES (null);"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_provenance (Provenance)
     VALUES (null);"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_origine (Origine) 
    VALUES (null);"""
    cr.execute(sql)
    sql = """INSERT INTO tbl_occupation (Occupation) 
    VALUES (null);"""
    cr.execute(sql)


def drop_database(cr):
    sql = """drop database accorderie_log_2019;"""
    try:
        cr.execute(sql)
    except Exception as e:
        pass


def create_database(cr):
    sql = """
CREATE DATABASE accorderie_log_2019;
"""
    cr.execute(sql)


def create_table(cr):
    sql = """
create table tbl_categorie
(
    NoCategorie    int unsigned auto_increment
        primary key,
    TitreCategorie varchar(255) charset latin1 null,
    Supprimer      int(1)                      null,
    Approuver      int(1)                      null
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create table tbl_info_logiciel_bd
(
    NoInfoLogicielBD        int unsigned auto_increment
        primary key,
    DerniereVersionLogiciel int unsigned                          null,
    MAJOblig                int(1) unsigned                       null,
    LienWeb                 varchar(255)                          null,
    DateCreation            timestamp default current_timestamp() null
)
    charset = utf8mb3;
"""
    cr.execute(sql)
    sql = """
create table tbl_occupation
(
    NoOccupation int unsigned auto_increment
        primary key,
    Occupation   varchar(35) null
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create table tbl_origine
(
    NoOrigine int unsigned auto_increment
        primary key,
    Origine   varchar(35) null
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create table tbl_provenance
(
    NoProvenance int unsigned auto_increment
        primary key,
    Provenance   varchar(35) null
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create table tbl_region
(
    NoRegion int unsigned auto_increment
        primary key,
    Region   varchar(60) null
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create table tbl_revenu_familial
(
    NoRevenuFamilial int unsigned auto_increment
        primary key,
    Revenu           varchar(35) null
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create table tbl_situation_maison
(
    NoSituationMaison int unsigned auto_increment
        primary key,
    Situation         varchar(35) null
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create table tbl_sous_categorie
(
    NoSousCategorieId  int(11) unsigned        null,
    NoSousCategorie    char(2)      default '' not null,
    NoCategorie        int unsigned default 0  not null,
    TitreSousCategorie varchar(255)            null,
    Supprimer          int(1)                  null,
    Approuver          int(1)                  null,
    primary key (NoSousCategorie, NoCategorie),
    constraint tbl_sous_categorie_NoSousCategorieId_uindex
        unique (NoSousCategorieId),
    constraint tbl_sous_categorie_tbl_categorie_NoCategorie_fk
        foreign key (NoCategorie) references tbl_categorie (NoCategorie)
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create table tbl_categorie_sous_categorie
(
    NoSousCategorieId        int(11) unsigned            null,
    NoCategorieSousCategorie int unsigned auto_increment
        primary key,
    NoSousCategorie          char(2) charset latin1      null,
    NoCategorie              int unsigned                null,
    TitreOffre               varchar(255) charset latin1 null,
    Supprimer                int(1)                      null,
    Approuver                int(1)                      null,
    Description              varchar(255) charset latin1 null,
    NoOffre                  int unsigned                null,
    constraint tbl_csc_tbl_sous_categorie_NoSousCategorieId_fk
        foreign key (NoSousCategorieId) references tbl_sous_categorie (NoSousCategorieId)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create fulltext index RchFullText_TitreDescrip
    on tbl_categorie_sous_categorie (TitreOffre, Description);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_sous_categorie_tbl_categorie1_idx
    on tbl_sous_categorie (NoCategorie);
"""
    cr.execute(sql)
    sql = """
create table tbl_taxe
(
    NoTaxe         int unsigned auto_increment
        primary key,
    TauxTaxePro    double unsigned            null,
    NoTaxePro      varchar(85) charset latin1 null,
    TauxTaxeFed    double unsigned            null,
    NoTaxeFed      varchar(85) charset latin1 null,
    TauxMajoration double unsigned            null
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create table tbl_titre
(
    NoTitre       int unsigned auto_increment
        primary key,
    Titre         varchar(50) charset latin1            null,
    Visible_Titre tinyint(1) unsigned                   null,
    DateMAJ_Titre timestamp default current_timestamp() null on update current_timestamp()
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create table tbl_type_communication
(
    NoTypeCommunication int unsigned auto_increment
        primary key,
    TypeCommunication   varchar(35) null
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create table tbl_type_fichier
(
    Id_TypeFichier      int unsigned auto_increment
        primary key,
    TypeFichier         varchar(80)                           null,
    DateMAJ_TypeFichier timestamp default current_timestamp() not null on update current_timestamp()
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create table tbl_type_tel
(
    NoTypeTel int unsigned auto_increment
        primary key,
    TypeTel   varchar(35) null
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create table tbl_ville
(
    NoVille  int unsigned auto_increment
        primary key,
    Ville    varchar(60)  null,
    NoRegion int unsigned null,
    constraint foreign_key_tbl_region_noregion
        foreign key (NoRegion) references tbl_region (NoRegion)
            on update set null on delete set null
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create table tbl_arrondissement
(
    NoArrondissement int unsigned auto_increment
        primary key,
    NoVille          int unsigned               null,
    Arrondissement   varchar(60) charset latin1 null,
    constraint foreign_key_tbl_ville_noville
        foreign key (NoVille) references tbl_ville (NoVille)
            on update set null on delete set null
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_arrondissement_tbl_ville1_idx
    on tbl_arrondissement (NoVille);
"""
    cr.execute(sql)
    sql = """
create table tbl_cartier
(
    NoCartier        int unsigned auto_increment
        primary key,
    NoArrondissement int unsigned default 0     not null,
    Cartier          varchar(60) charset latin1 null,
    constraint foreign_key_tbl_arrondissement_noarrondissement
        foreign key (NoArrondissement) references tbl_arrondissement (NoArrondissement)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create table tbl_accorderie
(
    NoAccorderie           int unsigned auto_increment
        primary key,
    NoRegion               int unsigned                          not null,
    NoVille                int unsigned                          not null,
    NoArrondissement       int unsigned                          null,
    NoCartier              int unsigned                          null,
    Nom                    varchar(45) charset latin1            null,
    NomComplet             varchar(255)                          not null,
    AdresseAccorderie      varchar(255) charset latin1           null,
    CodePostalAccorderie   varchar(7) charset latin1             null,
    TelAccorderie          varchar(10) charset latin1            null,
    TelecopieurAccorderie  varchar(10) charset latin1            null,
    CourrielAccorderie     varchar(255) charset latin1           null,
    MessageGrpAchat        text                                  null,
    MessageAccueil         text                                  null,
    URL_Public_Accorderie  varchar(255)                          null,
    URL_Transac_Accorderie varchar(255)                          null,
    URL_LogoAccorderie     varchar(255)                          null,
    GrpAchat_Admin         tinyint   default 0                   null,
    GrpAchat_Accordeur     tinyint   default 0                   null,
    NonVisible             int       default 0                   not null,
    DateMAJ_Accorderie     timestamp default current_timestamp() null on update current_timestamp(),
    constraint foreign_key_tbl_accorderie_noarrondissement
        foreign key (NoArrondissement) references tbl_arrondissement (NoArrondissement)
            on update set null on delete set null,
    constraint foreign_key_tbl_accorderie_nocartier
        foreign key (NoCartier) references tbl_cartier (NoCartier),
    constraint foreign_key_tbl_accorderie_noregion
        foreign key (NoRegion) references tbl_region (NoRegion),
    constraint foreign_key_tbl_accorderie_noville
        foreign key (NoVille) references tbl_ville (NoVille)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_accorderie_tbl_arrondissement1_idx
    on tbl_accorderie (NoArrondissement);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_accorderie_tbl_cartier1_idx
    on tbl_accorderie (NoCartier);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_accorderie_tbl_region1_idx
    on tbl_accorderie (NoRegion);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_accorderie_tbl_ville1_idx
    on tbl_accorderie (NoVille);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_cartier_tbl_arrondissement1_idx
    on tbl_cartier (NoArrondissement);
"""
    cr.execute(sql)
    sql = """
create table tbl_dmd_adhesion
(
    NoDmdAdhesion int unsigned auto_increment
        primary key,
    NoAccorderie  int unsigned default 0                   not null,
    Nom           varchar(45) charset latin1               null,
    Prenom        varchar(45) charset latin1               null,
    Telephone     varchar(10) charset latin1               null,
    Poste         varchar(10) charset latin1               null,
    Courriel      varchar(255) charset latin1              null,
    Supprimer     smallint(1)  default 0                   null,
    Transferer    smallint(1)  default 0                   null,
    EnAttente     tinyint      default 0                   null,
    DateMAJ       timestamp    default current_timestamp() null,
    constraint tbl_dmd_adhesion_tbl_accorderie_NoAccorderie_fk
        foreign key (NoAccorderie) references tbl_accorderie (NoAccorderie)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_dmd_adhesion_tbl_accorderie1_idx
    on tbl_dmd_adhesion (NoAccorderie);
"""
    cr.execute(sql)
    sql = """
create table tbl_fichier
(
    Id_Fichier                  int unsigned auto_increment
        primary key,
    Id_TypeFichier              int unsigned                                 not null,
    NoAccorderie                int unsigned                                 not null,
    NomFichierStokage           varchar(255)                                 not null,
    NomFichierOriginal          varchar(255)                                 not null,
    Si_Admin                    tinyint unsigned default 1                   null,
    Si_AccorderieLocalSeulement tinyint unsigned default 1                   null,
    Si_Disponible               tinyint unsigned default 0                   null,
    DateMAJ_Fichier             timestamp        default current_timestamp() null on update current_timestamp(),
    constraint tbl_fichier_tbl_accorderie_NoAccorderie_fk
        foreign key (NoAccorderie) references tbl_accorderie (NoAccorderie),
    constraint tbl_fichier_tbl_type_fichier_Id_TypeFichier_fk
        foreign key (Id_TypeFichier) references tbl_type_fichier (Id_TypeFichier)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_fichier_tbl_accorderie1_idx
    on tbl_fichier (NoAccorderie);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_fichier_tbl_type_fichier1_idx
    on tbl_fichier (Id_TypeFichier);
"""
    cr.execute(sql)
    sql = """
create table tbl_fournisseur
(
    NoFournisseur         int unsigned auto_increment
        primary key,
    NoAccorderie          int unsigned                                    not null,
    NoRegion              int unsigned                                    not null,
    NoVille               int unsigned                                    not null,
    NomFournisseur        varchar(80) charset latin1                      null,
    Adresse               varchar(80) charset latin1                      null,
    CodePostalFournisseur varchar(7) charset latin1                       null,
    TelFournisseur        varchar(14) charset latin1                      null,
    FaxFounisseur         varchar(40) charset latin1                      null,
    CourrielFournisseur   varchar(255) charset latin1                     null,
    NomContact            varchar(100) charset latin1                     null,
    PosteContact          varchar(8) charset latin1                       null,
    CourrielContact       varchar(255) charset latin1                     null,
    NoteFournisseur       text charset latin1                             null,
    Visible_Fournisseur   tinyint(1) unsigned default 1                   null,
    DateMAJ_Fournisseur   timestamp           default current_timestamp() null on update current_timestamp(),
    constraint tbl_fournisseur_tbl_accorderie_NoAccorderie_fk
        foreign key (NoAccorderie) references tbl_accorderie (NoAccorderie),
    constraint tbl_fournisseur_tbl_region_NoRegion_fk
        foreign key (NoRegion) references tbl_region (NoRegion),
    constraint tbl_fournisseur_tbl_ville_NoVille_fk
        foreign key (NoVille) references tbl_ville (NoVille)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_fournisseur_tbl_accorderie1_idx
    on tbl_fournisseur (NoAccorderie);
"""
    cr.execute(sql)
    sql = """
create table tbl_membre
(
    NoMembre             int unsigned auto_increment
        primary key,
    NoCartier            int unsigned default 0                   null,
    NoAccorderie         int unsigned                             not null,
    NoPointService       int unsigned                             null,
    NoPointService2      int unsigned                             null,
    NoTypeCommunication  int unsigned                             null,
    NoOccupation         int unsigned                             null,
    NoOrigine            int unsigned                             null,
    NoSituationMaison    int unsigned                             null,
    NoProvenance         int unsigned                             null,
    NoRevenuFamilial     int unsigned                             null,
    NoArrondissement     int unsigned                             null,
    NoVille              int unsigned                             not null,
    NoRegion             int unsigned                             not null,
    MembreCA             tinyint      default 0                   null,
    PartSocialPaye       tinyint      default 0                   null,
    CodePostal           varchar(7)                               null,
    DateAdhesion         date                                     null,
    Nom                  varchar(45)                              null,
    Prenom               varchar(45)                              null,
    Adresse              varchar(255)                             null,
    Telephone1           varchar(10)                              null,
    PosteTel1            varchar(10)                              null,
    NoTypeTel1           int unsigned                             null,
    Telephone2           varchar(10)                              null,
    PosteTel2            varchar(10)                              null,
    NoTypeTel2           int unsigned                             null,
    Telephone3           varchar(10)                              null,
    PosteTel3            varchar(10)                              null,
    NoTypeTel3           int unsigned                             null,
    Courriel             varchar(255)                             null,
    AchatRegrouper       tinyint(1)                               null,
    PretActif            tinyint(1)                               null,
    PretRadier           tinyint(1)                               null,
    PretPayer            tinyint(1)                               null,
    EtatCompteCourriel   tinyint(1)                               null,
    BottinTel            tinyint(1)                               null,
    BottinCourriel       tinyint(1)                               null,
    MembreActif          tinyint(1)   default -1                  null,
    MembreConjoint       tinyint(1)                               null,
    NoMembreConjoint     int unsigned                             null,
    Memo                 text                                     null,
    Sexe                 tinyint(1)                               null,
    AnneeNaissance       int(4)                                   null,
    PrecisezOrigine      varchar(45)                              null,
    NomUtilisateur       varchar(15)                              null,
    MotDePasse           varchar(15)                              null,
    ProfilApprouver      tinyint(1)   default -1                  null,
    MembrePrinc          tinyint(1)                               null,
    NomAccorderie        varchar(90)                              null,
    RecevoirCourrielGRP  tinyint(1)                               null,
    PasCommunication     tinyint(1)                               null,
    DescriptionAccordeur varchar(255)                             null,
    Date_MAJ_Membre      timestamp    default current_timestamp() null on update current_timestamp(),
    TransfereDe          int unsigned                             null,
    EstUnPointService    tinyint(1)                               null,
    constraint tbl_membre_tbl_accorderie_NoAccorderie_fk
        foreign key (NoAccorderie) references tbl_accorderie (NoAccorderie),
    constraint tbl_membre_tbl_accorderie_NoAccorderie_2_fk
        foreign key (TransfereDe) references tbl_accorderie (NoAccorderie),
    constraint tbl_membre_tbl_type_tel_NoTypeTel_fk
        foreign key (NoTypeTel1) references tbl_type_tel (NoTypeTel),
    constraint tbl_membre_tbl_type_tel_NoTypeTel_2_fk
        foreign key (NoTypeTel2) references tbl_type_tel (NoTypeTel),
    constraint tbl_membre_tbl_type_tel_NoTypeTel_3_fk
        foreign key (NoTypeTel3) references tbl_type_tel (NoTypeTel),
    constraint tbl_membre_tbl_membre_NoMembre_fk
        foreign key (NoMembreConjoint) references tbl_membre (NoMembre),
    constraint tbl_membre_tbl_arrondissement_NoArrondissement_fk
        foreign key (NoArrondissement) references tbl_arrondissement (NoArrondissement),
    constraint tbl_membre_tbl_cartier_NoCartier_fk
        foreign key (NoCartier) references tbl_cartier (NoCartier),
    constraint tbl_membre_tbl_occupation_NoOccupation_fk
        foreign key (NoOccupation) references tbl_occupation (NoOccupation),
    constraint tbl_membre_tbl_origine_NoOrigine_fk
        foreign key (NoOrigine) references tbl_origine (NoOrigine),
    constraint tbl_membre_tbl_provenance_NoProvenance_fk
        foreign key (NoProvenance) references tbl_provenance (NoProvenance),
    constraint tbl_membre_tbl_region_NoRegion_fk
        foreign key (NoRegion) references tbl_region (NoRegion),
    constraint tbl_membre_tbl_revenu_familial_NoRevenuFamilial_fk
        foreign key (NoRevenuFamilial) references tbl_revenu_familial (NoRevenuFamilial),
    constraint tbl_membre_tbl_situation_maison_NoSituationMaison_fk
        foreign key (NoSituationMaison) references tbl_situation_maison (NoSituationMaison),
    constraint tbl_membre_tbl_type_communication_NoTypeCommunication_fk
        foreign key (NoTypeCommunication) references tbl_type_communication (NoTypeCommunication),
    constraint tbl_membre_tbl_ville_NoVille_fk
        foreign key (NoVille) references tbl_ville (NoVille)
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create table tbl_achat_ponctuel
(
    NoAchatPonctuel           int unsigned auto_increment
        primary key,
    NoMembre                  int unsigned                                 not null,
    DateAchatPonctuel         date                                         null,
    MontantPaiementAchatPonct decimal(8, 2)    default 0.00                null,
    AchatPoncFacturer         tinyint unsigned default 0                   null,
    TaxeF_AchatPonct          double unsigned  default 0                   null,
    TaxeP_AchatPonct          double unsigned  default 0                   null,
    Majoration_AchatPonct     double unsigned  default 0                   null,
    DateMAJ_AchantPonct       timestamp        default current_timestamp() null on update current_timestamp(),
    constraint tbl_achat_ponctuel_tbl_membre_NoMembre_fk
        foreign key (NoMembre) references tbl_membre (NoMembre)
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_achat_ponctuel_tbl_membre1_idx
    on tbl_achat_ponctuel (NoMembre);
"""
    cr.execute(sql)
    sql = """
create table tbl_demande_service
(
    NoDemandeService int unsigned auto_increment
        primary key,
    NoMembre         int unsigned                null,
    NoAccorderie     int unsigned                null,
    TitreDemande     varchar(255) charset latin1 null,
    Description      varchar(255) charset latin1 null,
    Approuve         int(1)                      null,
    Supprimer        int(1)                      null,
    Transmit         int(1)                      null,
    DateDebut        date                        null,
    DateFin          date                        null,
    constraint tbl_demande_service_tbl_accorderie_NoAccorderie_fk
        foreign key (NoAccorderie) references tbl_accorderie (NoAccorderie),
    constraint tbl_demande_service_tbl_membre_NoMembre_fk
        foreign key (NoMembre) references tbl_membre (NoMembre)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_demande_service_tbl_accorderie1_idx
    on tbl_demande_service (NoAccorderie);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_demande_service_tbl_membre1_idx
    on tbl_demande_service (NoMembre);
"""
    cr.execute(sql)
    sql = """
create fulltext index tbl_demande_service_index1460
    on tbl_demande_service (TitreDemande, Description);
"""
    cr.execute(sql)
    sql = """
create table tbl_droits_admin
(
    NoMembre            int unsigned default 0 not null
        primary key,
    GestionProfil       int(1)       default 0 null,
    GestionCatSousCat   int(1)       default 0 null,
    GestionOffre        int(1)       default 0 null,
    GestionOffreMembre  int(1)       default 0 null,
    SaisieEchange       int(1)       default 0 null,
    Validation          int(1)       default 0 null,
    GestionDmd          int(1)       default 0 null,
    GroupeAchat         tinyint      default 0 null,
    ConsulterProfil     tinyint      default 0 null,
    ConsulterEtatCompte tinyint      default 0 null,
    GestionFichier      tinyint      default 0 null,
    constraint tbl_droits_admin_tbl_membre_NoMembre_fk
        foreign key (NoMembre) references tbl_membre (NoMembre)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_droits_admin_tbl_membre1_idx
    on tbl_droits_admin (NoMembre);
"""
    cr.execute(sql)
    sql = """
create table tbl_log_acces
(
    Id_log_acces          int unsigned auto_increment
        primary key,
    NoMembre              int unsigned default 0                   null,
    IP_Client_V4          varchar(50)                              null,
    Navigateur            varchar(100)                             null,
    Statut                varchar(45)                              null,
    NomUsagerEssayer      varchar(45)                              null,
    Referer               varchar(255)                             null,
    Resolution_H          int          default 0                   null,
    Resolution_W          int          default 0                   null,
    DateHeure_Deconnexion datetime                                 null,
    DateHeureConnexion    timestamp    default current_timestamp() null,
    constraint tbl_log_acces_tbl_membre_NoMembre_fk
        foreign key (NoMembre) references tbl_membre (NoMembre)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_log_acces_tbl_membre1_idx
    on tbl_log_acces (NoMembre);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_accorderie_idx
    on tbl_membre (NoAccorderie);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_arrondissement1_idx
    on tbl_membre (NoArrondissement);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_cartier1_idx
    on tbl_membre (NoCartier);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_occupation1_idx
    on tbl_membre (NoOccupation);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_origine1_idx
    on tbl_membre (NoOrigine);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_pointservice1_idx
    on tbl_membre (NoPointService);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_pointservice12_idx
    on tbl_membre (NoPointService2);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_provenance1_idx
    on tbl_membre (NoProvenance);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_region1_idx
    on tbl_membre (NoRegion);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_revenu_familial1_idx
    on tbl_membre (NoRevenuFamilial);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_situation_maison1_idx
    on tbl_membre (NoSituationMaison);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_type_communication1_idx
    on tbl_membre (NoTypeCommunication);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_type_tel1_idx
    on tbl_membre (NoTypeTel3);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_type_tel2_idx
    on tbl_membre (NoTypeTel1);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_type_tel3_idx
    on tbl_membre (NoTypeTel2);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_membre_tbl_ville1_idx
    on tbl_membre (NoVille);
"""
    cr.execute(sql)
    sql = """
create fulltext index rch
    on tbl_membre (Nom, Prenom, Telephone1, Telephone2, Telephone3, Courriel, NomUtilisateur, Memo);
"""
    cr.execute(sql)
    sql = """
create table tbl_offre_service_membre
(
    NoOffreServiceMembre       int unsigned auto_increment
        primary key,
    NoMembre                   int unsigned                             null,
    NoAccorderie               int unsigned                             null,
    NoCategorieSousCategorie   int unsigned                             null,
    TitreOffreSpecial          varchar(255)                             null,
    Conditionx                 varchar(255)                             null,
    Disponibilite              varchar(255)                             null,
    Tarif                      varchar(255)                             null,
    Description                varchar(255)                             null,
    DateAffichage              date                                     null,
    DateDebut                  date                                     null,
    DateFin                    date                                     null,
    Approuve                   int(1)                                   null,
    OffreSpecial               int(1)                                   null,
    Supprimer                  int(1)                                   null,
    Fait                       int(1)                                   null,
    ConditionOffre             varchar(255)                             null,
    NbFoisConsulterOffreMembre int unsigned default 0                   null,
    DateMAJ_ServiceMembre      timestamp    default current_timestamp() not null on update current_timestamp(),
    constraint tbl_offre_service_membre_tbl_accorderie_NoAccorderie_fk
        foreign key (NoAccorderie) references tbl_accorderie (NoAccorderie),
    constraint tbl_offre_service_membre_tbl_membre_NoMembre_fk
        foreign key (NoMembre) references tbl_membre (NoMembre),
    constraint tbl_osm_tbl_categorie_sous_categorie_NoCategorieSousCategorie_fk
        foreign key (NoCategorieSousCategorie) references tbl_categorie_sous_categorie (NoCategorieSousCategorie)
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create fulltext index RchFullText_OffreSpe
    on tbl_offre_service_membre (TitreOffreSpecial, Description);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_offre_service_membre_tbl_accorderie1_idx
    on tbl_offre_service_membre (NoAccorderie);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_offre_service_membre_tbl_categorie_sous_categorie1_idx
    on tbl_offre_service_membre (NoCategorieSousCategorie);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_offre_service_membre_tbl_membre1_idx
    on tbl_offre_service_membre (NoMembre);
"""
    cr.execute(sql)
    sql = """
create table tbl_pointservice
(
    NoPointService         int unsigned auto_increment
        primary key,
    NoAccorderie           int unsigned                                 not null,
    NoMembre               int unsigned                                 null,
    NoMembre2              int unsigned                                 null,
    NomPointService        varchar(255) charset latin1                  null,
    OrdrePointService      tinyint unsigned default 0                   null,
    NoteGrpAchatPageClient text                                         null,
    DateMAJ_PointService   timestamp        default current_timestamp() null on update current_timestamp(),
    constraint tbl_pointservice_tbl_accorderie_NoAccorderie_fk
        foreign key (NoAccorderie) references tbl_accorderie (NoAccorderie),
    constraint tbl_pointservice_tbl_membre_NoMembre_fk
        foreign key (NoMembre) references tbl_membre (NoMembre),
    constraint tbl_pointservice2_tbl_membre_NoMembre_fk
        foreign key (NoMembre2) references tbl_membre (NoMembre)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create table tbl_commande
(
    NoCommande      int unsigned auto_increment
        primary key,
    NoPointService  int unsigned                                 not null,
    NoRefCommande   int unsigned     default 0                   null,
    DateCmdDebut    date                                         null,
    DateCmdFin      date                                         null,
    DateCueillette  date                                         null,
    TaxePCommande   double unsigned  default 0                   null,
    TaxeFCommande   double unsigned  default 0                   null,
    Majoration      double unsigned  default 0                   null,
    CommandeTermine tinyint unsigned default 0                   null,
    DateMAJ_Cmd     timestamp        default current_timestamp() null on update current_timestamp(),
    constraint tbl_commande_tbl_pointservice_NoPointService_fk
        foreign key (NoPointService) references tbl_pointservice (NoPointService)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_commande_tbl_pointservice1_idx
    on tbl_commande (NoPointService);
"""
    cr.execute(sql)
    sql = """
create table tbl_commande_membre
(
    NoCommandeMembre     int unsigned auto_increment
        primary key,
    NoCommande           int unsigned                                 not null,
    NoMembre             int unsigned                                 null,
    NumRefMembre         int unsigned     default 0                   null,
    CmdConfirmer         tinyint unsigned default 0                   null,
    Facturer             tinyint unsigned default 0                   null,
    MontantPaiement      decimal(10, 2)   default 0.00                null,
    CoutUnitaireAJour    tinyint unsigned default 0                   null,
    DateCmdMb            datetime                                     null,
    DateFacture          date                                         null,
    ArchiveSousTotal     decimal(10, 2)   default 0.00                null,
    ArchiveTotMajoration decimal(10, 2)   default 0.00                null,
    ArchiveTotTxFed      decimal(10, 2)   default 0.00                null,
    ArchiveTotTxProv     decimal(10, 2)   default 0.00                null,
    DateMAJ_CmdMembre    timestamp        default current_timestamp() null on update current_timestamp(),
    constraint tbl_commande_membre_tbl_commande_NoCommande_fk
        foreign key (NoCommande) references tbl_commande (NoCommande),
    constraint tbl_commande_membre_tbl_membre_NoMembre_fk
        foreign key (NoMembre) references tbl_membre (NoMembre)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_commande_membre_tbl_commande1_idx
    on tbl_commande_membre (NoCommande);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_commande_membre_tbl_membre1_idx
    on tbl_commande_membre (NoMembre);
"""
    cr.execute(sql)
    sql = """
create table tbl_commentaire
(
    NoCommentaire              int unsigned auto_increment
        primary key,
    NoPointService             int unsigned                                 not null,
    NoMembreSource             int unsigned                                 not null,
    NoMembreViser              int unsigned                                 null,
    NoOffreServiceMembre       int unsigned                                 null,
    NoDemandeService           int unsigned                                 null,
    DateHeureAjout             datetime                                     null,
    Situation_Impliquant       tinyint unsigned                             null,
    NomEmployer                varchar(50)                                  null,
    NomComite                  varchar(50)                                  null,
    AutreSituation             varchar(81)                                  null,
    SatisfactionInsatisfaction tinyint unsigned                             null,
    DateIncident               date                                         null,
    TypeOffre                  tinyint unsigned                             null,
    ResumerSituation           text                                         null,
    Demarche                   text                                         null,
    SolutionPourRegler         text                                         null,
    AutreCommentaire           text                                         null,
    SiConfidentiel             tinyint unsigned                             null,
    NoteAdministrative         text                                         null,
    ConsulterAccorderie        tinyint unsigned default 0                   null,
    ConsulterReseau            tinyint unsigned default 0                   null,
    DateMaj_Commentaire        timestamp        default current_timestamp() null on update current_timestamp(),
    constraint tbl_commentaire_tbl_demande_service_NoDemandeService_fk
        foreign key (NoDemandeService) references tbl_demande_service (NoDemandeService),
    constraint tbl_commentaire_tbl_membre_NoMembre_fk
        foreign key (NoMembreSource) references tbl_membre (NoMembre),
    constraint tbl_commentaire_tbl_membre_NoMembre_fk_2
        foreign key (NoMembreViser) references tbl_membre (NoMembre),
    constraint tbl_commentaire_tbl_offre_service_membre_NoOffreServiceMembre_fk
        foreign key (NoOffreServiceMembre) references tbl_offre_service_membre (NoOffreServiceMembre),
    constraint tbl_commentaire_tbl_pointservice_NoPointService_fk
        foreign key (NoPointService) references tbl_pointservice (NoPointService)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_commentaire_tbl_demande_service1_idx
    on tbl_commentaire (NoDemandeService);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_commentaire_tbl_offre_service_membre1_idx
    on tbl_commentaire (NoOffreServiceMembre);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_commentaire_tbl_pointservice1_idx
    on tbl_commentaire (NoPointService);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_commentaire_tbl_pointservice2_idx
    on tbl_commentaire (NoMembreSource);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_commentaire_tbl_pointservice3_idx
    on tbl_commentaire (NoMembreViser);
"""
    cr.execute(sql)
    sql = """
create table tbl_echange_service
(
    NoEchangeService     int unsigned auto_increment
        primary key,
    NoPointService       int unsigned    null,
    NoMembreVendeur      int unsigned    null,
    NoMembreAcheteur     int unsigned    null,
    NoDemandeService     int unsigned    null,
    NoOffreServiceMembre int unsigned    null,
    NbHeure              float           null,
    DateEchange          date            null,
    TypeEchange          int(1) unsigned null,
    Remarque             varchar(100)    null,
    Commentaire          varchar(255)    null,
    constraint tbl_echange_service_acheteur_tbl_membre_NoMembre_fk
        foreign key (NoMembreAcheteur) references tbl_membre (NoMembre),
    constraint tbl_echange_service_tbl_demande_service_NoDemandeService_fk
        foreign key (NoDemandeService) references tbl_demande_service (NoDemandeService),
    constraint tbl_echange_service_tbl_pointservice_NoPointService_fk
        foreign key (NoPointService) references tbl_pointservice (NoPointService),
    constraint tbl_echange_service_vendeur_tbl_membre_NoMembre_fk
        foreign key (NoMembreVendeur) references tbl_membre (NoMembre),
    constraint tbl_es_tbl_offre_service_membre_NoOffreServiceMembre_fk
        foreign key (NoOffreServiceMembre) references tbl_offre_service_membre (NoOffreServiceMembre)
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create index Index_Teste
    on tbl_echange_service (NoEchangeService, NoMembreVendeur, NoMembreAcheteur, TypeEchange);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_echange_service_tbl_demande_service1_idx
    on tbl_echange_service (NoDemandeService);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_echange_service_tbl_membre1_idx
    on tbl_echange_service (NoMembreVendeur);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_echange_service_tbl_membre2_idx
    on tbl_echange_service (NoMembreAcheteur);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_echange_service_tbl_offre_service_membre1_idx
    on tbl_echange_service (NoOffreServiceMembre);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_echange_service_tbl_pointservice1_idx
    on tbl_echange_service (NoPointService);
"""
    cr.execute(sql)
    sql = """
alter table tbl_membre
    add constraint tbl_membre_tbl_pointservice_NoPointService_fk
        foreign key (NoPointService) references tbl_pointservice (NoPointService);
"""
    cr.execute(sql)
    sql = """
alter table tbl_membre
    add constraint tbl_membre_tbl_pointservice2_NoPointService_fk
        foreign key (NoPointService2) references tbl_pointservice (NoPointService);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_pointservice_tbl_accorderie1_idx
    on tbl_pointservice (NoAccorderie);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_pointservice_tbl_membre1_idx
    on tbl_pointservice (NoMembre);
"""
    cr.execute(sql)
    sql = """
create table tbl_pointservice_fournisseur
(
    NoPointServiceFournisseur       int unsigned auto_increment
        primary key,
    NoPointService                  int unsigned                          not null,
    NoFournisseur                   int unsigned                          not null,
    DateMAJ_PointServiceFournisseur timestamp default current_timestamp() null on update current_timestamp(),
    constraint tbl_pointservice_fournisseur_tbl_fournisseur_NoFournisseur_fk
        foreign key (NoFournisseur) references tbl_fournisseur (NoFournisseur),
    constraint tbl_pointservice_fournisseur_tbl_pointservice_NoPointService_fk
        foreign key (NoPointService) references tbl_pointservice (NoPointService)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_pointservice_fournisseur_tbl_fournisseur1_idx
    on tbl_pointservice_fournisseur (NoFournisseur);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_pointservice_fournisseur_tbl_pointservice1_idx
    on tbl_pointservice_fournisseur (NoPointService);
"""
    cr.execute(sql)
    sql = """
create table tbl_pret
(
    Id_Pret                int unsigned auto_increment
        primary key,
    NoMembre               int unsigned                          not null,
    NoMembre_Intermediaire int unsigned                          null,
    NoMembre_Responsable   int unsigned                          not null,
    DateDemandePret        datetime                              null,
    MontantDemande         decimal(8, 2) unsigned                null,
    RaisonEmprunt          text                                  null,
    DateComitePret         datetime                              null,
    Si_PretAccorder        tinyint unsigned                      null,
    MontantAccorder        decimal(8, 2) unsigned                null,
    Note                   text                                  null,
    Recommandation         text                                  null,
    TautInteretAnnuel      decimal(2, 2) unsigned                null,
    DatePret               datetime                              null,
    NbreMois               int unsigned                          null,
    NbrePaiement           int unsigned                          null,
    DateMAJ_Pret           timestamp default current_timestamp() null on update current_timestamp(),
    constraint tbl_pret_tbl_membre_NoMembre_fk
        foreign key (NoMembre) references tbl_membre (NoMembre),
    constraint tbl_pret_tbl_membre_NoMembre_fk_2
        foreign key (NoMembre_Intermediaire) references tbl_membre (NoMembre)
            on update set null on delete set null,
    constraint tbl_pret_tbl_membre_NoMembre_fk_3
        foreign key (NoMembre_Responsable) references tbl_membre (NoMembre)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create table tbl_mensualite
(
    Id_Mensualite int unsigned auto_increment
        primary key,
    Id_Pret       int unsigned not null,
    constraint tbl_mensualite_tbl_pret_Id_Pret_fk
        foreign key (Id_Pret) references tbl_pret (Id_Pret)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_mensualite_tbl_Pret1_idx
    on tbl_mensualite (Id_Pret);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_pret_tbl_membre1_idx
    on tbl_pret (NoMembre);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_pret_tbl_membre2_idx
    on tbl_pret (NoMembre_Intermediaire);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_pret_tbl_membre3_idx
    on tbl_pret (NoMembre_Responsable);
"""
    cr.execute(sql)
    sql = """
create table tbl_produit
(
    NoProduit       int unsigned auto_increment
        primary key,
    NoTitre         int unsigned                                    not null,
    NoAccorderie    int unsigned                                    not null,
    NomProduit      varchar(80) charset latin1                      null,
    TaxableF        tinyint(1) unsigned default 0                   null,
    TaxableP        tinyint(1) unsigned default 0                   null,
    Visible_Produit tinyint(1) unsigned default 0                   null,
    DateMAJ_Produit timestamp           default current_timestamp() null on update current_timestamp(),
    constraint tbl_produit_tbl_accorderie_NoAccorderie_fk
        foreign key (NoAccorderie) references tbl_accorderie (NoAccorderie),
    constraint tbl_produit_tbl_titre_NoTitre_fk
        foreign key (NoTitre) references tbl_titre (NoTitre)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create table tbl_fournisseur_produit
(
    NoFournisseurProduit       int unsigned auto_increment
        primary key,
    NoFournisseur              int unsigned                                       null,
    NoProduit                  int unsigned                                       not null,
    CodeProduit                varchar(25)                                        null,
    zQteStokeAcc               int unsigned           default 0                   null,
    zCoutUnitaire              decimal(5, 2) unsigned default 0.00                null,
    Visible_FournisseurProduit tinyint                default 1                   null,
    DateMAJ_FournProduit       timestamp              default current_timestamp() null on update current_timestamp(),
    constraint UniqueFournisseurProduit
        unique (NoFournisseur, NoProduit),
    constraint tbl_fournisseur_produit_tbl_fournisseur_NoFournisseur_fk
        foreign key (NoFournisseur) references tbl_fournisseur (NoFournisseur),
    constraint tbl_fournisseur_produit_tbl_produit_NoProduit_fk
        foreign key (NoProduit) references tbl_produit (NoProduit)
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create table tbl_achat_ponctuel_produit
(
    NoAchatPonctuelProduit      int unsigned auto_increment
        primary key,
    NoAchatPonctuel             int unsigned                                not null,
    NoFournisseurProduit        int unsigned                                not null,
    QteAcheter                  double unsigned default 0                   null,
    CoutUnit_AchatPonctProd     decimal(8, 2)   default 0.00                null,
    SiTaxableF_AchatPonctProd   tinyint         default 0                   null,
    SiTaxableP_AchatPonctProd   tinyint         default 0                   null,
    PrixFacturer_AchatPonctProd decimal(8, 2)   default 0.00                null,
    DateMAJ_AchatPoncProduit    timestamp       default current_timestamp() null on update current_timestamp(),
    constraint UniqueAchatPoncProduit
        unique (NoAchatPonctuel, NoFournisseurProduit),
    constraint tbl_achat_ponctuel_produit_tbl_achat_ponctuel_NoAchatPonctuel_fk
        foreign key (NoAchatPonctuel) references tbl_achat_ponctuel (NoAchatPonctuel),
    constraint tbl_achat_pp_tbl_fournisseur_produit_NoFournisseurProduit_fk
        foreign key (NoFournisseurProduit) references tbl_fournisseur_produit (NoFournisseurProduit)
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_achat_ponctuel_produit_tbl_achat_ponctuel1_idx
    on tbl_achat_ponctuel_produit (NoAchatPonctuel);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_achat_ponctuel_produit_tbl_fournisseur_produit1_idx
    on tbl_achat_ponctuel_produit (NoFournisseurProduit);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_fournisseur_produit_tbl_fournisseur1_idx
    on tbl_fournisseur_produit (NoFournisseur);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_fournisseur_produit_tbl_produit1_idx
    on tbl_fournisseur_produit (NoProduit);
"""
    cr.execute(sql)
    sql = """
create table tbl_fournisseur_produit_commande
(
    NoFournisseurProduitCommande int unsigned auto_increment
        primary key,
    NoCommande                   int unsigned                                 not null,
    NoFournisseurProduit         int unsigned                                 not null,
    NbBoiteMinFournisseur        tinyint unsigned default 0                   null,
    QteParBoitePrevu             double unsigned  default 0                   null,
    CoutUnitPrevu                decimal(7, 2)    default 0.00                null,
    Disponible                   tinyint unsigned default 1                   null,
    DateMAJ_FournProdCommande    timestamp        default current_timestamp() null on update current_timestamp(),
    constraint Unique_Produit
        unique (NoCommande, NoFournisseurProduit),
    constraint tbl_fournisseur_produit_commande_tbl_commande_NoCommande_fk
        foreign key (NoCommande) references tbl_commande (NoCommande),
    constraint tbl_fpc_tbl_fournisseur_produit_NoFournisseurProduit_fk
        foreign key (NoFournisseurProduit) references tbl_fournisseur_produit (NoFournisseurProduit)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create table tbl_commande_membre_produit
(
    NoCmdMbProduit               int unsigned auto_increment
        primary key,
    NoCommandeMembre             int unsigned                              not null,
    NoFournisseurProduitCommande int unsigned                              not null,
    Qte                          double        default 0                   null,
    QteDePlus                    double        default 0                   null,
    Ajustement                   double        default 0                   null,
    CoutUnitaire_Facture         decimal(5, 2) default 0.00                null,
    SiTaxableP_Facture           tinyint       default 0                   null,
    SiTaxableF_Facture           tinyint       default 0                   null,
    PrixFacturer_Manuel          decimal(5, 2) default 0.00                null,
    DateMAJ_CmdMembreProd        timestamp     default current_timestamp() null on update current_timestamp(),
    constraint tbl_cmp_tbl_commande_membre_NoCommandeMembre_fk
        foreign key (NoCommandeMembre) references tbl_commande_membre (NoCommandeMembre),
    constraint tbl_cmp_tbl_fpc_NoFournisseurProduitCommande_fk
        foreign key (NoFournisseurProduitCommande) references tbl_fournisseur_produit_commande (NoFournisseurProduitCommande)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_commande_membre_produit_tbl_commande_membre1_idx
    on tbl_commande_membre_produit (NoCommandeMembre);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_commande_membre_produit_tbl_fournisseur_produit_comm_idx
    on tbl_commande_membre_produit (NoFournisseurProduitCommande);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_fournisseur_produit_commande_tbl_commande1_idx
    on tbl_fournisseur_produit_commande (NoCommande);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_fournisseur_produit_commande_tbl_fournisseur_produit_idx
    on tbl_fournisseur_produit_commande (NoFournisseurProduit);
"""
    cr.execute(sql)
    sql = """
create table tbl_fournisseur_produit_pointservice
(
    NoFournisseurProduitPointservice int unsigned auto_increment
        primary key,
    NoFournisseurProduit             int unsigned                              not null,
    NoPointService                   int unsigned                              not null,
    QteStokeAcc                      int           default 0                   null,
    CoutUnitaire                     decimal(5, 2) default 0.00                null,
    DateMAJ_FournProdPtServ          timestamp     default current_timestamp() null on update current_timestamp(),
    constraint UniqueProduitFournPointService
        unique (NoFournisseurProduit, NoPointService),
    constraint tbl_fpps_tbl_fournisseur_produit_NoFournisseurProduit_fk
        foreign key (NoFournisseurProduit) references tbl_fournisseur_produit (NoFournisseurProduit),
    constraint tbl_fpps_tbl_pointservice_NoPointService_fk
        foreign key (NoPointService) references tbl_pointservice (NoPointService)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_fournisseur_produit_pointservice_tbl_fournisseur_pro_idx
    on tbl_fournisseur_produit_pointservice (NoFournisseurProduit);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_fournisseur_produit_pointservice_tbl_pointservice1_idx
    on tbl_fournisseur_produit_pointservice (NoPointService);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_produit_tbl_accorderie1_idx
    on tbl_produit (NoAccorderie);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_produit_tbl_titre1_idx
    on tbl_produit (NoTitre);
"""
    cr.execute(sql)
    sql = """
create table tbl_type_compte
(
    NoMembre             int unsigned default 0 not null
        primary key,
    AccodeurSimple       int(1)                 null,
    Admin                int(1)                 null,
    AdminChef            int(1)                 null,
    Reseau               int(1)                 null,
    SPIP                 int unsigned default 0 null,
    AdminPointService    int(1)       default 0 null,
    AdminOrdPointService int(1)                 null,
    constraint tbl_type_compte_tbl_membre_NoMembre_fk
        foreign key (NoMembre) references tbl_membre (NoMembre)
)
    charset = latin1;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_type_compte_tbl_membre1_idx
    on tbl_type_compte (NoMembre);
"""
    cr.execute(sql)
    sql = """
create table tbl_versement
(
    Id_Versement      int unsigned auto_increment
        primary key,
    Id_Mensualite     int unsigned                          not null,
    MontantVersement  decimal(8, 2) unsigned                null,
    DateMAJ_Versement timestamp default current_timestamp() null on update current_timestamp(),
    constraint tbl_versement_tbl_mensualite_Id_Mensualite_fk
        foreign key (Id_Mensualite) references tbl_mensualite (Id_Mensualite)
)
    collate = latin1_general_ci;
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_versement_tbl_mensualite1_idx
    on tbl_versement (Id_Mensualite);
"""
    cr.execute(sql)
    sql = """
create index fk_tbl_ville_tbl_region1_idx
    on tbl_ville (NoRegion);
    """
    cr.execute(sql)


if __name__ == "__main__":
    main()

from odoo import _, api, fields, models


class OffreServiceMembre(models.Model):
    _name = "offre.service.membre"
    _description = "Model Offre_service_membre belonging to Module Tbl"

    approuve = fields.Integer(string="Field Approuve")

    conditionoffre = fields.Char(string="Field Conditionoffre")

    conditionx = fields.Char(string="Field Conditionx")

    dateaffichage = fields.Date(string="Field Dateaffichage")

    datedebut = fields.Date(string="Field Datedebut")

    datefin = fields.Date(string="Field Datefin")

    datemaj_servicemembre = fields.Datetime(
        string="Field Datemaj_servicemembre",
        required=True,
    )

    description = fields.Char(string="Field Description")

    disponibilite = fields.Char(string="Field Disponibilite")

    fait = fields.Integer(string="Field Fait")

    name = fields.Char(string="Field Name")

    nbfoisconsulteroffremembre = fields.Integer(
        string="Field Nbfoisconsulteroffremembre"
    )

    noaccorderie = fields.Integer(string="Field Noaccorderie")

    nocategoriesouscategorie = fields.Integer(
        string="Field Nocategoriesouscategorie"
    )

    nomembre = fields.Integer(string="Field Nomembre")

    nooffreservicemembre = fields.Integer(
        string="Field Nooffreservicemembre",
        required=True,
    )

    offrespecial = fields.Integer(string="Field Offrespecial")

    supprimer = fields.Integer(string="Field Supprimer")

    tarif = fields.Char(string="Field Tarif")

    titreoffrespecial = fields.Char(string="Field Titreoffrespecial")

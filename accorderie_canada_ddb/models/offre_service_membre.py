from odoo import _, api, models, fields


class OffreServiceMembre(models.Model):
    _name = "offre.service.membre"
    _description = "Model Offre_service_membre belonging to Module Tbl"

    approuve = fields.Integer()

    conditionoffre = fields.Char()

    conditionx = fields.Char()

    dateaffichage = fields.Date()

    datedebut = fields.Date()

    datefin = fields.Date()

    datemaj_servicemembre = fields.Datetime(
        string="Datemaj servicemembre",
        required=True,
    )

    description = fields.Char()

    disponibilite = fields.Char()

    fait = fields.Integer()

    name = fields.Char()

    nbfoisconsulteroffremembre = fields.Integer()

    noaccorderie = fields.Many2one(comodel_name="accorderie")

    nocategoriesouscategorie = fields.Many2one(
        comodel_name="categorie.sous.categorie"
    )

    nomembre = fields.Many2one(comodel_name="membre")

    offrespecial = fields.Integer()

    supprimer = fields.Integer()

    tarif = fields.Char()

    titreoffrespecial = fields.Char()

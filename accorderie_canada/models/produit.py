from odoo import _, api, fields, models


class Produit(models.Model):
    _name = "produit"
    _description = "Model Produit belonging to Module Tbl"

    datemaj_produit = fields.Datetime(string="Field Datemaj_produit")

    name = fields.Char(string="Field Name")

    noaccorderie = fields.Integer(
        string="Field Noaccorderie",
        required=True,
    )

    nomproduit = fields.Char(string="Field Nomproduit")

    noproduit = fields.Integer(
        string="Field Noproduit",
        required=True,
    )

    notitre = fields.Integer(
        string="Field Notitre",
        required=True,
    )

    taxablef = fields.Integer(string="Field Taxablef")

    taxablep = fields.Integer(string="Field Taxablep")

    visible_produit = fields.Integer(string="Field Visible_produit")

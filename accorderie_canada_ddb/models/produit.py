from odoo import _, api, models, fields


class Produit(models.Model):
    _name = "produit"
    _description = "Model Produit belonging to Module Tbl"

    datemaj_produit = fields.Datetime(string="Datemaj produit")

    name = fields.Char()

    noaccorderie = fields.Integer(required=True)

    nomproduit = fields.Char()

    noproduit = fields.Integer(required=True)

    notitre = fields.Integer(required=True)

    taxablef = fields.Integer()

    taxablep = fields.Integer()

    visible_produit = fields.Integer(string="Visible produit")

from odoo import _, api, fields, models


class Pret(models.Model):
    _name = "pret"
    _description = "Model Pret belonging to Module Tbl"

    datecomitepret = fields.Datetime(string="Field Datecomitepret")

    datedemandepret = fields.Datetime(string="Field Datedemandepret")

    datemaj_pret = fields.Datetime(string="Field Datemaj_pret")

    datepret = fields.Datetime(string="Field Datepret")

    id_pret = fields.Integer(
        string="Field Id_pret",
        required=True,
    )

    montantaccorder = fields.Float(string="Field Montantaccorder")

    montantdemande = fields.Float(string="Field Montantdemande")

    name = fields.Char(string="Field Name")

    nbremois = fields.Integer(string="Field Nbremois")

    nbrepaiement = fields.Integer(string="Field Nbrepaiement")

    nomembre = fields.Integer(
        string="Field Nomembre",
        required=True,
    )

    nomembre_intermediaire = fields.Integer(
        string="Field Nomembre_intermediaire"
    )

    nomembre_responsable = fields.Integer(
        string="Field Nomembre_responsable",
        required=True,
    )

    note = fields.Text(string="Field Note")

    raisonemprunt = fields.Text(string="Field Raisonemprunt")

    recommandation = fields.Text(string="Field Recommandation")

    si_pretaccorder = fields.Integer(string="Field Si_pretaccorder")

    tautinteretannuel = fields.Float(string="Field Tautinteretannuel")

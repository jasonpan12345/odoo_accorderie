from odoo import _, api, models, fields


class Pret(models.Model):
    _name = "pret"
    _description = "Model Pret belonging to Module Tbl"

    datecomitepret = fields.Datetime()

    datedemandepret = fields.Datetime()

    datemaj_pret = fields.Datetime(string="Datemaj pret")

    datepret = fields.Datetime()

    id_pret = fields.Integer(
        string="Id pret",
        required=True,
    )

    montantaccorder = fields.Float()

    montantdemande = fields.Float()

    name = fields.Char()

    nbremois = fields.Integer()

    nbrepaiement = fields.Integer()

    nomembre = fields.Integer(required=True)

    nomembre_intermediaire = fields.Integer(string="Nomembre intermediaire")

    nomembre_responsable = fields.Integer(
        string="Nomembre responsable",
        required=True,
    )

    note = fields.Text()

    raisonemprunt = fields.Text()

    recommandation = fields.Text()

    si_pretaccorder = fields.Integer(string="Si pretaccorder")

    tautinteretannuel = fields.Float()

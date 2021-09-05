from odoo import _, api, models, fields


class AccorderieFichier(models.Model):
    _name = "accorderie.fichier"
    _description = "Accorderie Fichier"

    datemaj_fichier = fields.Datetime(string="Datemaj fichier")

    id_typefichier = fields.Many2one(
        string="Id typefichier",
        comodel_name="accorderie.type.fichier",
        required=True,
    )

    name = fields.Char()

    noaccorderie = fields.Many2one(
        comodel_name="accorderie.accorderie",
        required=True,
    )

    nomfichieroriginal = fields.Char(required=True)

    nomfichierstokage = fields.Char(required=True)

    si_accorderielocalseulement = fields.Integer(
        string="Si accorderielocalseulement"
    )

    si_admin = fields.Integer(string="Si admin")

    si_disponible = fields.Integer(string="Si disponible")

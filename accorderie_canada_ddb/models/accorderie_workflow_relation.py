from odoo import _, api, fields, models


class AccorderieWorkflowRelation(models.Model):
    _name = "accorderie.workflow.relation"
    _description = "Accorderie Workflow Relation"

    name = fields.Char(string="Nom")

    body_html = fields.Html(string="HTML")

    diagram_id = fields.Many2one(
        comodel_name="accorderie.workflow",
        string="Diagram",
    )

    icon = fields.Char(string="icon")

    state_dst = fields.Many2one(
        comodel_name="accorderie.workflow.state",
        string="State destination",
    )

    state_src = fields.Many2one(
        comodel_name="accorderie.workflow.state",
        string="State source",
    )

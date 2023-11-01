# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    production_id = fields.Many2one(
        "mrp.production",
        compute="_compute_production_id",
        string="Production Order",
        store=True,
    )

    @api.depends("procurement_group_id")
    def _compute_production_id(self):
        for line in self:
            line.production_id = False
            group = line.procurement_group_id
            if not group:
                continue
            move = self.env["stock.move"].search(
                [("group_id", "=", group.id), ("production_id", "!=", False)],
                order="id",
                limit=1,
            )
            if move:
                line.production_id = move.production_id

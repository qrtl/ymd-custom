# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models


class MrpProduction(models.Model):
    _inherit = "mrp.production"
    _rec_names_search = ["name", "product_id"]

    def name_get(self):
        res = []
        for production in self:
            name = "{} ({})".format(production.name, production.product_id.name)
            res.append((production.id, name))
        return res

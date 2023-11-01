# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models


class MrpProduction(models.Model):
    _inherit = "mrp.production"
    _rec_names_search = ["name", "product_id"]

    def name_get(self):
        res = super().name_get()
        for production in self:
            name = ""
            for i, (k, v) in enumerate(res):
                if k == production.id:
                    name = v
                    del res[i]
                    break
            if name != production.name:
                name += " " + production.name
            name = "{} ({})".format(name, production.product_id.name)
            res.append((production.id, name))
        return res

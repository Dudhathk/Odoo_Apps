from odoo import fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def get_vehicles(self):
        self.ensure_one()
        view_id = self.env.ref('purchase.purchase_order_form').id
        # self.env('purchase.order').status_create_po = True
        self._context.status_create_po = True
        # print("\n\n Hello this is from  other library\n\n")
        return {
            'name': _('New PO'),
            'view_mode': 'form',
            'res_model': 'purchase.order',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'new',
            'status_create_po': True,
            'context': {'status_create_po': True}
        }


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    status_create_po = fields.Boolean('PO Status', readonly=True)

    def create_so_here(self):
        self.ensure_one()
        view_id = self.env.ref('sale.view_order_form').id
        # self.env('purchase.order').status_create_po = True
        # print("\n\n Hello this is from  other library\n\n")
        return {
            'name': _('New SO'),
            'view_mode': 'form',
            'res_model': 'sale.order',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
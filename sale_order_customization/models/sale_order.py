from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_price = fields.Float(string="Total Price", store=True)

    delivery_charge = fields.Float(string='Delievery charge', copy=False, compute='_compute_delivery_charge',
                                       store=True)

    @api.depends('amount_total')
    def _compute_delivery_charge(self):
        for order in self:
            delivery_charge= order.amount_total * 0.10
            print("delivery_charge",delivery_charge)
            self.delivery_charge= delivery_charge

    @api.depends('order_line.price_total', 'delivery_charge')
    def _amount_all(self):
        res = super(SaleOrder, self)._amount_all()
        print(res)
        for i in self:
            i.amount_total += i.delivery_charge
        return res

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['delivery_charge'] = self.delivery_charge
        return invoice_vals



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    brand = fields.Char(string='Brand', readonly=True)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.brand = self.product_id.product_tmpl_id.brand
            if self.price_unit < self.product_id.product_tmpl_id.minimum_cost:
                raise ValidationError('Unit Price Must be greater than minimum cost of product')






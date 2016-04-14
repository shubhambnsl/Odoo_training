# Electricals application
from openerp import models, fields, api

#extend product.template model with supplier name

class electricals_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    supplier_name = fields.Char("Supplier Name")
    servingsize = fields.Float("Serving Size")
    lastupdated = fields.Date("Last Updated")
    is_extension=fields.Boolean("Extensions")

class electricals2_res_users_meal(models.Model):
    _name = "res.users.meal"
    name = fields.Char("Meal Name")
    meal_date = fields.Datetime("Meal Date")
    item_ids = fields.One2many('res.users.mealitems','meal_id')        #link with mealitems model
    user_id = fields.Many2one("res.users", "Meal User")

    @api.one
    @api.depends('item_ids.servings')

    def _calcservingsize(self):
        currentservingsize = 0
        for mealitem in self.item_ids:
            currentservingsize = currentservingsize + mealitem.item_id.servingsize
        self.totalservingsize = currentservingsize

    totalservingsize = fields.Integer(string= "Total Serving Size", store=True,compute="_calcservingsize")
    notes = fields.Text("Notes")

class electricals2_res_users_mealitems(models.Model):
    _name = "res.users.mealitems"
    meal_id = fields.Many2one('res.users.meal')
    item_id = fields.Many2one('product.template','Meal items')
    servings = fields.Float('Servings')
    supplier_name = fields.Char(related = "item_id.supplier_name", string = "Supplier Name per item", store = True, readonly=True)
    notes = fields.Text('Meal Items Notes')

class electricals_res_partner(models.Model):

    _name = 'res.partner'
    _inherit = 'res.partner'

    Date_Of_Birth = fields.Date("Date_Of_Birth")


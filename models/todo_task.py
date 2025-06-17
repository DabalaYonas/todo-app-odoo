from odoo import models, fields, api

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-Do Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], string='Priority', default='medium')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)
    due_date = fields.Date(string='Due Date')
    category_id = fields.Many2one('todo.category', string='Category')
    assigned_user_id = fields.Many2one('res.users', string='Assigned To', default=lambda self: self.env.user)
    progress = fields.Integer(
        string='Progress (%)', 
        default=0, 
        group_operator='avg',
        compute='_compute_progress',
        store=True)

    @api.depends('state')
    def _compute_progress(self):
        for task in self:
            if task.state == 'done':
                task.progress = 100
            elif task.state == 'in_progress':
                task.progress = 50
            else:
                task.progress = 0

    def action_set_in_progress(self):
        self.ensure_one()
        self.write({'state': 'in_progress'})

    def action_set_done(self):
        self.ensure_one()
        self.write({'state': 'done'})

    def action_set_cancelled(self):
        self.ensure_one()
        self.write({'state': 'cancelled'})

class TodoCategory(models.Model):
    _name = 'todo.category'
    _description = 'To-Do Task Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')
# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class Pisos (models.Model):
    _name = "inmo.pisos"
    _description = "Pisos"
    
    direccion = fields.Char("Direccion", required=True)
    precio = fields.Float("Precio", required = True)
    estado = fields.Selection(
        [('disponible','Disponible'),
        ('alquilado','Alquilado'),
        ('vendido','Vendido'),
        ('no disponible','No Disponible')],
        'State', default="disponible")
    descripcion = fields.Char("Descripcion")
    img_piso = fields.Binary("Foto Piso")

class Alquiler (models.Model):
    _name = "inmo.alquiler"
    _descripcion = "Alquiler"
    _order = "date_end desc"

    direccion = fields.Char("Direccion", required=True)
    date_start = fields.Date('Inicio Alquiler', default=lambda *a: (datetime.now().strftime('%Y-%m-%d')))
    date_end = fields.Date('Fin Alquiler', default = lambda *a: (datetime.now() + timedelta(days=(6))).strftime('%Y-%m-%d'))

    @api.constrains('date_end', 'date_start')
    def _check_dates(self):
        for loan in self:
            if loan.date_start > loan.date_end:
                raise models.ValidationError('Start date After end Date!')

class Clientes (models.Model):
    _name = "inmo.clientes"
    _description = "Clientes"
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    member_number = fields.Char()
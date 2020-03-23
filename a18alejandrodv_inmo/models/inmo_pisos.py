# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
from _datetime import timedelta

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
    _descripcion = 'Alquiler'
    _order = "fecha_fin desc"

    fecha_inicio = fields.Date("Inicio Alquiler", default= lambda *a: (datetime.now().strftime('%Y-%m-%d')))
    fecha_fin = fields.Date("Inicio Alquiler", default= lambda *a: (datetime.now() +timedelta(days=(365))).strftime('%Y-%m-%d'))


    @api.constrains('fecha_fin', 'fecha_inicio')
    def _check_dates(self):
        for loan in self:
            if loan.fecha_inicio > loan.fecha_fin:
                raise models.ValidationError('Start date After end Date!')
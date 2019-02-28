# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError

class empleado(models.Model):
    _name = 'paintball.empleado'

    name = fields.Char(string = "DNI", required = True)
    nombre = fields.Char(string="Nombre", required = True)
    apellidos = fields.Char(string="Apellidos", required=True)
    sueldo = fields.Integer(string="Sueldo", required=True)
    telefono = fields.Integer(string="Telefono de contacto")

    @api.onchange('name')
    def validate_dni(self):
        if self.name:
            match = re.match('[1-9]{8}[BCDFGHJKLMNPQRSTVXYZ]{1}$', self.name)
            if match == None:
                raise ValidationError('No es un DNI valido')

class material(models.Model):
    _name = 'paintball.material'

    name = fields.Char(string = "IDENTIFICADOR", required = True)
    nombre = fields.Char(string="Nombre", required = True)
    categoria = fields.Selection([('0', 'Arma'), ('1', 'Casco'), ('2', 'Mono'), ('3', 'Mascara'), ('4', 'Bolas')], string="Categoria", default = "0")
    cantidad = fields.Integer(string="cantidad", required=True)

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

class campo(models.Model):
    _name = 'paintball.campo'

    name = fields.Char(string = "IDENTIFICADOR", required = True)
    nombre = fields.Char(string="Nombre", required = True)
    metros = fields.Integer(string="Metros2", required = True)
    descripcion = fields.Char(string="descripcion", required = True)
    encargado = fields.Many2one ("paintball.empleado", string="Encargado")

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

class campeonato(models.Model):
    _name = 'paintball.campeonato'

    name = fields.Char(string = "IDENTIFICADOR", required = True)
    año = fields.Char(string="Año", required = True)
    num_equipos = fields.Integer(string="Numero de participantes", required = True)
    equipo = fields.Many2one("paintball.equipo", string="Equipo ganador")

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

class cliente(models.Model):
    _name = 'paintball.cliente'

    name = fields.Char(string = "IDENTIFICADOR", required = True)
    nombre = fields.Char(string="Nombre", required = True)
    apellidos = fields.Char(string="Apellidos", required=True)
    fecha_nac = fields.Date(string="Fecha de nacimiento", required=True)
    telefono = fields.Integer(string="Telefono de contacto")
    equipo = fields.Many2one("paintball.equipo", string="Equipo")

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

class equipo(models.Model):
    _name = 'paintball.equipo'

    name = fields.Char(string = "IDENTIFICADOR", required = True)
    nombre = fields.Char(string="Nombre", required = True)
    telefono = fields.Integer(string="Telefono de contacto")

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

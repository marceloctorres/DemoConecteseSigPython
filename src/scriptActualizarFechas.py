# -*- coding: utf-8 -*-

from DemoConecteseSigPy.Herramientas import Procesos

Procesos.ActualizarFecha(
        portal = 'https://marceloctorresn.maps.arcgis.com/', 
        usuario = 'marceloctorresn', 
        clave = 'm4rc3l025202$$', 
        servicio= 'PuntosInteres',
        nombreTabla='PuntoInteres',
        campoFecha = 'fecha',
        salidaRelativa = True,
        rutaSalida = "../../logs")

#!/usr/bin/env python3
# encoding: UTF-8

"""
    Herramienta IP_GeoLocation Tool.
    
    
    IP_Locacion - Recuperar Informacion De Geo_localizacion Ip
    Desarrollado Por http://ip-api.com
     
    Este Programa Es Software Libre:Puedes      Redistribuirlo y/o Modificarlo. 
    Bajo Los Términos De La Licencia Pública General GNU Publicada Por La Free Software Foundation.
     Ya Sea La versión De La Licencia,O(A Su Elección) Cualquier Versión Posterior.

    Este Programa Se Distribuye Con La Esperanza De Que Sea Util.
    Pero SIN NINGUNA GARANTÍA; Sin Siquiera La Garantía Implícita De COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR.
 Ver el Licencia pública general GNU para obtener más detalles.

    Debería Haber Recibido Una Copia De La Licencia Pública General GNU Junto Con Este Programa. 
    Si No, Ver <http://www.gnu.org/licenses/>.
    
    Para Obtener Más Información, Consulte El Archivo 'LICENCIA' Para Obtener Permiso De Copia. 

"""

__author__  = 'Ivan-M-YT-TLM-SDP'


import sys, os
from core.IpGeoLocationLib import IpGeoLocationLib
from core.Logger import Logger
from core.Menu import parser,args,banner
    
def main():

    # no args provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    logsDir = os.path.join(os.getcwd(), 'logs')
    #resultsDir = os.path.join(os.getcwd(), 'results')
    if not os.path.exists(logsDir):
        os.mkdir(logsDir)
    #if not os.path.exists(resultsDir):
    #    os.mkdir(resultsDir)
        
    logger = Logger(args.nolog, args.verbose)
    
    #objetivo único o múltiples objetivos 
    if(args.target and args.tlist):
        logger.PrintError("Puede solicitar información de Geolocalización ya sea para un solo objetivo (-t) o una lista de objetivos (-T). No ambos!", args.nolog)
        sys.exit(2)
        
    #mi dirección IP o objetivo único
    if(args.target and args.myip):
        logger.PrintError("Puede solicitar información de geolocalización ya sea para un único objetivo (-t) o su propia dirección IP. No ambos!", args.nolog)
        sys.exit(3)
        
    #múltiples objetivos o mi dirección IP
    if(args.tlist and args.myip):
        logger.PrintError("Puede solicitar información de geolocalización ya sea para un único objetivo (-t) o su propia dirección IP. No ambos!", args.nolog)
        sys.exit(4)
    
    #Solo se permiten objetivos únicos y Google Maps.
    if(args.tlist and args.g):
        logger.PrintError("La ubicación de Google Maps funciona solo con objetivos únicos.", args.nolog)
        sys.exit(5)
    
    #Especificar usuario-agente o aleatorio
    if(args.uagent and args.ulist):
        logger.PrintError("Puede especificar una cadena de agente de usuario o dejar que IPGeolocation elija cadenas de agente de usuario aleatorias de un archivo.", args.nolog)
        sys.exit(6)
        
    #proxy aleatorio
    if(args.proxy and args.xlist):
        logger.PrintError("Puede especificar un proxy o dejar que IPGeolocation elija conexiones de proxy aleatorias desde un archivo.", args.nolog)
        sys.exit(7)
        
        
    #biblioteca de inicio
    ipGeoLocRequest = IpGeoLocationLib(args.target, logger, args.noprint)
    
    print(banner)
    
    #Recuperar Información
    if not ipGeoLocRequest.GetInfo(args.uagent, args.tlist, 
                                     args.ulist, args.proxy, args.xlist,
                                     args.csv, args.xml, args.txt, args.g):
        logger.PrintError("Error al recuperar la información de geolocalización de IP.")
        sys.exit(8)


if __name__ == '__main__':
    main()
    
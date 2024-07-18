# imported logging to ensure visability on console 
import logging
import os

import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError

logger = logging.getLogger(__name__)

types = {
    'LandmarkName':'major landmark building',
    'OccupancyType':'multi-unit dwelling',
    'SubaddressType':'multi-unit dwelling',
    'USPSBoxID':'PO Box',
    'SubaddressType':'Non-Residential unit',
    }

class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]
    
    def get(self, request):
        addr = request.query_params.get('address')
        parse_values = self.parse(addr)
        logger.warning('Inside get, after self.parse', parse_values)
        
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        return Response({'components': parse_values})

    def parse(self, address):

        address_components = usaddress.parse(address)
        logger.warning('Inside self.parse')
        logger.critical(address_components[0])
        address_type = ''

        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        return address_components, address_type

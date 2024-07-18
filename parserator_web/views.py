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

# created types dictionary to deduce addr_type 
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
        try:
            parse_values, addr_type = self.parse(addr)

            return Response({
                'input_string': addr,
                'address_components': parse_values,
                'address_type': addr_type,
            }, 200)
        except:
            return Response({'Error':'There was an error in your submission'}, 412)     

    def parse(self, address):

        address_components = usaddress.parse(address)
        
        for pair in address_components:
            # Checking for a type match to determine addr_type #
            if pair[1] in types.keys():
                type = pair[1]
                # Assign type based on types match value
                address_type = types[type]
                break
            address_type = 'Residential'
                
        return address_components, address_type

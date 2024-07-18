# imported logging to ensure visability on console 
import logging
import os

import usaddress
from django.views.generic import TemplateView
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer



logger = logging.getLogger(__name__)

# created types dictionary to deduce addr_type
# realized that .tag() would be the correct use
# of the usaddress methods available

# types = {
#     'LandmarkName':'major landmark building',
#     'OccupancyType':'multi-unit dwelling',
#     'SubaddressType':'multi-unit dwelling',
#     'USPSBoxID':'PO Box',
#     'SubaddressType':'Non-Residential unit',
#     }

class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]
    
    def get(self, request):
        addr = request.query_params.get('address')

        if not addr:
            return Response({
                'ErrorMessage': 'The input field can not be left empty'
            }, 400)
        
        try:
            parse_values, addr_type = self.parse(addr)
            logger.warning('After Parse:')
            logger.warning(parse_values, addr_type)
            
            return Response({
                'input_string': addr,
                'address_components': parse_values,
                'address_type': addr_type,
                }, 200)
        
        # Handles repeated tags within parse() response 
        except usaddress.RepeatedLabelError as rle:
            logger.error('Parsing Error:', rle)
            return Response({
                'ErrorMessage': 'You must enter a valid US address, be sure there are not repeating values.',
                }, 412)
        
        # Handles all other errors
        except Exception as e:
            return Response({
                'ErrorMessage': 'There was an unexpected error while processing your request, try again.',
                'ErrorData': e
                }, 500)

    def parse(self, address):

        address_components, address_type = usaddress.tag(address)
        # address_type = 'Residential' #Default
        
        # for pair in address_components:
        #     # Checking for a type match to determine addr_type #
        #     if pair[1] in types.keys():
        #         type = pair[1]
        #         # Assign type based on types match value
        #         address_type = types[type]
        #         break
        if 'error' in address:
            raise ValueError('Invalid address format')
                
        return address_components, address_type

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
# realized that .tag() miight be the correct use
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
        invalid_characters = set("@$%^&*()_+={}[]|:;'<>?!")

        addr = request.query_params.get('address')
        for char in addr:
            if char in invalid_characters:
                return Response({
                    'ErrorMessage':'Please be sure to use only valid Address characters'
                }, 400)

        if not addr:
            return Response({
                'ErrorMessage': 'The input field can not be left empty'
            }, 400)
        
        try:
            parse_values, addr_type = self.parse(addr)
            
            return Response({
                'input_string': addr,
                'address_components': parse_values,
                'address_type': addr_type,
                }, 200)
        
        # Handles repeated tags within parse() response 
        except usaddress.RepeatedLabelError as rle:

            return Response({
                'ErrorMessage': 'You must enter a valid US address, be sure there are not repeating values.',
                }, 400)
        
        # Handles all other errors
        except Exception as e:
            return Response({
                'ErrorMessage': 'There was an unexpected error while processing your request, try again.',
                'ErrorData': e
                }, 400)

    def parse(self, address):

        address_components, address_type = usaddress.tag(address)
                
        return address_components, address_type

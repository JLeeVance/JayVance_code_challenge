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


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]
    logger.critical('Critial: HIT')
    logger.warning('HIT')
    

    def get(self, request):
        address = request.query_params.get('address')
        logger.warning(address)
        
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        return Response({'message': 'Hello, World'})

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        return address_components, address_type

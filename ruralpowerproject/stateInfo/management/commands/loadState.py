import os
from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping
from stateInfo.models import State



class Command(BaseCommand):
    args = 'no args'
    help = 'load state from shp file'

    def handle(self, *args, **options):
    	self.stdout.write('Import USA State')
    	state_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../shpData/southStates.shp'))
    	state_mapping = {'statefp' : 'STATEFP','name' : 'NAME','geom' : 'POLYGON25D', }
    	lm = LayerMapping(State, state_shp, state_mapping,transform=False, encoding='iso-8859-1')
    	lm.save(strict=True, verbose=True)
    	self.stdout.write('Import OK')




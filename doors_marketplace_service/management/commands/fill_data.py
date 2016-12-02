# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import logging
import os
import requests
from doors_marketplace_service.models import Actions
import doors_marketplace_service.localsettings as settings

logger = logging.getLogger(__name__)

def add_new_actions(actions_name,foto):

    action = Actions.objects.create(name=actions_name, actual=True)
    upload_file(action, foto)

def upload_file(action, file):
    image_data = {'type': 'marketplace',
                  'object': 'action',
                  'id': action.id
                  }
    manager = getattr(requests, 'post')
    files = {'file': open(file, 'rb')}
    resp = manager(settings.services['files_service'] + '/' + 'upload_file',
               data=image_data, files=files)
    if resp.status_code == 200:
        action.foto = []
        action.foto.append(resp.json().get('path'))
        action.save()

class Command(BaseCommand):
    help = ' fill actions '

    def add_arguments(self, parser):
        parser.add_argument('--path',
                            action='store',
                            dest='path',
                            type=str,
                            default='',
                            help='path to files')
        parser.add_argument('--filename',
                            action='store',
                            dest='filename',
                            type=str,
                            default='uploading_actions.txt',
                            help='data filename')

    def handle(self, *args, **options):
        try:
            import_file = options['path']
            filename = options['filename']
            with open(os.path.join(import_file, filename)) as import_data:
                for line in import_data:
                    actions_name, fotos_list = line.split(';')
                    for foto in fotos_list.split(','):
                        if True:
                            add_new_actions(actions_name + '_' + foto, os.path.join(import_file, foto + '.jpg'))
                            print 'add action - %s' % foto
                        #except:
                        #    pass

        except Exception, e:
            print e
            logger.exception(e)



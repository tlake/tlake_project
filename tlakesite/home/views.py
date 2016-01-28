from __future__ import print_function

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import HomePageMessage, ResumeFolderID

import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools


class HomePageView(ListView):
    model = HomePageMessage
    template_name = 'home.html'

    def resume_link(self):
        # _folder_id = "0B6D4ecmbxciiekhzYXRHQ2duelU"
        _folder_id = ResumeFolderID.objects.first().folder_id

        def _get_credentials():
            """Gets valid user credentials from storage.

            If nothing has been stored, or if the stored credentials are invalid,
            the OAuth2 flow is completed to obtain the new credentials.

            Returns:
                Credentials, the obtained credential.
            """
            home_dir = os.path.expanduser('~')
            credential_dir = os.path.join(home_dir, '.credentials')
            if not os.path.exists(credential_dir):
                os.makedirs(credential_dir)
            credential_path = os.path.join(credential_dir,
                                           'drive-python-quickstart.json')

            store = oauth2client.file.Storage(credential_path)
            credentials = store.get()
            if not credentials or credentials.invalid:
                flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
                flow.user_agent = APPLICATION_NAME
                if flags:
                    credentials = tools.run_flow(flow, store, flags)
                else: # Needed only for compatibility with Python 2.6
                    credentials = tools.run(flow, store)
                print('Storing credentials to ' + credential_path)
            return credentials

        def _get_file_id(service, folder_id):
            """ Returns the ID of the first file found inside the
            folder designated by folder_id.
            """
            children = service.children().list(folderId=folder_id).execute()

            return children.get('items', [])[0]['id']

        credentials = _get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('drive', 'v2', http=http)

        file_id = _get_file_id(service, _folder_id)

        return "https://drive.google.com/file/d/" + file_id + "/view"


# coding: utf-8
from __future__ import absolute_import, division, print_function
import os

from google.appengine.ext import blobstore

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(
            {'upload_url': blobstore.create_upload_url('/finish_upload')}
        ))


class FinishUpload(webapp2.RequestHandler):
    def post(self):
        self.error(500)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/finish_upload', FinishUpload),
], debug=True)

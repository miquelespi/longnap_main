#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import urllib

# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.write('Hello world!')

class MainHandler(webapp2.RequestHandler):
    def get(self,fname=None):
        if fname is None: fname='index.html'
        path = os.path.join(os.path.split(__file__)[0], 'html/'+fname)
        f = open(path)
        self.response.out.write(f.read())


class KoreanHandler(webapp2.RequestHandler):
    def get(self,fname=None):
        if fname is None: fname='index.html'
        path = os.path.join(os.path.split(__file__)[0], 'html/korean/'+fname)
        f = open(path)
        self.response.out.write(f.read())

class KoreanHandlerAlone(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.split(__file__)[0], 'html/korean/index.html')
        f = open(path)
        self.response.out.write(f.read())

class MainHandler(webapp2.RequestHandler):
    def get(self,fname=None):
        if fname is None: fname='index.html'
        path = os.path.join(os.path.split(__file__)[0], 'html/'+fname)
        f = open(path)
        self.response.out.write(f.read())


class MiquelHandler(webapp2.RequestHandler):
    def get(self,fname=None):
        if fname is None: fname='index.html'
        path = os.path.join(os.path.split(__file__)[0], 'html/miquel/'+fname)
        f = open(path)
        self.response.out.write(f.read())

class MiquelHandlerAlone(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.split(__file__)[0], 'html/miquel/index.html')
        f = open(path)
        self.response.out.write(f.read())
class KoreanHandlerStyle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.split(__file__)[0], 'html/korean/style_korean.css')
        f = open(path)
        self.response.out.write(f.read())


app = webapp2.WSGIApplication([
    ('/79', KoreanHandlerAlone),
    ('/79/([^/]+)?', KoreanHandler),
    ('/miquel', MiquelHandlerAlone),
    ('/miquel/([^/]+)?', MiquelHandler),
    ('/korean', KoreanHandlerAlone),
    ('/korean/([^/]+)?', KoreanHandler),
    ('/koreanwithhyangsun', KoreanHandlerAlone),
    ('/koreanwithhyangsun/([^/]+)?', KoreanHandler),
    ('/style_korean.css', KoreanHandlerStyle),
    ('/([^/]+)?', MainHandler),
], debug=True)

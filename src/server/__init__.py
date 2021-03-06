from flask import Flask
from flask_restplus import Api
import os
class Server():
  def __init__(self):
    self.app = Flask(__name__)
    self.app.config['BUNDLE_ERRORS'] = True
    self.api = Api(
      self.app, 
      version='1.0', 
      title='covid19 API',
      description='Covid19 Status API',
      doc='/docs'
    )

  def run(self, ):
    port = int(os.environ.get('PORT'))
    self.app.run(debug=False, port=port, threaded=True)


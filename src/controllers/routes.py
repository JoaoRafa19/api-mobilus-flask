from datetime import date, time, datetime
import requests
from flask import jsonify
from flask_restplus import Resource
from .api import api
import asyncio

@api.route('/info')
class Main(Resource):

  def get (self):
    
    response = {
    "title":"Covid 19 Status API",
    "powered_by":"Python/Flask",
    "description":"API for get covid19 status",
    "owner":'João Pedro Rafael Santos Silva'
    }
    return response
    
@api.route('/covid/status/confirmed')
class Confirmed(Resource):

  
  def get (self):
    
    lastDate = date.fromordinal(date.toordinal(date.today())-180)
    
    casos = requests.get(f'https://api.covid19api.com/total/country/brazil/status/confirmed?from={lastDate}T00:00:00Z&to={date.today()}T00:00:00Z')
    
    return casos.json()

@api.route('/covid/status')
class Status(Resource):
  def get(self):
    lastDate = date.fromordinal(date.toordinal(date.today())-180)
    
    casos = requests.get(f'https://api.covid19api.com/total/country/brazil?from={lastDate}T00:00:00Z&to={date.today()}T00:00:00Z')
    
    return casos.json()


@api.route('/covid/lastwoweaks')
class LastTwoWeaks(Resource):
  def get(self):
    lastDate = date.fromordinal(date.toordinal(date.today())-14)
    casos = requests.get(f'https://api.covid19api.com/total/country/brazil?from={lastDate}T00:00:00Z&to={date.today()}T00:00:00Z')
    return casos.json()
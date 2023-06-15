import requests
import os
import json

class HarnessConnector:
    
    def __init__(self, url, json_file, api_key):
        self.url = url
        self.json_file = json_file
        self.api_key = api_key
    
    def create_connector(self):
        json_object = open(self.json_file)
        json_data = json.load(json_object)
        request_headers = {
            'x-api-key': self.api_key,
            'Content-Type': 'application/json'
        }
        requests.post(self.url, data=json_data, headers=request_headers)




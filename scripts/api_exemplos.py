#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hackathon IDP 2023

Exemplo de acesso a API.

@author: cafe
"""

import requests

end_points = 'https://hackarestaurante-2023.azurewebsites.net/swagger/v1/swagger.json'
rest = 'https://hackarestaurante-2023.azurewebsites.net'
r = requests.get(end_points)
end_points = r.json()
paths = end_points['paths']

r = requests.get(rest+list(paths.keys())[0])
response = r.json()
print(response)

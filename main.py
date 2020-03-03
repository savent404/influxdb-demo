# -*- coding: utf-8 -*-

import os
import json
from influxdb import InfluxDBClient

def connect(config):
    client = InfluxDBClient(config['host'], config['host_port'],
        config['user_name'], config['password'], config['dbname'])
    return client

def reviewData(client):
    rs = client.query('select * from device_CCV1 limit 3')
    res = []
    for it in rs.get_points():
        res.extend(it)
    print(format(res))

if __name__ == '__main__':
    config_file = os.path.dirname(os.path.realpath(__file__)) + '/config.json'
    with open(config_file) as f:
        config = json.load(f)
    client = connect(config)
    reviewData(client)
    client.close()
    

# -*- coding: utf-8 -*-
# The MIT License (MIT)
# Copyright © 2015 Eli Song

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


def parse(client, server_name, subserver_name, response):
    name = server_name + subserver_name
    options = {'geoconv': parse_gcv,
               'directionroutematrix': parse_drx,
               'locationip': parse_lip,
               'direction': parse_drn,
               'geocoder': parse_gcr,
               'placesuggestion': parse_psn,
               'placesearch': parse_psh,
               'placedetail': parse_pdl,
               'placeeventsearch': parse_peh,
               'placeeventdetail': parse_pel
               }

    return options[name](response)


def parse_gcv(response):
    result_raw = response['result']
    if len(result_raw) > 1:
        result_parse = [{'lng': rr['x'], 'lat': rr['y']} for rr in result_raw]
    else:
        result_parse = {'lng': result_raw[0]['x'], 'lat': result_raw[0]['y']}
    return result_parse


def parse_drx(response):
    result_raw = response['result']['elements']
    if len(result_raw) > 1:
        result_parse = []
        for rr in result_raw:
            if 'distance' in rr:
                result_parse.append({'distance': rr['distance']['value'],
                                    'duration': rr['duration']['value']})
            else:
                result_parse.append({'status': rr['status'],
                                    'message': rr['message']})
    else:
        if 'distance' in rr:
            result_parse = {'distance': result_raw[0]['distance']['value'],
                            'duration': result_raw[0]['duration']['value']}
        else:
            result_parse = {'status': result_raw[0]['status'],
                            'message': result_raw[0]['message']}

    return result_parse


def parse_lip(response):
    result_raw = response['content']
    result_raw['address_detail'].pop('city_code')
    result_parse = {'address': result_raw['address_detail'],
                    'location': {'lng': float(result_raw['point']['x']),
                                 'lat': float(result_raw['point']['y'])}}
    return result_parse


def parse_drn(response):
    # if type==1
    if response['type'] == 1:
        result_raw = response['result']
        # if mode==drving/walking
        if 'content' in result_raw['origin']:
            origin = result_raw['origin']['content']
            for i, ori in enumerate(origin):
                ori.pop('telephone')
                origin[i] = ori

            destination = result_raw['destination']
            for j, des in enumerate(destination):
                des.pop('telephone')
                destination[j] = des

        # if mode=transit
        else:
            origin = result_raw['origin']
            for i, ori in enumerate(origin):
                ori.pop('uid')
                origin[i] = ori

            destination = result_raw['destination']
            for j, des in enumerate(destination):
                des.pop('uid')
                destination[j] = des

        result_parse = {'origin_maybe': origin,
                        'destination_maybe': destination}
    # if type==2
    else:
        origin_raw = response['result']['origin']
        destination_raw = response['result']['destination']
        routes = response['result']['routes']
        # if mode=transit
        if 'scheme' in routes[0]:
            routes = [rou['scheme'][0] for rou in routes]
        origin = origin_raw['originPt']
        destination = destination_raw['destinationPt']

        result_parse = {'routes': routes, 'origin': origin,
                        'destination': destination}
    return result_parse


def parse_gcr(response):
    result_parse = response['result']
    return result_parse


def parse_psn(response):
    result_parse = response['result']
    for i, rr in enumerate(result_parse):
        if 'cityid' in rr: rr.pop('cityid')
        if 'uid' in rr: rr.pop('uid')
        if 'business' in rr: rr.pop('business')
        result_parse[i] = rr
    return result_parse


def parse_psh(response):
    result_parse = response['results']
    for i, rp in enumerate(result_parse):
        if 'street_id' in rp: rp.pop('street_id')
        if 'detail' in rp: rp.pop('detail')
        result_parse[i] = rp
    return result_parse


def parse_pdl(response):
    result_parse = response['result']
    for i, rp in enumerate(result_parse):
        if 'detail' in rp: rp.pop('detail')
        result_parse[i] = rp
    return result_parse


def parse_peh(response):
    result_parse = response['results']
    return result_parse


def parse_pel(response):
    result_parse = response['result']
    return result_parse

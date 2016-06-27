# -*- coding: utf-8 -*-
# The MIT License (MIT)
# Copyright © 2015 Eli Song

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
PY2 = sys.version[0] == '2'
import re


def place_search(client, query, region=None, bounds=None,
                 location=None, **kwargs):
    """This module sends requests for "query", and returns general
        geographic information. It also needs assigning one and only one of
        following key words: "region", "bounds", "location", so as to set
        search type. For more details, please refer to Baidu's official
        description.

    Attention! You should always use <lng, lat>, NOT <lat, lng> whenever you
        need. It will be converted to <lat, lng> if raw API requires.
        Moreover, default return is a simpler version of raw API callback, of
        course, you can set 'raw=True' for complete raw json callback.

    Reference: http://developer.baidu.com/map/index.php?title=webapi/guide/webservice-placeapi
    """

    sep_pattern = re.compile(r'[,;|]')

    if not any([region, bounds, location]):
        raise ValueError('please assign one and only one of search types: \
                         "region", "bounds", "location".')

    elif bounds:
        if isinstance(bounds, str):
            sep_bounds = sep_pattern.split(bounds)
            if len(sep_bounds) != 4:
                raise ValueError('"bounds" incorrect! It may like this: \
                                 \nbounds="116.404,39.915;116.414,39.975".')
            else:
                reorder_bounds = [sep_bounds[i] for i in [1, 0, 3, 2]]
                kwargs['bounds'] = ','.join(reorder_bounds)

        elif isinstance(bounds, list):
            if len(bounds) != 2:
                raise ValueError('"bounds" incorrect! It may like this: \
                                 \nbounds=[[116.404, 39.915], [116.414, \
                                 39.975]].')
            else:
                comb_bounds = [','.join(map(str, bo[::-1])) for bo in bounds]
                kwargs['bounds'] = ','.join(comb_bounds)

        else:
            raise ValueError('"bounds" must be a str or list instance!')

    elif location:
        if isinstance(location, str):
            sep_location = sep_pattern.split(location)
            if len(sep_location) != 2:
                raise ValueError('"location" incorrect! It may like this: \
                                 \nlocation="116.404,39.915".')
            else:
                kwargs['location'] = ','.join(sep_location[::-1])

        elif isinstance(location, list):
            if len(location) != 2:
                raise ValueError('"location" incorrect! It may like this: \
                                 \nlocation=[116.404, 39.915]')
            else:
                kwargs['location'] = ','.join(map(str, location[::-1]))

        else:
            raise ValueError('"location" must be a str or list instance!')
    else:
        kwargs['region'] = region

    kwargs.update({'server_name': 'place', 'version': 'v2',
                   'subserver_name': 'search', 'query': query})

    return client.get(kwargs)


def place_detail(client, uid=None, uids=None, **kwargs):
    """This module sends requests for "uid"/"uids"("uids" for more than two
        uids), and returns detail information. For more details, please refer
        to Baidu's official description.

    Attention! Default return is a simpler version of raw API callback, of
        course, you can set 'raw=True' for complete raw json callback.

    Reference: http://developer.baidu.com/map/index.php?title=webapi/guide/webservice-placeapi
    """

    sep_pattern = re.compile(r'[,;|]')

    if not any([uid, uids]):
        raise ValueError('please assign "uid" or "uids".')
    elif uids:
        sep_uids = sep_pattern.split(kwargs['uids'])
        kwargs['uids'] = ','.join(sep_uids)
    else:
        kwargs['uid'] = uid

    kwargs.update({'server_name': 'place', 'version': 'v2',
                   'subserver_name': 'detail'})

    return client.get(kwargs)


def place_eventsearch(client, query, event, region, bounds=None,
                      location=None, **kwargs):
    """This module sends requests for event determined by "query", "event",
        "region", and returns event information. It also needs assigning one
        and only one of following key words: "bounds", "location", so as to set
        search type. 【 Quite not sure why "region" argument here does't have equal stage to `bounds` or `location` like situation in
          place_search？】 For more details, please refer to Baidu's official
        description.

    Attention! You should always use <lng, lat>, NOT <lat, lng> whenever you
        need. It will be converted to <lat, lng> if raw API requires.
        Moreover, default return is a simpler version of raw API callback, of
        course, you can set 'raw=True' for complete raw json callback.

    Reference: http://developer.baidu.com/map/index.php?title=webapi/guide/webservice-placeapi
    """

    sep_pattern = re.compile(r'[,;|]')

    if not any([bounds, location]):
        raise ValueError('please assign either "bounds" or "location".')
    elif bounds:
        if isinstance(bounds, str):
            sep_bounds = sep_pattern.split(bounds)
            if len(sep_bounds) != 4:
                raise ValueError('"bounds" incorrect! It may like this: \
                                 \nbounds="116.404,39.915;116.414,39.975".')
            else:
                reorder_bounds = [sep_bounds[i] for i in [1, 0, 3, 2]]
                kwargs['bounds'] = ','.join(reorder_bounds)

        elif isinstance(bounds, list):
            if len(bounds) != 2:
                raise ValueError('"bounds" incorrect! It may like this: \
                                 \nbounds=[[116.404, 39.915], [116.414, \
                                 39.975]].')
            else:
                comb_bounds = [','.join(map(str, bo[::-1])) for bo in bounds]
                kwargs['bounds'] = ','.join(comb_bounds)

        else:
            raise ValueError('"bounds" must be a str or list instance!')

    else:
        if isinstance(location, str):
            sep_location = sep_pattern.split(location)
            if len(sep_location) != 2:
                raise ValueError('"location" incorrect! It may like this: \
                                 \nlocation="116.404,39.915".')
            else:
                kwargs['location'] = ','.join(sep_location[::-1])

        elif isinstance(location, list):
            if len(location) != 2:
                raise ValueError('"location" incorrect! It may like this: \
                                 \nlocation=[116.404, 39.915]')
            else:
                kwargs['location'] = ','.join(map(str, location[::-1]))

        else:
            raise ValueError('"location" must be a str or list instance!')

    kwargs.update({'server_name': 'place', 'version': 'v2',
                   'subserver_name': 'eventsearch', 'query': query,
                   'event': event, 'region': region})

    return client.get(kwargs)


def place_eventdetail(client, uid, **kwargs):
    """This module sends requests for POI "uid", and returns event detail
        information. For more details, please refer to Baidu's official
        description.

    Attention! NO supports for 2 uids or more in one request. Moreover,
        default return is a simpler version of raw API callback, of
        course, you can set 'raw=True' for complete raw json callback.

    Reference: http://developer.baidu.com/map/index.php?title=webapi/guide/webservice-placeapi
    """

    kwargs.update({'server_name': 'place', 'version': 'v2',
                   'subserver_name': 'eventdetail', 'uid': uid})
    return client.get(kwargs)


def place_suggest(client, query, region, **kwargs):
    """This module sends requests for event determined by "query" and
        "region", and returns best search suggestion. For more details, please
        refer to Baidu's official description.

    Attention! You should always use <lng, lat>, NOT <lat, lng> whenever you
        need. It will be converted to <lat, lng> if raw API requires.
        Moreover, default return is a simpler version of raw API callback, of
        course, you can set 'raw=True' for complete raw json callback.

    Reference: http://developer.baidu.com/map/index.php?title=webapi/place-suggestion-api
    """

    check_location = 'location' in kwargs
    sep_pattern = re.compile(r'[,;|]')

    if check_location:
        location = kwargs['location']
        if isinstance(location, str):
            sep_location = sep_pattern.split(location)
            if len(sep_location) != 2:
                raise ValueError('"location" incorrect! It may like this: \
                                 \nlocation="116.404,39.915".')
            else:
                kwargs['location'] = ','.join(sep_location[::-1])

        elif isinstance(location, list):
            if len(location) != 2:
                raise ValueError('"location" incorrect! It may like this: \
                                 \nlocation=[116.404, 39.915]')
            else:
                kwargs['location'] = ','.join(map(str, location[::-1]))

        else:
            raise ValueError('"location" must be a str or list instance!')

    kwargs.update({'server_name': 'place', 'version': 'v2',
                   'subserver_name': 'suggestion', 'region': region,
                   'query': query})

    return client.get(kwargs)


def geocode(client, address=None, location=None, **kwargs):
    """This module sends requests for "address", and returns "location"
        information, or conversely. For more details, please refer to Baidu's
        official description.

    Attention! You should always use <lng, lat>, NOT <lat, lng> whenever you
        need. It will be converted to <lat, lng> if raw API requires.
        Moreover, default return is a simpler version of raw API callback, of
        course, you can set 'raw=True' for complete raw json callback.

    Reference: http://developer.baidu.com/map/index.php?title=webapi/guide/webservice-geocoding
    """

    sep_pattern = re.compile(r'[,;|]')

    if not any([address, location]):
        raise ValueError('please assign either "address" or "location".')

    elif location:
        if isinstance(location, str):
            sep_location = sep_pattern.split(location)
            if len(sep_location) != 2:
                raise ValueError('"location" incorrect! It may like this: \
                                 \nlocation="116.404,39.915".')
            else:
                kwargs['location'] = ','.join(sep_location[::-1])

        elif isinstance(location, list):
            if len(location) != 2:
                raise ValueError('"location" incorrect! It may like this: \
                                 \nlocation=[116.404, 39.915]')
            else:
                kwargs['location'] = ','.join(map(str, location[::-1]))

        else:
            raise ValueError('"location" must be a str or list instance!')
    else:
        kwargs['address'] = address

    kwargs.update({'server_name': 'geocoder', 'version': 'v2',
                   'subserver_name': ''})

    return client.get(kwargs)


def direct(client, origin, destination, mode='driving', region=None,
           origin_region=None, destination_region=None, **kwargs):
    """This module sends requests for route determined by "origin",
        "destination" and "mode='driving'", returns direction information. If
        mode="driving", It needs assigning "origin_region" and
        "destination_region"; if mode="walking" or "transit", It also needs
        assigning "region". For more details, please refer to Baidu's official
        description.

    Attention! You should always use <lng, lat>, NOT <lat, lng> whenever you
        need. It will be converted to <lat, lng> if raw API requires.
        Moreover, default return is a simpler version of raw API callback, of
        course, you can set 'raw=True' for complete raw json callback.

    Reference: http://developer.baidu.com/map/index.php?title=webapi/direction-api
    """

    CN_pattern = re.compile(u'[\u4e00-\u9fa5]+')

    if isinstance(origin, str):
        if PY2:
            u_origin = origin.decode('utf-8')
        else:
            u_origin = origin
        match = CN_pattern.search(u_origin)
        if not match:
            origin = ','.join(origin.split(',')[::-1])
    elif isinstance(origin, list):
        origin = map(str, origin)
        origin = ','.join(origin[::-1])
    else:
        raise ValueError('"origin"  must be a str or list instance!')

    if isinstance(destination, str):
        if PY2:
            u_destination = destination.decode('utf-8')
        else:
            u_destination = destination
        match = CN_pattern.search(u_destination)
        if not match:
            destination = ','.join(destination.split(',')[::-1])
    elif isinstance(destination, list):
        destination = map(str, destination)
        destination = ','.join(destination[::-1])
    else:
        raise ValueError('"destination" must be a str or list instance!')

    if mode == 'driving':
        if not all([origin_region, destination_region]):
            raise ValueError('please assign "origin_region" and \
                             "destination_region".')
        kwargs.update({'origin_region': origin_region,
                      'destination_region': destination_region})
    elif mode in ['walking', 'transit']:
        if not region:
            raise ValueError('please assign "region".')
        kwargs.update({'region': region,
                      'mode': mode})
    else:
        raise ValueError('"mode" incorrect! It must be in ["driving", \
                         "walking", "transit"].')

    kwargs.update({'server_name': 'direction', 'version': 'v1',
                   'subserver_name': '', 'origin': origin,
                   'destination': destination})

    return client.get(kwargs)


def ip_locate(client, ip=None, **kwargs):
    """This module requests location information for given ip or current local
        ip. For more details, please refer to Baidu's official description.

    Attention! Default return is a simpler version of raw API callback, of
        course, you can set 'raw=True' for complete raw json callback.

    Reference: http://developer.baidu.com/map/index.php?title=webapi/ip-api
    """

    if ip:
        IPpattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
        match = IPpattern.match(ip)
        if not match:
            raise ValueError('"ip" incorrect!')
        kwargs['ip'] = ip

    kwargs.update({'server_name': 'location', 'version': '',
                  'subserver_name': 'ip'})

    return client.get(kwargs)


def route_matrix(client, origins, destinations, **kwargs):
    """This module requests routes information, from origin points(upper
        limits 5) to destination points(upper limits 5). For more details,
        please refer to Baidu's official description.

    Attention! You should always use <lng, lat>, NOT <lat, lng> whenever you
        need. It will be converted to <lat, lng> if raw API requires.
        Moreover, default return is a simpler version of raw API callback, of
        course, you can set 'raw=True' for complete raw json callback.

    Reference: http://developer.baidu.com/map/index.php?title=webapi/route-matrix-api
    """

    sep_pattern = re.compile(r'[,;|]')
    CN_pattern = re.compile(u'[\u4e00-\u9fa5]+')

    is_origins_str = isinstance(origins, str)
    is_origins_list = isinstance(origins, list)
    if not any([is_origins_str, is_origins_list]):
        raise ValueError('"origins" must be str or list!')
    elif is_origins_str:
        sep_origins = sep_pattern.split(origins)
        # u_origins = origins.decode('utf-8')
        u_origins = origins
        CN_pattern = re.compile(u'[\u4e00-\u9fa5]+')
        match = CN_pattern.search(u_origins)
        if match:
            if len(sep_origins) > 5:
                raise ValueError('"origins" incorrect! upper limits is 5.')
            else:
                origins = '|'.join(sep_origins)
        else:
            if len(sep_origins) > 10:
                raise ValueError('"origins"incorrect! upper limits is 5.')
            else:
                temp = [','.join(sep_origins[(2*x):(2*x+2)][::-1])
                        for x in range(0, len(sep_origins)/2)]
                origins = '|'.join(temp)

    else:
        # element in list is CN_pattern characters.
        if len(origins[0]) == 1:
            origins = '|'.join(origins)
        # element in list is list/tuple of lng,lat.
        else:
            origins = [map(str, l) for l in origins]
            origins = '|'.join([','.join(l[::-1]) for l in origins])

    is_destinations_str = isinstance(destinations, str)
    is_destinations_list = isinstance(destinations, list)

    if not any([is_destinations_str, is_destinations_list]):
        raise ValueError('"destinations" must be str or list!')
    elif is_destinations_str:
        sep_destinations = sep_pattern.split(destinations)
        # u_destinations = destinations.decode('utf-8')
        u_destinations = destinations
        CN_pattern = re.compile(u'[\u4e00-\u9fa5]+')
        match = CN_pattern.search(u_destinations)
        if match:
            if len(sep_destinations) > 5:
                raise ValueError('"destinations" incorrect! upper limits is \
                                 5.')
            else:
                destinations = '|'.join(sep_destinations)
        else:
            if len(sep_destinations) > 10:
                raise ValueError('"destinations"incorrect! upper limits is 5.')
            else:
                temp = [','.join(sep_destinations[(2*x):(2*x+2)][::-1])
                        for x in range(0, len(sep_destinations)/2)]
                destinations = '|'.join(temp)

    else:
        if len(destinations[0]) == 1:
            destinations = '|'.join(destinations)
        else:
            # first, map to str.
            destinations = [map(str, l) for l in destinations]
            destinations = '|'.join([','.join(l[::-1]) for l in destinations])

    kwargs.update({'server_name': 'direction', 'version': 'v1',
                   'subserver_name': 'routematrix', 'origins': origins,
                   'destinations': destinations})

    return client.get(kwargs)


def geoconv(client, coords, **kwargs):
    """This module converts coords from some standard type to another. For
        more details, please refer to Baidu's official description.

    Attention! You should always use <lng, lat>, NOT <lat, lng> whenever you
        need. It will be converted to <lat, lng> if raw API requires.
        Moreover, default return is a simpler version of raw API callback, of
        course, you can set 'raw=True' for complete raw json callback.

    Reference: http://developer.baidu.com/map/index.php?title=webapi/guide/changeposition
    """

    sep_pattern = re.compile(r'[,;|]')
    is_str = isinstance(coords, str)
    is_list = isinstance(coords, list)

    if not any([is_str, is_list]):
        raise ValueError('"coords" must be str or list!')
    elif is_str:
        flat_co = sep_pattern.split(coords)
    elif is_list and isinstance(coords[0], list):
        flat_co = [str(c) for co in coords for c in co]
    else:
        flat_co = map(str, coords)

    if len(flat_co) > 200:
        raise ValueError('"coords" incorrect! upper limits is 100.')
    else:
        iter_co = iter(flat_co)
        coords = ';'.join([','.join(ic) for ic in zip(iter_co, iter_co)])

    kwargs.update({'server_name': 'geoconv', 'version': 'v1',
                  'subserver_name': '', 'coords': coords})

    return client.get(kwargs)


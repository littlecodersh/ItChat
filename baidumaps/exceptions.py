# -*- coding: utf-8 -*-
# The MIT License (MIT)
# Copyright © 2015 Eli Song

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

messages = {'geoconv': {'1': '内部错误', '21': 'from非法', '22': 'to非法',
                        '24': 'coords格式非法', '25': 'coords个数非法，超过限制'},
            'directionroutematrix': {'1': '服务器内部错误', '2': '请求参数非法',
                                     '3': '权限校验失败', '4': '配额校验失败',
                                     '5': 'Ak不存在或者非法',
                                     '11': '起终点信息模糊',
                                     '12': '起点或者终点超过5个',
                                     '101': '服务禁用',
                                     '102': '不通过白名单或者安全码不对'},
            'locationip': {'200': 'APP不存在，AK有误请检查再重试',
                           '2': 'ip地址有误'},
            'direction': {'2': '参数错误', '5': '权限或配额校验失败'},
            'geocoder': {'1': '服务器内部错误', '2': '请求参数非法',
                         '3': '权限校验失败', '4': '配额校验失败',
                         '5': 'ak不存在或者非法', '101': '服务禁用',
                         '102': '不通过白名单或者安全码不对', '2xx': '无权限',
                         '3xx': '配额错误'},
            'placesuggestion': {'2': '请求参数非法', '3': '权限校验失败',
                                '4': '配额校验失败', '5': 'ak不存在或者非法',
                                '2xx': '无权限', '3xx': '配额错误'},
            'placesearch': {'2': '请求参数非法', '3': '权限校验失败',
                            '4': '配额校验失败', '5': 'ak不存在或者非法',
                            '2xx': '无权限', '3xx': '配额错误'},
            'placedetail': {'2': '请求参数非法', '3': '权限校验失败',
                            '4': '配额校验失败', '5': 'ak不存在或者非法',
                            '2xx': '无权限', '3xx': '配额错误'},
            'placeeventsearch': {'2': '请求参数非法', '3': '权限校验失败',
                                 '4': '配额校验失败', '5': 'ak不存在或者非法',
                                 '2xx': '无权限', '3xx': '配额错误'},
            'placeeventdetail': {'2': '请求参数非法', '3': '权限校验失败',
                                 '4': '配额校验失败', '5': 'ak不存在或者非法',
                                 '2xx': '无权限', '3xx': '配额错误'}}


class StatusError(Exception):

    def __init__(self, server_name, subserver_name, status):
        self.name = server_name + subserver_name
        self.status = str(status)

    def __str__(self):
        check_status = self.status in messages[self.name]
        if check_status:
            return "[status %s]: %s." % (self.status,
                                         messages[self.name][self.status])
        else:
            return "[status %s]: %s." % (self.status, '非官方文档所列的未知错误！')

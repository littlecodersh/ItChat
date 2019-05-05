def load_request(core):
    core.post_raw = post_raw
    core.get_raw = get_raw

def post_raw(self, headers={}, **kwargs):
    headers.setdefault('User-Agent', self.userAgent)
    return self.s.post(headers=headers, **kwargs)

def get_raw(self, headers={}, **kwargs):
    headers.setdefault('User-Agent', self.userAgent)
    return self.s.get(headers=headers, **kwargs)

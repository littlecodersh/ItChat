def load_error(core):
    core.error_register=error_register

def error_register(self,accept_all_errors):
    if not accept_all_errors:
        raise NotImplementedError()
    def register(fn):
        self.functionDict['Error'].append(fn)
    return register

from blinker import Namespace

_signals = Namespace()

scan_qr_code = _signals.signal('scan-qr-code')
confirm_login = _signals.signal('confirm-login')
logged_in = _signals.signal('logged-in')

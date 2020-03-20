#!/bin/python3.6
from flansible import app, config
import platform
import ssl

#Visual studio remote debugger
if platform.node() == 'mgmt':
    try:
        import ptvsd
        ptvsd.enable_attach(secret='my_secret', address = ('0.0.0.0', 3000))
    except:
        pass

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('/usr/local/etc/flansible/flansible_cert.cer', '/usr/local/etc/flansible/flansible_privkey.pem')
context.protocol = ssl.OP_NO_TLSv1 # prevents TLS 1.0
context.protocol = ssl.OP_NO_TLSv1_1 # prevents TLS 1.1
context.set_ciphers('HIGH:!3DES:!aNULL')


if __name__ == '__main__':
    app.run(ssl_context=context, debug=True, host=config.get("Default", "Flask_tcp_ip"), use_reloader=False, port=int(config.get("Default", "Flask_tcp_port")))

# -*- encoding:utf-8 -*-
# create by Administrator on 2018/7/18
from coapthon.server.coap import CoAP
from resource import BasicResource


class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('basic/', BasicResource())


def main():
    server = CoAPServer("0.0.0.0", 5683)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print "Server Shutdown"
        server.close()
        print "Exiting..."


if __name__ == '__main__':
    main()

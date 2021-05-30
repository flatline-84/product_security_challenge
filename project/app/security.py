from werkzeug.wrappers import Request, Response, ResponseStream
import ipaddress

from config import Config


class SecurityHardening():
    def __init__(
        self,
        app: "WSGIApplication",
    ):
        self.app = app

        # If someone fails login three times, you go on the naughty list
        self.naughty_list = {}
        self.naughty_counter = Config().naughty_counter

        # Allowed list of subnets
        self.allowed_subnet = Config().allowed_subnet

    def __call__(self, environ, start_response):

        # start_response(status, response_headers) <- how it's implemented
        request = Request(environ)
        response = Response(environ)

        ###

        # Login bruteforce blocker for requests
        if b'naughty' in request.query_string:
            # Add you into the naughty list
            if request.remote_addr not in self.naughty_list:
                self.naughty_list[request.remote_addr] = 0

            self.naughty_list[request.remote_addr] += 1
            print("added to naughty list %d" %
                  self.naughty_list[request.remote_addr])

        if request.remote_addr in self.naughty_list:
            if self.naughty_list[request.remote_addr] > self.naughty_counter:
                environ["PATH_INFO"] = '/blocked'
                # environ["REQUEST_URI"] = '/blocked'
                # environ["RAW_URI"] = '/'

        # If the IP address shouldn't be allowed in
        if ipaddress.ip_address(request.remote_addr) not in ipaddress.ip_network(self.allowed_subnet):
            environ["PATH_INFO"] = '/blocked'
            # environ["REQUEST_URI"] = '/blocked'
            # environ["RAW_URI"] = '/'

        data = self.app(environ, start_response)

        return data

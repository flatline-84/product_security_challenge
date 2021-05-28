from werkzeug.wrappers import Request, Response, ResponseStream

from pprint import pprint
import typing as t
import sys

class SecurityHardening():
    def __init__(
        self,
        app: "WSGIApplication",
    ):
        self.app = app
        # self._stream = stream

        # If someone fails login three times, you go on the naughty list
        self.naughty_list = {}
    
    def __call__(self, environ, start_response):

        # start_response(status, response_headers) <- how it's implemented
        request = Request(environ)
        response = Response(environ)

        response_body: t.List[bytes] = []
        def catching_start_response(status, headers, exc_info=None):  # type: ignore
            start_response(status, headers, exc_info)
            return response_body.append

        def runapp() -> None:
            app_iter = self._app(
                environ, t.cast("StartResponse", catching_start_response)
            )
            response_body.extend(app_iter)

            if hasattr(app_iter, "close"):
                app_iter.close()  # type: ignore


        body = b"".join(response_body)



        ### Bruteforce blocker for requests
        if b'naughty' in request.query_string:
            # Add you into the naughty list
            if request.remote_addr not in self.naughty_list:
                self.naughty_list[request.remote_addr] = 0

            self.naughty_list[request.remote_addr] += 1
            print("added to naughty list %d" % self.naughty_list[request.remote_addr])

        if request.remote_addr in self.naughty_list:
            if self.naughty_list[request.remote_addr] >= 3:
                environ["PATH_INFO"] = '/'
                environ["REQUEST_URI"] = '/'
                environ["RAW_URI"] = '/'

        # pprint(environ)
        # pprint(start_response())
        ### Do the hardening here

        # return [body]

        data = self.app(environ, start_response)

        return data
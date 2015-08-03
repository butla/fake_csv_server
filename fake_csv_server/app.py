import tornado.escape
import tornado.httpserver
import tornado.gen
import tornado.ioloop
import tornado.web


class FakeCsvHandler(tornado.web.RequestHandler):

    COLUMN_HEADERS = 'COL_0,COL_1,COL_2,COL_3,COL_4,COL_5,COL_6,COL_7\n'
    ONE_KILOBYTE_CHUNK = ''.join('000000000000000,111111111111111,222222222222222,333333333333333,444444444444444,'
                                 '555555555555555,666666666666666,777777777777777\n' for _ in range(8))

    @tornado.gen.coroutine
    def get(self, str_kilobyte_count):
        kilobyte_count = int(str_kilobyte_count)
        self._set_file_headers(kilobyte_count)

        self.write(self.COLUMN_HEADERS)
        for _ in range(kilobyte_count):
            self.write(self.ONE_KILOBYTE_CHUNK)
            yield self.flush()

    def _set_file_headers(self, size_in_kilobytes):
        num_bytes = size_in_kilobytes * 1024 + len(self.COLUMN_HEADERS)
        self.set_header('Content-Length', num_bytes)
        self.set_header('Content-type', 'text/csv')
        self.set_header('Content-disposition', 'attachment;filename={}_kilobytes.csv'.format(size_in_kilobytes))


def make_app():
    return tornado.web.Application([
        (r"/([0-9]+)", FakeCsvHandler),
    ])

if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(make_app())
    server.bind(9090)
    server.start(0)
    tornado.ioloop.IOLoop.current().start()

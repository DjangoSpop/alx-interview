import io
import sys
from unittest import TestCase
from unittest.mock import patch

from stats import parse_logs

class TestStats(TestCase):
    def test_parse_logs(self):
        logs = [
            '127.0.0.1 - GET /index.html 200 1024\n',
            '127.0.0.1 - POST /login 401 512\n',
            '127.0.0.1 - GET /about 200 2048\n',
            '127.0.0.1 - GET /contact 404 0\n',
            '127.0.0.1 - GET /index.html 200 512\n',
            '127.0.0.1 - GET /about 200 1024\n',
            '127.0.0.1 - POST /login 401 512\n',
            '127.0.0.1 - GET /contact 404 0\n',
            '127.0.0.1 - GET /index.html 200 1024\n',
            '127.0.0.1 - GET /about 200 2048\n',
            '127.0.0.1 - POST /login 401 512\n',
            '127.0.0.1 - GET /contact 404 0\n',
            '127.0.0.1 - GET /index.html 200 512\n',
            '127.0.0.1 - GET /about 200 1024\n',
            '127.0.0.1 - POST /login 401 512\n',
            '127.0.0.1 - GET /contact 404 0\n',
            '127.0.0.1 - GET /index.html 200 1024\n',
            '127.0.0.1 - GET /about 200 2048\n',
            '127.0.0.1 - POST /login 401 512\n',
            '127.0.0.1 - GET /contact 404 0\n',
        ]

        expected_output = [
            'Total file size: 20480',
            '200: 10',
            '301: 0',
            '400: 0',
            '401: 6',
            '403: 0',
            '404: 4',
            '405: 0',
            '500: 0',
        ]

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            sys.stdin = io.StringIO(''.join(logs))
            parse_logs()
            output = fake_out.getvalue().strip().split('\n')

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
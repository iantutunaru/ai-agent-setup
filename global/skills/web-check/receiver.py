"""Local helper for web-check: gives the page measure.js and saves what the page sends back as files.

    python -I receiver.py <folder to save into> [port]

    GET  /measure.js     this folder's measure.js, never cached
    POST /save/<name>    writes the body to <folder>/<name> (letters, digits, dot and dash only)

Bound to 127.0.0.1 only. Results go from the page straight to files, so they do not pass through the chat.
Stop it when the measuring is done.
"""
import re
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(sys.argv[1])
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 8765
OUT.mkdir(parents=True, exist_ok=True)


class Handler(BaseHTTPRequestHandler):
    def _head(self, status, kind=None):
        self.send_response(status)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-store")
        if kind:
            self.send_header("Content-Type", kind)
        self.end_headers()

    def do_GET(self):
        if self.path.split("?")[0] == "/measure.js":
            self._head(200, "application/javascript; charset=utf-8")
            self.wfile.write((HERE / "measure.js").read_bytes())
        else:
            self._head(404)

    def do_POST(self):
        name = re.fullmatch(r"/save/([A-Za-z0-9.\-]+)", self.path)
        if not name:
            self._head(400)
            return
        body = self.rfile.read(int(self.headers.get("Content-Length", "0")))
        (OUT / name.group(1)).write_bytes(body)
        self._head(200, "text/plain")
        self.wfile.write(str(len(body)).encode())

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print(f"web-check receiver on http://127.0.0.1:{PORT}, saving into {OUT}", flush=True)
    HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()

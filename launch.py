from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path
import threading
import webbrowser

root = Path(__file__).resolve().parent
handler = partial(SimpleHTTPRequestHandler, directory=str(root))
try:
    server = ThreadingHTTPServer(("127.0.0.1", 8000), handler)
except OSError:
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
url = "http://127.0.0.1:%d/index.html" % server.server_port
print("ClearSky Tower:", url)
print("Keep this window open. Press Ctrl+C to stop.")
threading.Timer(0.5, lambda: webbrowser.open(url)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()

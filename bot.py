import os
import logging
from threading import Thread
from web import app

# ---------------------------
# FLASK SERVER (SEPARATE)
# ---------------------------
def run_flask():
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False
    )

# Run Flask in background (daemon thread)
Thread(target=run_flask, daemon=True).start()

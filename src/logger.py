# src/logger.py
import os, logging, sys

os.makedirs("logs", exist_ok=True)

class SafeStreamHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            super().emit(record)
        except UnicodeEncodeError:
            # fallback: strip non-encodable chars
            msg = self.format(record).encode(self.stream.encoding, errors="ignore").decode(self.stream.encoding)
            self.stream.write(msg + self.terminator)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] → %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log", encoding="utf-8"),
        SafeStreamHandler(sys.stdout),
    ]
)

logger = logging.getLogger("AgentLogger")

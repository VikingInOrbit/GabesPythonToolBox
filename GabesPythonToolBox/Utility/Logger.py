import csv
import os
from datetime import datetime


class Logger:
    # simplified names
    path = None
    encoding = None
    first_write = True
    headers = [
        "message",
        "message_type",
        "group",
        "filename",
        "filepath",
        "lineno",
        "timestamp",
    ]

    @classmethod
    def start_logger(cls, file_path: str = "", character_encoding: str = "utf-8"):
        import csv
        import os
        from datetime import datetime

        # Default folder if no path is provided
        if not file_path:
            file_path = "log/"

        # If only a directory is provided (no basename) generate unique filename
        if not os.path.basename(file_path):
            unique_id = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = os.path.join(file_path, f"log_{unique_id}.csv")

        cls.path = os.path.abspath(file_path)
        cls.encoding = character_encoding

        # Ensure the directory exists
        os.makedirs(os.path.dirname(cls.path), exist_ok=True)

        # Initialize CSV with headers if file doesn't exist
        if not os.path.exists(cls.path):
            with open(cls.path, mode="w", encoding=cls.encoding, newline="") as f:
                writer = csv.DictWriter(f, fieldnames=cls.headers)
                writer.writeheader()

        cls.first_write = False

    @classmethod
    def save_to_file(cls, data: list[dict]):
        from ..Suporting.csvWriterLogger import write_csv

        first_write = not cls.first_write
        mode = "w" if first_write else "a"
        data_mode = "all" if first_write else "body"
        write_csv(cls.path, data=data, mode=mode, data_mode=data_mode)
        cls.first_write = True

    @classmethod
    def log(
        cls, message: str, message_type: str = "-", group: str = None, verbose=None
    ):
        """Log one message entry"""
        if cls.path is None:
            raise RuntimeError("Logger not started. Call start_logger first.")

        # support None/partial verbose objects
        filename = getattr(verbose, "filename", "") if verbose is not None else ""
        filepath = os.path.dirname(filename) if filename else ""
        fname = os.path.basename(filename) if filename else ""
        lineno = getattr(verbose, "lineno", 0) if verbose is not None else 0

        entry = {
            "message": message,
            "message_type": message_type,
            "group": group or "",
            "filename": fname,
            "filepath": filepath,
            "lineno": lineno,
            "timestamp": datetime.now().isoformat(),
        }

        cls.save_to_file([entry])

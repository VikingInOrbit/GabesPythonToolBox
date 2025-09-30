import os 
from datetime import datetime 
import csv

class Logger:
    file_path = None
    file_encoding = None
    first_write_done = True
    headers = ["message", "message_type", "group", "filename", "filepath", "lineno", "timestamp"]

    @classmethod
    def start_logger(cls, file_path: str = "", character_encoding: str = 'utf-8'):
        import csv
        from datetime import datetime
        import os
    
        # Default folder if no path is provided
        if not file_path:
            file_path = "log/"
    
        # If only a directory is provided, generate unique filename
        if not os.path.basename(file_path):
            unique_id = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = os.path.join(file_path, f"log_{unique_id}.csv")
    
        cls.file_path = os.path.abspath(file_path)
        cls.file_encoding = character_encoding
    
        # Ensure the directory exists
        os.makedirs(os.path.dirname(cls.file_path), exist_ok=True)
    
        # Initialize CSV with headers if file doesn't exist
        if not os.path.exists(cls.file_path):
            with open(cls.file_path, mode="w", encoding=cls.file_encoding, newline="") as f:
                writer = csv.DictWriter(f, fieldnames=cls.headers)
                writer.writeheader()
    
        cls.first_write_done = False


    @classmethod
    def save_to_file(cls, data: list[dict]):
        from ..Suporting.csvWriterLogger import write_csv
        first_write = not cls.first_write_done
        mode = "w" if first_write else "a"
        data_mode = "all" if first_write else "body"
        write_csv(cls.file_path, data=data, mode=mode, data_mode=data_mode)
        cls.first_write_done = True


    @classmethod
    def log(cls, message: str, message_type: str = "-", group: str = None, verbose=None):
        """Log one message entry"""
        if cls.file_path is None:
            raise RuntimeError("Logger not started. Call start_logger first.")

        entry = {
            "message": message,
            "message_type": message_type,
            "group": group or "",
            "filename": os.path.basename(verbose.filename),
            "filepath": os.path.dirname(verbose.filename),
            "lineno": verbose.lineno,
            "timestamp": datetime.now().isoformat()
        }

        cls.save_to_file([entry])

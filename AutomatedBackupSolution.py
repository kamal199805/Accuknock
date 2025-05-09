import os
import tarfile
import subprocess
import logging
from datetime import datetime

# === Configuration ===
SOURCE_DIR = "/path/to/your/directory"  # Directory to back up
BACKUP_NAME = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.tar.gz"
REMOTE_USER = "your_user"
REMOTE_HOST = "your.remote.server"
REMOTE_DIR = "/remote/backup/path/"
LOG_FILE = "backup_report.log"

# === Logging Setup ===
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_backup(source, backup_file):
    try:
        with tarfile.open(backup_file, "w:gz") as tar:
            tar.add(source, arcname=os.path.basename(source))
        logging.info(f"Backup archive created: {backup_file}")
        return True
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        return False

def send_to_remote(backup_file):
    try:
        remote_path = f"{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIR}"
        result = subprocess.run(["scp", backup_file, remote_path], check=True)
        logging.info(f"Backup transferred to {remote_path}")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to transfer backup: {e}")
        return False

if __name__ == "__main__":
    print(f"\nStarting backup: {datetime.now()}")
    if create_backup(SOURCE_DIR, BACKUP_NAME):
        if send_to_remote(BACKUP_NAME):
            print("✅ Backup successful and transferred.")
        else:
            print("⚠️ Backup created, but transfer failed.")
    else:
        print("❌ Backup failed.")

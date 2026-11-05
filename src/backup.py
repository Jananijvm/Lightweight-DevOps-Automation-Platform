
import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKUP_DIR = os.path.join(PROJECT_ROOT, "backups")


def create_backup():
    os.makedirs(BACKUP_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(
        BACKUP_DIR,
        f"devops_platform_{timestamp}.sql"
    )

    command = [
        "mysqldump",
        "--no-tablespaces",
        "--single-transaction",
        "-h", os.getenv("DB_HOST"),
        "-P", os.getenv("DB_PORT", "3306"),
        "-u", os.getenv("DB_USER"),
        f"--result-file={backup_file}",
        os.getenv("DB_NAME")
    ]

    env = os.environ.copy()
    env["MYSQL_PWD"] = os.getenv("DB_PASSWORD", "")

    try:
        subprocess.run(command, env=env, check=True)
        print("Database backup created successfully!")
        print("Backup file:", backup_file)

    except subprocess.CalledProcessError as error:
        print("Database backup failed:", error)


if __name__ == "__main__":
    create_backup()

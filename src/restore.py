
import os
import subprocess
from dotenv import load_dotenv

load_dotenv()
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_NAME:", os.getenv("DB_NAME"))

def restore_backup(backup_file):
    if not os.path.isfile(backup_file):
        print("Backup file not found!")
        return

    command = [
        "mysql",
        "-h", os.getenv("DB_HOST"),
        "-P", os.getenv("DB_PORT", "3306"),
        "-u", os.getenv("DB_USER"),
        os.getenv("RESTORE_DB_NAME", "devops_restore_test")
    ]

    env = os.environ.copy()
    env["MYSQL_PWD"] = os.getenv("DB_PASSWORD", "")

    try:
        with open(backup_file, "rb") as sql_file:
            print("Restore command:", command)
            subprocess.run(
                command,
                stdin=sql_file,
                env=env,
                check=True
            )

        print("Database restored successfully!")

    except subprocess.CalledProcessError as error:
        print("Database restoration failed:", error)


if __name__ == "__main__":
    restore_backup(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "backups",
            "devops_platform_20261031_101113.sql"
        )
    )

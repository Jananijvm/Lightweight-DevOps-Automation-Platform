import os

from src.database import get_db_connection
from src.activation import activate_release


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rollback_release():
    connection = get_db_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT version
                FROM deployment_logs
                WHERE application_name = %s
                AND status = 'SUCCESS'
                ORDER BY deployed_at DESC
                LIMIT 1 OFFSET 1
            """, ("DevOps Automation Platform",))

            previous_deployment = cursor.fetchone()

        if not previous_deployment:
            print("No previous successful deployment found.")
            return

        previous_version = previous_deployment["version"]

        release_path = os.path.join(
            PROJECT_ROOT, "releases", previous_version
        )

        if not os.path.isdir(release_path):
            print(f"Rollback failed: Release {previous_version} does not exist.")
            return

        print("Rolling back to version:", previous_version)

        activate_release(previous_version)

    except Exception as error:
        print("Rollback failed:", error)

    finally:
        connection.close()


if __name__ == "__main__":
    rollback_release()
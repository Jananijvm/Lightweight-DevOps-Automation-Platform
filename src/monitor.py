from src.database import get_db_connection


def check_latest_deployment():
    connection = get_db_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT application_name, version, status, commit_id, deployed_at
                FROM deployment_logs
                ORDER BY deployed_at DESC
                LIMIT 1
            """)

            deployment = cursor.fetchone()

            if deployment is None:
                print("No deployment records found.")
                return

            print("Latest Deployment:")
            print("Application:", deployment["application_name"])
            print("Version:", deployment["version"])
            print("Status:", deployment["status"])
            print("Commit ID:", deployment["commit_id"])
            print("Deployed At:", deployment["deployed_at"])

            if deployment["status"] == "SUCCESS":
                print("Deployment check: Healthy")
            else:
                print("Deployment check: Failed")

    except Exception as error:
        print("Monitoring failed:", error)

    finally:
        connection.close()


if __name__ == "__main__":
    check_latest_deployment()
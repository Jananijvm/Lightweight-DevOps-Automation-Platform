from src.database import get_db_connection
from src.git_manager import get_current_commit

def record_deployment(application_name, version, status):
    connection = get_db_connection()
    commit_id = get_current_commit()

    try:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO deployment_logs
                (application_name, version, status, commit_id)
                VALUES (%s, %s, %s, %s)
            """

            cursor.execute(
                sql,
                (application_name, version, status, commit_id)
            )

        connection.commit()
        print("Deployment record saved successfully!")

    except Exception as error:
        connection.rollback()
        print("Failed to save deployment:", error)

    finally:
        connection.close()

def get_deployment_history():
    connection = get_db_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, application_name, version, status, commit_id, deployed_at
                FROM deployment_logs
                ORDER BY deployed_at DESC
            """)
            deployments = cursor.fetchall()

            for deployment in deployments:
                print(deployment)

    except Exception as error:
        print("Failed to retrieve deployment history:", error)

    finally:
        connection.close()

if __name__ == "__main__":
    record_deployment("Worker-Finder", "1.0.1", "SUCCESS")

    print("\nDeployment History:")
    get_deployment_history()
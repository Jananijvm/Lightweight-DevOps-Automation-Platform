from src.database import get_db_connection

try:
    connection = get_db_connection()

    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS deployment_logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                application_name VARCHAR(100) NOT NULL,
                version VARCHAR(50) NOT NULL,
                status VARCHAR(30) NOT NULL,
                deployed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

    connection.commit()
    print("deployment_logs table created successfully!")

except Exception as error:
    print("Table creation failed:", error)

finally:
    if 'connection' in locals():
        connection.close()
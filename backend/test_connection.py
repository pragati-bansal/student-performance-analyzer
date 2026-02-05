from db_config import get_connection

def test_db_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        print("✅ Database connection successful!")
        print("📂 Tables in database:")
        for table in tables:
            print(table[0])

        cursor.close()
        conn.close()

    except Exception as e:
        print("❌ Database connection failed")
        print("Error:", e)


if __name__ == "__main__":
    test_db_connection()

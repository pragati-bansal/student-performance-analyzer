from db_config import get_connection
import csv


# ---------- DATA FETCHING ----------

def fetch_all_performance():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student_subject_performance;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


def fetch_weak_subjects(threshold):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT *
    FROM student_subject_performance
    WHERE avg_percentage < %s;
    """
    cursor.execute(query, (threshold,))
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


# ---------- ANALYSIS LOGIC ----------

def performance_label(avg_percentage):
    avg = float(avg_percentage)
    if avg >= 75:
        return "Excellent"
    elif avg >= 50:
        return "Average"
    else:
        return "Weak"
    

def fetch_student_performance(student_name):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT *
    FROM student_subject_performance
    WHERE student_name = %s;
    """
    cursor.execute(query, (student_name,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data

def fetch_top_performers(limit=3):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT student_name,
           ROUND(AVG(avg_percentage), 2) AS overall_avg
    FROM student_subject_performance
    GROUP BY student_name
    ORDER BY overall_avg DESC
    LIMIT %s;
    """
    cursor.execute(query, (limit,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data


def export_to_csv(filename, data):
    if not data:
        print("❌ No data to export")
        return

    headers = data[0].keys()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ CSV file created: {filename}")


# ---------- MENU ----------

def show_menu():
    print("\n📊 Student Performance Analyzer")
    print("1. View all student performance")
    print("2. View weak subjects")
    print("3. View performance of a specific student")
    print("4. View top performers")
    print("5. Export last result to CSV")
    print("6. Exit")


# ---------- MAIN ----------

if __name__ == "__main__":
    last_data = []

    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3/4/5/6): ").strip()

        if choice == "1":
            data = fetch_all_performance()
            last_data = data

            print("\n📊 All Student Performance:\n")
            for row in data:
                label = performance_label(row["avg_percentage"])
                print(
                    f"{row['student_name']} | {row['subject_name']} | "
                    f"{row['avg_percentage']}% | {label}"
                )

        elif choice == "2":
            threshold = int(input("Enter threshold percentage: ").strip())
            data = fetch_weak_subjects(threshold)
            last_data = data


            print(f"\n⚠️ Weak Subjects (Below {threshold}%):\n")
            if not data:
                print("No weak subjects found 🎉")

            for row in data:
                label = performance_label(row["avg_percentage"])
                print(
                    f"{row['student_name']} | {row['subject_name']} | "
                    f"{row['avg_percentage']}% | {label}"
                )
        elif choice == "3":
            name = input("Enter student name: ").strip()
            data = fetch_student_performance(name)
            last_data = data


            if not data:
                print("No data found for this student ❌")
                continue

            print(f"\n📘 Performance for {name}:\n")
            for row in data:
                label = performance_label(row["avg_percentage"])
                print(
                f"{row['subject_name']} | {row['avg_percentage']}% | {label}"
            )
        elif choice == "4":
            top = fetch_top_performers()
            last_data = data

            print("\n🏆 Top Performers:\n")
            for row in top:
                print(f"{row['student_name']} | {row['overall_avg']}%")

        elif choice == "5":
            filename = input("Enter CSV filename (example: output.csv): ").strip()
            export_to_csv(filename, last_data)

        elif choice == "5":
            print("👋 Exiting Analyzer")
            break


        else:
            print("❌ Invalid choice. Try again.")



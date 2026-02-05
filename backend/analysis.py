from db_config import get_connection

def get_student_subject_performance():
    """
    Fetch average performance per student per subject
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM student_subject_performance;"
    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data


def get_weak_subjects(threshold=40):
    """
    Identify weak subjects based on average percentage
    """
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


if __name__ == "__main__":
    print("📊 Student Subject Performance:")
    performance = get_student_subject_performance()
    for row in performance:
        print(row)

    print("\n⚠️ Weak Subjects:")
    weak_subjects = get_weak_subjects(50)
    for row in weak_subjects:
        print(row)

def get_performance_label(avg_percentage):
    avg = float(avg_percentage)

    if avg >= 75:
        return "Excellent"
    elif avg >= 50:
        return "Average"
    else:
        return "Weak"
        
if __name__ == "__main__":
    print("📊 Student Subject Performance:\n")
    performance = get_student_subject_performance()

    for row in performance:
        label = get_performance_label(row["avg_percentage"])
        print(
            f"{row['student_name']} | {row['subject_name']} | "
            f"{row['avg_percentage']}% | {label}"
        )

    print("\n⚠️ Weak Subjects:\n")
    weak_subjects = get_weak_subjects(50)

    for row in weak_subjects:
        label = get_performance_label(row["avg_percentage"])
        print(
            f"{row['student_name']} | {row['subject_name']} | "
            f"{row['avg_percentage']}% | {label}"
        )


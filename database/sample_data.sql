INSERT INTO students (name, class, section) VALUES
('Aarav Sharma', '10', 'A'),
('Ananya Verma', '10', 'B');

INSERT INTO subjects (subject_name) VALUES
('Mathematics'),
('Physics'),
('Computer Science');

INSERT INTO marks (student_id, subject_id, test_name, marks_obtained, max_marks, exam_date) VALUES
(1, 1, 'Midterm', 78, 100, '2024-09-15'),
(1, 2, 'Midterm', 62, 100, '2024-09-16'),
(2, 1, 'Midterm', 45, 100, '2024-09-15'),
(2, 3, 'Midterm', 88, 100, '2024-09-17');

INSERT INTO attendance (student_id, subject_id, total_classes, attended_classes) VALUES
(1, 1, 50, 45),
(1, 2, 50, 38),
(2, 1, 50, 30),
(2, 3, 50, 48);



import csv


def read_csv_file(file):
    list_exam = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list_exam.append(row)
    return list_exam


def create_csv_file(file_data, file_name):
    fieldnames = ['Exam Name', 'Number of Candidates', 'Number of Passed Exams',
                  'Number of Failed Exams', 'Best Score', 'Worst Score']
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(fieldnames)
        for key, value in file_data.items():
            writer.writerow(value.values())
            print(value)



def make_report(file):
    list_report = {}
    for row in file:
        exam_name = row.get('Exam Name')
        score = int(row.get('Score'))
        grade = row.get('Grade')
        if exam_name in list_report:
            number_of_candidates = list_report.get(exam_name).get('number_of_candidates') + 1
            if grade == 'Pass':
                number_of_passed = list_report.get(exam_name).get('number_of_passed') + 1
            else:
                number_of_passed = list_report.get(exam_name).get('number_of_passed')
            if grade == 'Fail':
                number_of_failed = list_report.get(exam_name).get('number_of_failed') + 1
            else:
                number_of_failed = list_report.get(exam_name).get('number_of_failed')
            if score > list_report.get(exam_name).get('best_score'):
                best_score = score
            else:
                best_score = list_report.get(exam_name).get('best_score')
            if score < list_report.get(exam_name).get('worst_score'):
                worst_score = score
            else:
                worst_score = list_report.get(exam_name).get('worst_score')
            list_report.update({exam_name: {
                'exam_name': exam_name,
                'number_of_candidates': number_of_candidates,
                'number_of_passed': number_of_passed,
                'number_of_failed': number_of_failed,
                'best_score': best_score,
                'worst_score': worst_score
            }})
        else:
            list_report.update({exam_name: {
                'exam_name': exam_name,
                'number_of_candidates': 1,
                'number_of_passed': 1 if grade == 'Pass' else 0,
                'number_of_failed': 1 if grade == 'Fail' else 0,
                'best_score': score,
                'worst_score': score
            }})
    return list_report


list_exam = read_csv_file('exam_results.csv')
report = make_report(list_exam)
create_csv_file(report, 'report.csv')

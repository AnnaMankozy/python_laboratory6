#Манько Анна КН-41/2
students = {
    "Іваненко Петро Петрович": {
        "група": "П-21",
        "курс": 2,
        "предмети": {"Вища математика": 85, "Програмування": 90, "Англійська": 78, "Предмет за вибором": 90},
        "адреса": "м. Київ, вул. Хрещатик, буд. 15, кв. 2",
        "номер телефону": "+38093123456",
        "форма фінансування": "Бюджет",
        "форма навчання": "Денна"
    },
    "Коваленко Олена Ігорівна": {
        "група": "П-21",
        "курс": 2,
        "предмети": {"Вища математика": 92, "Програмування": 88, "Англійська": 84, "Предмет за вибором": 88},
        "адреса": "м. Львів, вул. Шевченка, буд. 101, кв. 12",
        "номер телефону": "+380671112233",
        "форма фінансування": "Бюджет",
        "форма навчання": "Заочна"
    },
    "Мельник Анна Сергіївна": {
        "група": "П-21",
        "курс": 2,
        "предмети": {"Вища математика": 70, "Програмування": 95, "Англійська": 68, "Предмет за вибором": 69},
        "адреса": "м. Одеса, вул. Дерибасівська, буд. 7, кв. 45",
        "номер телефону": "+380501234890",
        "форма фінансування": "Бюджет",
        "форма навчання": "Денна"
    }
}

#Манько Анна КН-41/2
def print_students(database):
    for student_name, student_info in database.items():
        print(f"\nСтудент: {student_name}")
        print(f"  Група: {student_info['група']}")
        print(f"  Курс: {student_info['курс']}")
        print("  Предмети та оцінки:")
        for subject_name, subject_grade in student_info['предмети'].items():
            print(f"    - {subject_name}: {subject_grade}")
        print(f"  Адреса: {student_info['адреса']}")
        print(f"  Номер телефону: {student_info['номер телефону']}")
        print(f"  Форма фінансування: {student_info['форма фінансування']}")
        print(f"  Форма навчання: {student_info['форма навчання']}")

#Манько Анна КН-41/2
def add_student(database, student_name, student_group, student_course, student_subjects, student_address, student_numer_of_phone, student_form_of_financing, student_form_of_study):
    database[student_name] = {
        "група": student_group,
        "курс": student_course,
        "предмети": student_subjects,
        "адреса": student_address,
        "номер телефону": student_numer_of_phone,
        "форма фінансування": student_form_of_financing,
        "форма навчання": student_form_of_study
    }
    print(f"Студента {student_name} додано до бази даних.")

# Функція Снаговської Дар'ї КН-41/2 (видалення студента) 
def delete_student(database, student_name):
    if student_name in database:
        del database[student_name]
        print(f"Студента {student_name} видалено.")
    else:
        print("Студента не знайдено!")

# Функція Братушки Ксенії КН-41/2 (обчислення середнього балу студента)
def average_grade(database, student_name):
    if student_name not in database:
        print("Студента не знайдено!")
        return
    grades = database[student_name]["предмети"].values()
    avg = sum(grades) / len(grades)
    print(f"Середній бал студента {student_name}: {avg:.2f}")    

#Спільні зміни в основному меню
while True:
    print("\nМеню:")
    print("Вивести усіх студентів -> 1 <-")
    print("Додати нового студента -> 2 <-")
    print("Видалити студента із записів -> 3 <-")
    print("Порахувати середній бал студента -> 4 <-")
    print("Вийти з програми -> 0 <-")

    choice = input("Введіть пункт меню: ")

    if choice == "1":
        print_students(students)

    elif choice == "2":
        name = input("Введіть ПІБ студента: ")
        group = input("Введіть групу: ")
        
        while True:
            try:
                course = int(input("Введіть курс: "))
                break
            except ValueError:
                print("Введіть ціле число для курсу!")

        default_subjects = ["Вища математика", "Програмування", "Англійська", "Предмет за вибором"]
        subjects = {}

        print("Введіть оцінки з кожного предмета:")
        for subject in default_subjects:
            while True:
                try:
                    grade = int(input(f"{subject}: "))
                    if 0 <= grade <= 100:
                        subjects[subject] = grade
                        break
                    else:
                        print("Оцінка має бути від 0 до 100.")
                except ValueError:
                    print("Введіть ціле число!")
                    
        address=input("Введіть адресу: ")
        numer_of_phone=input("Введіть номер телефону: ")
        form_of_financing=input("Введіть форму фінансування: ")
        form_of_study=input("Введіть форму навчання: ")
        add_student(students, name, group, course, subjects, address, numer_of_phone,form_of_financing,form_of_study)

    elif choice == "3":
        name = input("Введіть ПІБ студента для видалення: ")
        delete_student(students, name)

    elif choice == "4":
        name = input("Введіть ПІБ студента: ")
        average_grade(students, name)
    
    elif choice == "0":
        print("Вихід із програми...")
        break

    else:
        print("Невірний вибір, спробуйте ще раз!")
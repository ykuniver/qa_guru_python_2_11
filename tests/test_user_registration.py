from demoqa_tests.model.application import app

from tests.test_data.users import student

# FluentPageObject with no StepsObject
def test_submit_student():
    (
        # GIVEN

        app.registration_form.given_opened()

        # WHEN

        .set_full_name(student.name, student.last_name)
        .set_email(student.email)
        .set_gender(student.gender)
        .set_phone_number(student.user_number)
        .set_birth_date(student.birth_year, student.birth_month, student.birth_day)
        .add_subjects(student.subjects)
        .add_hobbies(student.hobbies)
        .upload_picture(student.picture_file)
        .set_current_address(student.current_address)
        .scroll_to_bottom()
        .set_state(student.state)
        .set_city(student.city)
        .submit_form()

        # THEN

        .should_have_submitted(
            [
                ('Student Name', f'{student.name} {student.last_name}'),
                ('Student Email', student.email),
                ('Gender', student.gender.value),
                ('Mobile', student.user_number),
                ('Date of Birth', f'{student.birth_day} {student.birth_month},{student.birth_year}'),
                ('Subjects', app.registration_form.get_subject_list(student.subjects)),
                ('Hobbies', app.registration_form.get_hobby_list(student.hobbies)),
                ('Picture', student.picture_file),
                ('Address', student.current_address),
                ('State and City', f'{student.state} {student.city}')
            ],
        )
    )


# StepsObject
def test_register_user():
    app.user_operations.register()

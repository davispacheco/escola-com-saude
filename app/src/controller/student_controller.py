# Este arquivo faz a ponte entre a view, o model e o service.

from src.model.student_model import \
    StudentModel
from src.service.student_service import \
    StudentService
from src.view.student_view import \
    StudentView


class StudentController:
    def __init__(self):
        self.service = StudentService()
        self.view = StudentView(self)

    def add_student(self, nome, idade, peso, altura, estado_saude):
        student = StudentModel(nome, idade, peso, altura, estado_saude)
        self.service.add_student(student)

    def process_data(self):
        return self.service.process_data()

    def run(self):
        self.view.mainloop()


if __name__ == '__main__':
    controller = StudentController()
    controller.run()

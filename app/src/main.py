# Este é o ponto de entrada do programa.

from src.controller.student_controller import StudentController

if __name__ == '__main__':
    controller = StudentController()
    controller.run()
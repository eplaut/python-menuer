'''

Menuer is a simple CLI module, helps to create a stable list-like menus

With easy to use API, you can arrange your functions into menus and get usable
command line application.

Example:

    import menuer

    class Student(object):
        def __init__(self):
            super(Student, self).__init__()
            self.grades = []

        @menuer.option
        def add_grade(self):
            course = raw_input('Enter course name: ')
            grade  = raw_input('Enter final grade: ')
            self.grades.append((course, grade))

        @menuer.option
        def print_transcript(self):
            if len(self.grades) == 0:
                raise menuer.InvalidOptionError('There are no grades to show')
            sum = 0
            for course, grade in self.grades:
                print('{}: {}'.format(course, grade))
                sum += int(grade)
            print('---------------\n'
                  'TOTAL: {}'.format(sum/len(self.grades))

    if __name__ == "__main__":
        menuer.run(Student())

'''
import time

try:
    input = raw_input
except NameError:
    # python3
    pass


class QuitMenuer(Exception):
    pass


class InvalidOptionError(Exception):
    pass


class Menuer(object):
    def __init__(self):
        super(Menuer, self).__init__()
        self.options = []

    @staticmethod
    def quit():
        raise QuitMenuer()

    def option(self, func):
        assert callable(func)
        self.options.append(func)

        return func

    def run(self, obj_instance, handle_exceptions=True):
        while True:
            try:
                print('')  # print new line
                option_format = '{}. {}'.format
                options_count = len(self.options)
                i = 0
                for i in range(options_count):
                    option_name = self.options[i].__name__
                    print(option_format(i+1, option_name.title()))
                print(option_format(i+2, 'Quit'))
                prompt = 'Enter your choice [1-{}] '
                choice = int(input(prompt.format(options_count+1))) - 1
                if choice == options_count:
                    self.quit()
                elif choice in range(options_count):
                    self.options[choice](obj_instance)
                else:
                    raise InvalidOptionError
            except InvalidOptionError as exc:
                print('Invalid option')
                print(str(exc))
            except QuitMenuer:
                print('bye')
                break
            except:
                if not handle_exceptions:
                    raise
            time.sleep(0.3)

_menuer = Menuer()
option = _menuer.option
run = _menuer.run
quit = _menuer.quit

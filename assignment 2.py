
def decorate(func):
    def wrapper(report):
        print(" report ")
        func(report)
        print("report")
    return wrapper


class Report:
    templates = []

    def __init__(self, title, content, template):
        self.title = title
        self.content = content
        self.template = template

    classmethod
    def add_template(cls, name):
        cls.templates.append(name)

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nTemplate: {self.template}"


decorate
def display(report):
    print(report)


# Main
Report.add_template("Academic")

r = Report("Student Report", "Neelam scored 90%", "Academic")

display(r)
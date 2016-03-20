from model import LoginPage


def test(app):
   projects =  app.soap.get_available_projects(LoginPage("administrator", "root"))
   print(projects[0])
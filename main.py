import tkinter as tk
import subprocess
import os

values = {"add_first_status": False, "add_second_status": False}

def right_directory():
    if os.getcwd().endswith("gitcourse"):
        return True
    else:
        return False


def is_repository():
    if ".git" in os.listdir(os.getcwd()):
        return True
    else:
        return False


def maintxt_exists():
    if "main.txt" in os.listdir(os.getcwd()):
        return True
    else:
        return False


def mainlog_exists():
    if "main.log" in os.listdir(os.getcwd()):
        return True
    else:
        return False



########################################################################################################################
#                                                   Page Classes                                                       #
########################################################################################################################


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class Introduction(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)


class Requirements(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

            if command == "git --version":

                if os.system(command) == 0:
                    task['bg'] = '#6b9e1f'
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                else:
                    output['text'] = "Es scheint kein Git installiert zu sein."

            else:
                output['text'] = "Bitte prüfe Rechtschreibung und Syntax des Befehls."

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Softwarevoraussetzungen", bg="#fff")
        title.place(x=0, y=0)

        task = tk.Label(description_container, text="Prüfe, ob Git installiert ist.", bg="#fff")
        task.place(x=0, y=175)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class GeneralStructure(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack()


class LocalStructure(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Basic commands")
        label.pack()


class RemoteStructure(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Basic commands")
        label.pack()


class NewProject(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

            if command == "mkdir gitcourse":
                if os.system(command) == 0:
                    output['text'] = "Das Verzeichnis 'gitcouse' wurde angelegt."
                    task1['bg'] = '#6b9e1f'
                elif os.system(command) == 256:
                    output['text'] = "Das Projekt wurde bereits angelegt."
                    task1['bg'] = '#6b9e1f'
                else:
                    output['text'] = "Bitte überprüfe deine Syntax!"
            elif command == "cd gitcourse":
                try:
                    os.chdir("gitcourse")
                    output['text'] = "Gewechselt in da Verzeichnis 'gitcourse'. Du befindet dich jetzt hier: {}".format(subprocess.check_output("pwd"))
                    task2['bg'] = '#6b9e1f'
                except:
                    if right_directory():
                        output['text'] = "Du befindest dich bereits im gitcourse-Projektordner."
                    else:
                        output['text'] = "Bist du sicher, dass du einen Projektordner namens 'gitcourse' angelegt hast?"

            else:
                output['text'] = "Bitter überprüfe die Synatx und die Rechtschreibung."

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Ein neues Projekt", bg="#fff")
        title.place(x=0, y=0)

        task1 = tk.Label(description_container, text="Lege einen neuen Projektordner mit dem Name 'gitcourse' an.", bg="#fff")
        task1.place(x=0, y=175)
        task2 = tk.Label(description_container, text="Wechlse in den angelegten Projektordner 'gitcourse'.",
                         bg="#fff")
        task2.place(x=0, y=195)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class InitializeRepo(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

            if right_directory():
                if command == "git init":
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task1['bg'] = '#6b9e1f'
                elif command == "ls -al":
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task2['bg'] = '#6b9e1f'
                else:
                    output['text'] = "Bitte überprüfe die Syntax und die Rechtschreibung."
            else:
                output['text'] = "Du befindest dich nicht im 'gitcourse-Projektordner!\n " \
                                 "Gehe zurück zum vorherigen Schritt und erledige die dort gestellten Aufgaben."

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Ein Git-Repository anlegen", bg="#fff")
        title.place(x=0, y=0)

        task1 = tk.Label(description_container, text="Lege ein Git-Repository an", bg="#fff")
        task1.place(x=0, y=175)
        task2 = tk.Label(description_container, text="Lass dir den Inhalt des Projektordners anzeigen.", bg="#fff")
        task2.place(x=0, y=195)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class ConfigGit(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

            if os.getcwd().endswith("gitcourse"):
                if ".git" in os.listdir(os.getcwd()):
                    if command.startswith("git config --global user.name"):
                        response = subprocess.check_output(command, shell=True)
                        output['text'] = response
                        task1['bg'] = '#6b9e1f'
                    elif command.startswith("git config --global user.mail"):
                        response = subprocess.check_output(command, shell=True)
                        output['text'] = response
                        task2['bg'] = '#6b9e1f'
                    elif command == "git config --list":
                        response = subprocess.check_output(command, shell=True)
                        output['text'] = response
                        task3['bg'] = '#6b9e1f'
                    else:
                        output['text'] = "Bitte überprüfe deine Syntax und Rechtschreibung!"
                else:
                    output['text'] = "Du hast noch kein Repository im gitcourse-Projektordner angelegt. \n " \
                                     "Bitte gehe zurück zum vorherigen Schritt und bearbeite die dortigen Aufgaben."
            else:
                output['text'] = "Du befindest dich nicht im gitcourse-Projektordner. \n " \
                                 "Bitte gehe zurück zu Schritt ... und bearbeite die dortigen Aufgaben!"


        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Get started with Git!", bg="#fff")
        title.place(x=0, y=0)

        task1 = tk.Label(description_container, text="Konfiguriere deinen Usernamen.", bg="#fff")
        task1.place(x=0, y=175)
        task2 = tk.Label(description_container, text="Konfiguriere deine Mailadresse.", bg="#fff")
        task2.place(x=0, y=195)
        task3 = tk.Label(description_container, text="Lass dir alle Konfigurationen anzeigen.", bg="#fff")
        task3.place(x=0, y=215)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class NewContent(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

            if right_directory():
                if is_repository():
                    if command == "touch main.txt":
                        if not maintxt_exists():
                            subprocess.check_output(command, shell=True)
                            output['text'] = "Die Datei 'main.txt' wurde angelegt."
                            task1['bg'] = '#6b9e1f'
                        else:
                            output['text'] = "Die Datei 'main.txt' existiert bereits!"
                    elif command == "touch main.log":
                        if not mainlog_exists():
                            subprocess.check_output(command, shell=True)
                            output['text'] = "Die Datei 'main.txt' wurde angelegt."
                            task2['bg'] = '#6b9e1f'
                        else:
                            output['text'] = "Die Datei 'main.log' existiert bereits!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Get started with Git!", bg="#fff")
        title.place(x=0, y=0)

        task1 = tk.Label(description_container, text="Lege die Datei 'main.txt' an.", bg="#fff")
        task1.place(x=0, y=175)
        task2 = tk.Label(description_container, text="Lege die Datei 'main.log' an.", bg="#fff")
        task2.place(x=0, y=195)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class Gitignore(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

           if right_directory():
               if is_repository():
                   if mainlog_exists() and maintxt_exists():
                       if command == "touch .gitignore":
                           subprocess.check_output(command, shell=True)
                           output['text'] = "Die Datei '.gitignore' wurde erfolgreich angelegt."
                           task1['bg'] = '#6b9e1f'
                       elif command == "echo 'main.log' >> .gitignore":
                           subprocess.check_output(command, shell=True)
                           output['text'] = "'main.log' wurde erfolgreich zur .gitignor ehinzugefügt."
                           task2['bg'] = '#6b9e1f'
                       else:
                            output['text'] = "Bitte überprüfe deine Syntax!"
                   else:
                       output['text'] = "Es fehlen die Dateien 'main.txt' und 'main.log'! \n " \
                                        "Bitte kehre zum letzten Schritt zurück und erledige die Aufgaben!"
               else:
                   output['text'] = "Du hast noch kein Repository angelegt! \n " \
                                    "Bitte keher zu Schritt ... zurück und arbeite die Aufgaben nacheinander ab!"
           else:
               output['text'] = "Du befindest dich nicht im gitcourse-Projektordner! \n " \
                                "Bitte kehre zu schritt ... zurück und arbeite die Aufgaben der Reihe nach ab!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Get started with Git!", bg="#fff")
        title.place(x=0, y=0)

        task1 = tk.Label(description_container, text="Lege die Datei .gitignore an!", bg="#fff")
        task1.place(x=0, y=175)
        task2 = tk.Label(description_container, text="Füge die main.log-Datei zur .gitignore hinzu", bg="#fff")
        task2.place(x=0, y=195)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class GitStatus(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

            if right_directory() and is_repository() and maintxt_exists() and mainlog_exists():
                if command == "git status":
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    checkbox['bg'] = '#6b9e1f'
                else:
                    output['text'] = "Bitte überprüfe deine Syntax!"
            else:
                output['text'] = "Du schienst einige Schritte übersprungen zu haben. \n" \
                                 "Bitte gehe zurük zu Schritt ... und arbeite die Aufgaben nacheinander ab!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Get started with Git!", bg="#fff")
        title.place(x=0, y=0)

        checkbox = tk.Label(description_container, text="Prüfe den ARchivierungsstatus deiner Respositories.", bg="#fff")
        checkbox.place(x=0, y=175)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class GitAdd(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

            if right_directory() and is_repository() and maintxt_exists() and mainlog_exists():
                if command == "git add main.txt":
                    subprocess.check_output(command, shell=True)
                    output['text'] = "main.txt wurde zur Archivierung vorgemerkt."
                    task1['bg'] = '#6b9e1f'
                elif command == "git status":
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    if not values["add_first_status"]:
                        task2['bg'] = '#6b9e1f'
                        values["add_first_status"] = True
                    elif values["add_first_status"] and not values["add_second_status"]:
                        task4['bg'] = '#6b9e1f'
                        values["add_second_status"] = True
                    elif values["add_second_status"] and values["add_first_status"]:
                        task2['bg'] = '#6b9e1f'
                        task4['bg'] = '#6b9e1f'
                elif command == "git add .gitignore":
                    subprocess.check_output(command, shell=True)
                    output['text'] = ".gitignore wurde zur Archivierung vorgemerkt."
                    task3['bg'] = '#6b9e1f'
                else:
                    output['text'] = "Bitte übeprüfe deine Syntax!"

            else:
                output['text'] = "Du schienst einige Schritte übersprungen zu haben. \n" \
                                 "Bitte gehe zurük zu Schritt ... und arbeite die Aufgaben nacheinander ab!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Get started with Git!", bg="#fff")
        title.place(x=0, y=0)

        task1 = tk.Label(description_container, text="Merke die Änderungen in der main.txt-Datei zur Versionierung vor.", bg="#fff")
        task1.place(x=0, y=175)
        task2 = tk.Label(description_container, text="Prüfe den Versionierungsstatus deines Repositories.", bg="#fff")
        task2.place(x=0, y=195)
        task3 = tk.Label(description_container, text="Merke die Änderungen in der .gitignore zur Versionierung vor!.", bg="#fff")
        task3.place(x=0, y=215)
        task4 = tk.Label(description_container, text="Prüfe den Versionierungsstatus deines Repositories.", bg="#fff")
        task4.place(x=0, y=235)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class GitCommit(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

           if right_directory() and is_repository() and mainlog_exists() and maintxt_exists():
               if command == 'git commit -m "updated .gitignore and added main-file"':
                   response = subprocess.check_output(command, shell=True)
                   output['text'] = response
                   task1['bg'] = '#6b9e1f'
               elif command == "git status":
                   response = subprocess.check_output(command, shell=True)
                   output['text'] = response
                   task2['bg'] = '#6b9e1f'

           else:
               output['text'] = "Du schienst einige Schritte übersprungen zu haben. \n" \
                                 "Bitte gehe zurük zu Schritt ... und arbeite die Aufgaben nacheinander ab!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Get started with Git!", bg="#fff")
        title.place(x=0, y=0)

        task1= tk.Label(description_container, text="Commite die vorgemerkten Änderungen in dein Repository.", bg="#fff")
        task1.place(x=0, y=175)
        task2 = tk.Label(description_container, text="Prüfe den Versionierungsstatus deines Repositories.", bg="#fff")
        task2.place(x=0, y=195)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class Summary(Page):
    pass

class Quiz(Page):
    pass

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Introduction(self)
        p2 = Requirements(self)
        p3 = GeneralStructure(self)
        p4 = LocalStructure(self)
        p5 = RemoteStructure(self)
        p6 = NewProject(self)
        p7 = InitializeRepo(self)
        p8 = ConfigGit(self)
        p9 = NewContent(self)
        p10 = Gitignore(self)
        p11 = GitStatus(self)
        p12 = GitAdd(self)
        p13 = GitCommit(self)
        p14 = Summary(self)
        p15 = Quiz(self)


        buttonframe = tk.Frame(self, bg="#6b9e1f", bd=10)
        container = tk.Frame(self, bg="#fff")
        buttonframe.pack(side="left", fill="y", expand=False)
        container.pack(side="left", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p9.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p10.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p11.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p12.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p13.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p14.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p15.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Was ist Git?", command=p1.lift, fg="#6b9e1f")
        b2 = tk.Button(buttonframe, text="Softwarevoraussetzungen", command=p2.lift, fg="#6b9e1f")
        b3 = tk.Button(buttonframe, text="Allgemeiner Aufbau eines VCS", command=p3.lift, fg="#6b9e1f")
        b4 = tk.Button(buttonframe, text="Lokales VCS", command=p4.lift, fg="#6b9e1f")
        b5 = tk.Button(buttonframe, text="Remote VCS", command=p5.lift, fg="#6b9e1f")
        b6 = tk.Button(buttonframe, text="Ein neues Projekt", command=p6.lift, fg="#6b9e1f")
        b7 = tk.Button(buttonframe, text="Ein Repository anlegen", command=p7.lift, fg="#6b9e1f")
        b8 = tk.Button(buttonframe, text="Git konfigurieren", command=p8.lift, fg="#6b9e1f")
        b9 = tk.Button(buttonframe, text="Inhalt für das Projekt", command=p9.lift, fg="#6b9e1f")
        b10 = tk.Button(buttonframe, text="Gitignore", command=p10.lift, fg="#6b9e1f")
        b11 = tk.Button(buttonframe, text="Git status", command=p11.lift, fg="#6b9e1f")
        b12 = tk.Button(buttonframe, text="Git add", command=p12.lift, fg="#6b9e1f")
        b13 = tk.Button(buttonframe, text="Git commit", command=p13.lift, fg="#6b9e1f")
        b14 = tk.Button(buttonframe, text="Zusammenfassung", command=p14.lift, fg="#6b9e1f")
        b15 = tk.Button(buttonframe, text="Quiz", command=p15.lift, fg="#6b9e1f")

        b1.pack(fill="x")
        b2.pack(fill="x")
        b3.pack(fill="x")
        b4.pack(fill="x")
        b5.pack(fill="x")
        b6.pack(fill="x")
        b7.pack(fill="x")
        b8.pack(fill="x")
        b9.pack(fill="x")
        b10.pack(fill="x")
        b11.pack(fill="x")
        b12.pack(fill="x")
        b13.pack(fill="x")
        b14.pack(fill="x")
        b15.pack(fill="x")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1200x800")
    root.mainloop()
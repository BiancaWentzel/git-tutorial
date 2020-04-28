# -*- coding: utf-8 -*-

import tkinter as tk
import subprocess
import os
import webbrowser

from utils import right_directory, is_repository, maintxt_exists, mainlog_exists

values = {
    "add_first_status": False,
    "add_second_status": False
}

font_color = "#0f425b"
fu_green = '#6b9e1f'
fu_grey = '#ccc'


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

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="Was ist Git?", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Git ist ein sogenanntes Versionierungskontrollsystem (VCS - Version Controll System)."
                             "\nEs dient zur Protokollierung und Archivierung sowie Dokumentation von Änderungen in "
                             "Dateien \nund ordnern eines projektes. Für alle registrierten Änderung wird eine Version des "
                             "gesamten \nProjektes wie ein Screenshot abgespeichert und mit Angaben zur Zeit und des "
                             "Autors sowie \neinem Kommentar des Autors zu den Änderungen archiviert."
                             "\n\nGit bietet folgende Möglichkeiten/ Vorteile:"
                             "\n- Änderungen können immer nachvollzogen werden"
                             "\n- man hat ein Archiv mit allen Versionen des Projektes"
                             "\n- man kann jederzeit ältere Versionen des projektes wiederherstellen"
                             "\n\nGit bietet durch die interne Regelung und Archivierung der Versionen hervorragende "
                             "Möglichkeiten,\num im team an einem Projekt zu arbeiten, ohne dass Änderungen verloren gehen."
                             "\n\nWeiterhin bieten Hostingdienste wie GitLab oder GitHub die Möglichkeit, Projektinhate auf"
                             "\nServern zu speichern, die von überall über das Internet erreichbar sind.",
                        font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.15)

        explanation = tk.Label(description_container, text="Weiterführende Links mit Informationen", bg="white",
                               font="TkFont 14 bold", fg=font_color)
        explanation.place(x=0, rely=0.60)

        links = tk.Label(description_container, text="https://de.wikipedia.org/wiki/Versionsverwaltung"
                                                     "\nhttps://git-scm.com/docs/git"
                                                     "\nhttps://de.wikipedia.org/wiki/Git"
                                                     "\nhttps://about.gitlab.com/"
                                                     "\nhttps://github.com/",
                         font="TkFont 12 bold", bg="white", fg=font_color, justify="left")
        links.place(x=0, rely=0.65)


class LocalStructure(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="Lokales VCS", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)

        img = tk.PhotoImage(file="./img/localVCS.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(x=0, rely=0.15)


class RemoteStructure(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="Remote VCS", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)

        explanation = tk.Label(description_container, text="", bg="white")
        explanation.pack()


class NewProject(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

            if command == "mkdir gitcourse":
                if os.system(command) == 0:
                    output['text'] = "Das Verzeichnis 'gitcouse' wurde angelegt."
                    task1['bg'] = '#6b9e1f'
                elif os.system(command) == 256:
                    output['text'] = "Das Projekt existiert bereits."
                    task1['bg'] = '#6b9e1f'
                else:
                    output['text'] = "Bitte überprüfe deine Syntax!"
            elif command == "cd gitcourse":
                try:
                    os.chdir("gitcourse")
                    output['text'] = "Gewechselt in da Verzeichnis 'gitcourse'. \nDu befindet dich jetzt hier: {}".format(subprocess.check_output("pwd"))
                    task2['bg'] = '#6b9e1f'
                except:
                    if right_directory():
                        output['text'] = "Du befindest dich bereits im gitcourse-Projektordner."
                    else:
                        output['text'] = "Bist du sicher, dass du einen Projektordner namens 'gitcourse' angelegt hast?"

            else:
                output['text'] = "Bitte überprüfe deine Syntax."

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Ein neues Projekt", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Nun wollen wir ein neues Projekt anlegen, in dem wir später ein Git-Repository "
                             "initialisieren, \num die grundlegenden Befehle zu lernen. Um einen neuen Projektordner "
                             "anzulegen, \ngibt es den Befehl 'mkdir' (make directoy). \n\nWenn man dann einen Projektordner "
                             "angelegt hat, möchte man in ihm arbeiten. \nDafür kann man mit 'cd '(change directory) in den "
                             "Projektordner wechseln.", font="TkFont 12 bold", bg="white", fg=font_color, justify="left")
        commands_title = tk.Label(description_container, text="Befehle", bg="white", font="TkFont 14 bold", fg=font_color)
        commands = tk.Label(description_container, text="- mkdir Verzeichnisname\n- cd Verzeichnisname", bg="white",
                            fg=font_color, font="TkFont 12 bold", justify="left")

        text.place(x=0, rely=0.15)
        commands_title.place(x=0, rely=0.45)
        commands.place(x=0, rely=0.55)


        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.75)
        task1 = tk.Label(description_container, text="1. Lege einen neuen Projektordner mit dem Name 'gitcourse' an.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.82)
        task2 = tk.Label(description_container, text="2. Wechsel in den angelegten Projektordner 'gitcourse'.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.9)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
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
                output['text'] = "Du befindest dich nicht im 'gitcourse-Projektordner!\n" \
                                 "Gehe zurück zum vorherigen Schritt und erledige die dort gestellten Aufgaben."

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Ein Repository anlegen", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                        text="Jetzt befinden wir uns im Projektverzeichnis (Working Directory) und wollen den Inhalt "
                             "des Projektes \nversionieren. Hierzu müssen wir ein Git-Repository initialisieren."
                             "Hierfür stellt Git \nden Befehl 'git init' bereit. Fürht man diesen Befehl aus, werden die"
                             "zwei zusätzlichen \nGit-Ebenen 'Staging Area (Zwischenablage)' und 'Repository (Archiv)' "
                             "angelegt, jedoch versteckt. \n\nMöchte man sehen, ob tasächlich ein Repsotiroy angelegt wurde, "
                             "kann man\nden Befehl 'ls --all' (list) ausführen und es sollte ein .git-Verzeichnis angezeigt "
                             "werden,\nwobei der . vor dem Verzeichnisnamen symbolisiert, dass es sich um einen\n"
                             "versteckten Ordner handelt.", font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        commands_title = tk.Label(description_container, text="Befehle", bg="white", font="TkFont 14 bold",
                                  fg=font_color)
        commands = tk.Label(description_container, text="- git init\n- ls -a", bg="white",
                            fg=font_color, font="TkFont 12 bold", justify="left")

        text.place(x=0, rely=0.15)
        commands_title.place(x=0, rely=0.55)
        commands.place(x=0, rely=0.62)

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.75)
        task1 = tk.Label(description_container, text="1. Lege ein Git-Repository an", bg="white", font="TkFont 12 bold",
                         fg=font_color, bd=5)
        task1.place(x=0, rely=0.82)
        task2 = tk.Label(description_container, text="2. Lass dir den Inhalt des Projektordners anzeigen.", bg="white",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.9)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
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
                    elif command.startswith("git config --global user.email"):
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

        title = tk.Label(description_container, text="Git konfigurieren",  bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                        text="Um nachvollziehen zu können, welche Verändeurngen und Archivierungsschritte von wem "
                             "gemacht \nwurden und Benachrichtigungen über Codeanfragen oder ähnliches bekommen zu "
                             "können, \nmuss sowohl der Benutzername als auch eine Email-Adresse konfiguriert werden. "
                             "\nDer Benutzername wird als Auto bei Änderungen hinterlegt.", font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        commands_title = tk.Label(description_container, text="Befehle", bg="white", font="TkFont 14 bold",
                                  fg=font_color)
        commands = tk.Label(description_container, text="- git config --global user.name 'Vorname Nachname'\n- git config --global user.email 'email@server.com'\n- git config --list", bg="white",
                            fg=font_color, font="TkFont 12 bold", justify="left")

        text.place(x=0, rely=0.15)
        commands_title.place(x=0, rely=0.45)
        commands.place(x=0, rely=0.52)

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.67)
        task1 = tk.Label(description_container, text="1. Konfiguriere deinen Usernamen.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.74)
        task2 = tk.Label(description_container, text="2. Konfiguriere deine Mailadresse.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.82)
        task3 = tk.Label(description_container, text="3. Lass dir alle Konfigurationen anzeigen.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task3.place(x=0, rely=0.9)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
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

        title = tk.Label(description_container, text="Get started with Git!", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                       text="Um verschiedenen Versionen unseres Projektes versionieren zu können braucht es Inhalt. "
                            "\nDiesen Inhalt wollen wir nun erstellen. Wir wollen zwei Dateien anlegen: 'main.txt' und 'main.log'."
                            "\n\nDies kann man mit dem Befehl 'touch' tun. Dieser Befehl ist eigentlich dafür gedacht,\n"
                            "den zeitstempel von Dateien zu erstellen oder zu bearbeiten. Existiert die angegebenen Datei"
                            "\njedoch nicht, wird die Datei und ihr Zeitstempel angelegt.", font="TkFont 12 bold",
                       bg="white", fg=font_color,
                       justify="left")
        commands_title = tk.Label(description_container, text="Befehle", bg="white", font="TkFont 14 bold",
                                  fg=font_color)
        commands = tk.Label(description_container,
                            text="- touch main.txt\n- touch main.log",
                            bg="white",
                            fg=font_color, font="TkFont 12 bold", justify="left")

        text.place(x=0, rely=0.15)
        commands_title.place(x=0, rely=0.55)
        commands.place(x=0, rely=0.62)

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.75)
        task1 = tk.Label(description_container, text="1. Lege die Datei 'main.txt' an.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.82)
        task2 = tk.Label(description_container, text="2. Lege die Datei 'main.log' an.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.9)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
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

        title = tk.Label(description_container, text="Gitignore", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Manchmal hat man Detien und Ordner, die man nicht mit versionieren möchte. Dazu zählen "
                             "Ordner,\nin denen Informationen und Software von virtuellen Umgebungen abgespeichert sind "
                             "sowie \nKonfigurationsdateien, die sensible Daten wie passwörter oder ähnliches enthalten."
                             "\n\nUm diese dateien trotzdem in ihrem zugehörigen Projekt zu haben aber nict zu versionieren, "
                             "\ngibt es die sogenannte '.gitignore'. Hierbei handelt es sich um eine versteckte Datei, "
                             "\nin die alle Ordner und Dateien geschrieben werden, die bei der Versionierung ignoriert "
                             "werden sollen.\nIn unserem Fall wollen wir die Datei main.log und ihr Inhalt nicht versionieren, "
                             "\ndeswegen müssen wir sie in der .gitignore vermerken.", font="TkFont 12 bold",
                        bg="white", fg=font_color,
                        justify="left")
        commands_title = tk.Label(description_container, text="Befehle", bg="white", font="TkFont 14 bold",
                                  fg=font_color)
        commands = tk.Label(description_container,
                            text="- touch .gitignore\n- echo 'main.log' >> .gitignore",
                            bg="white",
                            fg=font_color, font="TkFont 12 bold", justify="left")

        text.place(x=0, rely=0.15)
        commands_title.place(x=0, rely=0.55)
        commands.place(x=0, rely=0.62)

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.75)
        task1 = tk.Label(description_container, text="1. Lege die Datei .gitignore an!", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.82)
        task2 = tk.Label(description_container, text="2. Füge die main.log-Datei zur .gitignore hinzu", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.9)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
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

        title = tk.Label(description_container, text="Git status", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.83)
        checkbox = tk.Label(description_container, text="1. Prüfe den ARchivierungsstatus deiner Respositories.",
                   font="TkFont 12 bold", fg=font_color, bd=5, bg="#fff")
        checkbox.place(x=0, rely=0.9)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)

        image2 = tk.Label(description_container, text="Staging Area", bg=font_color, fg="white", bd=15)
        image3 = tk.Label(description_container, text="Repository", bg=font_color, fg="white", bd=15)
        image2.place(y=0, relx=0.8)
        image3.place(y=45, relx=0.8)


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

        title = tk.Label(description_container, text="Git add", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.59)
        task1 = tk.Label(description_container, text="1. Merke die Änderungen in der main.txt-Datei zur Versionierung vor.",
                         bg="#fff", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.66)
        task2 = tk.Label(description_container, text="2. Prüfe den Versionierungsstatus deines Repositories.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.74)
        task3 = tk.Label(description_container, text="3. Merke die Änderungen in der .gitignore zur Versionierung vor!.",
                         bg="#fff", font="TkFont 12 bold", fg=font_color, bd=5)
        task3.place(x=0, rely=0.82)
        task4 = tk.Label(description_container, text="4. Prüfe den Versionierungsstatus deines Repositories.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task4.place(x=0, rely=0.9)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)

        image = tk.Label(description_container, text="Staging Area", bd=30, bg=font_color, fg="white")
        image.place(y=0, relx=0.8)


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

        title = tk.Label(description_container, text="Git commit", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.75)
        task1= tk.Label(description_container, text="1. Commite die vorgemerkten Änderungen in dein Repository.",
                        bg="#fff", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.82)
        task2 = tk.Label(description_container, text="2. Prüfe den Versionierungsstatus deines Repositories.",
                         bg="#fff", font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.9)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()))
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)

        image = tk.Label(description_container, text="Repository", bd=30, bg=font_color, fg="white")
        image.place(y=0, relx=0.8)


class Summary(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def callback(filename):
            webbrowser.open('file://' + os.path.realpath(filename))

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="Zusammenfassung", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                        text="Du hast den ersten teil des Totiroals zu Git fertig. Du kannst das Tutorial jederzeit "
                             "wiederholen. \n\nDu solltest jetzt folgende Fakten und Befehle rund ums Thema Git wissen:"
                             "\n- Was ist Git und wie ist es aufgebaut"
                             "\n- Initialisieren eines Repositories und konfigurieren von Git (git init, git config)"
                             "\n- Übersicht über gemachte Änderungen (git status)"
                             "\n- Vormerken von Änderungen zur Archivierung (git add)"
                             "\n- Archivierung von Änderungen (git commit)"
                             "\n\nUm dein Wissen nochmal zu festigen bzw. zu prüfen, folge dem Link zum Quiz und bearbeite dieses.", font="TkFont 12 bold",
                        bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.1)

        link1 = tk.Button(description_container, text="--> Quiz <--", fg="white", bg=fu_green, font="TkFont 12 bold", cursor="hand2")
        link1.place(relx=0.4, rely=0.37)
        link1.bind("<Button-1>", lambda e: callback("Quiz.html"))

        additional = tk.Label(description_container, text="Bei Anmerkungen, Fragen oder Fehlern und Problemen mit dem "
                                                          "Tutorial oder allgemein zu Git,\nschreib mir entweder über "
                                                          "RocketChat oder per Mail: bianca1409@zedat.fu-berlin.de",
                              font="TkFont 12 bold", bg="white", fg=font_color, justify="left")
        additional.place(x=0, rely=0.92)





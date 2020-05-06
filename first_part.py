# -*- coding: utf-8 -*-

import tkinter as tk
import subprocess
import os
import webbrowser

from utils import right_directory, is_repository, file_exists

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

        title = tk.Label(description_container, text="1. Was ist Git? Und worfür braucht man es?", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Git ist ein sogenanntes Versionskontrollsystem (VCS - Version Controll System)."
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
        text.place(x=0, rely=0.50)

        img = tk.PhotoImage(file="./img/vc-xkcd.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.15, rely=0.10)


class GeneralStructure(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="2. Allgemeine Struktur", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                        text="Primär findet Versionierung mit Git lokal auf deinem rechner statt. "
                        "Hierbei gliedert sich die lokale\nVersionierung hauptsächlich in 3 Ebenenen: das working "
                             "Directory, die staging Area und\ndas repository. Hierbei sind die staging Area und das "
                             "repsoitory virtuellen Ebenen,\ndie ersteinaml nicht sichtbar sind. Zum Navigation oder "
                             "Registrierung von Änderungen gibt es\nzahlreiche Befehle, die zur Interkation der "
                             "einzelnen Ebenen dienen.",font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.1)

        text2 = tk.Label(description_container,text="Weiterhin gibt es ein sogenanntes Remote Repository, dass durch unterschiedliche "
                             "\nSoftwaredienstw ie GitLab oder Github genutz werden kann."
                             "Die einzelnen Ebenen werden im \nFolgenden detaillierter erläutert.",font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        text2.place(x=0, rely=0.85)

        img = tk.PhotoImage(file="./img/generalstructure.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.15, rely=0.25)


class WorkingDirectory(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="3. Working Directory", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Das Working Directory ist das Arbeitsverzeichnis, also der Projektordne,r in dem sich\n "
                             "alle Dateien und Dokumente befinden, die zum Projekt gehören. \nDas Working Directory ist der"
                             "Ort, an dem alle Änderungen staffinden \nund erst einmal unabhängig ist von Git und Versionierung."
                             "Sobald man das Projekt \njedoch versionieren möchte, ist es auch der Ort, an dem ein "
                             "Repository angelegt wird.",font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.1)

        img = tk.PhotoImage(file="./img/areas.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.15, rely=0.45)


class StagingArea(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="4. Staging Area", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Wenn man nun ein Projekt verionieren möchte, initialisiert man ein Repository. \nBei der "
                             "Initialisierung werden zwei unsichtbare Zwischenebenen angelegt. \nEine davon ist die sogenannte Staging Area."
                             "Diese Ebene kann man als \nZwischenablage oder Mekrzettel verstehen. Wenn man eine Änderung "
                             "gemacht hat,\ndie man gerne versionieren bzw. Archivieren möchte, so merkt man diese in der \nStaging Area vor."
                             "\nDas kann man mit allen Änderungen machen. Die Staging Area ist also soetwas\n wie ein Merkzettel "
                             "für alle Änderungen, die in Repository (Archiv) übernommen werden sollen.",
                        font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.1)

        img = tk.PhotoImage(file="./img/areas.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(x=0, rely=0.35)

        img = tk.PhotoImage(file="./img/gitadd.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(x=0, rely=0.35)


class Repository(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="5. Repository", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Die letzte und wichtigste Ebene bei einer Versionierung wird Repository genannt. \nDas "
                             "Repsoritory ist sozusagen das Archiv, in dem alle Versionen des Projektes \nabgespeichert werden."
                             "Wenn man nun also Änderungen an seinem Projekt gemacht hat \nund diese Änderungen zur "
                             "Archivierung in der Staging Area vorgemerkt hat, dann wird \nsoetwas wie ein Snapshot vom "
                             "gesamten Projekt mit diesen Änderungen gemacht und \nim Archiv gespeichert. Mit Zeitstempel, "
                             "Autor und Kommentar des Autoren.",font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.1)

        img = tk.PhotoImage(file="./img/areas.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(x=0, rely=0.35)

        img = tk.PhotoImage(file="./img/gitcommit.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(x=0, rely=0.35)


class RemoteRepository(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="6. Remote Repository", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                        text="Versionierung ist ein mächtiges Werkzeug und bietet sich sehr gut für Arbeiten im Team "
                             "an.\nSolange du jedoch nicht auf einem Server arbeitet und versionierst, sondern nur lokal\n"
                             "auf deinem Rechner, ist dies jedoch nicht möglich. Da man sich auch nicht unbedingt\n einen "
                             "Server beorgen möchte, gibt es Diensteleister wie GitLab oder Github. \nHierbei handelt es "
                             "sich um Onlineserver, auf denen man sein Repsoitory speichern kann."
                             "\nDas nennt sich dann Remote Repository. Es ist eine Kopie deines lokalen Reposiorries, \ndann "
                             "üüber das Internet erreichbar ist. Das bietet den Vorteil, dass man jederzeit und \nvon "
                             "überall an sein Projekt hernakommt und daran arbeiten kann, weil man das lokale \nund remote "
                             "Reposirtory synchronisieren kann. Weiterhin bietet es die Möglichkeit, \ndass mehrerer Leute "
                             "an diesem Projekt arbeiten, mit der Schnittstelle des remote Repositores.",font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.1)

        img = tk.PhotoImage(file="./img/remote.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(x=0, rely=0.45)


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
                    output['text'] = "Gewechselt in das Verzeichnis 'gitcourse'. \nDu befindet dich jetzt hier: {}".format(subprocess.check_output("pwd"))
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

        title = tk.Label(description_container, text="7. Ein neues Projekt", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Nun wollen wir ein neues Projekt anlegen, in dem wir später ein Git-Repository "
                             "initialisieren, \num die grundlegenden Befehle zu lernen. Um einen neuen Projektordner "
                             "anzulegen, \ngibt es den Befehl 'mkdir' (make directoy). \n\nWenn man dann einen Projektordner "
                             "angelegt hat, möchte man in ihm arbeiten. \nDafür kann man mit 'cd '(change directory) in den "
                             "Projektordner wechseln.", font="TkFont 12 bold", bg="white", fg=font_color, justify="left")

        text.place(x=0, rely=0.15)


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
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()), bg=fu_green, fg="white")
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
                    if is_repository():
                        output['text'] = "Du hast bereits ein Repository initialisiert!"
                        task1['bg'] = '#6b9e1f'
                    else:
                        response = subprocess.check_output(command, shell=True)
                        output['text'] = response
                        task1['bg'] = '#6b9e1f'
                elif command == "ls -a":
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

        title = tk.Label(description_container, text="8. Ein Repository anlegen", bg="#fff", font="TkHeaderFont 24 bold",
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


        text.place(x=0, rely=0.15)

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
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()), bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class ConfigGit(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

            if right_directory():
                if is_repository():
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

        title = tk.Label(description_container, text="9. Git konfigurieren",  bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                        text="Um nachvollziehen zu können, welche Verändeurngen und Archivierungsschritte von wem "
                             "gemacht \nwurden und Benachrichtigungen über Codeanfragen oder ähnliches bekommen zu "
                             "können, \nmuss sowohl der Benutzername als auch eine Email-Adresse konfiguriert werden. "
                             "\nDer Benutzername wird als Auto bei Änderungen hinterlegt.", font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")


        text.place(x=0, rely=0.15)


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
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()), bg=fu_green, fg="White")
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
                        if not file_exists("main.txt"):
                            subprocess.check_output(command, shell=True)
                            output['text'] = "Die Datei 'main.txt' wurde angelegt."
                            task1['bg'] = '#6b9e1f'
                        else:
                            output['text'] = "Die Datei 'main.txt' existiert bereits!"
                            task1['bg'] = fu_green
                    elif command == "touch main.log":
                        if not file_exists("main.log"):
                            subprocess.check_output(command, shell=True)
                            output['text'] = "Die Datei 'main.log' wurde angelegt."
                            task2['bg'] = '#6b9e1f'
                        else:
                            output['text'] = "Die Datei 'main.log' existiert bereits!"
                            task2['bg'] = fu_green
                    elif command == "touch second.txt":
                        if not file_exists("second.txt"):
                            subprocess.check_output(command, shell=True)
                            output['text'] = "Die Datei 'second.txt' wurde angelegt."
                            task3['bg'] = '#6b9e1f'
                        else:
                            output['text'] = "Die Datei 'second.txt' existiert bereits!"
                            task3['bg'] = fu_green
                    elif command == "touch third.txt":
                        if not file_exists("third.txt"):
                            subprocess.check_output(command, shell=True)
                            output['text'] = "Die Datei 'thid.txt' wurde angelegt."
                            task4['bg'] = '#6b9e1f'
                        else:
                            output['text'] = "Die Datei 'third.txt' existiert bereits!"
                            task4['bg'] = fu_green
                else:
                    output['text'] = "Du hast noch kein Repository initialisiert.\n Bitte gehe zurück zu Schritt ... zurück und erledige alle Aufgaben!"
            else:
                output['text'] = "Du befindest dich nicht im gitcourse-Verzeichnis.\n Bitte geh zurück zu Schritt ... und erledige alle Aufgaben!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="10. Inhalt für das Projekt", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                       text="Um verschiedenen Versionen unseres Projektes versionieren zu können braucht es Inhalt. "
                            "\nDiesen Inhalt wollen wir nun erstellen. Wir wollen vier Dateien anlegen: 'main.txt', 'main.log', \n'second.txt' und 'third.txt'."
                            "\n\nDies kann man mit dem Befehl 'touch' tun. Dieser Befehl ist eigentlich dafür gedacht,\n"
                            "den zeitstempel von Dateien zu erstellen oder zu bearbeiten. Existiert die angegebenen Datei"
                            "\njedoch nicht, wird die Datei und ihr Zeitstempel angelegt.", font="TkFont 12 bold",
                       bg="white", fg=font_color,
                       justify="left")


        text.place(x=0, rely=0.15)


        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.75)
        task1 = tk.Label(description_container, text="1. Lege die Datei 'main.txt' an.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.66)
        task2 = tk.Label(description_container, text="2. Lege die Datei 'main.log' an.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.74)
        task3 = tk.Label(description_container, text="3. Lege die Datei 'second.txt' an.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task3.place(x=0, rely=0.82)
        task4 = tk.Label(description_container, text="4. Lege die Datei 'third.txt' an.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task4.place(x=0, rely=0.9)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()), bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class Gitignore(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

           if right_directory():
               if is_repository():
                   if file_exists("main.txt") and file_exists("main.log") and file_exists("second.txt") and file_exists("third.txt"):
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
                       output['text'] = "Es fehlen die Dateien 'main.txt', 'main.log', 'second.txt' and 'third.txt'! \n " \
                                        "Bitte kehre zum letzten Schritt zurück und erledige die Aufgaben!"
               else:
                   output['text'] = "Du hast noch kein Repository angelegt! \n " \
                                    "Bitte keher zu Schritt ... zurück und arbeite die Aufgaben nacheinander ab!"
           else:
               output['text'] = "Du befindest dich nicht im gitcourse-Projektordner! \n " \
                                "Bitte kehre zu schritt ... zurück und arbeite die Aufgaben der Reihe nach ab!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="11. Gitignore", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Manchmal hat man Detien und Ordner, die man nicht mit ver-\nsionieren möchte. Dazu zählen "
                             "Ordner, in denen Informationen und Software von virtuellen Umgebungen abgespeichert sind "
                             "sowie \nKonfigurationsdateien, die sensible Daten wie passwörter oder ähnliches enthalten."
                             "\n\nUm diese dateien trotzdem in ihrem zugehörigen Projekt zu haben aber nict zu versionieren, "
                             "\ngibt es die sogenannte '.gitignore'. Hierbei handelt es sich um eine versteckte Datei, "
                             "\nin die alle Ordner und Dateien geschrieben werden, die bei der Versionierung ignoriert "
                             "werden sollen.\nIn unserem Fall wollen wir die Datei main.log und ihr Inhalt nicht versionieren, "
                             "\ndeswegen müssen wir sie in der .gitignore vermerken.", font="TkFont 12 bold",
                        bg="white", fg=font_color,
                        justify="left")


        text.place(x=0, rely=0.1)


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
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()), bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)

        img = tk.PhotoImage(file="./img/gitignore.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.70, rely=0.0)


class GitStatusNew(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

            if right_directory() and is_repository() and file_exists("main.txt") and file_exists("main.log") \
                    and file_exists("second.txt") and file_exists("third.txt"):
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

        title = tk.Label(description_container, text="12. Git status (unversioniert)", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Nun haben wir Änderungen an unserem Projekt vorgenommen. Man kann beim Arbeiten an einem "
                             "\nprojekt gern mal den Überblick darüber velieren, wo man Änderunge vorgenommen hat."
                             "\nHierzu stellt git einen Befehl 'status' bereit. Dieser zeigt alle Dateien und Ordner an, "
                             "\ndie verändert wurden. Das beinhaltet sowohl veränderungen an bestehenden Dateien\nund "
                             "ordner sowie das Anlegen und Löschen dieser."
                             "\n\nJe nachdem, welche Zusatnd zutrofft, zeigt 'git status' die Änderugen unterschiedlich an."
                             "\nDateien und Ordner, id eneu angelegt wurden, werden unter dem Punkt 'Unversioniert Dateien' \nangezeigt."
                             "Da sie vorher nicht existierten udn demnach natürlich auch noch nicht versioniert \nwerden konnten."
                             "Dies triftt auf alle unsere angelegten dateine zu. \n\nAuffällig hierbei, die 'main.log' wird "
                             "nicht angezeigt, da sie in der .gitignore vermekt ist und \ndemnach nicht berücksichtigt werden soll.", font="TkFont 12 bold",
                        bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.12)



        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.83)
        checkbox = tk.Label(description_container, text="1. Prüfe den ARchivierungsstatus deiner Respositories.",
                   font="TkFont 12 bold", fg=font_color, bd=5, bg="#fff")
        checkbox.place(x=0, rely=0.9)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()), bg=fu_green,
                               fg="white", font="TkFont 10 bold")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class GitAdd(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

            if right_directory() and is_repository() and file_exists("main.txt") and file_exists("main.log") \
                    and file_exists("second.txt") and file_exists("third.txt"):
                if command == "git add main.txt":
                    subprocess.check_output(command, shell=True)
                    output['text'] = "main.txt wurde zur Archivierung vorgemerkt."
                    task1['bg'] = '#6b9e1f'
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

        title = tk.Label(description_container, text="13. Git add", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                        text="Wenn du Änderungen an einem Projekt gemacht hast, die du als eine neue Projketversion\nim "
                             "archiv also dem Reposiroty speicher nöchtest, musst du sie zur speicherung vormerken. "
                             "\nHierzu stellt git den befehl 'add' bereit. Dieser merkt alle benannten Änderungen zur\n "
                             "Archivierung vor."
                            "\nDas heißt, die Änderungen im Working Directory werden zur Stagig Area hinzugefügt. "
                            "\nEs gibt mehrere Möglichkeiten, Dateien und Ordner zur Versionierung vorzumerken. \nMan "
                             "kann einzelne Dateien und Ordner vormerken, indem man sie nametlich bennent: \n'git add Dateiname."
                             "\nOder man kann alle veränderten Dateien vormerken mit 'git add .' \nHierbei muss man jedoch "
                             "darauf achten, dass nur alle Dateien des AKTUELLEN Verzeichnisses \nvorgemerkt werden."
                             "Deteien und Ordner, die über dem aktuellen Verzeichnis liegen, \nwerden nicht vorgemerkt.",
                        font="TkFont 12 bold", bg="white", fg=font_color, justify="left")
        text.place(x=0, rely=0.10)



        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.82)
        task1 = tk.Label(description_container, text="1. Merke die Änderungen in der main.txt-Datei zur Versionierung vor.",
                         bg="#fff", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.88)
        task3 = tk.Label(description_container, text="2. Merke die Änderungen in der .gitignore zur Versionierung vor!.",
                         bg="#fff", font="TkFont 12 bold", fg=font_color, bd=5)
        task3.place(x=0, rely=0.94)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()), bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)

        img = tk.PhotoImage(file="./img/gitadd.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.25, rely=0.61)


class GitStatusAdded(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

            if right_directory() and is_repository() and file_exists("main.txt") and file_exists("main.log") \
                    and file_exists("second.txt") and file_exists("third.txt"):
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

        title = tk.Label(description_container, text="14. Git status (vorgemerkt)", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Nun hast du 'main.txt' und '.gitignore' zur Staging area hinzugefügt, also zur "
                             "\nVersionierung vorgemerkt. Der Befehl 'git status' dient außerdem dazu, zu überprüfen,\nob "
                             "und welche Dateien zur Versionierung vorgemerkt sind."
                             "Wenn wir nun den Status prüfen, \nsehen wir, dass '.gitignore' und 'main.txt' unter dem Punkt"
                             "'zum Commit vorgemerkte \nÄnderungen' gelistet sind."
                             "Weiterhin sehen wir die Dateien 'second.txt' und 'third.txt' \nnach wie vor als 'unversioniert "
                             "Dateien' gelistet sind.",
                        font="TkFont 12 bold",
                        bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.12)



        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.83)
        checkbox = tk.Label(description_container, text="1. Prüfe den ARchivierungsstatus deiner Respositories.",
                            font="TkFont 12 bold", fg=font_color, bd=5, bg="#fff")
        checkbox.place(x=0, rely=0.9)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()),
                               bg=fu_green,
                               fg="white", font="TkFont 10 bold")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class GitCommit(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

           if right_directory() and is_repository() and file_exists("main.txt") and file_exists("main.log") \
                    and file_exists("second.txt") and file_exists("third.txt"):
               if command.startswith("git commit -m "):
                   response = subprocess.check_output(command, shell=True)
                   output['text'] = response
                   task1['bg'] = '#6b9e1f'
               else:
                   output['text'] = "Prüfe deine Syntax und die Commitmessage!"
           else:
               output['text'] = "Du schienst einige Schritte übersprungen zu haben. \n" \
                                 "Bitte gehe zurük zu Schritt ... und arbeite die Aufgaben nacheinander ab!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="15. Git commit", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Wenn man nun mit seinen Änderunge fertig ist, möchte man die neue Version des Porjektes\nim"
                             "Repository, also dem Archiv, speichern. Dies tut man mit 'git commit'. Zu jedem \nCommit sollte"
                             "man eine kurze Beschreibung dessen mitliefern, was man geändert hat,\ndamit man später alle "
                             "Änderungen nachvollzeihen kann. Dies tut man am besten, indem \nman den Befehl mit der Option "
                             "-m ergänzt in Verbidung mit der sogenannten Commitmessage."
                             "\n\nBeim Commiten speichert man nur alle Änderungen, die in der Staging Area zur Archivierung\n "
                             "vorgemerkt wurden im Repositry. Alle anderen Änderungen bleiben zwar erhalten, \nsind aber nicht im "
                             "gespeicherten Snapshot im Repository vorhanden. \nDiese kann man in einer nächsten Version "
                             "speichern oder zurücksetzen.", font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.1)



        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.85)
        task1= tk.Label(description_container, text="1. Commite die vorgemerkten Änderungen in dein Repository.",
                        bg="#fff", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.92)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()), bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)

        img = tk.PhotoImage(file="./img/gitcommit.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(x=0, rely=0.515)


class GitStatusAll(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

            if right_directory() and is_repository() and file_exists("main.txt") and file_exists("main.log") \
                    and file_exists("second.txt") and file_exists("third.txt"):
                if command == "git status":
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task2['bg'] = '#6b9e1f'
                elif command == "echo 'Erster Inhalt' >> main.txt":
                    subprocess.check_output(command, shell=True)
                    output['text'] = "Du hast 'Erster Inhalt' in die main.txt geschrieben."
                    task1['bg'] = fu_green
                else:
                    output['text'] = "Bitte überprüfe deine Syntax!"
            else:
                output['text'] = "Du schienst einige Schritte übersprungen zu haben. \n" \
                                 "Bitte gehe zurük zu Schritt ... und arbeite die Aufgaben nacheinander ab!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="16. Git status (nicht vorgemerkt)", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Nun hast du eine Version deines Projektes als Snapchot im Repository (Arciv) gespeichert."
                             "\nNun wollen wir noch eine Änderung an der 'main.txt# vornehmen, indem wir 'erster Inhalt' "
                             "\nin die Datei schreiben."
                             "\n\nNun wollen wir ein letztes Mal den Status unserer Ändeurngen begutachten."
                             "\nWeiterhin sind 'second.txt# und 'third.txt' als unversionierte ateien vorgemerkt."
                             "\nDie gitignore wurde im letzten Commit im Archiv gesoeichert und seitdem nicht mehr "
                             "verändert, \nsodass die Datei nicht im Status augleistet wird."
                             "Neu hinzugekommen sind die Änderungen, \ndie in der 'main.txt' gemacht wurden."
                             "Da diese datei nicht neu angelegt wurde aber\n Änderungen enthalt, die nicht zur "
                             "Archivierung vorgemerkt sind, wird sie unter dem Punkt \n'Änderungen, die nicht zum "
                             "Commit vorgemerkt sind'' gelistet. "
                             "\nAlle Änderunge, die in einem Projekt stattfinden, werden einer der drei Kategorien "
                             "\nzugeodnet und dementsprechend an der passenden Stelle gelistet. \nSo hat man immer einen Überblick"
                             "über den Stand seineS projektes."
                             "Sollte man nicht mehr ganz \nzusammenbekommen, wo sich welche datei befindet und was man mit "
                             "ihr machen kann,\n schreibt git immer befehlsvorschläge dazu.",
                        font="TkFont 12 bold",
                        bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.12)

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.88)
        task1 = tk.Label(description_container, text="1. Ändere den Inhalt der 'main.txt'",
                            font="TkFont 12 bold", fg=font_color, bd=5, bg="#fff")
        task1.place(x=0, rely=0.75)
        task2 = tk.Label(description_container, text="2. Prüfe den Archivierungsstatus deines Projektes",
                         font="TkFont 12 bold", fg=font_color, bd=5, bg="#fff")
        task2.place(x=0, rely=0.95)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()),
                               bg=fu_green,
                               fg="white", font="TkFont 10 bold")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class Summary(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def callback(filename):
            webbrowser.open('file://' + os.path.realpath(filename))

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="17. Zusammenfassung", font="TkHeaderFont 24 bold", bg='white',
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
                             "\n\nUm dein Wissen nochmal zu festigen bzw. zu prüfen, folge dem Link zum Quiz und bearbeite \ndieses.", font="TkFont 12 bold",
                        bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.1)

        img = tk.PhotoImage(file="./img/localVCS.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(x=0, rely=0.15)

        link1 = tk.Button(description_container, text="--> Quiz <--", fg="white", bg=fu_green, font="TkFont 12 bold", cursor="hand2")
        link1.place(relx=0.4, rely=0.37)
        link1.bind("<Button-1>", lambda e: callback("questionaire/first_questionaire.html"))

        additional = tk.Label(description_container, text="Bei Anmerkungen, Fragen oder Fehlern und Problemen mit dem "
                                                          "Tutorial oder allgemein zu Git,\nschreib mir entweder über "
                                                          "RocketChat oder per Mail: bianca1409@zedat.fu-berlin.de",
                              font="TkFont 12 bold", bg="white", fg=font_color, justify="left")
        additional.place(x=0, rely=0.92)





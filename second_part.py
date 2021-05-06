# -*- coding: utf-8 -*-

import tkinter as tk
import subprocess
import os
import webbrowser
import platform

from utils import file_exists

font_color = "#0f425b"
fu_green = '#6b9e1f'
fu_grey = '#ccc'


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

        title = tk.Label(description_container, text="1. Rückblick", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, wrap="word", pady=5, padx=5)
        text.place(x=0, rely=0.07, relwidth=1, relheight=0.23)
        text.insert("1.0", "Im letzten Teil des Tutorials haben wir die grundlegenden Strukturen und Befehle von Git gelernt."
                           " Die gelernten Befehle sind die, die man in der Regel am häufigsten benutzt, wenn man mit Git arbeitet. "
                           "\n\nDas bisher gelernte kratzt jedoch nur an der Oberfläche dessen, was mit Git möglich ist. Git bietet noch zahlreiche nützliche Befehle, "
                           "die wir in diesem Teil des Tutorials lernen werden. Außerdem wollen wir uns ein Remote Repository auf dem GitLab-Server "
                           "des Instituts anlegen und die Interaktion zwischen lokalem und Remote Repository erkunden.")
        additional = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, wrap="word", pady=5, padx=5)
        additional.place(x=0, rely=0.82, relwidth=1, relheight=0.15)
        additional.insert("1.0", "Dieser Teil des Tutorials funktioniert geauso wie der erste. Du bekommst "
                           "Informationen zu einer bestimmten Struktur oder einem Befehl und sollst diesen dann im integrierten Terminal ausführen."
                                 "\nDu kannst das Tutorial auch nebenbei in einem extra Terminal ausführen, musst jedoch auch hier darauf achten, "
                                 "dass einige der Befehle abhängig vom Betriebssystem sind.")

        img = tk.PhotoImage(file="./img/generalstructure.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.15, rely=0.30)


class Preparation(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if command == "mkdir new_repo":
                if os.system(command) == 0:
                    output['text'] = "Das Verzeichnis 'new_repo' wurde angelegt."
                elif platform.system() == "Windows" and os.system(command) != 0:
                    output['text'] = "Das Verzeichnis existiert bereits!"
                elif platform.system() != "Windows" and os.system(command) == 256:
                    output['text'] = "Das Projekt existiert bereits."
            elif command == "cd new_repo":
                try:
                    os.chdir("./new_repo")
                    output['text'] = "Gewechselt in das Verzeichnis 'new_repo'.{}".format(os.getcwd())
                    task1['bg'] = '#6b9e1f'
                except:
                    if os.getcwd().endswith("new_repo"):
                        output['text'] = "Du befindest dich bereits im new_repo-Verzeichnis. {}".format(os.getcwd())
                        task1['bg'] = '#6b9e1f'
                    else:
                        output['text'] = "Bist du sicher, dass du einen Projektordner namens 'new_repo' angelegt hast?"
            elif command == "git init":
                if os.getcwd().endswith("new_repo"):
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task2['bg'] = fu_green
                else:
                    output['text'] = "Du befindest dich nicht im Verzeichnis new_repo. Wechsel in das Verzeichnis!"
            elif command == "git status":
                if os.getcwd().endswith("new_repo"):
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                else:
                    output['text'] = "Du befindest dich nicht im Verzeichnis new_repo. Wechsel in das Verzeichnis!"
            elif command.startswith("git add"):
                if os.getcwd().endswith("new_repo"):
                    subprocess.check_output(command, shell=True)
                    output['text'] = "Datei wurde zur Versionierung vorgemerkt."
                else:
                    output['text'] = "Du befindest dich nicht im Verzeichnis new_repo. Wechsel in das Verzeichnis!"
            elif command.startswith("git commit -m"):
                if os.getcwd().endswith("new_repo"):
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task4['bg'] = fu_green
                else:
                    output['text'] = "Du befindest dich nicht im Verzeichnis new_repo. Wechsel in das Verzeichnis!"
            elif command == "touch first.txt":
                if os.getcwd().endswith("new_repo"):
                    if platform.system() == "Windows":
                        try:
                            subprocess.check_output("<nul (set/p z=)>first.txt", shell=True)
                            output['text'] = "Die Datei first.txt wurde angelegt."
                        except:
                            pass
                    else:
                        subprocess.check_output(command, shell=True)
                    output['text'] = "Die Datei first.txt wurde erfolgreich angelegt."
                else:
                    output['text'] = "Du befindest dich nicht im Verzeichnis new_repo. Wechsel in das Verzeichnis!"
            elif command == "touch second.txt":
                if os.getcwd().endswith("new_repo"):
                    if platform.system() == "Windows":
                        try:
                            subprocess.check_output("<nul (set/p z=)>second.txt", shell=True)
                            output['text'] = "Die Datei second.txt wurde angelegt."
                        except:
                            pass
                    else:
                        subprocess.check_output(command, shell=True)
                    output['text'] = "Die Datei second.txt wurde erfolgreich angelegt."
                else:
                    output['text'] = "Du befindest dich nicht im Verzeichnis new_repo. Wechsel in das Verzeichnis!"
            elif command == "touch third.txt":
                if os.getcwd().endswith("new_repo"):
                    if platform.system() == "Windows":
                        try:
                            subprocess.check_output("<nul (set/p z=)>third.txt", shell=True)
                            output['text'] = "Die Datei third.txt wurde angelegt."
                            task3['bg'] = fu_green
                        except:
                            pass
                    else:
                        subprocess.check_output(command, shell=True)
                    output['text'] = "Die Datei third.txt wurde erfolgreich angelegt."
                    task3['bg'] = fu_green
                else:
                    output['text'] = "Du befindest dich nicht im Verzeichnis new_repo. Wechsel in das Verzeichnis!"
            else:
                output['text'] = "Prüfe deine Syntax!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="2. Vorbereitungen", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, wrap="word", pady=5,
                       padx=5)
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.54)
        text.insert("1.0",
                    "Im vorherigen Teil des Tutorials haben wir ein Repository angelegt und in diesem zahlreiche Befehle ausprobiert. "
                    "Das wollen wir im jetzigen Teil des Tutorials auch machen. In einem neuen Repository können wir, "
                    "wie bereits im ersten Teil, Dateien anlegen, versionieren und unterschiedliche Git-Befehle ausprobieren."
                    "\n\nHier eine kleine Erinnerung an die im ersten Teil schon verwendeten Befehle:"
                    "\n- mkdir Verzeichnisname (Anlegen eines Verzeichnisses)"
                    "\n- cd Verzeichnisname (Wechseln in das angegebene Verzeichnis)"
                    "\n- git init (Anlegen eines Repositorys)"
                    "\n- touch Dateiname (Anlegen einer leeren Datei mit dem angegebenen Namen)"
                    "\n- git add (Vormerken zur Versionierung)"
                    "\n- git commit -m \"Commitmessage\" (Aktuelle Projektversion speichern)")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.65)
        task1 = tk.Label(description_container, text="1. Lege einen neuen Ordner namens 'new_repo' an und wechsel in dieses Verzeichnis..",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.72)
        task2 = tk.Label(description_container,
                         text="2. Initiiiere ein Repository in diesem Verzeichnis",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.79)
        task3 = tk.Label(description_container,
                         text="3. Lege 3 neue Dateien an: first.txt, second.txt und third.txt",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task3.place(x=0, rely=0.86)
        task4 = tk.Label(description_container,
                         text="4. Merke alle Dateien zur Versionierung vor und commite sie.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task4.place(x=0, rely=0.93)


        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()),
                               bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class GitDiff(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if command == "echo \"Der erste Inhalt\" >> first.txt":
                subprocess.check_output(command, shell=True)
                output['text'] = "Inahlt in die Datei first.txt geschrieben."
                task1['bg'] = fu_green
            elif command == "git diff first.txt":
                if os.getcwd().endswith("new_repo"):
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task2['bg'] = fu_green
                else:
                    output['text'] = "Wechsel bitte zuerst in das new_repo-Verzeichnis!"
            else:
                output['text'] = "Überprüfe deine Syntax!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="3. Git diff", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.65)
        text.insert("1.0", "Wenn man sehr viele Änderungen macht, kann man schnell mal den Überblick verlieren welche man gemacht hat. "
                           "Der Befehl 'git status' hilft ja bereits, um zu sehen, an welcher Datei Veränderungen vorgenommen wurden."
                           " Das ist schön und gut, aber man will natürlich auch wissen, was genau man in der Datei verändert hat. "
                           "Vor allem, wenn die Änderungen nicht von einem selbst stammen. "
                           "\n\nHierzu gibt es den Befehl 'git diff Dateiname'."
                           " Dieser zeigt einem alle gemachten Änderungen in der Datei an. Hier wird verglichen zwischen "
                           "dem Inhalt der Datei beim letzten Commit und dem Inhalt, der seitdem dazugekommenen ist und nicht commited wurde."
                           " Alle von Änderungen betroffenen Codezeilen werden dann im Terminal angezeigt. Genauer gesagt, werden beide Versionen angezeigt: "
                           "die alte und die neue Version."
                           " Die alte Version des Codes wird mit einem Minus gekennzecihnet, die neue Version mit einem Plus."
                           "\n\nIm vorherigen Schritt haben wir die leere Datei first.txt commited und werden nun einen neuen Satz in diese Datei schreiben, "
                           "der dann durch 'git diff' markiert werden sollte.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.77)
        task1 = tk.Label(description_container, text="1. Schreibe den Text \"Der erste Inhalt\" in die Datei first.txt.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.84)
        task2 = tk.Label(description_container, text="2. Lass dir die Unterschiede in der first.txt anzeigen",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.92)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()),
                               bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class GitCheckout(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if os.getcwd().endswith("new_repo"):
                if command == "git checkout first.txt":
                    subprocess.check_output(command, shell=True)
                    output['text'] = "Alle Änderungen in der Datei first.txt wurden rückgängig gemacht"
                    task1['bg'] = fu_green
                elif command == "git status":
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task2['bg'] = fu_green
                else:
                    output['text'] = "Überprüfe deine Syntax!"
            else:
                output['text'] = "Du befindest dich nicht im new_repo-Verzeichnis! Gehe ein paar Schritte zurück " \
                                 "und wechsel in das Verzeichnis!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="4. Git checkout", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.65)
        text.insert("1.0", "Es kann natürlich vorkommen, dass man eine Weile an seinem Projekt gearbeitet hat und irgendwann merkt,"
                           " dass man totalen Blödsinn gemacht hat und eigentlich alles rückgängig machen will. "
                           "Hierzu gibt es verscheidene Möglichkeiten, die speziell auf den Versionierungssstatus der Änderungen bezogen sind."
                           "\n\nZuerst wollen wir Änderungen rückgängig machen, die noch nicht zum Commit vorgemerkt sind und auch noch nicht commited wurden. "
                           "Also Änderungen, die bisher nur im Working Directory zu finden sind."
                           "\n\nHierzu gibt es den Befehl 'git checkout' den man entweder auf eine bestimmte Datei beziehen kann 'git checkout Dateiname' oder "
                           "auf alle gemachten Änderungen 'git checkout *'."
                           "\n\nNachdem du mit 'git checkout' die Änderungen in der first.txt rückgängig gemacht hast, kannst du den Status des Repositorys prüfen. "
                           "Du solltest sehen, dass die Datei 'first.txt' nicht mehr angezeigt wird, da alle Änderungen rückgängig gemacht wurden.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.77)
        task1 = tk.Label(description_container, text="1. Mache alle Änderungen in der first.txt rückgängig.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.84)
        task2 = tk.Label(description_container, text="2. Prüfe den Änderungsstatus deines Repositorys.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.92)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()),
                               bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)

        img = tk.PhotoImage(file="./img/gitcheckout.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.815, rely=0.76)


class GitReset(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if os.getcwd().endswith("new_repo"):
                if file_exists("second.txt"):
                    if command == "git add second.txt":
                        subprocess.check_output(command, shell=True)
                        output['text'] = "Die Datei second.txt wurde zur Versionierung vorgemerkt!"
                        task2['bg'] = fu_green
                    elif command == "git status":
                        response = subprocess.check_output(command, shell=True)
                        output['text'] = response
                    elif command == "git reset second.txt":
                        subprocess.check_output(command, shell=True)
                        output['text'] = "Vormerkung der Datei second.txt rückgängig gemacht!"
                        task3['bg'] = fu_green
                    elif command == "echo \"Das hier wird vorgemerkt.\" >> second.txt":
                        subprocess.check_output(command, shell=True)
                        output['text'] = "Der Satz wurde in die Datei second.txt geschrieben."
                        task1['bg'] = fu_green
                    else:
                        output['text'] = "Überprüfe deine Syntax!"
                else:
                    output['text'] = "Die Datei second.txt existiert nicht.\nGehe einige Schritte zurück und erledige alle Aufgaben!"
            else:
                output['text'] = "Du befindest dich nicht im Verzeichnis gitcourse.\n Gehe zurück zu Schritt ... und " \
                                 "wechsel das Verzeichnis!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="5. Git reset", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.61)
        text.insert("1.0", "Es kann vorkommen, dass man in einem Projekt Änderungen gemacht und zur Versionierung vorgemerkt hat, "
                           "die man eigentlich doch nicht versionieren möchte. "
                           "Das ist natürlich ungünstig und deswegen will man diese dann wieder aus der Vormerkungen herausnehmen. "
                           "Hierzu bietet Git den Befehl 'git reset'. Mit 'git reset Dateiname' kann man eine oder meherere "
                           "Dateien aus der Staging Area entfernen."
                           "\nIm Status-Bereich von Git werden die Änderungen also aus der Staging Area ('Zum Commit vorgemerkte Änderungen') "
                           "zurück in das Working Directory verschoben ('Unversionierte Dateien' oder 'Nicht zum commit vorgemerkte Änderungen')"
                           "\n\nDas wollen wir mal ausprobieren. Zuerst schreiben wir den Text 'Das hier wird vorgemerkt.' "
                           "in die 'second.txt' und merken diese Änderungen zur Versionieurng vor."
                           " Die Vormerkung können wir uns mit 'git status' anzeigen lassen"
                           " und mit 'git reset Dateiname' machen wir diese Vormerkung rückgängig. Mit 'git status' "
                           "sollte man nun sehen, dass die Änderungen nicht mehr in der Staging Area (Zum Commit vorgemerkt) gelistet sind.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.72)
        task1 = tk.Label(description_container, text="1. Schreibe \"Das hier wird vorgemerkt.\" in die Datei second.txt.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.79)
        task2 = tk.Label(description_container, text="2. Merke die second.txt zur Versionierung vor.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.86)
        task3 = tk.Label(description_container, text="3. Mache den Staging-Prozess der second.txt-Datei rückgängig.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task3.place(x=0, rely=0.93)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()),
                               bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)

        img = tk.PhotoImage(file="./img/gitreset.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.65, rely=0.75)


class GitLog(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if os.getcwd().endswith("new_repo"):
                if command == "git log":
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task1['bg'] = fu_green
                else:
                    output['text'] = "Überprüfe deine Syntax!"
            else:
                output['text'] = "Du befindest dich nicht im new_repo-Verzeichnis! Gehe ein paar Schritte zurück und" \
                                 " wechsel in das Verzeichnis!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="6. Git log", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=0.6, relheight=0.4)
        text.insert("1.0", "Im Laufe der Bearbeitung eines Projektes archiviert man sehr viele Projektversionen."
                           " Hierzu ist es auch gut, einen Überblick über alle Versionen zu haben, vor allem, wenn man "
                           "doch mal zu einer früheren Version zurückkehren möchte."
                           "\n\nHierzu stellt Git das Werkzeug der Commit-History bereit. Diese beinhaltet die Liste aller gemachten"
                           "Commits, also aller versionierten Projektversionen. ")
        text2 = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5, wrap="word")
        text2.place(x=0, rely=0.51, relwidth=1, relheight=0.32)
        text2.insert("1.0", "Mit dem Befehl 'git log' kann man sich diese Commit-History anzeigen lassen. Jeder Eintrag enhält den Autor des Commits, "
                           "den Zeitstempel, die mitgelieferte Commitmessage sowie eine Referenz. Diese Referenz ist einen "
                           "eindeutige Zahlen- und Buchtsbenkombination, die einem Commit zugeordnet ist."
                           "\n\nHier zeigt sich außerdem, warum es so wichtig ist, eine vernünftige Commitmessage mitzuliefern, "
                           "da man sonst sehr schwer nachvollziehen kann welche Änderungen in den jeweiligen Commits gemacht "
                           "wurden.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.84)
        task1 = tk.Label(description_container, text="1. Lass dir die Commit-History anzeigen.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.92)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()),
                               bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)

        img = tk.PhotoImage(file="./img/commitmessages.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.62, rely=0.05)


class GitResetSoftDescription(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="7. Git reset soft", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.05, relwidth=1, relheight=0.38)
        text.insert("1.0", "Warum haben wir uns nun die Commit-History angesehen? Um einen Überblick über alle Commits zu "
                           "haben und so die Möglichkeit, alte Commits wiederherzustellen bzw. Commits rückgängig zu machen oder zu löschen."
                           "\n\nEs kann vorkommen, dass man eine Projektversion archiviert hat, also ins Repository committet."
                           " Merkt man jedoch, dass man vielleicht noch nicht fertig war mit den Änderungen, dann gibt es eine Möglichkeit,"
                           "eine Projektversion aud dem Repository zurück in die Staging Area zu holen. Man macht also "
                           "einen Commit rückgängig, jedoch ohne die Änderungen zu verlieren."
                           "\n\nHierzu gibt es den Befehl 'git reset --soft HEAD'."
                           "\nUnd genau hier kommt die Commit-History ins Spiel. Es gibt mehrere Wege, auf einen früheren Commit zurückzusetzen."
                           " Man kann mit 'HEAD~1' einen Commit (oder entsprechend der Zahl mehrere Commits) zurückspringen. "
                           "Bei einer großen Menge an Commits wird das aber irgendwann etwas schwierig, auch wenn es selten vorkommt, dass man so weit zurückgeht.")

        img = tk.PhotoImage(file="./img/resetsoft.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.17, rely=0.48)


class GitResetSoft(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if os.getcwd().endswith("new_repo"):
                if file_exists("third.txt"):
                    if command == "git log":
                        response = subprocess.check_output(command, shell=True)
                        output['text'] = response
                        task2['bg'] = fu_green
                    elif command == "git status":
                        response = subprocess.check_output(command, shell=True)
                        output['text'] = response
                        task4['bg'] = fu_green

                    elif command == "git add third.txt":
                        subprocess.check_output(command, shell=True)
                        output['text'] = "Die Datei third.txt wurde zur Archivierung vorgemerkt."
                    elif command.startswith("git commit -m"):
                        response = subprocess.check_output(command, shell=True)
                        output['text'] = response
                        task1['bg'] = fu_green
                    elif command == "git reset --soft HEAD~1":
                        subprocess.check_output(command, shell=True)
                        output['text'] = "Der Commit wurde rückgängig gemacht und die Änderungen wurden in die Staging" \
                                         " Area übernommen."
                        task3['bg'] = fu_green
                    elif command == "echo \"Diese Änderungen gehen nicht verloren\" >> third.txt":
                        subprocess.check_output(command, shell=True)
                        output['text'] = "Der Satz 'Diese Änderungen eghen nicht veloren' wurde in die third.txt geschrieben."
                    else:
                        output['text'] = "Prüfe deine Syntax!"
                else:
                    output['text'] = "die datei third.txt existiert nicht.\nGehe einige schritte zurück und arbeite die Aufgaben nacheinander ab!"
            else:
                output['text'] = "Du befindest dich nicht im new_repo-Verzeichnis.\nGehe einige Schritte zurück und befolge die Aufgaben."

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="8. Git reset soft", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.37)
        text.insert("1.0", "Nun wollen wir mit 'git reset --soft HEAD~1' den letzten Commit zurücksetzen. Die dort "
                           "gespeicherten Änderungen also zurück in die Staging Area verschieben."
                           "\nDa wir bisher nur einen Commit in der History haben, speichern wir einen neuen. "
                           "Hierzu wollen wir zuerst die Datei third.txt verändern und dann versionieren."
                           " Nun können wir die Commit-History checken und sollten den neuen Commit sehen."
                           " Diesen können wir dann rückgängig machen, was sowohl die Entfernung des Commits aus der "
                           "Commit-History bewirkt als auch Veränderungen im Status des Repositorys.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.63)
        task1 = tk.Label(description_container, text="1. Schreibe 'Diese Änderungen gehen nicht verloren' in die third.txt und versioniere sie. (add & commit)",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.70)
        task2 = tk.Label(description_container, text="2. Lass dir die Commit-History anzeigen",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.77)
        task3 = tk.Label(description_container, text="3. Mach den Commit rückgängig.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task3.place(x=0, rely=0.84)
        task4 = tk.Label(description_container, text="3. Prüfe, ob die zuvor commiteten Änderungen nun in der Staging Area vorgemerkt sind. ",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task4.place(x=0, rely=0.92)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()),
                               bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)

        img = tk.PhotoImage(file="./img/gitresetsoft.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.37, rely=0.4)


class GitResetHardDescription(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="9. Git reset hard", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.07, relwidth=1, relheight=0.35)
        text.insert("1.0", "Man kann also Commits rückgängig machen, ohne dass die Veränderungen verloren gehen und dann "
                           "weiter an dieser Projektversion arbeiten und irgendwann, wenn man fertig ist, erneut committen."
                           "\n\nEs kommt aber auch vor, dass man etwas komplett nicht mehr braucht oder aus versehen etwas "
                           "so doll kaputt gemacht hat, dass es nicht mehr funktioniert und man den Code auch wirklich "
                           "nicht mehr haben will."
                           "\n\nHierzu gibt es dann den Befehl 'git reset --hard HEAD'. Dieser funktioniert äquivalent zum "
                           "vorherigen Befehl, nur dass hier die archivierte Version komplett weggeschmissen wird. Will "
                           "man also auf den vorvorletzen Commit vor dem aktuellen zurücksetzen, werden alle Commits und "
                           "Änderungen nach dem vorvorletzen komplett gelöscht. Und hiermit ist das unwiederbringliche Löschen gemeint.")

        img = tk.PhotoImage(file="./img/resethard.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.17, rely=0.45)


class GitResetHard(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if os.getcwd().endswith("new_repo"):
                if file_exists("third.txt"):
                    if command.startswith("git commit -m"):
                        response = subprocess.check_output(command, shell=True)
                        output['text'] = response
                        task1['bg'] = fu_green
                    elif command == "git status":
                        response = subprocess.check_output(command, shell=True)
                        output['text'] = response
                        task4['bg'] = fu_green
                    elif command == "git log":
                        response = subprocess.check_output(command, shell=True)
                        output['text'] = response
                        task2['bg'] = fu_green
                    elif command == "git reset --hard HEAD~1":
                        subprocess.check_output(command, shell=True)
                        output['text'] = "Letzter Commit wurde gelöscht!"
                        task3['bg'] = fu_green
                    else:
                        output['text'] = "Prüfe deine Syntax!"
                else:
                    output['text'] = "Die Datei third.txt existiert nicht.\nGehe einige Schritte zurück und erledige die dort gestellten Aufgaben!"
            else:
                output['text'] = "Du befindest dich nicht im Verzeichnis new_repo.\n" \
                                 "Gehe einige Schritte zurück und erledige alle dort angegebenen Aufgaben!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="10. Git reset hard", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.38)
        text.insert("1.0", "Jetzt wollen wir einen Commit komplett löschen. Dazu wiederholen wir einen Teil der Schritte "
                           "aus dem Teil des Soft-Resets."
                           "Wir merken erneut die Datei 'third.txt' vor, commiten sie "
                           "und können uns den neuen Commit erneut in der Commit-History ansehen."
                           "\n\nNun wollen wir den Commit rückgängig machen bzw. entsorgen indem wir den Befehl 'git reset --hard HEAD~1' ausführen. "
                           "Hiermit stellen wir den vorletzten Commit wieder her und löschen den letzten Commit komplett."
                           " Das bedeutet, die Änderungen des letzten Commits werden NICHT in die Staging Area verschoben sondern unwiederbringlich gelöscht!")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.63)
        task1 = tk.Label(description_container, text="1. Committe die Änderungen der third.txt.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.70)
        task2 = tk.Label(description_container, text="2. Lass dir die Commit-History anzeigen",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.77)
        task3 = tk.Label(description_container, text="3. Lösche den Commit.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task3.place(x=0, rely=0.84)
        task4 = tk.Label(description_container,
                         text="4. Kontrolliere, ob die zuvor versionierten Änderungen NICHT in der Staging Area gelistet sind.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task4.place(x=0, rely=0.92)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()),
                               bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)

        img = tk.PhotoImage(file="./img/gitresethard.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.45, rely=0.50)

#######################################################################################################################
class RemoteRepository(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="11. Remote Repository", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.07, relwidth=1, relheight=0.22)
        text.insert("1.0", "Nun kennen wir die wichtigsten und am häufigsten genutzten Befehle, um lokal "
                           "Projektsoftware oder -inhalt zu versionieren. Nun wollen wir uns mit dem Remote Repository "
                           "und der Platform GitLab auseinandersetzen."
                           "\nHierzu musst du dich mit deinem Institutsaccount auf dem GitLab-Server anmelden: gitlab.met.fu-berlin.de"
                           "\n\nHier beitet dir ein kleiner grüner Button die Möglichkeit, ein neues Repository anzulegen. Was wir jetzt auch machen wollen.")
        text3 = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text3.place(x=0, rely=0.43, relwidth=1, relheight=0.17)
        text3.insert("1.0", "Hast du diesen Button gedrückt, kannst du dein neues, leeres Repository benennen. Wir wollen es 'first_repo' nennen."
                            "\n\nWir haben nun ein neues, leeres Repository, dass sich momentan jedoch nur auf dem GitLab-Server des Instituts befindet, "
                            "aber noch nicht auf deinem Rechner. Das wollen wir gleich ändern.")

        img = tk.PhotoImage(file="./img/newremoterepo.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.12, rely=0.3)

        img = tk.PhotoImage(file="./img/remotereponaming.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.12, rely=0.61)


class SSHKey(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="12. SSH-Key", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.07, relwidth=1, relheight=0.40)
        text.insert("1.0", "Nun haben wir ein Remote Repository auf dem GitLab-Servers des Instituts. "
                           "Jede Interaktion mit dem Remote Remote Repository über die Konsole würde eine Abfrage deiner"
                           " Benutzerdaten fordern, also Benutzername und Passwort. Das ist auf Dauer relativ hinderlich und so gibt es die "
                           "Möglichkeit, einen SSH-Key zu hinterlegen. Dieser besteht aus einem öffentlichen und einem privaten Teil."
                           "Den Schlüssel erzeugst du auf deinem Rechner und hinterlegst den öffentlichen teil des Schlüssels im GitLab. "
                           "So kommunizieren der GitLab-Server und dein rechner über ein gesicherte Verbindung, ohne jedes mal deine Nutzerdaen "
                           "eingeben zu müssen."
                           "\n\nUm einen SSH-Key zu hinterlgen, musst du im GitLab auf dein Profil unter Settings nach SSH-Key suchen."
                           " Dort kannst du für jeden Rechner einen SSH-Schlüssel hinterlegen. "
                           " Am oberen Ende der Seite, auf der man SSH-Schlüssel hinterlegen kann, befindet sich ein Link, der erklärt, "
                           "wie man für sein Betriebssystem einen Schlüssel erzeugt und hinterlegt."
                           "\n\nSobald du einen Schlüssel erzegt und hinterlegt hast, können wir zum nächsten Schritt übergehen.")


        img = tk.PhotoImage(file="./img/addkey.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0, rely=0.5)

        img = tk.PhotoImage(file="./img/sshguide.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.5, rely=0.5)


class CloneRepo(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if command == "cd ..":
                try:
                    os.chdir("..")
                    output['text'] = "Gewechselt in das Verzeichnis '..'.{}".format(os.getcwd())
                    task1['bg'] = '#6b9e1f'
                except:
                    output['text'] = "Es ist ein Fehler aufgetreten."
            elif command == "cd first_repo":
                try:
                    os.chdir("./first_repo")
                    output['text'] = "Gewechselt in das Verzeichnis 'first_repo'.{}".format(os.getcwd())
                    task2['bg'] = fu_green
                except:
                    if os.getcwd().endswith("first_repo"):
                        output['text'] = "Du befindest dich bereits im first_repo-Verzeichnis. {}".format(os.getcwd())
                        task2['bg'] = fu_green
                    else:
                        output['text'] = "Bist du sicher, dass du das Repository geklont hast?"
            elif command.startswith("git clone"):
                #if not os.getcwd().endswith("git_tutorial"):
                #    output['text'] = "Du befindest dich nicht im übergeordneten Verzeichnis, Wechsel bitte!"
                #else:
                subprocess.check_output(command, shell=True)
                output['text'] = "Respository geklont"
            else:
                output['text'] = "Überprüfe deine Syntax!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="13. Repository klonen", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.57)
        text.insert("1.0", "Nun haben wir einen SSH-Key an- und hinterlegt, damit dieser Rechner jederzeit ohne Passwortabfrage mit "
                           "dem GitLab-Server des Instituts kommunizieren kann."
                           "\n\nJetzt wollen wir das leere Repository, das wir vorhin angelegt haben, auf unseren Rechner übertragen."
                           " Hierzu klont man dieses mit dem Befehl 'git clone'. Wir wollen das Repository von dem GitLab-Server des "
                           "Instituts klonen und müssen im Befehl den Ort benennen, von dem das Repository geklont werden muss."
                           "\nDieser Ort ist ein Link zum Remote Repository, der in deinem leeren Repository auf der GitLab-Seite angezeigt wird."
                           " Den dort angezeigten Befel kopierst du einfach und überträgst ihn ins Terminal, wo du ihn ausführst."
                           "\n\nIm Moment befinden wir uns noch im Verzeichnis new_repo. Hier wollen wir nun nicht mehr "
                           "arbeiten, wir müssen also in den darübergelegenen Ordner (..) wechseln.")
        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.77)
        task1 = tk.Label(description_container, text="1. Wechsle in das übergeordnete Verzeichnis.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.84)
        task2 = tk.Label(description_container, text="2. Klone dein neues Repository und wechsel in das neue Repository.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.92)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()),
                               bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)

        img = tk.PhotoImage(file="./img/clonerepo.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.42, rely=0.7)


class GitPush(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if not os.getcwd().endswith("first_repo"):
                output['text'] = "Du befindest dich nicht im Verzeichnis first_repo. Gehe einen Schritt zurück und wechsel bitte!"
            else:
                if command == "git push -u origin master":
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task2['bg'] = fu_green
                elif command == "touch main.txt":
                    if platform.system() == "Windows":
                        try:
                            subprocess.check_output("<nul (set/p z=)>main.txt", shell=True)
                            output['text'] = "Die Datei main.txt wurde angelegt."
                        except:
                            pass
                    else:
                        subprocess.check_output(command, shell=True)
                    output['text'] = "Die Datei main.txt wurde erfolgreich angelegt."
                elif command == "git add main.txt" or command == "git add .":
                    subprocess.check_output(command, shell=True)
                    output['text'] = "Die Datei wurde voremerkt."
                elif command.startswith("git commit -m"):
                    subprocess.check_output(command, shell=True)
                    output['text'] = "Änderungen committet."
                    task1['bg'] = fu_green
                else:
                    output['text'] = "Prüfe deine Syntax!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="14. Git push", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.66)
        text.insert("1.0", "Nun haben wir das leere neue Repository auf unseren Rechner kopiert und wollen es befüllen. "
                           "Dazu legen wir mit dem touch-Befehl eine neue Datei an und merken sie erst zur Versionierung "
                           "vor und dann committen wir sie."
                           "\n\nSo haben wir dann eine neue Projektversion, die sich jedoch nur lokal auf unserem Rechner befindet. "
                           "Wenn wir das Repository mitsamt Commit-History jetzt auf den GitLab-Server kopieren wollen,"
                           "verwenden wir den Befehl 'git push'."
                           "\nIn der Regel ist dies der Befehl, mit dem man das lokale Repository auf den Server kopiert. Beim allerersten Push zum Server jedoch,"
                           "muss mann den Befehl ergänzen: 'git push -u origin master'."
                           "\n\nDer Befehl speichert mit '-u origin' die URL, von der wir zuvor das Repositroy geklont haben als Ursprungs-URL,"
                           "die bei jedem Push als Adresse des Remote Repositorys auf dem Server verwendet wird. Mit 'master' wird"
                           "ein sogenannter Branch gesetzt. Branches sind ein wichitges und mächtiges Werkzeug in Git, werden hier"
                           "aber nicht weiter thematisiert, weil das unnötig komplex wäre.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.77)
        task1 = tk.Label(description_container, text="1. Lege die Datei main.txt an, merke sie vor und committe sie.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.84)
        task2 = tk.Label(description_container, text="2. Pushe eine Kopie deines lokalen Repositorys auf den GitLab-Server.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.92)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()),
                               bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)

        img = tk.PhotoImage(file="./img/gitpush.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.66, rely=0.77)


class RemoteChanges(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="15. Remote Changes", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.07, relwidth=1, relheight=0.28)
        text.insert("1.0", "Nun wissen wir, wie man die Version des lokalen Repositorys auf den Server kopiert. "
                           "Die Platform GitLab bietet die Möglichkeit, auch über die Online-Oberfläche den Inhalt des Projektes zu bearbeiten."
                           "Wir wollen jetzt in unserer main.txt-Datei ein paar Änderungen vornehmen."
                           "\n\nHierzu gibt es bei der Auswahl der Datei einen Button 'Edit'. Daraufhin öffnet sich ein Editor, in dem man die Datei bearbeiten kann."
                           " Wir schreiben einfach ein paar Sätze in die Datei. Sind alle Änderungen gemacht, "
                           "kann man unter dem Editors noch eine Commit-Message eingeben und die Änderungen dann speichern."
                           "\n\nJede Änderung über die Web-GUI wird sofort als Commit gespeichert.")

        img = tk.PhotoImage(file="./img/editfile.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.12, rely=0.35)

        img = tk.PhotoImage(file="./img/remotechanges.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.19, rely=0.48)


class GitPull(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if not os.getcwd().endswith("first_repo"):
                output['text'] = "Du befindest dich nicht im Verzeichnis first_repo. Gehe einige Schritte zurück und wechsel bitte!"
            else:
                if command == "git pull":
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task1['bg'] = fu_green
                else:
                    output['text'] = "Prüfe deine Syntax!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="16. Git pull", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.4)
        text.insert("1.0", "So nun haben wir online Änderungen an unserem Projekt vorgenommen und somit auch das Repository verändert."
                           "\n\nWie bekommen wir nun jedoch die aktuelle Version des Repositorys auf unseren Rechner, um da weiterzuarbeiten?"
                           "\n\nHierzu gibt es den Befehl 'git pull'. Dieser kopiert das online gespeicherte Remote Repository mitsamt Commit-History und überträgt alle Änderungen "
                           "auf das lokale Repository.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.84)
        task1 = tk.Label(description_container, text="1. Kopiere den Inhalt des Remote Repositorys in dein lokales Repository.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.92)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()),
                               bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)

        img = tk.PhotoImage(file="./img/gitpull.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.25, rely=0.55)


class MergeConflict(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="17. Mergekonflikte", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.07, relwidth=1, relheight=0.5)
        text.insert("1.0", "Es kann jedoch passieren, dass man lokal an seinem Projekt arbeitet und gleichzeitig jemand anderes"
                           " eine neue Version ins Remote Repository gespeichert hat."
                           " Man arbeitet also lokal mit einer veraltetetn Version des Projektes."
                           "\n\nWill man die eigenen Änderungen nun in das Remote Repository pushen, kann es zu Problemen kommen."
                           " Git kann Änderungen zusammenführen aber manchmal kann es sein, dass Änderungen an der gleichen Datei "
                           "gemacht werden und an diesem Punkt weiß Git nicht, wie diese Änderungen zusammengeführt werden sollen."
                           " Es kommt zu einem sogenannten Mergekonflikt."
                           "\n\nAlle Dateien, die Mergekonflikte enthalten, werden mit 'git status' unter dem Punkt 'Nicht zusammengeführt Pfade' gelistet."
                           " Der betroffene Code in der Datei wird gekennzeichnet."
                           " Der Code zwischen <<<<<<< HEAD und ======== ist die Version des Codes die sich im Remote Repsoitory befindet."
                           " Der Code zwischen ==== und >>>>>> Commit-Referenz (Buchstaben- und Zahlenkombination) enthält die Version deiner Änderungen."
                           "\n\nDa solche Mergekonflikte öfters mal auftreten können, wenn man mit mehreren Leuten im Team an einem Projekt arbeitet, "
                           "muss man auch wissen, wie man einen solchen Mergekonflikt löst.")


class CreateMergeConflict(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if os.getcwd().endswith("first_repo"):
                if command == "git add ." or command == "git add main.txt":
                    subprocess.check_output(command, shell=True)
                    output['text'] = "Die Datei main.txt wurde vorgemerkt."
                elif command.startswith("git commit -m"):
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task2['bg'] = fu_green
                else:
                    output['text'] = "Prüfe deine Syntax!"
            else:
                output['text'] = "Du befindest dich nicht im first_repo-Verzeichnis.\nGehe einige Schritte zurück und erledige die Aufgaben!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="18. Mergekonflikte provozieren", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.5)
        text.insert("1.0","Nun wollen wir einen Megrkonflikt auslösen. Hierzu werden wir die Datei main.txt zum einen lokal verändern"
                          " und dann außerdem im Remote Repository. Da wir dann zwei unterschiedlcihe Projektversionen haben, "
                          "die in ein und derselben Datei Änderungen aufweisen, weiß Git nicht, wie die Änderungen zusammengeführt werden sollen."
                          "\n\nEine gute Praxis, um Mergekonflikte so gut es geht zu vermeiden ist es, bevor man mit der Arbeit am "
                          "Projekt anfängt, jedes mal zu zu pullen. So hat man immer die neustes Version des projektes und sollten doch mal parallel "
                          "Änderungen gemacht worden sein, kann Git sie entweder selbstständig zusammenführen oder man muss den Konflikt selbst lösen.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.72)
        task1 = tk.Label(description_container,
                         text="1. Öffne, ändere und speichere die main.txt mit einem Editor deiner Wahl. (wird nicht markiert)",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.79)
        task2 = tk.Label(description_container,
                         text="2. Versioniere diese Änderung: git add und git commit.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.86)
        task3 = tk.Label(description_container,
                         text="3. Öffne die main.txt über die Web-GUI und bearbeite und speichere sie.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task3.place(x=0, rely=0.93)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()),
                               bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)



class ResolveMergeConflicts(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if os.getcwd().endswith("first_repo"):
                if command == "git pull":
                    subprocess.check_output(command, shell=True)
                    output['text'] = "Mergekonflikt!"
                    task1['bg'] = fu_green
                elif command == "git add main.txt" or command == "git add .":
                    subprocess.check_output(command, shell=True)
                    output['text'] = "Datei wurde vorgemerkt."
                elif command.startswith("git commit -m"):
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task3['bg'] = fu_green
                elif command == "git push":
                    subprocess.check_output(command, shell=True)
                    output['text'] = "Die neuen Änderungen wurde auf das remote Repository übertragen."
                    task4['bg'] = fu_green
                else:
                    output['text'] = "Prüfe deine Syntax!"
            else:
                output['text'] = "Du befindest dich im falschen Verzeichnis. \nBitte gehe einige Schritte zurück und wechsel ins first-Repo-Verzeichnis!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="19. Mergekonflikte lösen", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.5)
        text.insert("1.0", "Wenn wir nun unsere lokalen Änderungen in das Remote Repository pushen wollen, beschwert sich Git, "
                           "dass es einen Mergekonflikt gibt. Wie löst man diesen nun auf?"
                           "\n\nMit 'git pull' holt man sich die Version des Remote Repositorys. Jetzt sind beide Versionen "
                           "in den betroffenen Dateien vermekrt und entsprechend markiert."
                           "\nNun gibt es drei Möglichkeiten, den Konflikt zu lösen. Entweder übernimmt man die eigene "
                           "Version, die Version aus dem Remote Repository oder man verbindet beide Versionen "
                           "zu einer neuen. "
                           "\nEntsprechend der Entscheidung löscht man die andere Version (oder eben nicht) "
                           "und dann löscht man noch alle Konfliktmarkierungen. Nun muss man diese komplett neue Version "
                           "der Datei wieder vormerken und comitten und dann kann man sie auch ins Remote Repostory pushen.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.65)
        task1 = tk.Label(description_container,
                         text="1. Pulle vom Remote Repository. (wird ggf. nicht grün markiert)",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.72)
        task2 = tk.Label(description_container,
                         text="2. Öffne einen Editor deiner Wahl und lösen den Mergekonflikt. (wird nicht grün markiert)",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.79)
        task3 = tk.Label(description_container,
                         text="3. Merke die Änderung zur Versionierung vor und committe sie.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task3.place(x=0, rely=0.86)
        task4 = tk.Label(description_container,
                         text="4. Pushe den gelösten Mergekonflikt ins Remote Repository",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task4.place(x=0, rely=0.93)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()),
                               bg=fu_green, fg="white")
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

        title = tk.Label(description_container, text="20. Zusammenfassung", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.07, relwidth=1, relheight=0.3)
        text.insert("1.0", "Großartig, du hast den zweiten Teil des Tutorials geschafft!"
                           "\n\nDu solltest jetzt eine ungefähre Vorstellung von Git und seinem Nutzen haben. Außerdem solltest du"
                           " die grundlegenden Strukturen und Befehle kennen, die man häufig verwendet. In der "
                           "Git-Dokumentation findest du noch ausführlichere Beschreibungen der Software und ihres Gebrauchs: https://git-scm.com/"
                           "\n\nAuch im zweiten Teil des Tutorials müssen Aufgaben bearbeitet und nachgewiesen werden:"
                           "\n1. Schicke mir den Link deines Remote Repositorys auf dem GitLab-Server"
                           "\n2. Bearbeite das Quiz und mache einen Screenshot von deinem Ergebnis"
                           "\n(Achtung beim klicken des Buttons öffen sich zwei Fenster. Das Fenster mit Fehlermeldung kann irgnoriert werden."
                           "\n Den Punkt für das Quiz gibt es nur bei mindestens 10 richtigen Antworten.")

        link1 = tk.Button(description_container, text="--> Quiz <--", fg="white", bg=fu_green, font="TkFont 12 bold",
                          cursor="hand2")
        link1.place(relx=0.25, rely=0.4, relwidth=0.5)
        link1.bind("<Button-1>", lambda e: callback("../questionaire/second_questionaire.html") or callback("./questionaire/second_questionaire.html"))

        img = tk.PhotoImage(file="./img/emergency.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.63, rely=0.5)

        additional = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        additional.place(relx=0.65, rely=0.84, relwidth=0.34, relheight=0.15)
        additional.insert("1.0", "Link und Sceenshot bis zum 06.05.2020 12:00 Uhr im Whiteboard hochladen. Fragen und Anmerkungen bitte per Mail an janaulrich@zedat.fu-berlin.de.")

        img = tk.PhotoImage(file="./img/generalstructure2.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0, rely=0.5)


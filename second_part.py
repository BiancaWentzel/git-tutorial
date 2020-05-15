# -*- coding: utf-8 -*-

import tkinter as tk
import subprocess
import os
import webbrowser
import platform

from utils import right_directory

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
        text.place(x=0, rely=0.07, relwidth=1, relheight=0.25)
        text.insert("1.0", "Im letzten Teil des Tutorials haben wir die grundlegenden Strukturen und Befehle von Git gelernt."
                           "Dies sind die Befehle, die man in der Regel am häufigsten benutzt, wenn man mit Git arbeitet. "
                           "\n\nAber wir haben bisher nur an der Oberfläche gekratzt. Git bietet noch zahlreiche nützliche Befehle, "
                           "die wir in diesem teil lernen werden. Außerdem wollen wir uns ein Remote Repository auf dem GitLab-Server "
                           "des Instituts anlegen und nützliche Features dieser Platform kennenlenrnen.")
        additional = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, wrap="word", pady=5, padx=5)
        additional.place(x=0, rely=0.57, relwidth=1, relheight=0.2)
        additional.insert("1.0", "Dieses Tutorial funktioniert geauso wie der erste Teil des Tutorials. Du bekommst "
                           "Informationen zu einer bestimmten Struktur oder einen Befehl und sollst diesen dann im integrierten terminal ausführen."
                           "Der zweite Teil des Tutorials baut auf dem ersten auf, also auf dem bereits angelegten Git-Repository namens 'gitcourse'.")

        img = tk.PhotoImage(file="./img/localVCS.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0, rely=0.35)


class GitDiff(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if command == "cd gitcourse":
                try:
                    os.chdir("./gitcourse")
                    output['text'] = "Gewechselt in das Verzeichnis 'gitcourse'.{}".format(os.getcwd())
                    task1['bg'] = fu_green
                except:
                    if right_directory():
                        output['text'] = "Du befindest dich bereits im gitcourse-Projektordner. {}".format(os.getcwd())
                        task2['bg'] = '#6b9e1f'
                    else:
                        output['text'] = "Es scheint, dass kein gitcourse-Ordner existiert. Hast du den ersten Teil des " \
                                         "Tutorials gemacht?"
            elif command == "git diff main.txt":
                if right_directory():
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task2['bg'] = fu_green
                else:
                    output['text'] = "Wechsel bitte zuerst in den gitcourse-Ordner!"
            else:
                output['text'] = "Überprüfe deine Syntax!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="2. Git diff", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.65)
        text.insert("1.0", "Wenn man sehr viele Änderungen macht, kann man ja schnell mal den Überblick verlieren. "
                           "Der Befehl 'git status' hilft ja bereits, um zu sehen, an welcher Datei Veränderungen vorgenommen wurden."
                           "Das ist schön und gut, aber man will natürlich auch wissen, was genau man in der Datei verändert hat. "
                           "Vor allem, wenn die Änderungen nicht von einem selbst stammen. "
                           "\n\nHierzu gibt es den Befehl 'git diff Dateiname'."
                           " Dieser zeigt einem alle gemachten Änderungen im Vergleich zum letzten Commit an."
                           " Alle von Änderungen betroffenen Codezeilen werden dann im Terminal angezeigt. Genauer gesagt, werden beide Versionen angezeigt."
                           " Das bedeutet, die alte Version (also die Version des letzten Commits) wird mit einem Minus vor dem Code angezeigt,"
                           " die neue Version des Codes wird mit einem Plus vor dem Code angezeigt."
                           "\n\n Wir wollen uns nun die aus dem letzten Tutorial gemachten Änderungen in der main.txt-Datei ansehen."
                           "Hierzu müssen wir wieder mit dem Befehl 'cd' in den gitcourse-Ordner wechseln und dann den 'git diff'-Befehl ausführen.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.77)
        task1 = tk.Label(description_container, text="1. Wechsel in das gitcourse-Verzeichnis.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.84)
        task2 = tk.Label(description_container, text="2. Lass dir die Änderungen in der main.txt anzeigen",
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
            if right_directory():
                if command == "git checkout main.txt":
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task1['bg'] = fu_green
                elif command == "git status":
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task2['bg'] = fu_green
                else:
                    output['text'] = "Überprüfe deine Syntax!"
            else:
                output['text'] = "Du befindest dich nicht im gitcourse-Verzeichnis! Gehe ein paar Schritte zurück " \
                                 "und wechsel in das Verzeichnis!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="3. Git checkout", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.65)
        text.insert("1.0", "Es kann natürlich vorkommen, dass man eine Weile an seinem Projekt gearbeitet hat und irgendwann merkt,"
                           "dass man totalen Blödsinn gemacht hat und das eigentlich alles rückgängig machen will."
                           "Hierzu gibt es verscheidene Möglichkeiten, die spezielle auf den Versionierungssstatus bezogen sind."
                           "\n\nZuerst wollen wir Änderungen rückgängig machen, die noch nicht zum Commit vorgemerkt sind und auch noch nicht commited wurden."
                           "Also Änderungen, die bisher nur im Working Directory zu finden sind."
                           "\n\nHierzu gibt es den Befehl 'git checkout' den man entweder auf eine bestimmte Datei beziehen kann 'git checkout Dateiname' oder "
                           "auf alle gemachten Änderungen 'git checkout *'."
                           "\n\nWenn du nun den Status der veränderungen mit 'git status' prüfst, solltest du sehen, dass die Datei "
                           "main.txt nicht mehr angezeigt wird, da alle Änderungen rückgängi gemacht wurden.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.77)
        task1 = tk.Label(description_container, text="1. Mache alle Änderungen in der main.txt rückgängig.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.84)
        task2 = tk.Label(description_container, text="2. Pürfe den Änderungsstatus deines repositorys.",
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
        panel.place(relx=0.7, rely=0.76)
    pass


class GitReset(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if command == "git add second.txt":
                pass
            elif command == "git status":
                pass
            elif command == "git reset second.txt":
                pass
            else:
                output['text'] = "Überpürfe deine Syntax!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="6. Git reset", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.6)
        text.insert("1.0", "Es kann vorkommen, dass man in einem Projekt Änderungen gemacht und zur Versionierung vorgemerkt hat, "
                           "die man eigentlich doch nicht versionieren möchte. Zum Beispiel kann man eine Konfig-Datei "
                           "mit Passwörtern zur Versionierung vorgemerkt haben, weil man alle Änderungen vorgemerkt hat "
                           "und vergessen hat, die Konfigurationsdatei in die .gitigno ezu schreiben."
                           "Das ist natürlich ungünstig und deswegen will man diese datei dann wieder aus der Vormerkungen herausnehmen."
                           "Hierzu bietet Git den Befehl 'reset'. Mit 'git reset Dateiname# kann man eine oder meherere "
                           "Datein aus der Staging Area entfernen, mit 'git reset' entfernt man alle vorgemerkten Änderungen."
                           "\n\nDas wollen wir mal ausprobieren. Zuerst merken wir hierfür die Änderungen der second.txt-Datei "
                           "zur Versionierung vor (git add). Die Vormkerung können wir uns wieder mit 'git status' anzeigen lassen"
                           " und mit 'git reset Dateiname' machen wir diese Vormerkung rückgängig. Und auch das können "
                           "wir uns wieder mit 'git status' ansehen.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.77)
        task1 = tk.Label(description_container, text="1. Merke die datei second.txt zum Commit vor.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.84)
        task1 = tk.Label(description_container, text="1. Mache den Staging-Prozess der second.txt-Datei rückgängig.",
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

        img = tk.PhotoImage(file="./img/gitreset.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.6, rely=0.67)


class GitLog(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if right_directory():
                if command == "git log":
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task1['bg'] = fu_green
                else:
                    output['text'] = "Überprüfe deine Syntax!"
            else:
                output['text'] = "Du befindest dich nicht im gitcourse-Verzeichnis! Gehe ein paar Schritte zurück und" \
                                 " wechsel in das Verzeichnis!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="5. Git log", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=0.6, relheight=0.4)
        text.insert("1.0", "Im Laufe der Bearbeitung eines Projektes archiviert man sehr viele Projektversionen."
                           "Hierzu ist es auch gut, einen Überblick über alle Versionen zu haben, vor allem, wenn man "
                           "doch mal zu einer früheren Version zurückkehren möchte."
                           "\n\nHierzu stellt Git das Werkzeug der Commit-History bereit. Diese beinhaltet die Liste aller gemachten"
                           "Commits, also aller versionierten Projektversionen. ")
        text2 = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5, wrap="word")
        text2.place(x=0, rely=0.5, relwidth=1, relheight=0.32)
        text2.insert("1.0", "Mit dem Befehl 'git log' kann man sich diese Commit-History anzeigen lassen. Jeder Eintrag enhält den Autor des Commits,"
                           "den Zeitstempel, die mitgelieferte Commitmessage sowie eine Referenz. Diese Referenz ist einen "
                           "eindeutige Zahlen- und Buchtsbenkombination, die einem Commit zugeordnet ist."
                           "\n\nHier zeigt sich außerdem, warum es so wichtig ist, eine vernünftige Commitmessage mitzuliefern, "
                           "da man sonst sehr schwer nachvollziehen kann, welche Änderungen in den jeweiligen Commits gemacht "
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
        text.place(x=0, rely=0.05, relwidth=1, relheight=0.35)
        text.insert("1.0", "Warum haben wir uns nun die Commit-History angesehen?"
                           "\n\nEs kann vorkommen, dass man eine Projektversion archiviert hat, also ins Repository commited."
                           "Merkt man jedoch, dass man vielleicht noch nicht fertig war mit den Änderungen, dann gibt es eine Möglichkeit,"
                           "eine Projektversion aud dem Repository zurück in die Staging Area zu holen. Man macht also "
                           "einen Commit rückgängig, jedoch ohne die Änderungen zu verlieren."
                           "Hierzu gibt es den Befehl 'git reset --soft HEAD'."
                           "\nUnd genau hier kommt die Commit-History ins Spiel. Es gibt mehrere Wege, auf einen früheren Commit zurückzusetzen."
                           "Man kann mit 'HEAD~1' einen Commit, oder entsprechend der Zahl mehrere Commit zurückspringen. "
                           "Bei einer großen Menge an Commits wird das aber irgendwann etwas schwirieg, auch wenn es selten vorkommt, dass man so weit zurückgeht."
                           "Man kann an auch eine Commit-Referenz direkt übergeben, die man sich aus der commit-History holt, also diese"
                           "eindeutige Zahlen- und Buchtsbanekombination, die wir in der Commit-History gesehen haben.")

        img = tk.PhotoImage(file="./img/resetsoft.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.17, rely=0.52)

        img = tk.PhotoImage(file="./img/gitresetsoft.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.17, rely=0.35)


class GitResetSoft(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            if right_directory():
                if command == "git log":
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task2['bg'] = fu_green
                elif command == "git status":
                    response = subprocess.check_output(command, shell=True)
                    output['text'] = response
                    task4['bg'] = fu_green
                elif command == "git add third.txt":
                    pass
                elif command.starts_with("git commit"):
                    pass
                elif command == "git reset --soft HEAD~1":
                    pass
            else:
                output['text'] = "Prüfe deine Syntax!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="7. Git reset soft", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.35)
        text.insert("1.0", "Nun wollen wir mit 'git reset --soft HEAD~1' auf den vorletzten Commit zurücksetzen. Also "
                           "den Commit vor dem aktuellsten und somit alle gemachten Änderungen des aktuellsten "
                           "Commits zurück in die Saging Area verschieben."
                           "Bisher haben wir jedoch nur einmal commited und wollen zuerst die Datei third.txt zur "
                           "Versionierung vormerken und dann commiten."
                           "Wenn wir das getan haben, können wir die Commit-History checken und dann den neuen Commit "
                           "rückgängig machen. Prüfen wir dann den Status der Änderungen, sollten sich die soeben "
                           "gemachten Änderungen wieder in der Staging Area befinden.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.63)
        task1 = tk.Label(description_container, text="1. Merke third.txt zur Versionierung vor und committe sie.",
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


class GitResetHardDescription(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="8. Git reset hard", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.05, relwidth=1, relheight=0.35)
        text.insert("1.0", "Man kann also Commit rückgängig machen, ohne dass die Veränderungen verloren gehen und dann "
                           "weiter an dieser Projektversion arbeiten und irgendwann, wenn an fertig ist, erneut commiten."
                           "\n\nEs kommt aber auch vor, dass man etwas komplett nicht mehr braucht oder aus versehen etwas "
                           "so doll kaputt gemacht hat, dass es nicht mehr funktioniert und man den Code auch wirklich "
                           "nicht mehr haben will."
                           "\n\nHierzu gibt es dann den Befehl #git reset --hard HEAD'. Dieser funktioniert äquivalent zum "
                           "vorherigen Befehl, nur dass hier die archivierte Version komplett weggeschmissen wird. Will "
                           "man also auf einige Commit vor dem aktuellen zurücksetzen, werden alle Commit, die nach "
                           "dem kommen, auf den man zurücksetzen will, komplett gelöscht. Und hiermit ist gelöscht geöscht "
                           "gemeint. Diese Versionen kann man auch nicht wieder herstellen, sie sind komplett weg.")

        img = tk.PhotoImage(file="./img/gitresethard.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.37, rely=0.37)

        img = tk.PhotoImage(file="./img/resethard.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.0, rely=0.57)


class GitResetHard(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            pass

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="8. Git reset hard", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.45)
        text.insert("1.0", "Jetzt wollen wir einen Commit komplett löschen. Dazu wiederholen wir einen Teil der Schritte "
                           "aus dem Schritt des Soft-Resets."
                           "Also merken wir erneut die Datei 'third.txt# zum Commit vor, commiten sie auch schließlich "
                           "und können uns den neuen Commit erneut in der Commit-History ansehen."
                           "Nun wollen wir den Commit loswerden und löschen ihn mit 'git reset --hard HEAD~1'."
                           "Und wenn wir diesmal in die Staging Area gucken (git status), ist dort auch nichts vorgemerkt zu finden."
                           "\n\n Anmerkung: In der Regel kommt er erfreulich selten vor, dass man etwas rückgängig machen "
                           "muss, aber es ist gut, es schonmal gesehen zu haben.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.63)
        task1 = tk.Label(description_container, text="1. Merke third.txt zur Versionierung vor und committe sie.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.70)
        task2 = tk.Label(description_container, text="2. Lass dir die Commit-History anzeigen",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.77)
        task3 = tk.Label(description_container, text="3. Lösche den Commit.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task3.place(x=0, rely=0.84)
        task4 = tk.Label(description_container,
                         text="3. Prüfe, ob die zuvor commiteten Änderungen nun in der Staging Area vorgemerkt sind. ",
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


class RemoteRepository(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="Remote Repository", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.05, relwidth=1, relheight=0.2)
        text.insert("1.0", "So nun kennen wir die wichtigsten und am häufigsten genutzten Befhele, um lokal "
                           "Projektsoftware oder -inhalt zu versionieren. Nun wollen wir uns mit dem Remote Repository "
                           "und dem Platform GitLab auseinandersetzen."
                           "\nHierzu musst du dich mit deinem Institutsaccount bei GitLab-Server anmelden: gitlab.met.fu-berlin.de"
                           "\n\nDort findest du dann eine Möglichkeit, ein neues Repository anzulegen."
                           "Drücke auf den Vutton, um ein neues Repository anzulegen.")
        text3 = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text3.place(x=0, rely=0.4, relwidth=1, relheight=0.07)
        text3.insert("1.0", "Nenne dieses im Textfeld der Gui 'first_repo'."
                           "Dies ist eine weitere Möglichkeit, ein Repository anzulegen, dass sich jedoch momentan nur auf dem GitLab-Server befindet.")

        img = tk.PhotoImage(file="./img/newremoterepo.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0, rely=0.25)

        img = tk.PhotoImage(file="./img/remotereponaming.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0, rely=0.47)


class CloneRepo(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command():
            pass

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Remote Repository", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.05, relwidth=1, relheight=0.27)
        text.insert("1.0", "Nun wurde ein leeres Repository angelegt."
                           "Im folgenden Dialog siehst du unterschiedliche Möglichkeiten, um dein Repository zu "
                           "befüllen bzw. auf deinen rechner zu übertragen."
                           "Wir wollen dieses Repository nun klonen. Es wird also das gesamte repository mitsamt "
                           "Commit-History lokal auf deinen rechner kopiert."
                           "Bisher ist jedoch ja alles leer. Wir orientieren uns nun an dem Punkt 'Ein neues Repository anlegen',"
                           "betrachten jedoch zunächst nur die ersten beiden Schritte."
                           "Abgewandelt werden muss dier Link, der bei 'git clone' übergeben wird. Hierzu muss der : "
                           "nach dem .de durch einen / ersetzt werden."
                           "\n\nIm Moment befinden wir uns noch im Verzeichnis gitcourse. Hier wollen wir nun nicht mehr "
                           "arbeiten, wir müssen also in den darübergelegenen Ordner (..) wechseln.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.77)
        task1 = tk.Label(description_container, text="1.Wechsle in das übergeordnete Verzeichnis.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.84)
        task2 = tk.Label(description_container, text="2. Klone dein neues Repository und wechsel in das neue repository.",
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
        panel.place(relx=0.5, rely=0.25)


class Readme(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command():
            pass

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Remote Repository", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.6)
        text.insert("1.0", "Der nächste Schritt in der Anleitung zeigt das Anlegen einer README.md-Datei."
                           "Dies ist die Datei, die auf der Startseite deines Remote-Repositorys angezeigt wird. Es "
                           "handelt sich um eine Markdown-Datei in der man in der Regel eine krze Beschreibung des "
                           "Inhalts des Repositorys festhält, sowie eine Installationsanleiteung oder Softwarevoraussetzungen."
                           "Es ist sozusagen das Aushängeschild deines Projekt auf dem du einen groben Überblick über die "
                           "Funktionalität deines projektes geben kannst."
                           "Du musst keine READMEDatei anlegen, aber es wäre durchaus sinnvoll."
                           "Für unser neues Projekt wollen wir auf jeden Fall eine README anlegen (touch-Befehl)."
                           "In diese Schreiben wir dann mit dem echo-Befehl:"
                           "echo \"## Mein erstes Repository\" >> README.md")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.77)
        task1 = tk.Label(description_container, text="1. Lege die Datei README.md an.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.84)
        task1 = tk.Label(description_container, text="2.Befülle die README.md mit dem oben genannten Text..",
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


class GitPush(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            pass

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Git push", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.6)
        text.insert("1.0", "So nun haben wir lokal auf unserem Rechner das online anlegete und geklonte Repository befüllt."
                           "Nun wollen wir diese erste Version des Projektes versionieren. Wir merken also alle Änderungen"
                           "zum Commit vor und commiten die Version dann. Schön und gut aber so befindet sich die neuste "
                           "Version des Projektes nur lokal auf unserem Rechner."
                           "Nun wollen wir diese Version auch in unseres Remote Repository kopieren. Hierzu gibt es den Befehl 'git push'."
                           "Diesen Befehl führt man so jedes Mal aus, wenn man sein lokales Repository ins Remote Repository kopieren will."
                           "Beim allerersten Push jedoch kommen zwei Optionen hinzu: 'git push -u origin master#."
                           "Mit orogin wird im Hintergund der Online-Link des Repositorys hinterlget, sodass du ihn nicht bei jedem Push mit angeben musst."
                           "master beschreibt den Hauptzweig, auf den das Archiv gepusht wird."
                           "In Git gibt es etwas, das sich Branches nennt, darauf wollen wir jedoch nicht weiter drauf eingehen, da das in diesem rahen zu komplex wird.")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.84)
        task1 = tk.Label(description_container, text="1. Kopiere dein lokales Repository in dein remote Repository..",
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


class Wiki(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)


        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="Remote Repository", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.6)
        text.insert("1.0", "Ein solcher GitLab-Server bietet viele hilfreiche Möglichkeiten, Informationen festzuhalten und zu verwalten."
                           "Eine Möglichkeit davon ist das Wiki. Dieses findest du in der Menüleiste am Rand")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.84)
        task1 = tk.Label(description_container, text="1. Lass dir die Commit-History anzeigen.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.92)

        img = tk.PhotoImage(file="./img/newremoterepo.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0, rely=0.35)



class Issues(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            pass

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="Remote Repository", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.6)
        text.insert("1.0", "")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.84)
        task1 = tk.Label(description_container, text="1. Lass dir die Commit-History anzeigen.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.92)

        img = tk.PhotoImage(file="./img/newremoterepo.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0, rely=0.35)

        img = tk.PhotoImage(file="./img/remotereponaming.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0, rely=0.35)

        img = tk.PhotoImage(file="./img/remotereponaming.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0, rely=0.35)





class GitPull(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            pass

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Git pull", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.6)
        text.insert("1.0", "")

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


class CreateMergeConflict(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            pass

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="Remote Repository", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.6)
        text.insert("1.0", "")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.84)
        task1 = tk.Label(description_container, text="1. Lass dir die Commit-History anzeigen.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.92)

        img = tk.PhotoImage(file="./img/newremoterepo.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0, rely=0.35)

        img = tk.PhotoImage(file="./img/remotereponaming.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0, rely=0.35)

        img = tk.PhotoImage(file="./img/remotereponaming.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0, rely=0.35)


class ResolveMergeConflicts(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            pass

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Mergekonflikte lösen", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.6)
        text.insert("1.0", "")

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.84)
        task1 = tk.Label(description_container, text="1. Lass dir die Commit-History anzeigen.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.92)


class Summary(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):
            pass

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="Zusammenfassung", bg="white", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Text(description_container, font="TkFont 12 bold", bg="white", fg=font_color, padx=5, pady=5,
                       wrap="word")
        text.place(x=0, rely=0.1, relwidth=1, relheight=0.6)
        text.insert("1.0", "")

        img = tk.PhotoImage(file="./img/emergency.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.48, rely=0.0)


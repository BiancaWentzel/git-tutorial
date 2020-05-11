# -*- coding: utf-8 -*-

import tkinter as tk
import subprocess
import os
import webbrowser
import platform

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
                        text="Wie oft ist es dir schon passiert, dass du aus Versehen Änderungen gemacht hast\noder "
                             "etwas gelöscht hast und dann alles nochmal machen musstest? Oder kennst du es,\nwenn man "
                             "für jede Änderungen eine neue Datei anlegt, um die alte Version nicht zu\nverlieren und "
                             "langsam den Überblick über die ganzen zusätzlichen Dateien verliert?"
                             "\n\nGenau hier setzt Git an und ist dein bester Freund, damit dein Projekt übersichtlich\n"
                             "bleibt und nichts verloren geht und sich jede Änderung nachvollziehen lässt."
                             "\n\nGit ist ein sogenanntes Versionskontrollsystem (VCS - Version Controll System)."
                             "\nEs dient zur Protokollierung, Archivierung und Dokumentation von Änderungen in "
                             "Dateien \nund Ordnern eines Projektes. Für alle vorgemerkten Änderung wird eine Version des "
                             "gesamten \nProjektes wie ein Schnappschuss abgespeichert und mit Angaben zur Zeit und zum "
                             "Autor sowie \neinem Kommentar des Autors zu den Änderungen archiviert. "
                             "\n\nWeiterhin bietet Git durch seine Funktionsweise die perfekte Umgebung, um im Team\nan "
                             "einem Projekt zu arbeiten. Teammitglieder können parallel an den gleichen Dateien\nund "
                             "Ordnern arbeiten, ohne dass etwas verloren geht. "
                             "In Verbindung mit einer Server-Platform\nwie GitLab oder GitHub ist der Projektinhalt außerdem "
                             "immer und von überall erreichbar,\nwas noch flexibleres Arbeiten ermöglicht.\n\n"
                             "Klicke Dich nun links im Inhaltsverzeichnis durch alle Kapitel durch.",
                        font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.49)

        img = tk.PhotoImage(file="./img/vc-xkcd.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.15, rely=0.1)


class GeneralStructure(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="2. Allgemeine Struktur", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                        text="Versionierung mit Git findet überwiegend lokal auf deinem Rechner statt.\nMan kann die "
                             "lokale Versionierung jedoch erweitern, indem man eine Platform wie\nGitLab oder GitHub nutzt, "
                             "um das Archiv (Remote Repository) auf einem Server zu hinterlegen."
                             "\n\nZuerst konzentrieren wir uns jedoch auf die lokale Versionierung. Grob gesagt,\nkann "
                             "man die Versionierung in drei Ebenen aufteilen:"
                             "\n- das Projektverzeichnis (working directory)"
                             "\n- die Zwischenablage (staging area)"
                             "\n- das Archiv (repository)"
                             "\n\nJede dieser Ebenen spielt eine wichtige Rolle in der Versionierung und dient einem\n"
                             "bestimmten Zweck. Dieser Zweck und die Interaktion zwischen den einzelnen Ebenen\nwird in "
                             "den folgenden Kapiteln näher erläutert.",font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.63)

        img = tk.PhotoImage(file="./img/generalstructure.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.1, rely=0.07)


class WorkingDirectory(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="3. Working Directory", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Die erste Ebene ist das Working Directory, also das Projektverzeichnis, in dem sich\nalle "
                             "Unterordner, Dateien und Dokumente des Projektes befinden. Dieses Verzeichnis\nist im "
                             "Wesentlichen erstmal unabhängig von Git und Versionierung."
                             "\n\nMöchte man nun jedoch alle Inhalte des Projektes versionieren, dann ist das der Ort,\nan "
                             "dem ein Repository angelegt wird. "
                             "Das bedeutet man sagt Git, dass man dieses\nProjekt versionieren möchte und Git legt "
                             "dann die übrigen zwei \nEbenen (Staging Area und Repository) als versteckte virtuelle Ebenen "
                             "in\ndiesem Projektordner an."
                             "\n\nAlso alles, was du in dem Projekt machst, sei es eine Änderung in einem Dokument\noder das "
                             "Anlegen einer neuen Datei, passiert im Working Directory und ist erst einmal\nunabhängig von Git."
                             ,font="TkFont 12 bold", bg="white", fg=font_color,
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
                        text="Kommen wir nun zur zweiten Ebene. Diese ist eigentlich nur virtuell und wurde\nbeim "
                             "Initalisieren eines Repositorys angelegt."
                             " Diese Ebene ist die Staging Area\nund kann als Zwischenablage oder Merkzettel gesehen werden."
                             "\nSie dient dazu, gemachte Änderungen zur Versionierung vorzumerken."
                             "\n\nDas heißt, wenn man einige Änderungen in seinem Projekt gemacht hat, kann man\nalle "
                             "relevanten Änderungen vormerken. Sie befinden sich dann also in\nder Staging Area (also virtuell, nicht wirklich)."
                             " Alle vorgemerkten Änderungen können\ndann in einem nächsten Schritt archiviert werden."
                             " Das betrifft dann aber auch \nwirklich nur die Änderungen, die vorgemerkt sind."
                             " Alle anderen Änderungen,\ndie gemacht wurden, aber nicht vorgemerkt, werden nicht mit archiviert, "
                             "sie bleiben\njedoch im Working Directory erhalten."
                             "\n\nDer Zweck der Staging Area liegt also darin, Änderungen zur Archivierung vorzumerken.\nGleichzeitig bietet sie "
                             "die Möglichkeit, nur spezifische Änderungen vorzumerken, damit\ndie einzelnen "
                             "Projektversionen, die archiviert werden, thematisch abgeschlossen sind\nbzw. besser strukturiert werden können.",
                        font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.07)

        img = tk.PhotoImage(file="./img/areas.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.15, rely=0.5)


class Repository(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="5. Repository", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Die letzte und wichtigste Ebene ist das Repository, also das Archiv. Wenn man ein\nProjekt "
                             "versionieren möchte, sagt man, dass man ein Repository anlegt, obwohl\nsowohl ein Repository als auch "
                             "eine Staging Area angelegt werden. Da jedoch\ndas Repository den Kernbestandteil der "
                             "Versionierung darstellt, benutzt man\nden Begriff Repository einfach übergreifend."
                             "\n\nDas Repository ist also das Archiv, in dem alle Versionen des Projektes gespeichert\nwerden. "
                             "Jede Version hat einen Zeitstempel, einen Autor und eine vom Autor\nverfasste Anmerkung "
                             "zur Version oder den gemachten Änderungen (Commit-Message)."
                             "\n\nDas Archiv bietet also die Möglichkeit, unterschiedliche Versionen eines Projektes "
                             "\nabzuspeichern und die einzelnen Änderungen Schritt für Schritt nachvollziehen zu können."
                             "\nBesonders mächtig wird das Repsoitory dadurch, dass man die Möglichkeit hat,\njede dieser "
                             "Versionen wiederherzustellen.",font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.07)

        img = tk.PhotoImage(file="./img/areas.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.15, rely=0.45)


class RemoteRepository(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=1)

        title = tk.Label(description_container, text="6. Remote Repository", font="TkHeaderFont 24 bold", bg='white',
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                        text="Vor allem für die Arbeit im Team ist Git sehr gut geeignet. Befindet sich dein Projekt\n"
                             "jedoch nur lokal auf deinem Rechner, ist das sehr schwierig. Um Versionierung\nund "
                             "das Arbeiten im Team zu ermöglichen, gibt es Platformen wie GitLab oder GitHub,\ndie online auf "
                             "einem Server eine Kopie deines lokalen Repositorys speichern.\nAlso ein sogenanntes Remote Repository."
                             "\n\nDieses Repository ist dann von überall über das Internet erreichbar und auch für deine\nTeammitglieder."
                             " Du kannst also lokal an deinem Rechner Änderungen vornhemen\nund diese versionieren, während ein "
                             "Teamkollege das auch macht. Wenn du mit deiner\nArbeit fertig bist, kannst du den neuen "
                             "Stand des Projektes, den du lokal in deinem\nRepository archiviert hast, auf das "
                             "Remote Repository übertragen.\nSo haben alle Teammitglieder immer die neueste Version des Projekts."
                             "\n\nAußerdem bietet ein solches Repository die Sicherheit, dass deine Projektdaten nicht\nverloren "
                             "gehen, wenn dein Rechner mal kaputt gehen sollte.",font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.07)

        img = tk.PhotoImage(file="./img/remote.png")
        panel = tk.Label(description_container, image=img)
        panel.image = img
        panel.place(relx=0.15, rely=0.47)


class NewProject(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

            if command == "mkdir gitcourse":
                if os.system(command) == 0:
                    output['text'] = "Das Verzeichnis 'gitcouse' wurde angelegt."
                    task1['bg'] = '#6b9e1f'
                elif platform.system() == "Windows" and os.system(command) != 0:
                    output['text'] = "Das Verzeichnis existiert bereits!"
                    task1['bg'] = '#6b9e1f'
                elif platform.system() != "Windows" and os.system(command) == 256:
                    output['text'] = "Das Projekt existiert bereits."
                    task1['bg'] = '#6b9e1f'
                else:
                    output['text'] = "Bitte überprüfe deine Syntax!"
            elif command == "cd gitcourse":
                try:
                    os.chdir("./gitcourse")
                    output['text'] = "Gewechselt in das Verzeichnis 'gitcourse'.{}".format(os.getcwd())
                    task2['bg'] = '#6b9e1f'
                except:
                    if right_directory():
                        output['text'] = "Du befindest dich bereits im gitcourse-Projektordner. {}".format(os.getcwd())
                        task2['bg'] = '#6b9e1f'
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
                        text="Um die grundlegenden Befehle von Git zu lernen und die Funktionsweise der Versionierung\n"
                             "zu verstehen, brauchen wir zuerst einmal einen Projektordner, also das sogenannte\n"
                             "Working Directory."
                             "\n\nUm über ein Terminal einen Ordner anzulegen, gibt es den Befehl 'mkdir' (make directory).\n"
                             "Mit 'mkdir Ordnername' legt man also einen neuen Ordner an, der den mitgegebenen\nNamen trägt."
                             " Da wir in diesem Ordner agieren wollen, wäre es besser, wenn wir uns\nin diesem Ordner befinden."
                             " Hierzu dient der Befehl 'cd Ordnername' (change directory),\nder dann in den angegebenen Ordner wechselt."
                             "\n\nAnmerkung: Das Tutorial hat ein eingebautes Terminal(siehe unten), das im Hintergund die\nübergebenen "
                             "Befehle ausführt (auf 'Run' klicken). Man könnte das Tutorial auch parallel in einem\n extra Terminal durcharbeiten, "
                             "muss dabei jedoch darauf achten, dass die ggf. Befehle\nvom Betribssystem abhängig sind."
                             , font="TkFont 12 bold", bg="white", fg=font_color, justify="left")

        text.place(x=0, rely=0.15)


        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.77)
        task1 = tk.Label(description_container, text="1. Lege einen neuen Projektordner mit dem Name 'gitcourse' an.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.84)
        task2 = tk.Label(description_container, text="2. Wechsel in den angelegten Projektordner 'gitcourse'.",
                         bg="white", font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.92)

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
                    if platform.system() == "Linux" or platform.system() == "MacOS":
                        response = subprocess.check_output(command, shell=True)
                        output['text'] = response
                        task2['bg'] = '#6b9e1f'
                    elif platform.system() == "Windows":
                        response = subprocess.check_output("dir",shell=True)
                        output['text'] = response
                        task2['bg'] = '#6b9e1f'
                else:
                    output['text'] = "Bitte überprüfe deine Syntax."
            else:
                output['text'] = "Du befindest dich nicht im 'gitcourse-Projektordner!\n" \
                                 "Gehe zurück zum vorherigen Schritt und erledige die dort gestellten Aufgaben."

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="8. Ein Repository anlegen", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                        text="Jetzt wollen wir anfangen, unser Projekt zu versionieren. Dafür müssen wir Git sagen,\n"
                             "dass wir das Projekt, in dem wir uns gerade befinden, versionieren möchten.\nAlso ein "
                             "Repository anlegen bzw. initiieren."
                             "\n\nAngelehnt daran legt der Befehl 'git init' ein neues leeres Repository (Archiv) an.\nBeim "
                             "Initialisieren werden nun zwei virtuellen Ebenen angelegt: \ndie Staging Area und das Repository."
                             "\nDiese Ebenen und alles rund um die Versionierung wird in einem versteckten Ordner (.git/)\nangelegt. "
                             "\n\nUm sich diesen versteckten Ordner anzeigen zu lassen und damit zu prüfen, ob wirklich\nein "
                             "Repository angelegt wurde, lassen wir uns den Inhalt des aktuellen Verzeichnisses\nanzeigen."
                             " Der Befehl 'ls -a' (list --all) zeigt alle Datein und Ordner im Projekt an,\nauch die "
                             "versteckten (also die, die mit einem Punkt beginnen)."
                             , font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")


        text.place(x=0, rely=0.15)

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.77)
        task1 = tk.Label(description_container, text="1. Lege ein Git-Repository an", bg="white", font="TkFont 12 bold",
                         fg=font_color, bd=5)
        task1.place(x=0, rely=0.84)
        task2 = tk.Label(description_container, text="2. Lass dir den Inhalt des Projektordners anzeigen.", bg="white",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.92)

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
                                 "Bitte gehe zurück zu Schritt 7 und bearbeite die dortigen Aufgaben!"


        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="9. Git konfigurieren",  bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                        text="Damit jede archivierte Projektversion mit Zeitstempel und Autor versehen werden kann,\nmuss "
                             "natürlich auch hinterlegt sein, wer der Autor ist. Dies macht man in der\nGit-Konfiguration."
                             "\nHier kann man verschiedene Variablen definieren, Minimum sind der Autor (Username)\nund die "
                             "dazugehörige Email-Adresse. Die "
                             "Email-Adresse bietet zusätzlich die Möglichkeit,\ndass man sich benachrichten lassen kann, "
                             "wenn es Änderungen im Projekt gab."
                             "\n\nUm die Variablen zu konfigurieren, gibt es den Befehl 'git config'. Diesem kann man die\n"
                             "gewünschte Variable und den dazugehörigen Wert übergeben und schon hat man die\nKonfiguration "
                             "geändert. Mit 'git config --global user.name \"Vorname Nachname\"'\nkonfiguriert man den Autor,"
                             " mit 'git config --global user.email \"username@zedat.fu-berlin.de\"'\nkonfiguriert man die Email."
                             "\nWenn man alle gewünschten Variablen konfiguriert hat, kann man sich die Konfigurationen "
                             "\nmit 'git config --list' ansehen."
                        , font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")


        text.place(x=0, rely=0.1)


        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.7)
        task1 = tk.Label(description_container, text="1. Konfiguriere deinen Usernamen.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.77)
        task2 = tk.Label(description_container, text="2. Konfiguriere deine Mailadresse.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.85)
        task3 = tk.Label(description_container, text="3. Lass dir alle Konfigurationen anzeigen.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task3.place(x=0, rely=0.93)

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
                            if platform.system() == "Windows":
                                try:
                                    subprocess.check_output("<nul (set/p z=)>main.txt", shell=True)
                                    output['text'] = "Die Datei 'main.txt' wurde angelegt."
                                    task1['bg'] = '#6b9e1f'
                                except:
                                    pass
                            else:
                                subprocess.check_output(command, shell=True)
                            output['text'] = "Die Datei 'main.txt' wurde angelegt."
                            task1['bg'] = '#6b9e1f'
                        else:
                            output['text'] = "Die Datei 'main.txt' existiert bereits!"
                            task1['bg'] = fu_green
                    elif command == "touch main.log":
                        if not file_exists("main.log"):
                            if platform.system() == "Windows":
                                try:
                                    subprocess.check_output("<nul (set/p z=)>main.log", shell=True)
                                    output['text'] = "Die Datei 'main.log' wurde angelegt."
                                    task1['bg'] = '#6b9e1f'
                                except:
                                    pass
                            else:
                                subprocess.check_output(command, shell=True)
                            output['text'] = "Die Datei 'main.log' wurde angelegt."
                            task2['bg'] = '#6b9e1f'
                        else:
                            output['text'] = "Die Datei 'main.log' existiert bereits!"
                            task2['bg'] = fu_green
                    elif command == "touch second.txt":
                        if not file_exists("second.txt"):
                            if platform.system() == "Windows":
                                try:
                                    subprocess.check_output("<nul (set/p z=)>second.txt", shell=True)
                                    output['text'] = "Die Datei 'second.txt' wurde angelegt."
                                    task1['bg'] = '#6b9e1f'
                                except:
                                    pass
                            else:
                                subprocess.check_output(command, shell=True)
                            output['text'] = "Die Datei 'second.txt' wurde angelegt."
                            task3['bg'] = '#6b9e1f'
                        else:
                            output['text'] = "Die Datei 'second.txt' existiert bereits!"
                            task3['bg'] = fu_green
                    elif command == "touch third.txt":
                        if not file_exists("third.txt"):
                            if platform.system() == "Windows":
                                try:
                                    subprocess.check_output("<nul (set/p z=)>third.txt", shell=True)
                                    output['text'] = "Die Datei 'third.txt' wurde angelegt."
                                    task1['bg'] = '#6b9e1f'
                                except:
                                    pass
                            else:
                                subprocess.check_output(command, shell=True)
                            output['text'] = "Die Datei 'thid.txt' wurde angelegt."
                            task4['bg'] = '#6b9e1f'
                        else:
                            output['text'] = "Die Datei 'third.txt' existiert bereits!"
                            task4['bg'] = fu_green
                else:
                    output['text'] = "Du hast noch kein Repository initialisiert.\n Bitte gehe zurück zu Schritt 8 zurück und erledige alle Aufgaben!"
            else:
                output['text'] = "Du befindest dich nicht im gitcourse-Verzeichnis.\n Bitte geh zurück zu Schritt 7 und erledige alle Aufgaben!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="10. Inhalt für das Projekt", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                       text="Um etwas zum Versionieren zu haben und uns die Funktionalität "
                            "der Staging Area\nanzusehen, braucht unser Projekt jetzt Inhalt. Hierzu wollen wir vier Dateien anlegen:"
                            "\nmain.txt, main.log, second.txt und third.txt."
                            "\n\nIm Terminal gibt es einen Trick um eine leere Datei anzulegen.\nHierzu kann man "
                            "den Befehl 'touch' verwenden. Dieser ist eigentlich dafür gedacht,\nden Zeitstempel einer "
                            "Datei zu ändern. Existiert die angegebene Datei jedoch nicht,\nwird diese angelegt und "
                            "gleichzeitig der Zeitstempel geändert."
                            "\n\nAuf diese Weise können wir mit 'touch Dateiname' eine leere Datei mit dem\nangegebenen Namen anlegen."
                        , font="TkFont 12 bold",
                       bg="white", fg=font_color,
                       justify="left")


        text.place(x=0, rely=0.1)


        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.62)
        task1 = tk.Label(description_container, text="1. Lege die Datei 'main.txt' an.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.68)
        task2 = tk.Label(description_container, text="2. Lege die Datei 'main.log' an.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.76)
        task3 = tk.Label(description_container, text="3. Lege die Datei 'second.txt' an.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task3.place(x=0, rely=0.84)
        task4 = tk.Label(description_container, text="4. Lege die Datei 'third.txt' an.", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task4.place(x=0, rely=0.92)

        terminal_container = tk.Frame(self, bg="#464e51")
        terminal_container.place(relwidth=1, relheight=0.4, rely=0.6)

        command_line = tk.Entry(terminal_container, bg="#464e51", fg="#ccc", font="TkFont 10 bold")
        command_line.place(relwidth=0.8, relheight=0.15)
        run_button = tk.Button(terminal_container, text="Run", command=lambda: run_command(command_line.get()), bg=fu_green, fg="white")
        run_button.place(relwidth=0.2, relheight=0.15, relx=0.8)
        output = tk.Label(terminal_container, bg="#464e51", bd=5, height=10, width=20, fg="#ccc", justify="left",
                          anchor="nw", font="TkFont 10 bold")
        output.place(relheight=0.85, relwidth=1, rely=0.15)


class Gitignore(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def run_command(command):

           if right_directory():
               if is_repository():
                   if file_exists("main.txt") and file_exists("main.log") and file_exists("second.txt") and file_exists("third.txt"):
                       if command == "touch .gitignore":
                           if platform.system() == "Windows":
                               try:
                                    subprocess.check_output("<nul (set/p z=)>.gitignore", shell=True)
                                    output['text'] = "Die Datei '.gitignore' wurde angelegt."
                                    task1['bg'] = '#6b9e1f'
                               except:
                                    pass
                           else:
                               subprocess.check_output(command, shell=True)
                           output['text'] = "Die Datei '.gitignore' wurde erfolgreich angelegt."
                           task1['bg'] = '#6b9e1f'
                       elif command == 'echo "main.log" >> .gitignore':
                           if platform.system() == "Windows":
                               subprocess.check_output("echo main.log >> .gitignore",shell=True)
                               output['text'] = "'main.log' wurde erfolgreich zur .gitignor ehinzugefügt."
                               task2['bg'] = '#6b9e1f'
                           else:
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
                                    "Bitte kehre zu Schritt 8 zurück und arbeite die Aufgaben nacheinander ab!"
           else:
               output['text'] = "Du befindest dich nicht im gitcourse-Projektordner! \n " \
                                "Bitte kehre zu Schritt 7 zurück und arbeite die Aufgaben der Reihe nach ab!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="11. Gitignore", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="In einem Projekt gibt es manchmal Dateien oder Ordner, die nicht\nversioniert "
                             "werden sollen. Das können Dateien sein, die\nsensible Daten wie Passwörter oder spezifische "
                             "Konfigurationen\nenthalten. Es können aber auch Ordner sein, die von deiner "
                             "\nEntwicklungsumgebung angelegt wurden."
                             "\nDamit solche Dateien und Ordner nicht mit versioniert werden, "
                             "\ngibt es die sogenannte '.gitignore'. Diese Datei enthält alle Namen,\nEndungen oder "
                             "Ordner, die du nicht mit in deinem Archiv haben\nwillst. Sie werden ignoriert."
                             "\n\nHierzu muss die Datei '.gitignore' angelegt werden. Dies können wir\nwieder mit dem touch-Befehl machen. "
                             "\nWichtig: Nicht den Punkt vor dem Dateinamen vergessen!"
                             "\nIn unserem Projekt wollen wir nicht, dass die Datei 'main.log'\nversioniert wird. Um sie in die "
                             ".gitignore einzutragen, können wir\nden Befehl 'echo \"main.log\" >> .gitignore' ausführen."
                             , font="TkFont 12 bold",
                        bg="white", fg=font_color,
                        justify="left")


        text.place(x=0, rely=0.1)


        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.79)
        task1 = tk.Label(description_container, text="1. Lege die Datei .gitignore an!", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.85)
        task2 = tk.Label(description_container, text="2. Füge die main.log-Datei zur .gitignore hinzu", bg="#fff",
                         font="TkFont 12 bold", fg=font_color, bd=5)
        task2.place(x=0, rely=0.93)

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
                output['text'] = "Du scheinst einige Schritte übersprungen zu haben.\n" \
                                 "Bitte gehe zurück zu Schritt 7 und arbeite die Aufgaben nacheinander ab!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="12. Git status (unversioniert)", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Beim Arbeiten an einem Projekt kann man schnell den Überblick verlieren, wo man etwas\n"
                             "geändert hat und welche der Änderungen man nun schon zur Archivierung vorgemerkt hat\noder nicht."
                             "\n\nMit 'git status' kann man sich alle Dateien und Ordner anzeigen lassen, in denen Änderungen\n"
                             "vorgenommen wurden. Das beinhaltet sowohl inhaltliche Änderungen sowie das Löschen\nund Neuanlegen "
                             "von Dateien und Ordnern."
                             " Alle diese Änderungen werden mit 'git status'\nangezeigt und noch zusätzlich kategorisiert."
                             "\nUnterschieden wird in 'unversioniert', 'vorgemerkt' und 'nicht vorgemerkt'. "
                             "\nDen Unterschied dieser Kategorisierungen werden wir in den folgenden Schritten verstehen\nlernen."
                             "\n\nWenn wir uns nun den Status unseres Projektes ansehen, dann werden die 'main.txt',\ndie 'second.txt'"
                             ",die 'third.txt' und die '.gitigore' unter dem Punkt 'Unversionierte Dateien'\nangezeigt. "
                             "Das trifft immer auf alle neu angelegten Dateien zu, da diese vorher nicht existierten\nund "
                             "somit auch noch nie archiviert werden konnten."
                             "\nWeiterhin sieht man, dass die 'main.log' nicht mit angezeigt wird. Hier greift die "
                             ".gitignore,\ndie dazu führt, dass diese Datei ignoriert wird."
                             , font="TkFont 12 bold",
                        bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.1)



        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.87)
        checkbox = tk.Label(description_container, text="1. Prüfe den Status deines Projektes",
                   font="TkFont 12 bold", fg=font_color, bd=5, bg="#fff")
        checkbox.place(x=0, rely=0.93)

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
                output['text'] = "Du scheinst einige Schritte übersprungen zu haben.\n" \
                                 "Bitte gehe zurück zu Schritt 7 und arbeite die Aufgaben nacheinander ab!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="13. Git add", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)

        text = tk.Label(description_container,
                        text="Nun wollen wir ein paar der gemachten Änderungen zur Versionierung vormerken, sie also\nin "
                             "die Staging Area verschieben."
                             " Mit 'git add Dateiname' kann man eine bestimmte Datei\nzur Archivierung vormerken. Man kann "
                             "auch eine Liste von Dateien vormerken oder\nmit 'git add .' alle Änderungen vormerken, die "
                             "im aktuellen Verzeichnis gemacht wurden."
                             "\nDas bedeutet, dass alle Änderungen, die in einem Verzeichnis darüber gemacht wurden, "
                             "\nnicht berücksichtigt werden. Achte also gut darauf in welchen Verzeichnis du dich befindest,\n"
                             "wenn du 'git add .' verwendest."
                             "\n\nWir wollen vorerst nur zwei Dateien zur Archivierung vormerken: 'main.txt' und\n"
                             "'.gitignore'. Das machen wir zur Übung am Anfang erstmal einzeln.\nAlso jede Datei wird "
                             "mit 'git add Dateiname' zur Staging Area hinzugefügt.",
                        font="TkFont 12 bold", bg="white", fg=font_color, justify="left")
        text.place(x=0, rely=0.10)



        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.82)
        task1 = tk.Label(description_container, text="1. Merke die Änderungen in der main.txt-Datei zur Versionierung vor.",
                         bg="#fff", font="TkFont 12 bold", fg=font_color, bd=5)
        task1.place(x=0, rely=0.88)
        task3 = tk.Label(description_container, text="2. Merke die Änderungen in der .gitignore zur Versionierung vor.",
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
        panel.place(relx=0.15, rely=0.61)


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
                output['text'] = "Du scheinst einige Schritte übersprungen zu haben.\n" \
                                 "Bitte gehe zurück zu Schritt 7 und arbeite die Aufgaben nacheinander ab!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="14. Git status (vorgemerkt)", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Da wir nun zwei Dateien zu Archivierung vorgemerkt haben, sollte sich deren Status\ngeändert haben."
                             " Wenn wir nun erneut 'git status' ausführen, sehen wir, dass diese\nbeiden Dateien nun unter "
                             "dem Punkt 'Zur Versionierung vorgemerkt' aufgelistet sind. "
                             "\n\nAlle Dateien, die in die Staging Area verschoben wurden, werden immer unter diesem\nPunkt "
                             "angezeigt. Sie sind also zur Archivierung bzw. zum Commit vorgemerkt."
                             "\n\nDie übrigen Dateien und deren Versionierung haben wir nicht verändert, also sind sie\n"
                             "weiterhin unter dem Punkt 'Unversionierte Dateien' gelistet."
                             "\n\nAnmerkung: In einigen Terminals werden Dateien, die zum Commit vorgemerkt sind,\n"
                             "grün markiert, die übrigen rot.",
                        font="TkFont 12 bold",
                        bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.12)



        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.83)
        checkbox = tk.Label(description_container, text="1. Prüfe den Status deiner Dateien.",
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
               output['text'] = "Du scheinst einige Schritte übersprungen zu haben.\n" \
                                 "Bitte gehe zurück zu Schritt 7 und arbeite die Aufgaben nacheinander ab!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="15. Git commit", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Nun wollen wir die aktuelle Projektversion mit den vorgemerkten Änderungen archivieren."
                             "\nHierbei wird also soetwas wie ein Schnappschuss von dem Projekt mit allen vorgemerkten\nÄnderungen gemacht und gespeichert."
                             " Man archiviert eine Projektversion mit dem Befehl\n'git commit'. Diesen kann man ohne weitere Optionen benutzen, sollte man jedoch nicht."
                             "\nWenn man den Befehl ohne Option ausführt, öffnet sich ein Editor, der nach einer \n Nachricht (Commit message) verlangt."
                             " Um das zu umgehen, liefern wir gleich eine\n commit message beim Ausführen des Befehls, indem wird die Option '-m' anfügen."
                             "\nEine Commitmessage ist wichtig, denn in dieser kann man eine kurze Beschreibung\nder Version"
                             " und der gemachten Änderungen mitliefern, damit man später alle\nÄnderungen nachvollziehen kann."
                             "\nMan sollte also auch etwas sinnvolles in diese Message schreiben."
                             "\n\nDa dies unser erster Commit ist, also die erste Archivierung, schreiben wir das mit in\ndie Message: "
                             "'git commit -m \"initial commit\"'."
                            , font="TkFont 12 bold", bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.1)



        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.85)
        task1= tk.Label(description_container, text="1. Commite die vorgemerkten Änderungen.",
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
        panel.place(relx=0.15, rely=0.7)


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
                elif command == "echo 'erster Inhalt' >> main.txt":
                    subprocess.check_output(command, shell=True)
                    output['text'] = "Du hast 'erster Inhalt' in die main.txt geschrieben."
                    task1['bg'] = fu_green
                else:
                    output['text'] = "Bitte überprüfe deine Syntax!"
            else:
                output['text'] = "Du scheinst einige Schritte übersprungen zu haben.\n" \
                                 "Bitte gehe zurück zu Schritt 7 und arbeite die Aufgaben nacheinander ab!"

        description_container = tk.Frame(self, bg="#fff", bd=10)
        description_container.place(relwidth=1, relheight=0.6)

        title = tk.Label(description_container, text="16. Git status (nicht vorgemerkt)", bg="#fff", font="TkHeaderFont 24 bold",
                         fg=font_color)
        title.place(x=0, y=0)
        text = tk.Label(description_container,
                        text="Hervorragend! Jetzt haben wir eine neue Version unseres Projektes archiviert. Die zuvor\n"
                             "angelegten Dateien 'second.txt' und 'third.txt' wurden nicht vorgemekt und sind in der\n"
                             "archivierten Version nicht enthalten. Sie existieren jedoch in unserem Working Directory "
                             "\nund wir könnten sie in eine spätere Version aufnehmen, wenn wir das wollen."
                             "\n\nWir wollen uns jedoch die letzte Kategorie ansehen, die 'git status' bietet."
                             "\nHierzu schreiben wir mit 'echo \"erster Inhalt\" >> main.txt' den Satz 'erster Inhalt' in die\nDatei 'main.txt'."
                             " Wenn wir das gemacht haben, prüfen wir den Status unserer Änderungen."
                             "\n\nDie soeben gemachte Änderung wird nun unter dem Punkt \n'Änderungen, die nicht zum "
                             "Commit vorgemerkt sind' angeziegt. Hier landen alle Änderungen,\ndie an bereits existierenden "
                             "Dateien gemacht wurden, die mindestens einmal archiviert wurden."
                             "\n\nDie Datei '.gitignore' wird nicht mehr gelistet, weil sie seit dem letzten Commit, also "
                             "der\nletzte Archivierung, nicht mehr verändert wurde. Gleiches würde für 'main.txt' gelten,\n"
                             "wenn wir nicht einen neuen Satz in die Datei geschrieben hätten.",
                        font="TkFont 12 bold",
                        bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.12)

        task_title = tk.Label(description_container, text="Aufgaben", font="TkFont 14 bold", bg="white", fg=font_color)
        task_title.place(x=0, rely=0.8)
        task1 = tk.Label(description_container, text="1. Ändere den Inhalt der 'main.txt'",
                            font="TkFont 12 bold", fg=font_color, bd=5, bg="#fff")
        task1.place(x=0, rely=0.87)
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
                        text="Super! Du hast den ersten Teil des Git-Tutorials geschafft."
                             "\nHier nochmal eine kleine Zusammenfassung dessen, was du nun wissen solltest:"
                             "\n- Was Git ist und wofür man es braucht"
                             "\n- Aus welchen Ebenen sich das lokale Git zusammensetzt und wozu diese gut sind"
                             "\n- Wie man eine Reposiroty anlegt, was die Datei .gitignore ist und wie man Git konfiguriert"
                             "\n- Die Befehle: git init, git config, git status, git add und git commit"
                             "\n\nNun kommen wir zur Hausaufgabe:"
                             "\nTeil 1 der Hausaufgabe ist es, dass du zurück zu Schritt 16. gehst, dort 'git status' ausführst\nund ein Screenshot vom Terminaloutput machst."
                             "\nTeil 2 der Hausaufgabe ist es, dass du das unten verlinkte Quiz löst und ebenfalls\nein Screenshot von der Anzeige deiner Ergebnisse machst."
                             "\n\nBeide Screenshots schickst du dann bitte bis spätestens 15.05.2020 12:00 Uhr an mich:\nbianca1409@zedat.fu-berlin.de"
                             , font="TkFont 12 bold",
                        bg="white", fg=font_color,
                        justify="left")
        text.place(x=0, rely=0.1)

        link1 = tk.Button(description_container, text="--> Quiz <--", fg="white", bg=fu_green, font="TkFont 12 bold", cursor="hand2")
        link1.place(relx=0.25, rely=0.57, relwidth=0.5)
        link1.bind("<Button-1>", lambda e: callback("questionaire/first_questionaire.html"))

        additional = tk.Label(description_container, text="Bei Anmerkungen zum Tutorial (Rechtschreibfehler, Bugs ...) "
                                                          "oder bei Fragen zum Thema Git,\nschreib mir einfach auf "
                                                          "RocketChat oder per Mail an die oben genannte Adresse.",
                              font="TkFont 12 bold", bg="white", fg=font_color, justify="left")
        additional.place(x=0, rely=0.92)





# Git Tutorial
![example_page](img/example.png)

## Überblick
Das Tutorial ist in 2 Teile aufgebaut:

##### 1. Basic commands
  * Was ist Git?
  * Struktur von Git
  * git init
  * Konfiguration
  * git status
  * git add
  * git commit
  
##### 2. Advanced commands
  * git diff
  * git log
  * git checkout
  * git reset
  * git push
  * git pull

## Anleitung zum Starten des Tutorials
### 1. Installiere Git:

   #### Linux:
   Führe einen der folgenden Befehle aus
      
       apt install git  (Debian, Ubuntu, Fedora ...)
       yum install git  (CentOS)
         
   #### MacOs:
   Führe den folgenden Befehl aus
      
        brew install git
         
   #### Windows:
      
   Downloade unter folgendem Link git und installiere es: https://gitforwindows.org/
       
       
### 2. Lade dir die Tutorialsoftware herunter:

Besuche die Gitlab-Seite des Instituts und logge dich mit den
Zugangsdaten ein, die Du auch im PC-Pool des Instituts benutzt: https://gitlab.met.fu-berlin.de

Suche über den 'Projects'-Reiter nach dem Projekt 'Git_Tutorial'  
![find_repo](img/find_repo.png)

Lade die Projektresourcen herunter (rechte Seite, wie im Bild markiert).
![download_repo](img/download_sourcecode.png)

Verschiebe die heruntergeladenen Projektresourcen (kommt z.B. als
zip-Datei) in einen Ordner deiner Wahl und entpacke sie. 


### 3. Installiere die Softwarevoraussetzungen
#### Linux und MacOS:
Öffne ein Terminal und installiere 'virtualenv':

    apt install virtualenv (Debian, Ubuntu, Fedora ...)
    yum install virtualenv (CentOS)
    brew install virtualenv (MacOS)

Navigiere zum Ort, an dem du die Software des Git-Tutorials gespeichert und entpackt hast.
Definiere eine neue leere virtuelle Umgebung:

    virtualenv venv
    
Aktiviere die virtuelle Umgebung und installiere das Tkinter-Paket:

    source venv/bin/activate
    pip install tkinter   
    
Sollte beim installieren von tkinter eine Fehlermeldung auftauchen,
probiere trotzdem den nächsten Schritt. Vielleicht war tkinter schon
installiert. Ansonsten kannst du auch probieren:

    sudo apt-get install python3-tk   

#### Windows:
Wenn du noch kein Python auf deinem Rechner hast, dann musst du aus
dem Windows-App-Store Python3.7 installieren. 
         
### 4. Starte das Tutorial:

#### Linux und MacOs:
Wechsel in den 'git_tutorial'-Ordner (`cd git_tutorial`) und führe den folgenden Befehl aus:

    python main_first_part.py (für den ersten Teil des Tutorials)
    python main_second_part.py (für den zweiten Teil des Tutorials)
    
#### Windows:
Suche über die Apps nach der Power-Shell und öffne sie.
Navigiere nun zum Ort, an dem du die Software des Git-Tutorials gespeichert und entpackt hast (`sl <path>` (set location)).
Wechsele in den 'git_tutorial'-Ordner (`sl git_tutorial`) und führe den folgenden Befehl aus:

    python main_first_part.py (für den ersten Teil des Tutorials)
    python main_second_part.py (für den zweiten Teil des Tutorials)
    
    

import tkinter as tk
from first_part import Introduction, LocalStructure, RemoteStructure, NewProject, \
    NewContent, InitializeRepo, ConfigGit, GitCommit, GitAdd, GitStatus, Gitignore, Summary

font_color = "#0f425b"
fu_green = '#6b9e1f'
fu_grey = '#ccc'

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Introduction(self)
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


        buttonframe = tk.Frame(self, bg=fu_grey, bd=10)
        container = tk.Frame(self, bg="#fff")
        buttonframe.pack(side="left", fill="y", expand=False)
        container.pack(side="left", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
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

        b1 = tk.Button(buttonframe, text="1. Was ist Git?", command=p1.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b4 = tk.Button(buttonframe, text="2. Lokales VCS", command=p4.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b5 = tk.Button(buttonframe, text="3. Remote VCS", command=p5.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b6 = tk.Button(buttonframe, text="4. Ein neues Projekt", command=p6.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b7 = tk.Button(buttonframe, text="5. Ein Repository anlegen", command=p7.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b8 = tk.Button(buttonframe, text="6. Git konfigurieren", command=p8.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b9 = tk.Button(buttonframe, text="7. Inhalt für das Projekt", command=p9.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b10 = tk.Button(buttonframe, text="8. Gitignore", command=p10.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b11 = tk.Button(buttonframe, text="9. Git status", command=p11.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b12 = tk.Button(buttonframe, text="10. Git add", command=p12.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b13 = tk.Button(buttonframe, text="11. Git commit", command=p13.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b14 = tk.Button(buttonframe, text="12. Zusammenfassung", command=p14.lift, fg="white", bg=fu_green, font="TkFont 10 bold")

        b1.pack(fill="x")
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

        p1.show()

root = tk.Tk()
main = MainView(root)
main.pack(side="top", fill="both", expand=True)
root.wm_geometry("1200x800")
root.mainloop()
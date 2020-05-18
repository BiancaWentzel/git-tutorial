# -*- coding: utf-8 -*-

import tkinter as tk
from second_part import Introduction, GitDiff, GitCheckout, GitLog, GitReset, GitResetSoft, GitResetHard, \
    RemoteRepository, GitPush, GitPull, ResolveMergeConflicts, Summary, CloneRepo, \
    CreateMergeConflict, GitResetSoftDescription, GitResetHardDescription, RemoteChanges, SSHKey, Preparation

font_color = "#0f425b"
fu_green = '#6b9e1f'
fu_grey = '#ccc'

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Introduction(self)
        p11 = Preparation(self)
        p2 = GitDiff(self)
        p3 = GitCheckout(self)
        p4 = GitReset(self)
        p5 = GitLog(self)
        p6 = GitResetSoftDescription(self)
        p61 = GitResetSoft(self)
        p7 = GitResetHardDescription(self)
        p71 = GitResetHard(self)
        p8 = RemoteRepository(self)
        p9 = SSHKey(self)
        p10 = CloneRepo(self)
        p12 = GitPush(self)
        p15 = RemoteChanges(self)
        p16 = GitPull(self)
        p17 = CreateMergeConflict(self)
        p18 = ResolveMergeConflicts(self)
        p19 = Summary(self)


        buttonframe = tk.Frame(self, bg=fu_grey, bd=10)
        container = tk.Frame(self, bg="#fff")
        buttonframe.pack(side="left", fill="y", expand=False)
        container.pack(side="left", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p11.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p61.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p71.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p9.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p10.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p12.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p15.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p16.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p17.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p18.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p19.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="1. Rückblick", command=p1.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b11 = tk.Button(buttonframe, text="2. Vorbereitungen", command=p11.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b2 = tk.Button(buttonframe, text="3. Git diff", command=p2.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b3 = tk.Button(buttonframe, text="4. Git checkout", command=p3.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b4 = tk.Button(buttonframe, text="5. Git reset", command=p4.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b5 = tk.Button(buttonframe, text="6. Git log", command=p5.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b6 = tk.Button(buttonframe, text="7. Git reset soft (1)", command=p6.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b61 = tk.Button(buttonframe, text="8. Git reset soft (2)", command=p61.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b7 = tk.Button(buttonframe, text="9. Git reset hard (1)", command=p7.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b71 = tk.Button(buttonframe, text="10. Git reset hard (2)", command=p71.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b8 = tk.Button(buttonframe, text="11. Remote Repository", command=p8.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b9 = tk.Button(buttonframe, text="12. SSH Key", command=p9.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b10 = tk.Button(buttonframe, text="13. Repository klonen", command=p10.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b12 = tk.Button(buttonframe, text="14. Git push", command=p12.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b15 = tk.Button(buttonframe, text="15. Remote Changes", command=p15.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b16 = tk.Button(buttonframe, text="16. Git pull", command=p16.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b17 = tk.Button(buttonframe, text="17. Mergekonflikte", command=p17.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b18 = tk.Button(buttonframe, text="18. Mergekonflikte lösen", command=p18.lift, fg="white", bg=fu_green, font="TkFont 10 bold")
        b19 = tk.Button(buttonframe, text="19. Zusammenfassung", command=p19.lift, fg="white", bg=fu_green, font="TkFont 10 bold")


        b1.pack(fill="x")
        b11.pack(fill="x")
        b2.pack(fill="x")
        b3.pack(fill="x")
        b4.pack(fill="x")
        b5.pack(fill="x")
        b6.pack(fill="x")
        b61.pack(fill="x")
        b7.pack(fill="x")
        b71.pack(fill="x")
        b8.pack(fill="x")
        b9.pack(fill="x")
        b10.pack(fill="x")
        b12.pack(fill="x")
        b15.pack(fill="x")
        b16.pack(fill="x")
        b17.pack(fill="x")
        b18.pack(fill="x")
        b19.pack(fill="x")

        p1.show()

root = tk.Tk()
main = MainView(root)
main.pack(side="top", fill="both", expand=True)
root.wm_geometry("1200x800")
root.mainloop()
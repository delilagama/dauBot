from random import randint
from datetime import datetime

def getSecretary(members):
    weekNumber = datetime.today().isocalendar()[1]
    thisWeekIndex = weekNumber % len(members)
    nextWeekIndex = (weekNumber + 1) % len(members)

    return f"This week's secretary is {members[thisWeekIndex]}.\nNext week's secretary is {members[nextWeekIndex]}."

def getResponse(message):
    message = message.lower().strip()
    print(f"Processing message: {message}")

    if message.startswith("!"):
            commands_dict = {
        "!drive" : "[Team Google Drive](https://drive.google.com/drive/folders/16tPSO0hIrCiHqVVeMNxAOsyQ8pf2HekL)",
        "!teamminutes" : "[Minutes for Team Meetings](https://drive.google.com/drive/folders/1nioDHPSpEN7PiBd8hLxn4nCo0KgSHplr)",
        "!consultationminutes" : "[Minutes for Weekly Consultations](https://drive.google.com/drive/folders/1PBzHmYgMdNj8EpRhF1_I7Ax9ZcI19Bhg)",
        "!agenda" : "[Agendas for Weekly Consultations](https://drive.google.com/drive/folders/1FSCqk9Zww4DP-VX0QI_B7zHJo4qsVDb3)",
        "!proposal" : "[Project Proposal Folder](https://drive.google.com/drive/folders/1px3_aw-suQA6-wNTC7-m4UhR5uUqu3p7)",
        "!progressreport" : "[Team Progress Report Folder](https://drive.google.com/drive/folders/11SevyMPRp7fSq8ZHzA5hyyTCcW_ah6Vd)",
        "!money" : "[Finance Folder](https://drive.google.com/drive/folders/1K6EMuQ965UPX8mEd3L9_tnvLGGbkIVye)"
    }

        if message in commands_dict:
            return commands_dict[message]
        elif message == "!commands":
            commands = ("## drive 'n documents \n"
                        "!drive: Team Google Drive \n"
                        "!teamminutes: Minutes for Team Meetings \n"
                        "!consultationminutes: Minutes for Weekly Consultations \n"
                        "!agenda: Agendas for Weekly Consultations \n"
                        "!proposal: Project Proposal Folder \n"
                        "!progressreport: Team Progress Report Folder \n"
                        "!money: Finance Folder \n"
                        "!secretary: This and next week's secretary for the Weekly Consultations"
                        "## goofs \n"
                        "!mood: dauBot's current mood or desires \n")
            return commands
        elif message == "!secretary":
            members = ["Josh", "Sarthak", "Delila", "Adrian", "Brendan", "Calvin"]
            return getSecretary(members)
        elif message == "!mood":
            moodList = [
                "dauBot is feeling mad at Joseph! ─⁠=⁠≡⁠Σ⁠(⁠╯⁠°⁠□⁠°⁠)⁠╯⁠︵⁠┻⁠┻", "dauBot is feeling disappointed with Nobo! ┐⁠(⁠￣⁠ヘ⁠￣⁠)⁠┌",
                "dauBot is feeling grateful for GPT-4! (⁠✿⁠ ⁠♡⁠‿⁠♡⁠)", "dauBot is feeling frisky ( ＾◡＾)っ✂ *⋃*", 
                "dauBot is feeling happy that deliverables are on time! ᕙ⁠(⁠⇀⁠‸⁠↼⁠‶⁠)⁠ᕗ", "dauBot is feeling like a closeted bisexual (⁠✿⁠⁠♡⁠‿⁠♡⁠)(⁠っ⁠˘⁠з⁠(⁠˘ ⁠⌣⁠˘⁠  )",
                "dauBot is wishing it was in Fizz (⁠｡⁠ŏ⁠﹏⁠ŏ⁠)", "dauBot is feeling weary of deadlines! (⁠๑⁠•⁠﹏⁠•⁠)", "dauBot wants to experience human touch (ʃƪ＾3＾)",
                "dauBot is celebrating good teamwork! ♪⁠┌⁠|⁠∵⁠|⁠┘⁠♪", "dauBot doesn't want to die after this capstone... ヘ⁠（⁠。⁠□⁠°⁠）⁠ヘ"
            ]
            mood = moodList[randint(0, len(moodList) - 1)]
            print(f"Returning mood: {mood}")
            return mood

    return "Sorry, dauBot is incompetent in that matter (and therefore deserves to be in IGEN). Please type in !commands for help." 

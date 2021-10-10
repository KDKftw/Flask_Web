class Menu():
    def __init__(self, name, description, comment):
        self.name = name
        self.description = description
        self.comment = comment

    def print_values(self):
        print("menu_name= " + self.name, "|| ", "menu_description= " + self.description, "|| " , "menu_coment= " + self.comment)

##annoucnment channel need to put into some shape printable

extra1 = """In this channel you will find new announcements and notifications, also rules and more...
⚠️ = important announcement
🔴 = useful/helpful announcement"""

extra2 = """ ⚠️ @everyone  Please, let the staff know your ingame main char nickname so we know who just came in our Discord and we can rename you by your nickname and call you like that 😇
Otherwise we will count with you like a you're not in our Discord."""

extra3 = """  ⚠️   @everyone RULES:
1. Speak english only
2. Keep etiquette in all channels
3. Be polite, don't be rude
4. Represent our guild in honorable light
5. Tell the staff your ingame main char nickname
If you break the rules, you will probably be muted or kicked, exceptionally banned."""

extra4 = """  @everyone GUILD RANKS:
1. Sylvanas = Guild Master
2. Nathanos = Head officer
3. Val'kyr = Officer
4. Raid leader = People capable of leading raid, explain tactics, know what to do in raids, can lead the people & society
5. Banshee = Test officer
6. Deathstalker = Rank for special people. People who are helpful, behave pretty good and sometimes put stuff in guild bank. Rank for loyal ones.
7. Apothecary = PvP rank for people who are PvP only or at least mainly PvP
8. Abomination = Rank for every 85 lvl
9. KEKW = Rank for people who need to calm down and shouldn't talk in guild chat
10. Zombie = Rank for newcomers, also for every 1-84 lvl
Roles (ranks) in Discord are equal to ranks ingame"""

extra5 ="""⚠️   @everyone Kicking for inactivity:
1. Sylvanas = Never kicked
2. Nathanos = Never kicked
3. Val'kyr = Never kicked, depends. Probably for more than month of inactivity
4. Raid leader = Never kicked, depends. Probably for more 3 weeks of inactivity
5. Banshee = Never kicked, depends. Probably for more than month of inactivity
6. Deathstalker = Kicked for 15+ days
7. Apothecary = Kicked for 13+ days
8. Abomination = Kicked for 13+ days
9. KEKW = Kicked for 10+ days
10. Zombie = Kicked for 11+ days
.
🔴   @everyone Also feel free to give any hints, tips, ideas, improvements how to improve our Discord. We appreciate any idea which may become reality! 😉"""

menu10contentExtra = [extra1, extra2, extra3, extra4, extra5]


menu0 = Menu("💬-general", "", "")
menu1 = Menu("🎉-clips-and-highlights", "" , "")
menu2 = Menu("👋-welcome", "", "just joining notifications")
menu3 = Menu("📷-screenshots", "" , "")
menu4 = Menu("🤡-memes", "" , "")
menu5 = Menu("🎵-music", "" , "music bot")
menu6 = Menu("🗼-weebs", "" , "")
menu7 = Menu("👾-raiding", "" , "")
menu8 = Menu("✅-guide","This is one of the most used guide for PvE cata which you will definitely use (or at least most probably will), anyway I am pretty sure many of use already use it: httpwww.tauri-veins.tk", "")
menu9 = Menu("⛔-blacklist", "Black list of members who used to be in guild and are no longer worth of being in our guild:", "")
menu10 = Menu("🔔-announcements", "menu10contentExtra", "")##viz list on content position
menu11 = Menu("🔒-guild_leadership", "", "big boys")

menu0.print_values()
menu1.print_values()
menu2.print_values()
menu3.print_values()
menu4.print_values()
menu5.print_values()
menu6.print_values()
menu7.print_values()
menu8.print_values()
menu9.print_values()
menu10.print_values()
menu11.print_values()

print(extra1)
print(extra2)
print(extra3)
print(extra4)
print(extra5)

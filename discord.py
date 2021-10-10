
class Menu():
    def __init__(self, name, description, comment):
        self.name = name
        self.description = description
        self.comment = comment

    def print_values(self):
        print("menu_name= " + self.name, "|| ", "menu_description= " + self.description, "|| " , "menu_coment= " + self.comment)

##annoucnment channel need to put into some shape printable

extra1 = "In this channel you will find new announcements and notifications, also rules and more... " \
         "⚠️ = important announcement" \
         "🔴 = useful/helpful announcement"
menu10contentExtra = [extra1]


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
menu10 = Menu("🔔-announcements", "In this channel you will find new announcements and notifications, also rules and more...⚠️ = important announcement 🔴 = useful/helpful announcement" + menu10contentExtra[0], "")
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
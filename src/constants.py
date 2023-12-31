from colorama import Fore, Style

input_variants = [
    "hello",
    "hi",
    "start",
    "add contact",
    "new contact",
    "create contact",
    "change contact",
    "change phone",
    "change contact details",
    "sort",
    "sort files",
    "need sort",
    "get contact",
    "show contact",
    "show person",
    "show contacts",
    "show address book",
    "show all book",
    "goodbye",
    "close",
    "end",
    "search user",
    "find contact",
    "find user",
    "help",
    "commands",
    "need help",
    "remove note",
    "delete note",
    "get note out",
    "add note",
    "new note",
    "create note",
    "find notes",
    "search notes",
    "remove contact",
    "delete contact",
    "take out contact",
    "edit note",
    "change note",
    "search by tag",
    "sort by tag",
    "show all notes",
    "show notebook",
    "show notes",
    "give me note",
    "find by tag",
    "give me note by tag",
    "tag sorting",
    "notebook sort by tag",
    "remake note",
    "game",
    "play",
    "fun",
]

STR_EPIC_COMMANDS = """ 
  ______                                                                   __           
 /      \                                                                 /  |          
/$$$$$$  |  ______   _____  ____   _____  ____    ______   _______    ____$$ |  _______ 
$$ |  $$/  /      \ /     \/    \ /     \/    \  /      \ /       \  /    $$ | /       |
$$ |      /$$$$$$  |$$$$$$ $$$$  |$$$$$$ $$$$  | $$$$$$  |$$$$$$$  |/$$$$$$$ |/$$$$$$$/ 
$$ |   __ $$ |  $$ |$$ | $$ | $$ |$$ | $$ | $$ | /    $$ |$$ |  $$ |$$ |  $$ |$$      \ 
$$ \__/  |$$ \__$$ |$$ | $$ | $$ |$$ | $$ | $$ |/$$$$$$$ |$$ |  $$ |$$ \__$$ | $$$$$$  |
$$    $$/ $$    $$/ $$ | $$ | $$ |$$ | $$ | $$ |$$    $$ |$$ |  $$ |$$    $$ |/     $$/ 
 $$$$$$/   $$$$$$/  $$/  $$/  $$/ $$/  $$/  $$/  $$$$$$$/ $$/   $$/  $$$$$$$/ $$$$$$$/   
 -----------------------------------------------------------------------------------------                                                                                                                                                                                                                                                                    
"""


STR_EPIC_ASSISTANT = f'''
              _.-"""""-._
             / .--.....-.\        Welcome to {Fore.GREEN}Jarvis{Style.RESET_ALL}, your personal assistant!
            / /          \\
            ||           ||       {Fore.GREEN}I am here to help you stay organized and manage your contacts, reminders, notes, and files efficiently. Here are the features I offer:{Style.RESET_ALL}
            ||  .--.  .--|/       -- {Fore.YELLOW}Contact book{Style.RESET_ALL}: You can save and manage your contacts with names, addresses, phone numbers, email addresses, and birthdays.
            /`    .  \ . |            I can store this information securely, allowing you to easily access and update it whenever needed.I can store this information securely, 
            \_       _)  |            allowing you to easily access and update it whenever needed. Also, I can remind you of upcoming birthdays from your contact book.
             |    ,____, ;        -- {Fore.YELLOW}Notebook{Style.RESET_ALL}: You can create and store text-based notes. These notes can contain important information, ideas, or anything you want to remember.
             | \   `--' /             You can search for specific notes using keywords or tags. I offer the ability to edit and delete notes, ensuring your information remains organized.
          _./\  '.____.'          -- {Fore.YELLOW}File Sorting{Style.RESET_ALL}: If you have files in a specified folder, I can help you sort them by categories such as images, documents, videos, and more.
       _.:::| `\      |\:._           This feature ensures that your files are organized and easily accessible.
     .::::::::`\ '.   / /::::.
    /jgs::::::::|/::\/:\|:::::\   {Fore.GREEN}With these features, I aim to make your life easier and help you stay on top of your contacts, reminders, notes, and files. How can I assist you today?{Style.RESET_ALL}
'''

CHECK_SECOND_ARG_CHANGE_CONTACT = ("phone", "email", "birthday", "address")
CHECK_SECOND_ARG_CHANGE_NOTE = ("title", "tag", "description")

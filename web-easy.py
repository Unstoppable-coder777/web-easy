#!/usr/bin/python3
import argparse
from src.modules import banner
from src.modules import web
from sys import platform
from os import system
from os.path import exists
import sys
from time import sleep
from src.modules.dictionaries import component_dict,choices
from src.modules.help import help
from rich.console import Console

if __name__ == "__main__":
    console = Console()

    class Misc:
        def preloader(self):
            for chr in banner.banner2:
                sleep(0.01)
                sys.stdout.write(chr)
                sys.stdout.flush()

        def Clear_screen(self):
            if platform == "linux" or platform == "linux2":
                system("clear")
            elif platform == "win32":
                system("cls")

        def banner_print(self, banner):
            self.banner = banner
            print(self.banner)

        def loader(self):
            banner.loading()

    class File_creator(Misc):

        def file_create(self, fname, code):
            self.filename = fname
            self.code = code
            self.content = web.html_mx(str(self.code))
            try:
                f = open(self.filename, "a")
                f.write(str(self.content))
                f.close()
                console.log(f"{filename} Created Successfully ...")
            except:
                Misc.Clear_screen(self)
                exit(banner.banner1)

    try:
        m = Misc()
        m.Clear_screen()

        f = File_creator()

        m.banner_print(banner.help_menu_banner)
        print("python web-easy.py --info")

        parser = argparse.ArgumentParser()

        parser.add_argument("-o","--output", help="Your FileName")

        parser.add_argument("-f","--file", help="Your Command-file Name")

        parser.add_argument(
            "-i",
            "--info",
            help="Give Detailed Info About Usage.",
            nargs="?",
            type=str.lower,
        )

        parser.add_argument(
            "-a",
            "--add",
            help="Mix The Components.",
            nargs="*",
            metavar=("components",),
            type=str.lower,
        )

        args = parser.parse_args()
        mx = args.add
        mxf = args.file
        filename = args.output

        def dry2(code):
            m.Clear_screen()
            m.banner_print(banner.help_menu_banner)
            tasks = [
                f"Command [{n}] Processing..." for n in range(1, len(sys.argv) - 3)
            ]
            with console.status("[bold green]Creating Your File...") as status:
                while tasks:
                    task = tasks.pop(0)
                    sleep(0.50)
                    console.log(f"{task}")
            console.log("Command [*] Completed ...")
            f.file_create(filename, code)

        value2 = dry2

        optionss2 = component_dict(value2)

        if mxf:
            try:
                for cmd in open(mxf, "r"):
                        cmd = str(cmd).strip().lower()
                        import re
                        cmd = re.sub("[\n]", "", cmd)

                        if cmd not in choices():
                            sys.stderr.write("[+] Please Pass The Valid Commands [+]")
                            sys.exit(0)

                if exists(f"{filename}"):
                    open(f"{filename}", "w").write(str(web.html_mx("bootstrap-start")))
                    for cmd in open(mxf, "r"):
                        cmd = str(cmd).strip().lower()
                        import re
                        cmd = re.sub("[\n]", "", cmd)
                        optionss2[cmd](str("bootstrap-" + cmd))
                    optionss2["end"](str("bootstrap-end"))

                else:
                    optionss2["start"](str("bootstrap-start"))
                    for cmd in open(mxf, "r"):
                        cmd = str(cmd).strip().lower()
                        cmd = re.sub("[\n]", "", cmd)
                        optionss2[cmd](str("bootstrap-" + cmd))
                    optionss2["end"](str("bootstrap-end"))

            except:
                pass

        elif mx:
            try:
                cmd2 = ""

                for i in range(0, len(mx)):
                        cmd2 = mx[i]
                        if cmd2 not in choices():
                            sys.stderr.write("[+] Please Pass The Valid Commands [+]")
                            sys.exit(0)
                            
                if exists(f"{filename}"):
                    open(f"{filename}", "w").write(str(web.html_mx("bootstrap-start")))
                    for i in range(0, len(mx)):
                        cmd2 = mx[i]
                        optionss2[cmd2](str("bootstrap-" + cmd2))
                    optionss2["end"](str("bootstrap-end"))
                else:
                    optionss2["start"](str("bootstrap-start"))
                    for i in range(0, len(mx)):
                        cmd2 = mx[i]
                        optionss2[cmd2](str("bootstrap-" + cmd2))
                    optionss2["end"](str("bootstrap-end"))
            except:
                pass
        
        for i in sys.argv:
            if (i == "--info" or i == "-i"):
                help()

    except (IOError) as e:
        sys.stderr(e)
        sys.exit()

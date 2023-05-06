help_menu_banner = """
       \_______/
   `.,-'\_____/`-.,'
    /`..'\ _ /`.,'\\
   /  /`.,' `.,'\  \\
__/__/__/     \__\__\__
  \  \  \     /  /  /     ┬ ┬┌─┐┌┐    ┌─┐┌─┐┌─┐┬ ┬ 
   \  \,'`._,'`./  /      │││├┤ ├┴┐───├┤ ├─┤└─┐└┬┘
    \,'`./___\,'`./       └┴┘└─┘└─┘   └─┘┴ ┴└─┘ ┴
   ,'`-./_____\,-'`.       ~ THE FRONTEND ASTRA ~
       /       \\                                  By:-Rohit Singh
"""

from rich.console import Console
console = Console()

def success(filename):
     console.log(f"{filename} Created Successfully ...")
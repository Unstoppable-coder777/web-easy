from sys import platform
from os import system
from .banner import help_menu_banner
from time import sleep
import sys

def Clear_screen():
    if platform == "linux" or platform == "linux2":
        system("clear")
    elif platform == "win32":
        system("cls")


def preloader():
    for chr in help_menu_banner:
        sleep(0.01)
        sys.stdout.write(chr)
        sys.stdout.flush()


def typing_animate(your_args,sleep_second):
    for chr in your_args:
        sleep(sleep_second)
        sys.stdout.write(chr)
        sys.stdout.flush()


def help():
    Clear_screen()
    data = ["-i --info    Give Detailed Info Usage",
            "-a --add     Merge Components",
            "-f --file    Merge Components Using TEXT file",
            "-o --output  Saves Your Output In a File",
        ]

    preloader()
    print("\nUSAGE : \n")
    typeing = "python web-easy.py [OPTION] COMMAND [ARGS] ... "+"\n"
    typing_animate(typeing,0.02)
    print("\n"+"Options:\n")
    for i in range(0, len(data)):
        print(data[i])

    colors_1 = [
        "    primary         pink    orange",
        "    secondary       blue    gray",
        "    info            teal    gray-dark",
        "    success         indigo  ",
        "    danger          purple  ",
        "    warning         red     ",
        "    light           yellow  ",
        "    dark            cyan    ",
        "    white           green   ",
    ]

    print("\nColors: ")
    print("\nBootstrap Colors    Custom Colors")
    print("="*16+" "*4+"="*14)
    for co1 in range(0, len(colors_1)):
        print(str(colors_1[co1]).capitalize())
    
    print("\nTotal Colors == 21")

    commandss = [
        "           Commands                            Description",
        "===============================     =========================================================",
        " navbar-color                        Simple Navbar",
        " navbar-color-sb                     Navbar With Search Bar",
        " navbar-color-sticky                 Sticky Navbar",
        " navbar-color-sb-sticky              Sticky Navbar With Search Bar",
        " navbar-btn-color-fg-color           Navbar With Login,SignUp Button",
        " navbar-dd-sb-color-fg-color         Navbar With Dropdown Menu,Search Bar",
        " navbar-dd-btn-color-fg-color        Navbar With Dropdown Menu,Login,Signup Button",
        " navbar-sb-btn-color-fg-color        Navbar With Search Bar,Login,SignUp Button",
        " navbar-dd-sb-btn-color-fg-color     Navbar With DropDown Menu,Search Bar,Login,SignUp Button",
        " navbar-2-color-fg-color             Simple Navbar-2",
        " navbar-2-dd-color-fg-color          Navbar-2 With DropDown Menu",
        " navbar-2-dd-sb-color-fg-color       Navbar-2 With Dropdown Menu,Search Bar",
        " navbar-2-btn-color-fg-color         Navbar-2 With Login,SignUp Button",
        " navbar-2-sb-btn-color-fg-color      Navbar-2 With Search Bar,Login,SignUp Button",
        " navbar-2-dd-btn-color-fg-color      Navbar-2 With Dropdown Menu,Login,Signup Button",
        " navbar-2-dd-sb-btn-color-fg-color   Navbar-2 With DropDown Menu,Search Bar,Login,SignUp Button",
        " navbar-hero-color-fg-color          Navbar With Hero Section,Foreground",
        " navbar-hero-img-color-fg-color      Navbar With Hero Section With Image Background,Foreground",
        " ic-navbar-color-fg-color            Simple Iconic Navbar With Foreground-color Icon",
        " ic-nm-navbar-color-fg-color         Simple Iconic Navbar With Icons Names,Foreground-color Icon",
        " ic-navbar-sb-color-fg-color         Iconic Navbar With Search Bar,Foreground-color Icon",
        " ic-nm-navbar-sb-color-fg-color      Iconic Navbar With Search Bar,Icons Names,Foreground-color Icon",
        " ic-navbar-btn-color-fg-color        Iconic Navbar With Login,Signup Button,Foreground-color Icon",
        " ic-nm-navbar-btn-color-fg-color     Iconic Navbar With Icons names,Login,Signup Button,Foreground-color Icon",
        " ic-navbar-sb-btn-color-fg-color     Iconic Navbar With Search Bar,Login,Signup Button,Foreground-color Icon",
        " ic-nm-navbar-sb-btn-color-fg-color  Iconic Navbar With Icons names,Search Bar,Login,Signup Button,Foreground-color Icon"+
        "\n---------------------------------------------------------------------------------------------",
        " sidebar-left-color-fg-color         Simple Left-Sidebar",
        " sidebar-right-color-fg-color        Simple Right-Sidebar"+
        "\n---------------------------------------------------------------------------------------------",
        " contact-form-color-fg-color         Simple Contact Form With BG,FG"+
        "\n---------------------------------------------------------------------------------------------",
        " carousel-slide                      Image Slider with Sliding Effect with medium height",
        " carousel-slide-fade                 Image Slider with Fade Effect with medium height",
        " carousel-slide-fs                   Fullscreen Image Slider with Sliding Effect with medium height",
        " carousel-slide-fade-fs              Fullscreen Image Slider with Fade Effect with medium height",
        " carousel-dark-slide                 Dark-mode Image Slider with Sliding Effect with medium height",
        " carousel-dark-slide-fade            Dark-mode Image Slider with Fade Effect with medium height",
        " carousel-dark-slide-fs              Dark-mode Fullscreen Image Slider with Sliding Effect with medium height",
        " carousel-dark-slide-fade-fs         Dark-mode Fullscreen Image Slider with Fade Effect with medium height"+
        "\n---------------------------------------------------------------------------------------------",
        " card-color                          Solid Color Card",
        " card-img-color                      Card With Image",
        " custom-card-img-1                   Custom Card With Background Image",
        " card-color-fg-color                 Normal Card With Foreground",
        " card-img-color-fg-color             Image Card With Foreground",
        " profile-card-color-fg-color         Profile Card With BG,FG",
        " product-card-color-fg-color         Product Card With BG,FG",
        " custom-product-card                 Custom Product Card With Add to cart,BG,FG",
        " ic-card-1-color-fg-color            Iconic Card-1 With ForeGround Color Icons",
        " ic-card-2-color-fg-color            Iconic Card-2 With ForeGround Color Icons",
        " ic-card-3-color-fg-color            Iconic Card-3 With ForeGround Color Icons"+
        "\n---------------------------------------------------------------------------------------------",
        " header-color-fg-color               Header With Background,ForeGround"+
        "\n---------------------------------------------------------------------------------------------",
        " hero-color-fg-color                 Minimalist Hero With Foreground",
        " hero-img                            Hero With Background-Image,Search-Bar",
        " hero-header-color-fg-color          Hero Section With Navigation,ForeGround",
        " hero-center-color-fg-color          Hero Section With Center-Position,ForeGround",
        " hero-left-color-fg-color            Hero Section With Left-Position,ForeGround",
        " hero-right-color-fg-color           Hero Section With Right-Position,ForeGround",
        " hero-img-2-color-fg-color           Hero With Background-Image,Foreground"+
        "\n---------------------------------------------------------------------------------------------",
        " jumbotron-1-color-fg-color          Single Jumbotron Component With BG,FG",
        " jumbotron-2-color-fg-color          Double Jumbotron Component With BG,FG"+
        "\n---------------------------------------------------------------------------------------------",
        " login-1-color-fg-color              Login Page With Background,ForeGround",
        " login-hero-1-color-fg-color         Login Page With Left Side Image",
        " login-hero-2-color-fg-color         Login Page With Right Side Image"+
        "\n---------------------------------------------------------------------------------------------",
        " register-1-color-fg-color           Register Page With Background,ForeGround"+
        "\n---------------------------------------------------------------------------------------------",
        " testimonial-color-fg-color          Testimonial Section With Foreground"+
        "\n---------------------------------------------------------------------------------------------",
        " showcase-color-fg-color             Showcase Section With Foreground"+
        "\n---------------------------------------------------------------------------------------------",
        " service-color-fg-color              Service Section With BG,FG"+
        "\n---------------------------------------------------------------------------------------------",
        " footer-color-fg-color               Footer Part With Foreground",
        " footer-2-color-fg-color             3-Column Footer With BG,FG"+
        "\n---------------------------------------------------------------------------------------------",
        " dashboard-color                     Admin Dashboard With BG",
    ]

    print("\n")
    total_components = 0
    for cmd in commandss:
        print(cmd)
        total_components +=1
    total_components = total_components - 2

    print("\nTotal Components == "+str(total_components))

    print("\n --add Examples : ")
    typing_animate("\n\t\tpython web-easy.py --add navbar-dark --output index.html",0.02)
    typing_animate("\n\t\tpython web-easy.py --add navbar-dark hero-light-fg-orange --output index.html",0.02)
    print("\n\n--file Examples : ")
    print("\n\t\t:: First Make A TEXT File and Writes Commands In It ::")
    typing_animate("\t\tpython web-easy.py --file cmd.txt --output index.html\n",0.02)
from src.modules import html_code
from src.modules.html_code import *


def basic_html(content):
    html = f"""<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<link rel="stylesheet" href="./src/css/bootstrap.css" />\n\t<meta charset="UTF-8" />\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge" />\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n\t<title>Document</title>\n</head>\n<body>{content}\n\t<script src="./src/js/bootstrap.bundle.min.js"></script>\n</body>\n</html>"""
    return html


def basic_html_2(content):
    html = f"""<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<link rel="stylesheet" href="./src/css/bootstrap.css" />\n\t<meta charset="UTF-8" />\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge" />\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n\t<title>Document</title>\n</head>\n<body>{content}\n\t<script src="./src/js/script2.js"></script>\n\t<script src="./src/js/bootstrap.bundle.min.js"></script>\n</body>\n</html>"""
    return html


start_html = """<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<link rel="stylesheet" href="./src/css/bootstrap.css" />\n\t<meta charset="UTF-8" />\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge" />\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n\t<title>Document</title>\n</head>\n<body>"""

end_html = (
    """\n\t<script src="./src/js/bootstrap.bundle.min.js"></script>\n</body>\n</html>"""
)


def html_mx(*args):
    cmd = list(args)
    colors = [
        "primary",
        "secondary",
        "info",
        "success",
        "danger",
        "warning",
        "light",
        "dark",
        "pink",
        "blue",
        "teal",
        "indigo",
        "purple",
        "red",
        "yellow",
        "cyan",
        "white",
        "green",
        "gray",
        "orange",
        "gray-dark",
    ]

    for i in range(0, len(cmd)):
        for j in range(0, len(colors)):
            for color in range(0, len(colors)):
                if cmd[i] == f"bootstrap-navbar-{colors[color]}":
                    getcode = html_code.custom_navbar_mix(f"{colors[color]}")
                    return getcode

                elif cmd[i] == f"bootstrap-navbar-{colors[color]}-sb":
                    getcode = html_code.custom_navbar_sb(f"{colors[color]}")
                    return getcode

                elif cmd[i] == f"bootstrap-navbar-{colors[color]}-sticky":
                    getcode = html_code.custom_navbar(f"{colors[color]}")
                    return getcode

                elif cmd[i] == f"bootstrap-navbar-{colors[color]}-sb-sticky":
                    getcode = html_code.custom_navbar_sb(f"{colors[color]}")
                    return getcode

                elif cmd[i] == f"bootstrap-card-{colors[color]}":
                    getcode = html_code.custom_card(f"{colors[color]}")
                    return getcode

                elif cmd[i] == f"bootstrap-card-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_card_fg(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i] == f"bootstrap-card-bordered-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_card_fg_bordered(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-card-img-{colors[color]}":
                    getcode = html_code.custom_card_img(f"{colors[color]}")
                    return getcode

                elif cmd[i] == f"bootstrap-card-img-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_card_img_fg(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == "bootstrap-start":
                    htmlc = start_html
                    return htmlc

                elif cmd[i] == "bootstrap-end":
                    htmlc = end_html
                    return htmlc

                elif cmd[i] == f"bootstrap-hero-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_hero(f"{colors[color]}", f"{colors[j]}")
                    return getcode

                elif cmd[i] == f"bootstrap-testimonial-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_testimonial(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-hero-img":
                    getcode = html_code.custom_hero_img()
                    return getcode

                elif cmd[i] == f"bootstrap-hero-img-2-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_hero_img2(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-showcase-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_showcase(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-footer-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_footer_first(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-footer-2-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_footer_2(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-navbar-hero-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_navhero(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i]
                    == f"bootstrap-navbar-hero-img-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_navhero_img(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-navbar-2-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_navbar_2(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-navbar-2-dd-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_navbar_2_dd(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-navbar-btn-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_navbar_btn(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-navbar-2-btn-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_navbar_2_btn(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i] == f"bootstrap-navbar-dd-btn-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_navbar_dd_btn(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i]
                    == f"bootstrap-navbar-2-dd-btn-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_navbar_2_dd_btn(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i] == f"bootstrap-navbar-sb-btn-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_navbar_sb_btn(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i]
                    == f"bootstrap-navbar-2-sb-btn-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_navbar_2_sb_btn(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i]
                    == f"bootstrap-navbar-dd-sb-btn-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_navbar_dd_sb_btn(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i]
                    == f"bootstrap-navbar-2-dd-sb-btn-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_navbar_2_dd_sb_btn(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-navbar-dd-sb-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_navbar_dd_sb(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i] == f"bootstrap-navbar-2-dd-sb-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_navbar_2_dd_sb(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-ic-navbar-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_ic_navbar(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-ic-nm-navbar-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_ic_nm_navbar(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-ic-navbar-sb-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_ic_sb_navbar(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i]
                    == f"bootstrap-ic-nm-navbar-sb-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_ic_nm_sb_navbar(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i] == f"bootstrap-ic-navbar-btn-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_ic_btn_navbar(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i]
                    == f"bootstrap-ic-nm-navbar-btn-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_ic_nm_btn_navbar(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i]
                    == f"bootstrap-ic-navbar-sb-btn-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_ic_sb_btn_navbar(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i]
                    == f"bootstrap-ic-nm-navbar-sb-btn-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_ic_nm_sb_btn_navbar(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-custom-card-img-1":
                    getcode = html_code.custom_card_img_2()
                    return getcode

                elif cmd[i] == f"bootstrap-ic-card-1-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_ic_card_1(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-ic-card-2-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_ic_card_2(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-ic-card-3-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_ic_card_3(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-hero-header-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_hero_section_1(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-hero-center-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_hero_section_2(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-hero-left-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_hero_section_4(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-hero-right-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_hero_section_3(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-jumbotron-1-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_jumbotron_1(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-jumbotron-2-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_jumbotron_2(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-login-1-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_login_1(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-register-1-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_register_1(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-header-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_header_1(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-carousel-slide":
                    getcode = html_code.custom_carousel_slide("normal")
                    return getcode

                elif cmd[i] == f"bootstrap-carousel-slide-fade":
                    getcode = html_code.custom_carousel_slide("carousel-fade")
                    return getcode

                elif cmd[i] == f"bootstrap-carousel-slide-fs":
                    getcode = html_code.custom_carousel_fullscreen_slide("normal")
                    return getcode

                elif cmd[i] == f"bootstrap-carousel-slide-fade-fs":
                    getcode = html_code.custom_carousel_fullscreen_slide(
                        "carousel-fade"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-carousel-dark-slide":
                    getcode = html_code.custom_carousel_slide_dark("normal")
                    return getcode

                elif cmd[i] == f"bootstrap-carousel-dark-slide-fade":
                    getcode = html_code.custom_carousel_slide_dark("carousel-fade")
                    return getcode

                elif cmd[i] == f"bootstrap-carousel-dark-slide-fs":
                    getcode = html_code.custom_carousel_fullscreen_slide_dark("normal")
                    return getcode

                elif cmd[i] == f"bootstrap-carousel-dark-slide-fade-fs":
                    getcode = html_code.custom_carousel_fullscreen_slide_dark(
                        "carousel-fade"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-login-hero-1-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_hero_login(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-login-hero-2-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_hero_login_2(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-service-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_service_1(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-profile-card-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_profile_card_1(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-contact-form-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_contact_form(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-sidebar-left-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_sidebar(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif (
                    cmd[i] == f"bootstrap-sidebar-right-{colors[color]}-fg-{colors[j]}"
                ):
                    getcode = html_code.custom_sidebar_2(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-dashboard-{colors[color]}":
                    getcode = html_code.custom_dashboard(f"{colors[color]}")
                    return getcode

                elif cmd[i] == f"bootstrap-product-card-{colors[color]}-fg-{colors[j]}":
                    getcode = html_code.custom_product_card(
                        f"{colors[color]}", f"{colors[j]}"
                    )
                    return getcode

                elif cmd[i] == f"bootstrap-custom-product-card":
                    getcode = html_code.custom_product_card_custom()
                    return getcode

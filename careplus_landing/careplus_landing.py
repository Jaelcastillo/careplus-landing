import reflex as rx

from careplus_landing.components.navbar import navbar
from careplus_landing.components.hero import hero_section


def index():

    return rx.box(

        navbar(),

        hero_section(),

        bg="#eef9fb",
        min_height="100vh",
        padding="2rem",
    )


app = rx.App()
app.add_page(index)
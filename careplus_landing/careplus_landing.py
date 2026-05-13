import reflex as rx
from careplus_landing.components.navbar import navbar
from careplus_landing.components.hero import hero
from careplus_landing.components.departments import departments
from careplus_landing.components.services import services, heartbeat_bar
 
 
def index() -> rx.Component:
    return rx.box(
        navbar(),
        hero(),
        departments(),
        services(),
        heartbeat_bar(),
        background="white",
        min_height="100vh",
        font_family="'Inter', 'Segoe UI', sans-serif",
    )
 
 
app = rx.App(
    style={
        "font_family": "'Inter', 'Segoe UI', sans-serif",
        "margin": "0",
        "padding": "0",
    },
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap",
    ],
)
app.add_page(index, route="/", title="Nova Super Specialist Hospital")
 
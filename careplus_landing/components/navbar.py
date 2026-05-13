import reflex as rx


def navbar():

    menu_items = [
        "Home",
        "Services",
        "Departments",
        "Doctors",
        "Contact",
    ]

    return rx.hstack(

       rx.text(
    "✚ CAREPLUS MEDICAL",
    font_weight="bold",
    font_size="20px",
    color="#111111",
),
        rx.hstack(
            *[
                rx.link(
                    item,
                    href="#",
                    color="black",
                    font_weight="medium",
                )
                for item in menu_items
            ],
            spacing="6",
        ),

        rx.button(
            "Book Appointment",
            bg="#70d6df",
            color="white",
            border_radius="999px",
            padding="1rem 1.5rem",
        ),

        justify="between",
        align="center",
        bg="white",
        padding="1.5rem 2rem",
        border_radius="25px",
        box_shadow="0 4px 12px rgba(0,0,0,0.05)",
        width="100%",
    )
import reflex as rx


def hero_section():

    return rx.box(

        rx.hstack(

            rx.vstack(

                rx.heading(
                    "Your Health,\nOur Priority",
                    font_size="64px",
                    line_height="1.1",
                    white_space="pre-line",
                    color="#111111",
                    font_weight="900",
                ),

                rx.text(
                    "Compassionate care for you and your family.",
                    color="#555555",
                    font_size="20px",
                ),

                spacing="5",
                align="start",
                width="50%",
            ),

            rx.image(
                src="https://images.unsplash.com/photo-1612349317150-e413f6a5b16d",
                width="450px",
                height="300px",
                border_radius="30px",
                object_fit="cover",
            ),

            justify="between",
            align="center",
            width="100%",
        ),

        rx.hstack(
            rx.vstack(
                rx.text("Department", font_weight="bold", color="#222"),
                rx.select(["Emergency", "Pediatric", "Cardiology"], placeholder="Department"),
                align="start",
            ),
            rx.vstack(
                rx.text("Doctor", font_weight="bold", color="#222"),
                rx.select(["Dr. Smith", "Dr. Johnson", "Dr. Brown"], placeholder="Doctor"),
                align="start",
            ),
            rx.vstack(
                rx.text("Date", font_weight="bold", color="#222"),
                rx.input(type="date"),
                align="start",
            ),
            rx.button(
                "Book Now",
                bg="#70d6df",
                color="white",
                border_radius="999px",
                padding="1rem 2rem",
                margin_top="1.6rem",
            ),
            bg="rgba(255,255,255,0.85)",
            padding="1.5rem",
            border_radius="20px",
            box_shadow="0 8px 25px rgba(0,0,0,0.10)",
            width="70%",
            position="absolute",
            bottom="-45px",
            left="50%",
            transform="translateX(-50%)",
            justify="between",
            align="center",
        ),

        bg="#dff7fa",
        padding="4rem",
        padding_bottom="6rem",
        border_radius="35px",
        margin_top="2rem",
        position="relative",
    )
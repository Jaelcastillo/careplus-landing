import reflex as rx


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Logo
            rx.hstack(
                rx.box(
                    rx.html("""
                    <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M14 2 L18 10 L27 11 L21 17 L22.5 26 L14 22 L5.5 26 L7 17 L1 11 L10 10 Z" fill="white" opacity="0.9"/>
                      <rect x="11" y="8" width="6" height="2" rx="1" fill="#4a9faf"/>
                      <rect x="13" y="6" width="2" height="6" rx="1" fill="#4a9faf"/>
                    </svg>
                    """),
                    background="rgba(255,255,255,0.25)",
                    border_radius="8px",
                    width="36px",
                    height="36px",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                ),
                rx.vstack(
                    rx.text("Nova Super", font_size="11px", font_weight="700", color="white", line_height="1"),
                    rx.text("Specialist hospital", font_size="10px", font_weight="400", color="rgba(255,255,255,0.85)", line_height="1"),
                    spacing="1",
                    align_items="start",
                ),
                spacing="2",
                align_items="center",
            ),
            # Nav links
            rx.hstack(
                rx.link("Home", href="#", color="white", font_size="14px", font_weight="600", text_decoration="none", border_bottom="2px solid white", padding_bottom="2px"),
                rx.link("Service", href="#", color="rgba(255,255,255,0.85)", font_size="14px", font_weight="400", text_decoration="none", _hover={"color": "white"}),
                rx.link("About Us", href="#", color="rgba(255,255,255,0.85)", font_size="14px", font_weight="400", text_decoration="none", _hover={"color": "white"}),
                rx.link("Blog", href="#", color="rgba(255,255,255,0.85)", font_size="14px", font_weight="400", text_decoration="none", _hover={"color": "white"}),
                rx.link("Contact Us", href="#", color="rgba(255,255,255,0.85)", font_size="14px", font_weight="400", text_decoration="none", _hover={"color": "white"}),
                spacing="7",
                align_items="center",
            ),
            # Book button
            rx.button(
                "Book Appointment",
                background="white",
                color="#3a8fa0",
                border_radius="25px",
                padding_x="20px",
                padding_y="10px",
                font_size="13px",
                font_weight="700",
                border="none",
                cursor="pointer",
                _hover={"background": "#f0fafa", "transform": "translateY(-1px)"},
                transition="all 0.2s ease",
            ),
            justify="between",
            align_items="center",
            width="100%",
        ),
        background="linear-gradient(135deg, #5badc0 0%, #4a9faf 50%, #3a8fa0 100%)",
        padding_x="36px",
        padding_y="16px",
        position="sticky",
        top="0",
        z_index="100",
    )
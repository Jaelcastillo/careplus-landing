import reflex as rx

MONITOR_SVG = """<svg width="44" height="44" viewBox="0 0 44 44" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect x="3" y="4" width="38" height="26" rx="4" fill="none" stroke="#5badc0" stroke-width="1.8"/>
<rect x="7" y="8" width="30" height="18" rx="1" fill="#e8f4f8"/>
<polyline points="9,21 13,21 16,13 19,29 21,15 23,23 27,23 31,21 35,21" stroke="#5badc0" stroke-width="1.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="18" y="30" width="8" height="6" fill="#5badc0" opacity="0.3"/>
<rect x="13" y="36" width="18" height="4" rx="2" fill="#5badc0" opacity="0.4"/>
</svg>"""

SCAN_SVG = """<svg width="44" height="44" viewBox="0 0 44 44" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect x="3" y="6" width="38" height="32" rx="4" fill="none" stroke="#5badc0" stroke-width="1.8"/>
<circle cx="22" cy="22" r="9" fill="none" stroke="#5badc0" stroke-width="1.4"/>
<circle cx="22" cy="22" r="4" fill="#5badc0" opacity="0.4"/>
<line x1="3" y1="22" x2="13" y2="22" stroke="#5badc0" stroke-width="1.4"/>
<line x1="31" y1="22" x2="41" y2="22" stroke="#5badc0" stroke-width="1.4"/>
</svg>"""

PILL_SVG = """<svg width="44" height="44" viewBox="0 0 44 44" fill="none" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="22" cy="22" rx="15" ry="8" fill="none" stroke="#5badc0" stroke-width="1.8" transform="rotate(-40 22 22)"/>
<line x1="12" y1="32" x2="32" y2="12" stroke="#5badc0" stroke-width="1.4"/>
<ellipse cx="22" cy="22" rx="15" ry="8" fill="#5badc0" opacity="0.15" transform="rotate(-40 22 22)"/>
</svg>"""

FLASK_SVG = """<svg width="44" height="44" viewBox="0 0 44 44" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M16 4 L16 18 L7 33 Q5 36 8 37 L36 37 Q39 36 37 33 L28 18 L28 4Z" fill="none" stroke="#5badc0" stroke-width="1.8" stroke-linejoin="round"/>
<path d="M12 27 Q22 23 32 27" fill="none" stroke="#5badc0" stroke-width="1.4"/>
<path d="M10 33 L34 33" fill="none" stroke="#5badc0" stroke-width="1" opacity="0.4"/>
<line x1="14" y1="4" x2="30" y2="4" stroke="#5badc0" stroke-width="1.8" stroke-linecap="round"/>
<path d="M12 27 Q22 23 32 27 L36 37 Q39 36 37 33 L28 18 L16 18 L7 33 Q5 36 8 37 L12 27Z" fill="#5badc0" opacity="0.12"/>
</svg>"""


def service_card_vertical(icon_svg: str, title: str, description: str) -> rx.Component:
    """Tarjeta con ícono grande arriba, título y descripción abajo."""
    return rx.box(
        rx.vstack(
            rx.box(
                rx.html(icon_svg),
                background="linear-gradient(135deg, #ddf0f7, #c8e6f0)",
                border_radius="12px",
                width="64px",
                height="64px",
                display="flex",
                align_items="center",
                justify_content="center",
                flex_shrink="0",
            ),
            rx.text(title, font_size="16px", font_weight="700", color="#0d2333"),
            rx.text(description, font_size="12px", color="#6b8a99", line_height="1.65"),
            align_items="start",
            spacing="3",
        ),
        background="white",
        border_radius="16px",
        padding="22px 20px",
        box_shadow="0 2px 16px rgba(0,0,0,0.07)",
        border="1px solid #e4f0f5",
        width="100%",
        _hover={
            "box_shadow": "0 6px 24px rgba(91,173,192,0.18)",
            "transform": "translateY(-2px)",
        },
        transition="all 0.25s ease",
        cursor="pointer",
    )


def heartbeat_bar() -> rx.Component:
    return rx.box(
        rx.html("""
        <svg viewBox="0 0 1200 50" preserveAspectRatio="none"
             xmlns="http://www.w3.org/2000/svg"
             style="width:100%;height:50px;display:block;">
          <polyline
            points="0,25 60,25 90,25 110,8 125,42 140,8 155,25
                    240,25 270,25 290,8 305,42 320,8 335,25
                    420,25 450,25 470,8 485,42 500,8 515,25
                    600,25 630,25 650,8 665,42 680,8 695,25
                    780,25 810,25 830,8 845,42 860,8 875,25
                    960,25 990,25 1010,8 1025,42 1040,8 1055,25
                    1140,25 1200,25"
            fill="none" stroke="#5badc0" stroke-width="2.2"
            stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        """),
        background="white",
        width="100%",
        height="50px",
        overflow="hidden",
        border_top="1px solid #e4f0f5",
    )


def services() -> rx.Component:
    return rx.box(
        # ── LAYOUT PRINCIPAL ────────────────────────────────────────
        rx.box(
            # COL 1 — Título + botón + Emergency + Pharmacy (apilados)
            rx.box(
                rx.vstack(
                    # Título
                    rx.heading(
                        "World-Class Healthcare Services for you and your loved ones",
                        font_size="26px",
                        font_weight="800",
                        color="white",
                        line_height="1.25",
                    ),
                    # Botón More Service
                    rx.button(
                        rx.hstack(
                            rx.text("More Service", font_size="13px", font_weight="600"),
                            rx.icon("arrow-right", size=13),
                            spacing="2",
                            align_items="center",
                        ),
                        background="transparent",
                        color="white",
                        border="2px solid white",
                        border_radius="25px",
                        padding_x="20px",
                        padding_y="10px",
                        cursor="pointer",
                        _hover={"background": "white", "color": "#3a8fa0"},
                        transition="all 0.2s ease",
                    ),
                    # Emergency card
                    service_card_vertical(
                        MONITOR_SVG,
                        "Emergency Services",
                        "24/7 immediate medical care for critical conditions, accidents, and life threatening situations. Equipped to handle trauma, cardiac arrest, and urgent interventions.",
                    ),
                    # Pharmacy card (parcialmente visible como en el original)
                    service_card_vertical(
                        PILL_SVG,
                        "Pharmacy",
                        "In-house medical store providing prescribed medications and health essentials, ensuring timely access to necessary drugs for both inpatients and outpatients.",
                    ),
                    align_items="start",
                    spacing="5",
                    width="100%",
                ),
                width="30%",
                flex_shrink="0",
            ),

            # COL 2 — Radiology (con offset arriba) + Laboratory
            rx.box(
                rx.vstack(
                    service_card_vertical(
                        SCAN_SVG,
                        "Radiology & Imaging",
                        "Advanced diagnostic imaging services including X-ray, CT scan, MRI, and ultrasound to assist in accurate and efficient diagnosis of medical conditions.",
                    ),
                    service_card_vertical(
                        FLASK_SVG,
                        "Laboratory Services",
                        "Comprehensive lab testing for blood, urine, and other samples, supporting fast and precise medical diagnosis and treatment planning.",
                    ),
                    align_items="start",
                    spacing="5",
                    width="100%",
                ),
                width="30%",
                flex_shrink="0",
                padding_top="120px",  # offset: Radiology empieza más arriba visualmente
            ),

            # COL 3 — Doctor image grande a la derecha
            rx.box(
                rx.image(
                    src="/DoctorMasculinoabajo.png",
                    height="520px",
                    object_fit="contain",
                    object_position="bottom center",
                    style={
                        "filter": "drop-shadow(-6px 0px 20px rgba(0,0,0,0.22))",
                        "display": "block",
                        "maxWidth": "100%",
                        "marginBottom": "0",
                    },
                ),
                width="40%",
                flex_shrink="0",
                display="flex",
                align_items="flex-end",
                justify_content="flex-end",
                padding_left="10px",
            ),

            display="flex",
            flex_direction="row",
            align_items="flex-end",
            gap="24px",
            width="100%",
            padding="48px 40px 0px 40px",
            overflow="hidden",
        ),

        background="linear-gradient(135deg, #3a7a90 0%, #2e6a80 50%, #1e5a70 100%)",
        width="100%",
        overflow="hidden",
        min_height="520px",
    )
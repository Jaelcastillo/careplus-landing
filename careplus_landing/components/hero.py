import reflex as rx


def stats_bar() -> rx.Component:
    def stat(number: str, label: str) -> rx.Component:
        return rx.vstack(
            rx.text(number, font_size="26px", font_weight="800", color="#1a2e3a", line_height="1"),
            rx.text(label, font_size="12px", color="#6b8a99", font_weight="500"),
            spacing="1",
            align_items="start",
        )

    return rx.hstack(
        stat("4500+", "Happy Patients"),
        rx.box(width="1px", height="40px", background="#d0e4ea"),
        stat("200", "Hospital Room"),
        rx.box(width="1px", height="40px", background="#d0e4ea"),
        stat("500+", "Award Win"),
        rx.box(width="1px", height="40px", background="#d0e4ea"),
        stat("20+", "Ambulance"),
        spacing="6",
        align_items="center",
        padding_y="24px",
        padding_x="40px",
        background="white",
    )


def search_filter_bar() -> rx.Component:
    def select_field(label: str) -> rx.Component:
        return rx.hstack(
            rx.text(label, font_size="13px", color="#4a6a7a", font_weight="500"),
            rx.icon("chevron-down", size=14, color="#4a6a7a"),
            spacing="2",
            align_items="center",
            justify="between",
            padding_x="16px",
            padding_y="13px",
            flex="1",
            cursor="pointer",
            border_right="1px solid #d0e4ea",
            _hover={"background": "rgba(91,173,192,0.05)"},
            min_width="160px",
        )

    return rx.box(
        rx.hstack(
            select_field("Select Department"),
            select_field("Select Doctor"),
            select_field("Select Date"),
            select_field("Select Location"),
            rx.hstack(
                rx.icon("search", size=14, color="#3a8fa0"),
                rx.text("Search", font_size="13px", color="#3a8fa0", font_weight="600"),
                spacing="2",
                align_items="center",
                background="white",
                padding_x="22px",
                padding_y="13px",
                border_radius="0 10px 10px 0",
                cursor="pointer",
                _hover={"background": "#f0fafa"},
            ),
            spacing="0",
            align_items="stretch",
            width="100%",
        ),
        background="#d8eef5",
        border_radius="12px",
        border="1px solid #c0d8e4",
        overflow="hidden",
        box_shadow="0 4px 24px rgba(58,143,160,0.10)",
        margin_x="40px",
        margin_top="0px",
        margin_bottom="0px",
    )


def hero() -> rx.Component:
    return rx.box(
        # ── HERO MAIN AREA ──────────────────────────────────────────
        rx.hstack(
            # LEFT — text content
            rx.vstack(
                rx.box(height="10px"),
                rx.heading(
                    "Premium Treatments for",
                    as_="h1",
                    font_size="38px",
                    font_weight="800",
                    color="#0d2333",
                    line_height="1.15",
                    letter_spacing="-0.5px",
                ),
                rx.heading(
                    "a Healthy Lifestyle",
                    as_="h1",
                    font_size="38px",
                    font_weight="800",
                    color="#0d2333",
                    line_height="1.15",
                    letter_spacing="-0.5px",
                    margin_top="-4px",
                ),
                rx.text(
                    "Seamlessly advance scalable architectures with future-ready growth strategies. "
                    "Efficiently implement low-risk, high-return process enhancements tailored for "
                    "mission-critical testing procedures, especially in publishing and related industries.",
                    font_size="13px",
                    color="#6b8a99",
                    line_height="1.7",
                    max_width="380px",
                    margin_top="4px",
                ),
                # View Our Hospital button only — search card moves to RIGHT side
                rx.hstack(
                    rx.button(
                        rx.hstack(
                            rx.text("View Our Hospital", font_size="14px", font_weight="600"),
                            rx.box(
                                rx.icon("play", size=12, color="#3a8fa0"),
                                background="white",
                                border_radius="50%",
                                width="24px",
                                height="24px",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                            ),
                            spacing="2",
                            align_items="center",
                        ),
                        background="linear-gradient(135deg, #5badc0, #3a8fa0)",
                        color="white",
                        border_radius="25px",
                        padding_x="20px",
                        padding_y="12px",
                        border="none",
                        cursor="pointer",
                        _hover={"opacity": "0.9", "transform": "translateY(-1px)"},
                        transition="all 0.2s ease",
                    ),
                    spacing="4",
                    align_items="center",
                    margin_top="8px",
                ),
                align_items="start",
                spacing="3",
                flex="1",
                padding_left="40px",
                padding_top="36px",
                padding_bottom="40px",
                z_index="2",
                position="relative",
            ),

            # RIGHT — doctor image with overlapping elements
            rx.box(
                # Teal blob circle behind doctor
                rx.box(
                    position="absolute",
                    top="20px",
                    right="30px",
                    width="340px",
                    height="400px",
                    border_radius="50% 50% 50% 50% / 40% 40% 60% 60%",
                    background="linear-gradient(160deg, #7ec8d8 0%, #5badc0 50%, #4a9faf 100%)",
                    z_index="0",
                ),
                # Small decorative circle bottom-left of blob
                rx.box(
                    position="absolute",
                    bottom="80px",
                    right="10px",
                    width="50px",
                    height="50px",
                    border_radius="50%",
                    background="#5badc0",
                    opacity="0.5",
                    z_index="0",
                ),

                # Doctor photo
                rx.image(
                    src="/image-removebg-preview.png",
                    height="420px",
                    object_fit="contain",
                    position="relative",
                    z_index="2",
                    style={"filter": "drop-shadow(0 8px 24px rgba(0,0,0,0.12))"},
                ),

                # 2500+ Doctors Online badge — top right
                rx.hstack(
                    rx.box(
                        width="10px",
                        height="10px",
                        border_radius="50%",
                        background="#22c55e",
                    ),
                    rx.text("2500+ Doctors Online", font_size="12px", font_weight="600", color="#1a2e3a"),
                    spacing="2",
                    align_items="center",
                    background="white",
                    border_radius="20px",
                    padding_x="12px",
                    padding_y="7px",
                    box_shadow="0 2px 12px rgba(0,0,0,0.1)",
                    position="absolute",
                    top="16px",
                    right="10px",
                    z_index="4",
                ),

                # Search the Medical card — overlapping bottom-left of image
                rx.hstack(
                    rx.box(
                        rx.icon("search", size=18, color="white"),
                        background="#1a2e3a",
                        border_radius="10px",
                        width="44px",
                        height="44px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        flex_shrink="0",
                    ),
                    rx.vstack(
                        rx.text("Search the Medical", font_size="13px", font_weight="700", color="#1a2e3a", line_height="1"),
                        rx.text("With more Care Option", font_size="11px", color="#6b8a99", line_height="1"),
                        spacing="1",
                        align_items="start",
                        gap="3px",
                    ),
                    spacing="3",
                    align_items="center",
                    background="white",
                    border_radius="12px",
                    padding_x="16px",
                    padding_y="12px",
                    box_shadow="0 6px 20px rgba(0,0,0,0.12)",
                    position="absolute",
                    # Overlapping: sits on top of doctor image, centre-bottom area
                    bottom="90px",
                    left="-10px",
                    z_index="5",
                    white_space="nowrap",
                ),

                position="relative",
                flex="1",
                min_height="440px",
                display="flex",
                align_items="flex-end",
                justify_content="center",
                overflow="visible",
            ),

            width="100%",
            spacing="0",
            align_items="stretch",
        ),

        # ── STATS BAR ────────────────────────────────────────────────
        rx.box(
            rx.divider(border_color="#d0e4ea"),
            stats_bar(),
            background="white",
        ),

        # ── SEARCH FILTER BAR ────────────────────────────────────────
        rx.box(
            search_filter_bar(),
            background="#eef8fb",
            padding_y="28px",
        ),

        background="linear-gradient(180deg, #eef8fb 0%, #e4f2f7 60%, white 100%)",
        style={
            "backgroundImage": "radial-gradient(circle, #c8dde6 1px, transparent 1px)",
            "backgroundSize": "30px 30px",
            "backgroundColor": "#eef8fb",
        },
        width="100%",
    )
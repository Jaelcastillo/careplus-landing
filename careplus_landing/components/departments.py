import reflex as rx

KIDNEY_SVG = """<svg width="90" height="90" viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="45" cy="45" r="44" fill="#eaf5f8" stroke="#d0e8f0" stroke-width="1"/>
<ellipse cx="32" cy="45" rx="13" ry="20" fill="#c8e6f0" stroke="#5badc0" stroke-width="1.5"/>
<ellipse cx="58" cy="45" rx="13" ry="20" fill="#c8e6f0" stroke="#5badc0" stroke-width="1.5"/>
<ellipse cx="32" cy="45" rx="7" ry="13" fill="#a8d4e4" stroke="#5badc0" stroke-width="1"/>
<ellipse cx="58" cy="45" rx="7" ry="13" fill="#a8d4e4" stroke="#5badc0" stroke-width="1"/>
<path d="M39 42 Q45 45 51 42" stroke="#5badc0" stroke-width="1.5" fill="none" stroke-linecap="round"/>
<path d="M39 48 Q45 45 51 48" stroke="#5badc0" stroke-width="1.5" fill="none" stroke-linecap="round"/>
<line x1="32" y1="28" x2="32" y2="30" stroke="#5badc0" stroke-width="1.5" stroke-linecap="round"/>
<line x1="58" y1="28" x2="58" y2="30" stroke="#5badc0" stroke-width="1.5" stroke-linecap="round"/>
<path d="M38 36 Q45 33 52 36" stroke="#5badc0" stroke-width="1.2" fill="none" stroke-linecap="round"/>
<path d="M38 54 Q45 57 52 54" stroke="#5badc0" stroke-width="1.2" fill="none" stroke-linecap="round"/>
</svg>"""

HEART_SVG = """<svg width="90" height="90" viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="45" cy="45" r="44" fill="#eaf5f8" stroke="#d0e8f0" stroke-width="1"/>
<path d="M45 68 C45 68 18 52 18 34 C18 24 26 18 34 20 C39 21 43 25 45 28 C47 25 51 21 56 20 C64 18 72 24 72 34 C72 52 45 68 45 68Z" fill="#c8e6f0" stroke="#5badc0" stroke-width="1.5"/>
<path d="M45 62 C45 62 22 48 22 34 C22 26 29 22 36 24 C40 25 43 28 45 31 C47 28 50 25 54 24 C61 22 68 26 68 34 C68 48 45 62 45 62Z" fill="#a8d4e4" stroke="#5badc0" stroke-width="1"/>
<path d="M34 38 L38 38 L40 30 L42 50 L44 34 L46 42 L50 42 L54 38 L58 38" stroke="#5badc0" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

LUNGS_SVG = """<svg width="90" height="90" viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="45" cy="45" r="44" fill="#eaf5f8" stroke="#d0e8f0" stroke-width="1"/>
<rect x="42" y="15" width="6" height="25" rx="3" fill="#c8e6f0" stroke="#5badc0" stroke-width="1.5"/>
<path d="M45 30 C45 30 26 33 22 46 C19 56 22 66 30 68 C36 70 40 66 42 60 C44 55 45 48 45 42" fill="#c8e6f0" stroke="#5badc0" stroke-width="1.5" stroke-linecap="round"/>
<path d="M45 30 C45 30 64 33 68 46 C71 56 68 66 60 68 C54 70 50 66 48 60 C46 55 45 48 45 42" fill="#c8e6f0" stroke="#5badc0" stroke-width="1.5" stroke-linecap="round"/>
<path d="M45 30 C45 30 26 33 22 46 C19 56 22 66 30 68 C36 70 40 66 42 60 C44 55 45 48 45 42" fill="#a8d4e4" stroke="none" opacity="0.5"/>
<path d="M45 30 C45 30 64 33 68 46 C71 56 68 66 60 68 C54 70 50 66 48 60 C46 55 45 48 45 42" fill="#a8d4e4" stroke="none" opacity="0.5"/>
<path d="M28 45 C30 42 34 40 36 42" stroke="#5badc0" stroke-width="1.2" fill="none" stroke-linecap="round"/>
<path d="M28 52 C30 48 36 47 38 50" stroke="#5badc0" stroke-width="1.2" fill="none" stroke-linecap="round"/>
<path d="M62 45 C60 42 56 40 54 42" stroke="#5badc0" stroke-width="1.2" fill="none" stroke-linecap="round"/>
<path d="M62 52 C60 48 54 47 52 50" stroke="#5badc0" stroke-width="1.2" fill="none" stroke-linecap="round"/>
</svg>"""

TOOTH_SVG = """<svg width="90" height="90" viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="45" cy="45" r="44" fill="#eaf5f8" stroke="#d0e8f0" stroke-width="1"/>
<path d="M30 22 C22 22 17 29 17 36 C17 44 20 52 23 60 C25 66 27 72 30 72 C33 72 33 66 36 60 C38 56 40 52 45 52 C50 52 52 56 54 60 C57 66 57 72 60 72 C63 72 65 66 67 60 C70 52 73 44 73 36 C73 29 68 22 60 22 C56 22 52 25 45 25 C38 25 34 22 30 22Z" fill="#c8e6f0" stroke="#5badc0" stroke-width="1.5"/>
<path d="M33 26 C27 28 24 33 24 38 C24 44 26 50 28 56" stroke="#5badc0" stroke-width="1.2" fill="none" stroke-linecap="round" opacity="0.7"/>
<path d="M45 25 C45 25 45 35 45 40" stroke="#5badc0" stroke-width="1.2" fill="none" stroke-linecap="round" opacity="0.7"/>
</svg>"""

BRAIN_SVG = """<svg width="90" height="90" viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="45" cy="45" r="44" fill="#eaf5f8" stroke="#d0e8f0" stroke-width="1"/>
<path d="M45 72 L45 58" stroke="#5badc0" stroke-width="2" stroke-linecap="round"/>
<path d="M45 58 C45 58 24 55 20 40 C17 27 26 18 36 21 C39 22 42 25 45 28" fill="#c8e6f0" stroke="#5badc0" stroke-width="1.5" stroke-linecap="round"/>
<path d="M45 58 C45 58 66 55 70 40 C73 27 64 18 54 21 C51 22 48 25 45 28" fill="#c8e6f0" stroke="#5badc0" stroke-width="1.5" stroke-linecap="round"/>
<path d="M20 40 C18 47 21 57 30 60 C36 62 41 60 45 58" fill="#a8d4e4" stroke="#5badc0" stroke-width="1.2" stroke-linecap="round"/>
<path d="M70 40 C72 47 69 57 60 60 C54 62 49 60 45 58" fill="#a8d4e4" stroke="#5badc0" stroke-width="1.2" stroke-linecap="round"/>
<path d="M24 34 C27 30 33 29 36 32" stroke="#5badc0" stroke-width="1.2" fill="none" stroke-linecap="round"/>
<path d="M66 34 C63 30 57 29 54 32" stroke="#5badc0" stroke-width="1.2" fill="none" stroke-linecap="round"/>
<path d="M22 48 C25 45 30 44 32 47" stroke="#5badc0" stroke-width="1.2" fill="none" stroke-linecap="round"/>
<path d="M68 48 C65 45 60 44 58 47" stroke="#5badc0" stroke-width="1.2" fill="none" stroke-linecap="round"/>
<ellipse cx="45" cy="74" rx="8" ry="4" fill="#a8d4e4" stroke="#5badc0" stroke-width="1"/>
</svg>"""

JOINT_SVG = """<svg width="90" height="90" viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="45" cy="45" r="44" fill="#eaf5f8" stroke="#d0e8f0" stroke-width="1"/>
<ellipse cx="45" cy="25" rx="12" ry="16" fill="#c8e6f0" stroke="#5badc0" stroke-width="1.5"/>
<ellipse cx="45" cy="65" rx="12" ry="16" fill="#c8e6f0" stroke="#5badc0" stroke-width="1.5"/>
<path d="M35 38 C35 38 30 42 30 45 C30 48 35 52 35 52" stroke="#5badc0" stroke-width="1.5" fill="none" stroke-linecap="round"/>
<path d="M55 38 C55 38 60 42 60 45 C60 48 55 52 55 52" stroke="#5badc0" stroke-width="1.5" fill="none" stroke-linecap="round"/>
<ellipse cx="45" cy="45" rx="10" ry="7" fill="#a8d4e4" stroke="#5badc0" stroke-width="1.2"/>
<line x1="33" y1="20" x2="33" y2="30" stroke="#5badc0" stroke-width="1.2" stroke-linecap="round"/>
<line x1="57" y1="20" x2="57" y2="30" stroke="#5badc0" stroke-width="1.2" stroke-linecap="round"/>
<line x1="33" y1="60" x2="33" y2="70" stroke="#5badc0" stroke-width="1.2" stroke-linecap="round"/>
<line x1="57" y1="60" x2="57" y2="70" stroke="#5badc0" stroke-width="1.2" stroke-linecap="round"/>
</svg>"""


def dept_icon_card(svg: str) -> rx.Component:
    return rx.box(
        rx.html(svg),
        background="white",
        border_radius="16px",
        width="120px",
        height="120px",
        display="flex",
        align_items="center",
        justify_content="center",
        border="1px solid #d8eaf0",
        box_shadow="0 2px 16px rgba(91,173,192,0.10)",
        _hover={
            "box_shadow": "0 8px 28px rgba(91,173,192,0.25)",
            "transform": "translateY(-4px)",
            "border_color": "#5badc0",
        },
        transition="all 0.25s ease",
        cursor="pointer",
    )


def departments() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    "Department Category",
                    font_size="24px",
                    font_weight="800",
                    color="#0d2333",
                    text_align="center",
                ),
                rx.text(
                    "Browse by department for tailored services and expert solutions",
                    font_size="14px",
                    color="#6b8a99",
                    text_align="center",
                ),
                spacing="2",
                align_items="center",
            ),
            rx.hstack(
                dept_icon_card(KIDNEY_SVG),
                dept_icon_card(HEART_SVG),
                dept_icon_card(LUNGS_SVG),
                dept_icon_card(TOOTH_SVG),
                dept_icon_card(BRAIN_SVG),
                dept_icon_card(JOINT_SVG),
                spacing="5",
                justify="center",
                flex_wrap="wrap",
                width="100%",
            ),
            spacing="8",
            align_items="center",
            width="100%",
        ),
        background="white",
        padding="48px 40px 56px",
        width="100%",
    )
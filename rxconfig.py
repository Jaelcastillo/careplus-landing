import reflex as rx

config = rx.Config(
    app_name="careplus_landing",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
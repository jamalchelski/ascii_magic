import ascii_magic
my_art = ascii_magic.from_image_file(
    'baby1.jpeg',
    columns=200,
    width_ratio=2,
    mode=ascii_magic.Modes.HTML
)
ascii_magic.to_html_file('index.html', my_art)
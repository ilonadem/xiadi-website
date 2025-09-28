import cairosvg

# 32×32 favicon
cairosvg.svg2png(url="assets/beetle.svg",
                 write_to="assets/beetle-32.png",
                 output_width=32, output_height=32,
                 background_color="transparent")

# 16×16
cairosvg.svg2png(url="assets/beetle.svg",
                 write_to="assets/beetle-16.png",
                 output_width=16, output_height=16,
                 background_color="transparent")

# 48×48
cairosvg.svg2png(url="assets/beetle.svg",
                 write_to="assets/beetle-48.png",
                 output_width=48, output_height=48,
                 background_color="transparent")

# 180×180 (Apple touch icon)
cairosvg.svg2png(url="assets/beetle.svg",
                 write_to="assets/beetle-apple-touch-icon.png",
                 output_width=180, output_height=180,
                 background_color="transparent")
# save images
def save_image(form_image):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = random_hex + f_ext
    image_path = os.path.join(app.root_path, 'static/profile_pics', image_fn)

    output_size = (300, 700)
    i = Image.open(form_image)
    i.thumbnail(output_size)
    i.save(image_path)

    return image_fn
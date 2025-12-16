import os
from docling_core.types.doc import PictureItem


def extract_images(doc, image_dir: str):
    os.makedirs(image_dir, exist_ok=True)

    image_paths = []
    counter = 1

    for element, _ in doc.iterate_items():
        if isinstance(element, PictureItem):
            img = element.get_image(doc)
            if img:
                path = os.path.join(image_dir, f"{counter}.png")
                img.save(path)
                image_paths.append(path)
                counter += 1

    return image_paths

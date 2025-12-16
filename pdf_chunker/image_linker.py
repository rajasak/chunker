def attach_images(sections, image_paths):
    image_index = 0
    enriched = []

    for title, text in sections:
        images = []

        while "<!-- image -->" in text and image_index < len(image_paths):
            img = image_paths[image_index]
            text = text.replace("<!-- image -->", img, 1)
            images.append(img)
            image_index += 1

        enriched.append({
            "title": title,
            "text": text.strip(),
            "image_path": images or None
        })

    return enriched

def generate_keywords(product_title):
    title = product_title.lower()
    return [
        f"best {title}",
        f"{title} review",
        f"buy {title} online",
        f"{title} price"
    ]

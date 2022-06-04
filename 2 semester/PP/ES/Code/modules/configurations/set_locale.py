import i18n


def setup() -> None:
    i18n.load_path.append("resources/locale/")
    i18n.set("locale", "ru")


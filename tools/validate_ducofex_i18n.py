from pathlib import Path

ROOT = Path("products/cnc/web/website_v1/Option1")
PAGES = [
    "index.html",
    "machines.html",
    "gen-1.html",
    "gen-2.html",
    "about-us.html",
    "contact-us.html",
    "partners.html",
    "printing-3d.html",
    "printable-models.html",
    "lokumai.html",
]


def main() -> int:
    errors = []
    for page in PAGES:
        html = (ROOT / page).read_text(encoding="utf-8")
        if 'data-lang-toggle="tr"' not in html:
            errors.append(f"{page}: missing TR toggle")
        if 'data-lang-toggle="en"' not in html:
            errors.append(f"{page}: missing EN toggle")
        if "js/ducofex-i18n.js" not in html:
            errors.append(f"{page}: missing i18n script include")
        if "https://www.youtube.com/@Ducofex" not in html:
            errors.append(f"{page}: missing youtube link")
    script_path = ROOT / "js/ducofex-i18n.js"
    if not script_path.exists():
        errors.append("missing js/ducofex-i18n.js")
    if errors:
        print("I18N VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("I18N VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

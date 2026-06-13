from pathlib import Path
import sys

ROOT = Path("products/cnc/web/website_v1/Option1")
PAGES = [
    "index.html",
    "machines.html",
    "gen-1.html",
    "gen-2.html",
    "about-us.html",
    "contact-us.html",
]
REQUIRED_NAV = [
    "Home",
    "Machines",
    "3D Printing",
    "Printable Models",
    "Partners",
    "About",
    "Contact",
    "LokumAI",
]
BANNED_WORDS = ["Library", "Books", "Authors", "Book Guide"]


def read_text(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def main() -> int:
    errors = []
    for page in PAGES:
        path = ROOT / page
        if not path.exists():
            errors.append(f"missing page: {page}")
            continue
        html = read_text(page)
        for nav_item in REQUIRED_NAV:
            if nav_item not in html:
                errors.append(f"{page}: missing nav item {nav_item}")
        if "images/brand/6x3.png" not in html:
            errors.append(f"{page}: missing brand logo path")
        for banned in BANNED_WORDS:
            if banned in html:
                errors.append(f"{page}: contains banned template word {banned}")
    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

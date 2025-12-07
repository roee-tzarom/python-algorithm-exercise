# Assignment 2.5 - Understanding Python Data Types
# Tasks: lists (log parsing), tuples (game stats), sets (unique visitors), dicts (products with tags)

from typing import List, Tuple

# משימה 2: מחשב סכום, ממוצע ןמקסימום של נזק מתוך רשימת פגיעות
def analyze_damage(hits: List[int]) -> Tuple[int, float, int]:

    total = sum(hits)

    if len(hits) <= 0:
        average = 0.0
        maximum = 0
    else:
        average = total / len(hits)
        maximum = max(hits)

    return total, average, maximum

# מדגים שימוש בפונקציה analyze_damage ופירוק של שלושת הערכים המוחזרים לשלושה משתנים
def demo_damage():

    hits = [10, 45, 90, 12, 70, 83]

    total, avg, mx = analyze_damage(hits)

    print(f"Total: {total}, Avg: {avg:.1f}, Max: {mx}")
# בג'אבה בשביל להחזיר שלושה ערכים הייתי כנראה יוצר מחלקת עזר עם שדות ובנאי רק לזה.
# בפייתון אני יכול להחזיר tuple ולעשות פירוק למשתנים מה שהרבה יותר נוח ופשוט בלי להסתבך

# משימה 3: שימוש ב-set כדי לעקוב אחרי מבקרים ולבדוק חיתוך עם משתמשי פרימיום (משתמשים מיוחדים\חשובים)
def demo_unique_visitors():

    visitors = set()

    visitors.add(101)
    visitors.add(202)
    visitors.add(303)
    visitors.add(101)
    visitors.add(404)
    visitors.add(202)

    print("All visitors set:", visitors)
    print("Number of unique visitors:", len(visitors))

    premium_users = {202, 555, 777}

    visited_and_premium = visitors & premium_users

    visited_not_premium = visitors - premium_users

    print("Visitors who are premium users:", visited_and_premium)
    print("Visitors who are not premium users:", visited_not_premium)

# משימה 4: מחזירה רשימה של כל המוצרים שיש להם tag מסוים בתוך סט התגיות שלהם
def get_products_with_tag(products, tag):

    result = []

    for product in products:

        if tag in product["tags"]:
            result.append(product)

    return result

# מדגים יצירה של רשימת מוצרים כמילונים וסינון המוצרים לפי תגית מסוימת
def demo_products():

    products = [
        {"name": "Tea", "price": 12.5, "tags": {"drink", "hot"}},
        {"name": "Apple", "price": 3.0, "tags": {"fruit", "food"}},
        {"name": "Coffee", "price": 15.0, "tags": {"drink", "hot"}},
    ]

    tag = "drink"

    matching_products = get_products_with_tag(products, tag)

    print(f'Products with tags "{tag}":')
    for p in matching_products:
        print(f"- {p['name']} (price: {p['price']})")

# משימה 1: פירוק שורת לוג לרשימה, שימוש בפיצול לפי רווחים, חיתוך חלקים מהרשימה,
# אינדקסים שליליים ובנייה של רשימה של זוגות (שם שדה, ערך)
def demo_log_parsing():

    log_line = "2025-11-16 17:42:10 WARNING User:moshe-m-ofer Action:PasswordAttempt Status:Failed Attempts:3 IP:192.168.1.77 Location:IL-TLV"

    parts = log_line.split()

    ip_field = parts[-2]
    location_field = parts[-1]

    middle_fields = parts[2:-2]

    parsed_fields = []

    for field in middle_fields:

        if ":" not in field:
            continue

        key, value = field.split(":",1)

        if key == "User":
            value = value.replace("-", " ")

        parsed_fields.append((key, value))


    ip_key, ip_value = ip_field.split(":", 1)
    loc_key, loc_value = location_field.split(":", 1)

    parsed_fields.append((ip_key, ip_value))
    parsed_fields.append((loc_key, loc_value))

    print("\nClean summary:")
    for key, value in parsed_fields:
        print(f"{key} = {value}")


if __name__ == "__main__":
    demo_log_parsing()
    demo_damage()
    demo_unique_visitors()
    demo_products()



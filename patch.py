import sys, re

try:
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Hide Framer Badge
    content = content.replace('id="__framer-badge-container"', 'id="__framer-badge-container" style="display:none!important;"')

    # Replace Artemis text logo with image new logo
    logo_img = '<img class="framer-hw9tkp" src="./logo.jpeg" style="height: 120px; width: auto; display: block;" alt="preksha logo" />'
    content = re.sub(r'<div class="framer-hw9tkp"[^>]*>.*?</div>', logo_img, content)

    # Replace words (respecting case loosely but user asked for "preksha")
    # Actually just replace the variations
    content = content.replace("Artemis", "Preksha")
    content = content.replace("artemis", "preksha")
    content = content.replace("ARTEMIS", "PREKSHA")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Success")
except Exception as e:
    print("Error:", e)

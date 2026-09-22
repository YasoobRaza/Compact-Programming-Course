# Task 5
dortmund_official_events = {
    "DEW21 Museum Night (DEW21 Museumsnacht)": "2026-09-19",
    "FATT - Festival of Arts, Tech & Taste (Kokerei Hansa)": "2026-09-19",
    "#diwodo: Digital Week 2026 (Digitalisierungsinitiative)": "2026-09-21",
    "Matisse: Symphony of Colors (Phoenix des Lumières)": "2026-09-21",
    "Djelem Djelem - The Roma Culture Festival": "2026-09-22",
    "Feierabend-Markt (Opernvorplatz - Theater Dortmund)": "2026-09-24",
    "Science Night: 2nd Dortmund Night of Science (Dortmunder U)": "2026-09-25",
    "Das Dortmunder Oktoberfest 2026 (Revierpark Wischlingen)": "2026-09-26",
    "World Press Photo 2026 Exhibition (Depot)": "2026-09-26",
    "Mondos Atelier - Painting with Earth Colors (Westfalenpark)": "2026-09-26",
    "Flo(h)rian Trödelmarkt / Flea Market (Westfalenpark)": "2026-09-27",
    "1st Philharmonic Concert: Sounds of the Soul (Konzerthaus)": "2026-09-29",
    "Kastanienfest / Chestnut Festival (Botanischer Garten Rombergpark)": "2026-10-04",
    "INDUSTRIAL / Seidenstraßen Exhibition (Kunsthalle Dortmund)": "2026-10-10",
    "Gartenlust - Autumn Market (Westfalenpark Dortmund)": "2026-10-11",
    "2nd Philharmonic Concert: Kopfkino (Konzerthaus Dortmund)": "2026-10-20",
    "Emerging Artists VI Exhibition (uzwei im Dortmunder U)": "2026-10-23",
    "SUPERHEROES Multimedia Exhibition (Deutsches Fußballmuseum)": "2026-09-19"
}

target_date = "2026-09-19"
print(f"Events running in Dortmund on {target_date}:")

for event, date in dortmund_official_events.items():
    if date == target_date:
        print(f"- {event}")

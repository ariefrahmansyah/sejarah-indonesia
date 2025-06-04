import json


def load_events(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def format_event(event):
    title = event.get("judul", "Peristiwa")
    start_date = event.get("tanggal_mulai")
    end_date = event.get("tanggal_selesai")

    if not start_date:
        return None  # Skip events without a start date

    if end_date:
        return f"{title} : {start_date}, {end_date}"
    else:
        return f"{title} : {start_date}, 1d"


def generate_mermaid_gantt(events):
    lines = [
        "```mermaid",
        "gantt",
        "    title Sejarah Indonesia",
        "    dateFormat  YYYY-MM-DD",
    ]

    for event in events:
        line = format_event(event)
        if line:
            lines.append(f"    {line}")

    lines.append("```")
    return "\n".join(lines)


def write_to_readme(content, readme_path="README.md"):
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# Sejarah Indonesia\n\n")
        f.write("Visualisasi garis waktu peristiwa sejarah Indonesia:\n\n")
        f.write(content)
        f.write("\n")


if __name__ == "__main__":
    events = load_events("data/events.json")
    mermaid_chart = generate_mermaid_gantt(events)
    write_to_readme(mermaid_chart)

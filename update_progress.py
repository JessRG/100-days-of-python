import os
import re

# Get the latest commit message from GitHub environment
commit_msg = os.getenv("COMMIT_MESSAGE", "").strip()

# Split the commit message into title and body lines
commit_lines = commit_msg.split('\n')
commit_title = commit_lines[0] if commit_lines else ""

# Extract the rest of the commit text to serve as your daily note description
commit_body_lines = [line.strip().lstrip('-* ').strip() for line in commit_lines[1:] if line.strip()]
commit_description = " ".join(commit_body_lines) if commit_body_lines else "Completed exercises and project tasks."

# Look for patterns like "Day 9" or "Day 24" in the commit title
match = re.search(r"Day\s*(\d+)", commit_title, re.IGNORECASE)

if match:
    current_day = int(match.group(1))

    # 1. Determine status strings based on the current day
    p1 = f"🟢 Days 1–15 Complete" if current_day > 15 else (
        f"🟡 Days 1-{current_day - 1} Complete / Day {current_day} In Progress" if current_day > 1 else f"🟡 Day 1 In Progress")
    p2 = f"🟢 Days 16–32 Complete" if current_day > 32 else (
        f"🟡 Day {current_day} In Progress" if current_day >= 16 else "⚪ Not Started")
    p3 = f"🟢 Days 33–58 Complete" if current_day > 58 else (
        f"🟡 Day {current_day} In Progress" if current_day >= 33 else "⚪ Not Started")
    p4 = f"🟢 Days 59–80 Complete" if current_day > 80 else (
        f"🟡 Day {current_day} In Progress" if current_day >= 59 else "⚪ Not Started")
    p5 = f"🟢 Days 81–100 Complete" if current_day == 100 else (
        f"🟡 Day {current_day} In Progress" if current_day >= 81 else "⚪ Not Started")

    # Rebuild the table markdown
    new_table = f"""<!-- START_PROGRESS_TRACKER -->

| Section | Target Days | Focus | Status |
| :--- | :---: | :--- | :---: |
| **Phase 1** | Days 1–15 | Python Fundamentals & Basics | {p1} |
| **Phase 2** | Days 16–32 | Intermediate Python & OOP | {p2} |
| **Phase 3** | Days 33–58 | Web Development, APIs, & Scraping | {p3} |
| **Phase 4** | Days 59–80 | Data Science & Advanced Automation | {p4} |
| **Phase 5** | Days 81–100 | Advanced Capstone Projects | {p5} |
<!-- END_PROGRESS_TRACKER -->"""

    # Read current README contents
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()

    # 2. Update the progress table
    table_pattern = r"<!-- START_PROGRESS_TRACKER -->.*?<!-- END_PROGRESS_TRACKER -->"
    content = re.sub(table_pattern, new_table, content, flags=re.DOTALL)

    # 3. Append the new log entry right below the anchor tag
    new_log_entry = f"<!-- LOG_ANCHOR -->\n*   **Day {current_day} Note:** {commit_description}"

    # Check if a log entry for this day already exists to avoid duplication
    day_log_marker = f"**Day {current_day} Note:**"
    if day_log_marker not in content:
        content = content.replace("<!-- LOG_ANCHOR -->", new_log_entry)
        print(f"Logged notes for Day {current_day}.")
    else:
        print(f"Log entry for Day {current_day} already exists. Skipping log duplication.")

    # Save all modifications back to README.md
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Successfully updated progress table to Day {current_day}!")
else:
    print("No day pattern found in the commit title. Skipping README generation.")

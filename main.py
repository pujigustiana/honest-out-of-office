import os
LINE = "I'm away until Monday, and honestly my inbox will greet me with 214 unread emails I am already dreading, so thank you for your patience while I pretend that number does not exist."
def main():
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
if __name__ == "__main__":
    main()

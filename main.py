"""Write the funniest sign for the haunted server room door to /output/entry.txt."""

import os

ENTRY = "NOTICE: The ghost in Rack 4 has root access now. Please stop asking it to fix the Wi-Fi."

# The gate requires 1 to 120 characters of UTF-8 text, not only whitespace.
assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, must be 1-120"
assert ENTRY.strip(), "entry must not be only whitespace"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY, end="")

if __name__ == "__main__":
    main()

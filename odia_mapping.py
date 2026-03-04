# Odia Legacy to Unicode Character Mapping

# This mapping file contains the character mapping from the Odia legacy font to Unicode.

mapping = {
    '\u0B05': '୅',  # ୅ (U+0B05)
    '\u0B06': '୆',  # ୆ (U+0B06)
    '\u0B07': 'େ',  # େ (U+0B07)
    '\u0B08': 'ୈ',  # ୈ (U+0B08)
    '\u0B10': '୐',  # ୐ (U+0B10)
    '\u0B13': '୓',  # ୓ (U+0B13)
    '\u0B14': '୔',  # ୔ (U+0B14)
    '\u0B15': '୕',  # ୕ (U+0B15)
    '\u0B16': 'ୖ',  # ୖ (U+0B16)
    '\u0B17': 'ୗ',  # ୗ (U+0B17)
    # Add more mappings as necessary
}

if __name__ == '__main__':
    # Example usage
    for legacy_char, unicode_char in mapping.items():
        print(f"Legacy: {legacy_char} -> Unicode: {unicode_char}")
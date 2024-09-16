import re


def capitalize_segment(segment):
    """Capitalize the first letter of a segment."""
    if segment:
        return segment[0].upper() + segment[1:]
    return segment


def capitalize_header(header):
    """
    Capitalizes each segment of the header separated by hyphens or underscores.
    Preserves suffixes after '~' if present.
    """
    # Split header and suffix if '~' is present
    if '~' in header:
        main_header, suffix = header.split('~', 1)
        suffix = '~' + suffix  # Reattach the '~' for later
    else:
        main_header, suffix = header, ''

    # Identify separators: hyphen or underscore
    # We'll use regex to split while keeping the separators
    tokens = re.split(r'([-_])', main_header)

    # Capitalize segments separated by hyphens or underscores
    capitalized_tokens = [capitalize_segment(token) if i % 2 == 0 else token for i, token in enumerate(tokens)]

    # Reconstruct the main header
    capitalized_main = ''.join(capitalized_tokens)

    # Combine with suffix
    return capitalized_main + suffix


def transform_wordlist(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            header = line.strip()
            if header:
                transformed = capitalize_header(header)
                outfile.write(transformed + '\n')


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Transform header wordlist to proper casing.')
    parser.add_argument('input', help='Path to the input wordlist file (lowercase headers).')
    parser.add_argument('output', help='Path to the output wordlist file (properly cased headers).')

    args = parser.parse_args()

    transform_wordlist(args.input, args.output)
    print(f"Transformation complete. Output saved to {args.output}")

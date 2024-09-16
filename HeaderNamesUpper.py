import re

def capitalize_header(header):
    """
    Capitalizes each segment of the header separated by hyphens.
    Preserves suffixes after '~' if present.
    """
    if '~' in header:
        main_header, suffix = header.split('~', 1)
    else:
        main_header, suffix = header, ''

    # Capitalize each part separated by '-'
    capitalized_main = '-'.join([word.capitalize() for word in main_header.split('-')])

    # Reattach the suffix if it exists
    return f"{capitalized_main}~{suffix}" if suffix else capitalized_main

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

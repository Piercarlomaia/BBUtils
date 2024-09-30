# Let's modify the code to write the list into a txt file

import ipaddress

# Function to generate IP encodings
def generate_ip_encodings(ip_range):
    encodings = []

    # Loop over each IP in the network range
    for ip in ip_range:
        ip_str = str(ip)
        decimal = int(ip)
        hexadecimal = hex(decimal)
        octal = oct(decimal)
        ipv6 = f"::ffff:{ip}"

        # Append all values to a flat list
        encodings.extend([
            ip_str,  # IP
            decimal,  # Decimal
            hexadecimal,  # Hexadecimal
            octal,  # Octal
            ipv6,  # IPv6
        ])

    return encodings

# Define IP ranges
ip_ranges = [
    ipaddress.IPv4Network('169.254.169.254/32'),  # Cloud metadata services (AWS, GCP, Azure)
    ipaddress.IPv4Network('127.0.0.0/16'),  # Localhost range
    ipaddress.IPv4Network('10.0.0.0/16'),  # Private network
    ipaddress.IPv4Network('10.1.0.0/24'),  # Additional private network
    ipaddress.IPv4Network('172.16.0.0/24'),  # Private network
    ipaddress.IPv4Network('172.16.1.0/24'),  # Expand private network
    ipaddress.IPv4Network('192.168.0.0/16'),  # Private network
    ipaddress.IPv4Network('192.168.1.0/24'),  # Home network
    ipaddress.IPv4Network('192.168.100.0/24'),  # Common home network
    ipaddress.IPv4Network('192.0.0.0/24'),  # Reserved range
    ipaddress.IPv4Network('169.254.0.0/16'),  # Link-local address block
    ipaddress.IPv4Network('8.8.8.0/24'),      # Google DNS (already /24)
    ipaddress.IPv4Network('1.1.1.0/24'),      # Cloudflare DNS (already /24)
]

# Generate encodings for each range
all_encodings = [
    'localhost',           # Standard localhost
    'localhosT',           # Capitalization variant
    '0',                   # Short wildcard
    '::1',                 # IPv6 loopback
    'localtest.me',        # Test domain
    '0.0.0.0',             # Wildcard IP
    '255.255.255.255',     # Broadcast address
    '127.1',               # Shortened localhost
]
for ip_range in ip_ranges:
    all_encodings.extend(generate_ip_encodings(ip_range))

# Write the list to a txt file
file_path = '../wordlists/ip_encodings_wordlist.txt'
with open(file_path, 'w') as f:
    for item in all_encodings:
        f.write(f"{item}\n")



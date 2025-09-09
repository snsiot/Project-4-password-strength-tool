import argparse
from zxcvbn import zxcvbn
from datetime import datetime

LEET_DICT = {
    'a': ['4', '@'],
    'e': ['3'],
    'i': ['1', '!'],
    'o': ['0'],
    's': ['$', '5'],
    't': ['7']
}

COMMON_YEARS = [str(year) for year in range(1990, datetime.now().year + 1)]

def analyze_password(password):
    result = zxcvbn(password)
    print(f"\n[+] Password Strength: {result['score']} / 4")
    print(f"    Estimated crack time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
    print(f"    Feedback: {result['feedback']}")
    return result['score']

def leetspeak_variants(word):
    variants = [word]
    for i, char in enumerate(word):
        if char.lower() in LEET_DICT:
            for replacement in LEET_DICT[char.lower()]:
                variants.append(word[:i] + replacement + word[i+1:])
    return list(set(variants))

def generate_wordlist(words, output_file="custom_wordlist.txt"):
    print(f"\n[+] Generating wordlist based on inputs: {words}")
    all_words = set()
    for word in words:
        base = word.lower()
        variants = leetspeak_variants(base)
        all_words.update(variants)
        for year in COMMON_YEARS[-10:]:  # last 10 years
            all_words.update({v + year for v in variants})
            all_words.update({year + v for v in variants})
    with open(output_file, "w") as f:
        for word in sorted(all_words):
            f.write(word + "\n")
    print(f"[✓] Wordlist saved to {output_file} with {len(all_words)} entries.")

def main():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer & Custom Wordlist Generator")
    parser.add_argument("-p", "--password", help="Password to analyze", required=True)
    parser.add_argument("-i", "--inputs", nargs="*", help="Custom inputs (name, pet, date, etc.)", required=False)
    args = parser.parse_args()
    analyze_password(args.password)
    if args.inputs:
        generate_wordlist(args.inputs)
    else:
        print("[!] No custom inputs provided. Wordlist not generated.")

if __name__ == "__main__":
    main()

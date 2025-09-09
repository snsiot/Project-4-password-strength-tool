# 🔐 Password Strength Analyzer + Wordlist Generator

## 🧠 Project Objective

This tool analyzes password strength using `zxcvbn` and generates **custom wordlists** based on user data like names, pets, or dates. Ideal for **cybersecurity education** and password auditing.

---

## ⚙️ Features

- 🔍 Analyze password strength (entropy, time to crack)
- 📝 Generate smart wordlists with:
  - Leetspeak variants
  - Years (e.g., 2023, 2024)
- 📁 Export wordlist as `.txt` for use with cracking tools
- 🧑‍💻 CLI interface using `argparse`

---

## 🚀 How to Use

### 1. Install Requirements

```bash
pip install -r requirements.txt

Run the Tool
python password_tool.py -p "MyPassword123" -i Alice 2024 fluffy

Output

Password analysis report (strength, feedback)
Wordlist saved as custom_wordlist.txt

🛡️ Ethical Disclaimer

⚠️ This tool is intended only for ethical and educational use.
❌ Do NOT use this on systems you do not own or have explicit permission to test.

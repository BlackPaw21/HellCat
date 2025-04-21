## Hellcat Launcher

![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg) ![Hashcat](https://img.shields.io/badge/hashcat-6.2.6+-orange.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg)

An **interactive**, colorized, Windows‑friendly Python wrapper around Hashcat, designed to simplify WPA‑PMKID/EAPOL cracking on Windows 11. Hellcat lets you:

- 🔒 Atomatically uses `-m 22000` (WPA unified PMKID/EAPOL)  
- 🎯 Choose between **Brute‑force (mask)** or **Dictionary/Hybrid** attacks  
- 🌡️ Set a custom **temperature abort** threshold  
- ⏱️ Auto‑refresh status every 5 seconds (configurable)   
- 🔧 Launch with a single `hellcat.bat` click
- 📃 Easy checkpoint restore

---

## 💾 Installation

### **#1 Clone the repository**  
   ```bash
   git clone https://github.com/BlackPaw21/hellcat.git
   cd hellcat
   ```

### **#2 Download HashCat**  
   https://hashcat.net/files/hashcat-6.2.6.7

### **#3 extract hashcat**  
   ```bash
   Extract "hashcat-6.2.6" into "HellCat"
   ```

### **#4 Double‑click** `hellcat.bat` to run (installs dependencies automatically).

---

## ⚙️ Usage

### Interactive Launch  
Double‑click **hellcat.bat** or run:
```bat
hellcat.bat
```
You’ll be guided through:
1. **Hash file path** (`.hc22000`)  
2. **Device IDs** (from `hashcat.exe -I`)  
3. **Use CPU alongside GPU?**  
4. **Attack mode** (Brute vs Dict)  
5. **Temperature abort** & **Status timer**  
6. **Mask/wordlist** settings  

- **Modes**  
  - `brute` (mask attack)  
  - `dict` (dictionary or hybrid)

- **Options**  
  - `--mask` – mask template for brute/hybrid  
  - `--inc-min`, `--inc-max` – incremental lengths  
  - `--wordlist` – path to your wordlist for dict mode  
  - `--temp-abort` – temperature threshold (°C)  
  - `--status-timer` – refresh interval (s)

---


## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

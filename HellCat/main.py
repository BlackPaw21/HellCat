#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

try:
    from colorama import init, Fore, Style
except ImportError:
    print("Please install dependencies: pip install colorama")
    sys.exit(1)

# Initialize colorama for colored CLI
init(autoreset=True)

def prompt_menu(title, options):
    print(Fore.CYAN + title)
    for idx, opt in enumerate(options, 1):
        print(Fore.GREEN + f"  {idx}. {opt}")
    while True:
        choice = input(Fore.YELLOW + "Select an option (number): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        print(Fore.RED + "Invalid selection. Try again.")


def prompt_input(prompt, default=None):
    if default is not None:
        prompt = f"{prompt} [{default}]: "
    else:
        prompt = f"{prompt}: "
    val = input(Fore.YELLOW + prompt)
    return val.strip() or default


def build_command(config):
    # Locate hashcat executable
    hc_dir = Path(__file__).parent / 'hashcat-6.2.6'
    hc_exe = hc_dir / 'hashcat.exe'

    cmd = [
        str(hc_exe),
        '--hash-type=22000',
        '--status',
        f"--status-timer={config['status_timer']}",
        f"--hwmon-temp-abort={config['temp_abort']}",
        '--optimized-kernel-enable',
        '--workload-profile=3'
    ]

    # Device selection: CPU + GPU or GPU only
    if config['use_cpu']:
        cmd += ['-D', '1,2', '-d', f"{config['cpu_id']},{config['gpu_id']}"]
    else:
        cmd += ['-D', '2', '-d', config['gpu_id']]

    # Attack mode: brute (mask) or dict (dictionary/hybrid)
    if config['mode'] == 'brute':
        cmd += [
            '--attack-mode=3',
            '--increment',
            f"--increment-min={config['inc_min']}",
            f"--increment-max={config['inc_max']}",
            '-1', '?l?u',
            config['hashfile'],
            config['mask']
        ]
    else:
        if config['mask']:
            # Hybrid: dictionary + mask
            cmd += ['--attack-mode=6', config['hashfile'], config['wordlist'], config['mask']]
        else:
            # Pure dictionary
            cmd += ['--attack-mode=0', config['hashfile'], config['wordlist']]

    return cmd


def main():
    print(Style.BRIGHT + Fore.MAGENTA + "\n=== Hellcat Launcher ===\n")

    # Prompt for hash file
    hashfile = prompt_input("Enter path to .hc22000 hash file")

    # Device configuration
    print(Fore.CYAN + "\n-- Device Configuration --")
    cpu_id = prompt_input("Enter CPU device ID (from 'hashcat.exe -I')", "1")
    gpu_id = prompt_input("Enter GPU device ID (from 'hashcat.exe -I')", "2")
    use_cpu = (prompt_menu("Use CPU alongside GPU?", ["No (GPU only)", "Yes (GPU + CPU)"]) == 2)

    # Attack mode selection
    print(Fore.CYAN + "\n-- Attack Mode --")
    mode = 'brute' if prompt_menu("Select attack mode:", ["Brute‑force (mask)", "Dictionary (wordlist/hybrid)"]) == 1 else 'dict'

    # Common settings
    temp_abort = prompt_input("Set temp abort (°C)", "85")
    status_timer = prompt_input("Status timer (seconds)", "5")

    config = {
        'hashfile': hashfile,
        'cpu_id': cpu_id,
        'gpu_id': gpu_id,
        'use_cpu': use_cpu,
        'mode': mode,
        'temp_abort': temp_abort,
        'status_timer': status_timer
    }

    # Mode‑specific settings
    if mode == 'brute':
        print(Fore.CYAN + "\n-- Brute‑Force Settings --")
        config['inc_min'] = prompt_input("Increment‑min length", "10")
        config['inc_max'] = prompt_input("Increment‑max length", "12")
        config['mask'] = prompt_input("Mask template (e.g. '?d?d?d?d?d?d?d?d?d?d?1?1')")
        config['wordlist'] = None
    else:
        print(Fore.CYAN + "\n-- Dictionary Settings --")
        config['wordlist'] = prompt_input("Enter path to wordlist file")
        if prompt_menu("Use hybrid mask?", ["No", "Yes"]) == 2:
            config['mask'] = prompt_input("Enter mask template (e.g. '?d?d?d?d')")
        else:
            config['mask'] = None
        config['inc_min'] = None
        config['inc_max'] = None

    # Build command and define working directory
    cmd = build_command(config)
    hc_dir = Path(__file__).parent / 'hashcat-6.2.6'

    print(Fore.BLUE + "\nRunning command:\n" + Fore.WHITE + ' '.join(cmd) + "\n")

    # Execute Hashcat within its directory so OpenCL/ kernels load correctly
    result = subprocess.run(cmd, shell=False, cwd=str(hc_dir))
    sys.exit(result.returncode)

if __name__ == '__main__':
    main()

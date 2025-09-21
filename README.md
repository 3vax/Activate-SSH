# Activate-SSH

A Python tool for automatically configuring SSH access on a Cisco switch or router via serial connection.

## Overview

This tool makes it easy to enable SSH on a fresh Cisco device by automating the configuration process.
It connects to the device via serial port, prompts the user for necessary variables, and applies the appropriate configuration based on device type.

## Features

- **Device Type Support**: Separate configurations for Cisco switches and routers
- **Interactive Setup**: User-friendly prompts with sensible defaults
- **Serial Port Management**: Includes a tool for the user to choose the correct serial port
- **Template-Based Configuration**: Easy to modify and add new command templates
- **Progress feedback**: Shows a progress bar during key generation and other long-running operations

## Quick Start

### Prerequisites

- Python 3.7+
- Cisco device connected via serial cable
- Free COM port for communication

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Activate-SSH
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. Run the main script:
```bash
python main.py
```

2. Choose from the menu:
   - **Option 1**: List available COM ports
   - **Option 2**: Configure a Cisco switch
   - **Option 3**: Configure a Cisco router

3. Follow the interactive prompts to provide the necessary information

## Project Structure
```
Activate-SSH/
├── main.py                          # Main entry point with menu system
├── scripts/
│   ├── cisco_settings.py            # Core configuration logic
│   ├── config.py                    # User input prompts and defaults
│   └── hard_coded_sw_settings.py    # Alternative hardcoded settings for testing
├── commands/
│   ├── cisco_switch_mgmt_commands.txt    # Switch configuration template
│   └── cisco_router_mgmt_commands.txt    # Router configuration template
├── tools/
│   └── list_ports.py                # Serial port enumeration utility
└── README.md                        # This file
```

## Disclaimer

This tool is designed for network administration and should only be used on devices you own or have explicit permission to configure. Always backup device configurations before making changes.
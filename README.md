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
git clone https://github.com/3vax/Activate-SSH
cd Activate-SSH
```
2. Create and activate a virtual environment:
```
python3 -m venv "your venv name"
source "your venv name"/bin/activate
```

3. Install dependencies:
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
├── main.py                          # Main entry point with menu 
├── scripts/
│   ├── cisco_settings.py            # Core configuration logic
│   ├── config.py                    # User input prompts and 
│   └── hard_coded_sw_settings.py    #  
├── commands/
│   ├── cisco_switch_mgmt_commands.txt    # Switch configuration 
│   └── cisco_router_mgmt_commands.txt    # Router configuration 
├── tools/
│   └── list_ports.py                # Serial port enumeration 
└── README.md                        # This file
```

## Disclaimer

This tool is designed for network administration and should only be used on devices you own or have explicit permission to configure. Always backup device configurations before making changes.

---------------------------------------------------------------------------------------------------------------------------------------------

# Aktiver SSH

## Oversikt

Dette scriptet skal gjøre det enklere å sette opp SSH på en ny Cisco switch eller ruter ved at den automatiserer konfigurasjons prosessen.
Den kobles til enheten via serial porten, den promter brukeren for de nødvendige variablene, og bruker riktig konfigurasjon basert på
enhets typen.

## Funksjoner
- **Enhets Type Support**: Separate konfigurasjoner for Cisco switcher og rutere
- **Interaktivt Oppsett**: Brukervennlige promts med fornuftige defaults
- **Serial Port Håndtering**: Inkluderer et verktøy for at brukeren skal kunne velge riktig serial port
- **Mal-Basert Konfigurasjon**: Enkelt og modifisere og legge til nye kommando maler
- **Fremdriftsindikator**: Viser en fremdriftsindikator under nøkkel generasjonen
- **A

## Quick Start

### Forutsetninger

- Python 3.7+
- Cisco enhet tilkoblet via serial kabel
- Tilgjengelig COM port for kommunikasjon
- WSL eller liknende med ansible installert

### Installasjon

1. Klon repositoryet fra github:
```bash
git clone https://github.com/3vax/Activate-SSH
cd Activate-SSH
```

2. Lag og aktiver det virtuelle miljøet:
```bash
python3 -m venv "your venv name"
source "your venv name"/bin/activate
```

3. Installer avhengigheter:
```bash
pip install -r requirements.txt
```

### Bruk
1. Skru på Cisco enheten

2. Koble til Cisco enheten med en seriel kabel

3. Gå inn på enheten med et program som Putty for å sikre at enheten ikke har noen konfigurasjon, samt at den har startet ordentlig og at du kansellerer automatisk oppsett. Du bør og kontrollere hvilken type interface enheten har. Da det kan være en variasjon på om det er
f.eks f0/1 ,g1/0/1 eller g0/0.
Når du skal gå ut av enheten sørg for at den viser: Switch> eller Router>
Enheten er nå klar for at scriptet skal sende kommandoer.
VIKTIG
Dette må bli bli gjort på hver enhet

3. Kjør hovedscripetet:
```bash
python3 main.py
```

4. Svar på promtene som du blir spurt om.

Om du skal bruke ansible playbøkene for videre oppsett gjør du følgende:

5. Koble til seriell kabelen til en switch du vil skal fungere som MLS

6. Kjør hovedscriptet:
```bash
python3 main.py
```
7. Velg korrekt COM port.

8. Set hostname til MLS

9. Set passord til cisco

10. Velg default VLAN, dette gjør du vet å trykke enter

11. Set IP-adressen til 10.99.0.5

12. Set subnet masken til default, dette gjør du ved å trykke enter.

13. Set MGMT interface porten til g1/0/1

14. Set access porten til g1/0/10

14. Set default gateway til 10.99.0.1

15. Set domene navnet til fsi.local

16. Set brukernavn cisco

17. Set passord cisco

18. Set SSH versjonen til default, dette gjør du vet å trykke enter

19. Sett nøkkel størrelsen til default, dette gjør du vet å trykke enter

20. Koble datamaskinen til access porten med en ethernetkabel

21. Legg til ansible playbøkene der du har dine ansible playbooks.

22. Enten legg til hostene i hosts filen inn i din hosts fil, eller kopier hosts filen til der du har ansible

23. Kjør playboken config_mls.yaml
```bash
ansible-playbook playbooks/config_mls.yaml
```

24. Koble fra og koble deg til det som skal bli ruter 1 med seriell kabelen. Koble og en ethernet kabel fra MLS sin port g1/0/1 til ruter 1 sin port g0/0

25. Velg korrekt COM port

26. Set hostname til R1

27. Set MGMT interface til g0/0

28. Set sub-interface til g0/0.99

29. Set IP-adressen itl 10.99.0.2

30. Set subnet mask til default, dette gjør du ved å trykke enter

31. Set VLAN id til default

32. Set domain name til fsi.local

33. Set brukernavn til cisco

34. Set passord til cisco

35. Set SSH versjon til default, dette gjør du ved å trykke enter

36. Set nøkkel størrelse til default, dette gjør du ved å trykke enter

37. Du skal nå kunne bruke SSH for å entre enheten

38. Kjør playboken config_r1.yaml
```bash
ansible-playbook playbooks/config_r1.yaml
```

39. Koble fra og koble deg til det som skal bli ruter 2 med seriell kabelen. Koble og en ethernetkabel fra MLS sin port g1/0/2 til ruter 2 sin port g0/0

40. Velg korrekt COM port

41. Set hostname til R2

42. Sett passordet til cisco

43. Set MGMT interface til g0/0

44. Set sub-interface port til g0/0.99

45. Set IP adressen til sub interface porten til 10.99.0.3

45. Set subnet masken til default

46. Set VLAN id for subnet interfacen til default

47. Set domene navnet til fsi.local

48. Set brukernavn til cisco

49. Set passord til cisco

50. Set SSH versjonen til default

51. Set nøkkel størrelsen til default

52. Du skal nå kunne bruke SSH for å entre enheten

53. Kjør playboken config_r2.yaml
```bash
ansible-playbook playbooks/config_r2.yaml
```
54. Koble fra og koble deg til det som skal bli switch 1 med seriell kabelen. Koble en ethernetkabel mellom switch 1 g1/0/1 til ruter 1 og switch 1 g1/0/2 til ruter 2.

55. Set hostname til S1

56. Set passordet på enheten til cisco

57. Set VLAN id til default

58. Set IP-adressen til 10.99.1.5

59. Set subnet masken til default

60. Set MGMT interface porten til g1/0/1

61. Set access interface porten til g1/0/10

62. Set default gateway til 10.99.1.1

63. Set domene navnet til fsi.local

64. Set brukernavnet til cisco

65. Set passordet til cisco

66. Set SSH versjon til default

67. Set nøkkel størrelse til default.

68. Du skal nå kunne bruke SSH for å entre enheten

69. Kjør playboken config_s1.yaml
```bash
ansible-playbook playbooks/config_s1.yaml
```
70. Koble fra og koble deg til det som skal bli switch 1 med seriell kabelen. Koble en ethernetkabel mellom switch 1 g1/0/3 til det som skal bli switch 2 på port g1/0/1

71. Set hostname til S2

72. Set passord til cisco

73. Set VLAN id til default

74. Set set IP-adressen til 10.99.1.6

75. Set subnet masken til default

76. Set MGMT interface port til g1/0/1

77. Set access interface porten til g1/0/10

78. Set default gateway til 10.99.1.1

79. Set domnene navn til fsi.local

80. Set brukernavn til cisco

81. Set passord til cisco

82. Set SSH versjon til default

83. Set nøkkel størrelsen til default

83. Du skal nå kunne koble det til enheten med SSH

84. Kjør playboken config_s2.yaml
```bash
ansible-playbook playbooks/config_s2.yaml
```
85. Koble fra og koble deg til det som skal bli switch 1 med seriell kabelen. Koble en ethernetkabel mellom switch 1 g1/0/23 til switch 2 sin port g/1/0/23, gjør det samme mellom portene g1/0/24. Koble fra ethernetkabel mellom switch 1 g1/0/3 til switch 2 sin port g1/0/1. Koble en ethernetkabel fra g1/0/2 på switch 2 til g1/0/1 på det som skal bli access layer switch 1.

86. Velg riktig COM port

87. Set hostname til ALS1

88. Set passordet til cisco

89. Set VLAN id til default

90. Set ip adresse til 10.99.1.7

91. Set subnet mask til default

92. Set MGMT interface porten til g1/0/1

93. Set access interface porten til g1/0/2

94. Set default gateway til 10.99.1.1

95. Set domene navnet til fsi.local

96. Set brukernavnet til cisco

97. Set passordet til cisco

97. Set SSH versjonen til default

98. Set nøkkel størrelsen til default

99. Du skal nå kunne koble deg til enheten med SSH

100. Kjør playboken config_als1.yaml
```bash
ansible-playbook playbooks/config_als1.yaml
```

101. Du skal nå kunne koble til en datamaskin på port g1/0/12 for VLAN10/STUD1 eller g1/0/14 for VLAN20/STUD2

Om dette ikke skulle fungere, så legges det ved en enhetsliste. Denne inneholder all informasjon som skulle være nødvendig for å fylle inn korrekte porter og IP adresser.

### Prosjektets struktur
```
Activate-SSH/
├── ansible
│   ├── config_als1.yaml # Ansible playbook for access layer switch 1
│   ├── config_mls.yaml # Ansible playbook for multi layer switchen
│   ├── config_r1.yaml # Ansible playbook for ruter 1
│   ├── config_r2.yaml # Ansible playbook for ruter 2
│   ├── config_s1.yaml # Ansible playbook for switch 1
│   ├── config_s2.yaml # Ansible playbook for switch 2
│   ├── r1_module_test.yaml # Bare forsøk på bruk av moduler
│   ├── hosts # En liste over hosts i forbindelse med ansible filene
├── main.py                          # Main entry point with menu 
├── scripts/
│   ├── cisco_settings.py            # Kjernen til konfigurasjonen av enhetene
│   ├── config.py                    # Prompts til brukeren og brukerens input
│   └── hard_coded_sw_settings.py    # En tidlig versjon av scriptet
├── commands/
│   ├── cisco_switch_mgmt_commands.txt    # Switch konfigurasjons kommandoer
│   └── cisco_router_mgmt_commands.txt    # Ruter konfigurasjons kommandoer
├── tools/
│   └── list_ports.py                # Serial port enumeration 
└── README.md                        # Denne filen

## Ansvarsfraskrivelse

Dette verktøyet er utviklet for nettverksadministrasjon og skal kun brukes på enheter du eier eller har eksplisitt tillatelse til å konfigurere. Ta alltid sikkerhetskopi av enhetskonfigurasjoner før du gjør endringer.
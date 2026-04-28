<p align="center">
  <img src="https://www.seven.io/wp-content/uploads/Logo.svg" width="250" alt="seven logo" />
</p>

<h1 align="center">seven SMS for OctoPrint</h1>

<p align="center">
  Send an SMS via the seven gateway when an <a href="https://octoprint.org/">OctoPrint</a> print job finishes.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-teal.svg" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/OctoPrint-1.5%2B-orange" alt="OctoPrint 1.5+" />
  <img src="https://img.shields.io/badge/Python-3.7%2B-yellow" alt="Python 3.7+" />
</p>

---

## Features

- **Job-Completion SMS** - Get notified when a print finishes (success or fail)
- **Templated Body** - Customise the SMS text with placeholders for printer name and status
- **Flash SMS Support** - Optional flash messages that bypass the recipient's inbox

Forked from [`OctoPrint-EmailNotifier`](https://github.com/anoved/OctoPrint-EmailNotifier).

## Prerequisites

- [OctoPrint](https://octoprint.org/) 1.5 or newer
- A [seven account](https://www.seven.io/) with API key ([How to get your API key](https://help.seven.io/en/developer/where-do-i-find-my-api-key))

## Installation

### Plugin Manager (recommended)

Open the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html) and install from URL:

```
https://github.com/seven-io/octoprint/archive/master.zip
```

### Manual

Download the [latest release](https://github.com/seven-io/octoprint/archive/master.zip), unpack it into your OctoPrint plugins directory and restart OctoPrint.

## Configuration

After install, go to **Settings > Plugins > seven** and configure:

| Field | Description |
|-------|-------------|
| `api_key` | seven API key (required) |
| `enabled` | Master switch for the plugin |
| `flash` | Send as [flash SMS](https://help.seven.io/en/flash-sms) |
| `message_template` | SMS body. Supports placeholders for printer name / status |
| `printer_name` | Identifier used inside `message_template` |
| `recipients` | Comma-separated list of recipient phone numbers |
| `sender` | Sender ID. Up to 11 alphanumeric or 16 numeric characters |

## Support

Need help? Feel free to [contact us](https://www.seven.io/en/company/contact/) or [open an issue](https://github.com/seven-io/octoprint/issues).

## License

[MIT](LICENSE)

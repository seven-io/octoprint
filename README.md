![](https://www.seven.io/wp-content/uploads/Logo.svg "seven Logo")

# OctoPrint-Seven

Plugin to send SMS after OctoPrint has completed a job. Based on [OctoPrint-EmailNotifier](https://github.com/anoved/OctoPrint-EmailNotifier).

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually from [GitHub](https://github.com/seven-io/octoprint/archive/master.zip).

After installation, go to `Settings -> Plugins -> seven` and fill out the form.

## Configuration

`api_key` seven API key required for sending

`enabled` whether the plugin is activated or not

`flash` whether SMS gets sent as flash or not

`message_template` the SMS text to send

`printer_name` an identifier for naming the printer

`recipients` a comma separated list of SMS recipient(s)

`sender` the value to use as the SMS sender

## Support

Need help? Feel free to [contact us](https://www.seven.io/en/company/contact/).

[![MIT](https://img.shields.io/badge/License-MIT-teal.svg)](LICENSE)

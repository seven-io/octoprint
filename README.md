# OctoPrint-Sms77

Plugin to send SMS after OctoPrint has completed a job. Based on [OctoPrint-EmailNotifier](https://github.com/anoved/OctoPrint-EmailNotifier).

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually from [GitHub](https://github.com/sms77io/OctoPrint-Sms77/archive/master.zip).

After installation, go to `Settings -> Plugins -> sms77` and fill out the form.

## Configuration

`api_key` sms77 API key required for sending

`enabled` whether the plugin is activated or not

`flash` whether SMS gets sent as flash or not

`message_template` the SMS text to send

`printer_name` an identifier for naming the printer

`recipients` a comma separated list of SMS recipient(s)

`sender` the value to use as the SMS sender


## License

Licensed under the terms of the [AGPLv3](http://opensource.org/licenses/AGPL-3.0).

# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from requests import post
import octoprint.plugin


class Sms77Plugin(
    octoprint.plugin.StartupPlugin,
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.EventHandlerPlugin
):
    def get_template_configs(self):
        return [
            dict(type="settings", name="sms77", custom_bindings=False)
        ]

    def get_settings_defaults(self):
        return dict(
            api_key="",
            enabled=False,
            flash=False,
            message_template="Printer {printer_name}: {filename} done printing after {elapsed_time}.",
            printer_name="",
            recipients="",
            sender="",
        )

    def on_event(self, event, payload):
        if event != "PrintDone" or not self._settings.get(['enabled']):
            return

        return self._send_txt(payload)

    def _send_txt(self, payload):
        import datetime
        import octoprint.util

        elapsed_time = octoprint.util.get_formatted_timedelta(
            datetime.timedelta(seconds=payload["time"]))
        tags = {
            'elapsed_time': elapsed_time,
            'filename': payload["name"],
            'printer_name': self._settings.get(["printer_name"])
        }
        sms_params = {
            'flash': 1 if self._settings.get(['flash']) else 0,
            'from': self._settings.get(['sender']),
            'text': self._settings.get(["message_template"]).format(**tags)
        }
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'SentWith': 'OctoPrint',
            'X-Api-Key': self._settings.get(['api_key'])
        }

        for to in self._settings.get(['recipients']).split(','):
            try:
                sms_params['to'] = to
                post('https://gateway.sms77.io/api/sms', headers=headers, json=sms_params)
            except Exception as e:
                self._logger.error("sms77 SMS error: %s" % (str(e)))
                continue
            else:
                self._logger.info("sms77 SMS sent to %s" % to)

        return True


__plugin_description__ = "Send SMS via sms77 within OctoPrint"
__plugin_implementation__ = Sms77Plugin()
__plugin_name__ = "sms77"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_version__ = "1.0.0"

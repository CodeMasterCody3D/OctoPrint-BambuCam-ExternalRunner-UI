import octoprint.plugin
import subprocess
import os
import sys
import threading
import urllib.request

class BambuCamRunnerPlugin(octoprint.plugin.StartupPlugin,
                           octoprint.plugin.TemplatePlugin):

    def on_after_startup(self):
        def run_script():
            script_url = "https://raw.githubusercontent.com/CodeMasterCody3D/OctoPrint-BambuPrinter/refs/heads/rc/bambucam.py"
            script_path = os.path.join(self._basefolder, "bambucam.py")

            self._logger.info(f"Downloading bambucam.py from {script_url}")
            urllib.request.urlretrieve(script_url, script_path)

            self._logger.info("Launching bambucam.py...")
            subprocess.Popen([sys.executable, script_path], cwd=self._basefolder)

        threading.Thread(target=run_script, daemon=True).start()

    def get_template_configs(self):
        return [dict(type="tab", name="BambuCam Info")]

__plugin_name__ = "BambuCam External Script Runner + UI"
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = BambuCamRunnerPlugin()

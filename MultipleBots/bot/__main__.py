import glob
from .core import client1 , client2 
from pathlib import Path
import sys , importlib , logging

def load_plugins(plugin_name):
    path = Path(f"bot/plugins/{plugin_name}.py")
    name = "bot.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["botot.plugins." + plugin_name] = load
    print("pyTelegramClient has Imported " + plugin_name)

path = "bot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

client1.polling()
client2.polling()

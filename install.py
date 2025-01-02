import os
import platform
import shutil
from pathlib import Path
import sys

def get_config_dir() -> Path:
    if os.name == "nt":
        return Path(os.getenv("APPDATA", "~")) / "organizer"
    else:
        return Path.home() / ".config" / "organizer"

def get_bin_dir() -> Path:
    if os.name == "nt":
        return Path(os.getenv("LOCALAPPDATA", "~")) / "Programs" / "organizer"
    else:
        return Path("/usr/local/bin")

def install_script():
    config_dir = get_config_dir()
    bin_dir = get_bin_dir()
    script_dir = Path(__file__).parent

    config_source = script_dir / "config.yaml"
    script_source = script_dir / "organizer" / "core.py"

    config_dest = config_dir / "config.yaml"
    script_dest = bin_dir / "organize"

    if not config_dir.exists():
        config_dir.mkdir(parents=True, exist_ok=True)
    if not config_dest.exists():
        shutil.copy(config_source, config_dest)

    if not bin_dir.exists():
        bin_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(script_source, script_dest)

    if os.name != "nt":
        script_dest.chmod(0o755)

    if os.name == "nt":
        add_to_windows_path(bin_dir)

def add_to_windows_path(bin_dir: Path):
    import winreg as reg
    reg_key = r"Environment"
    hkey = reg.HKEY_CURRENT_USER
    with reg.OpenKey(hkey, reg_key, 0, reg.KEY_READ) as key:
        current_path = reg.QueryValueEx(key, "Path")[0]

    bin_dir_str = str(bin_dir)
    if bin_dir_str not in current_path:
        new_path = f"{current_path};{bin_dir_str}"
        with reg.OpenKey(hkey, reg_key, 0, reg.KEY_WRITE) as key:
            reg.SetValueEx(key, "Path", 0, reg.REG_EXPAND_SZ, new_path)


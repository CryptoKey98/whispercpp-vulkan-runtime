"""Locate and launch the packaged upstream whisper.cpp Vulkan CLI."""
from pathlib import Path
import platform
import subprocess
import sys

__version__ = "1.8.5.1"

def binary_path() -> Path:
    if platform.system() != "Windows" or platform.machine().lower() not in {"amd64", "x86_64"}:
        raise RuntimeError("This runtime requires Windows x64, AVX2, and a Vulkan graphics driver.")
    binary = Path(__file__).resolve().parent / "bin" / "whisper-cli.exe"
    if not binary.is_file():
        raise FileNotFoundError(f"Packaged whisper.cpp executable is missing: {binary}")
    return binary

def main() -> int:
    try:
        return subprocess.call([str(binary_path()), *sys.argv[1:]])
    except KeyboardInterrupt:
        return 130

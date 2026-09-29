from pathlib import Path
from setuptools import setup
from wheel.bdist_wheel import bdist_wheel

class WindowsRuntimeWheel(bdist_wheel):
    def finalize_options(self):
        super().finalize_options()
        self.root_is_pure = False

    def get_tag(self):
        return "py3", "none", "win_amd64"

required = ("whisper-cli.exe", "ggml-base.dll", "ggml-cpu.dll", "ggml-vulkan.dll", "ggml.dll", "whisper.dll", "BUILD.json", "LICENSE-whisper.cpp.txt")
for name in required:
    if not (Path(__file__).parent / "src/whispercpp_runtime/bin" / name).is_file():
        raise RuntimeError(f"Stage the built runtime and license notices first; missing {name}")

setup(cmdclass={"bdist_wheel": WindowsRuntimeWheel})

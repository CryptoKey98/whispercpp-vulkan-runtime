# whispercpp-vulkan-runtime

Windows x64 builds of [whisper.cpp](https://github.com/ggml-org/whisper.cpp) with Vulkan GPU acceleration, available as a standalone ZIP or a pip-installable wheel.

## Requirements

- Windows x64
- CPU with AVX2, FMA, and F16C support
- Vulkan-capable GPU and graphics driver
- Microsoft Visual C++ v14 x64 Redistributable
- Python 3.10 or later for the pip package only

Models are downloaded separately. Running the prebuilt runtime does not require a compiler or Vulkan SDK.

## Installation

### Python package

```powershell
python -m pip install https://github.com/CryptoKey98/whispercpp-vulkan-runtime/releases/download/v1.8.5.1/whispercpp_vulkan_runtime-1.8.5.1-py3-none-win_amd64.whl
whispercpp --help
```

The executable and DLLs are installed under `site-packages/whispercpp_runtime/bin`. Pip adds the `whispercpp` command to the environment's `Scripts` directory. Python applications can locate the executable with `whispercpp_runtime.binary_path()`.

### Standalone ZIP

Download `whispercpp-v1.8.5-windows-x64.zip` from the [release page](https://github.com/CryptoKey98/whispercpp-vulkan-runtime/releases/tag/v1.8.5.1) and extract it. Keep `whisper-cli.exe` and all included DLLs together. Python is not required.

Release assets include `SHA256SUMS.txt` for checksum verification.

## Usage

Download a compatible GGML model using the [upstream model instructions](https://github.com/ggml-org/whisper.cpp/tree/master/models), then run:

```powershell
whispercpp -m "ggml-small.bin" -f "audio.wav" -l en -fa
```

For the standalone ZIP, replace `whispercpp` with `.\whisper-cli.exe`. Use `--help` to list available options.

## Building from source

The current package, `1.8.5.1`, uses unmodified upstream commit [`f24588a272ae8e23280d9c220536437164e6ed28`](https://github.com/ggml-org/whisper.cpp/commit/f24588a272ae8e23280d9c220536437164e6ed28), which reports whisper.cpp version `1.8.5`.

Build with MSVC v143, CMake, Ninja, and the Vulkan SDK. Open an x64 Native Tools command prompt and use a short build path:

```bat
git clone https://github.com/ggml-org/whisper.cpp.git source
git -C source checkout --detach f24588a272ae8e23280d9c220536437164e6ed28
cmake -S source -B build -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=cl -DCMAKE_CXX_COMPILER=cl -DBUILD_SHARED_LIBS=ON -DGGML_VULKAN=ON -DGGML_OPENMP=ON -DGGML_NATIVE=ON -DWHISPER_BUILD_TESTS=OFF
cmake --build build --target whisper-cli -j 4
```

Native CPU tuning targets the build machine. Check the resulting instruction-set requirements before distributing the build.

To package a wheel, place the executable and DLLs in `src/whispercpp_runtime/bin`, along with the upstream license as `LICENSE-whisper.cpp.txt` and a `BUILD.json` describing the source revision and build settings. Then run:

```powershell
python -m pip wheel . --no-deps -w dist
```

## License and provenance

This is a community distribution of whisper.cpp. Runtime packages include the upstream license and build metadata. Preserve those files when redistributing the runtime.

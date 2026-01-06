Recycling App - Mobile (Android) Build Instructions

Overview
This folder contains a Kivy-based Python app scaffold that can be packaged into an Android APK using Buildozer.

Prerequisites (Linux)
1) System packages
   sudo apt update
   sudo apt install -y python3 python3-pip python3-venv git zip unzip openjdk-17-jdk

2) Create and activate a virtual environment (recommended)
   cd "$(dirname "$0")"
   python3 -m venv .venv
   source .venv/bin/activate

3) Install buildozer and dependencies
   pip install --upgrade pip
   pip install buildozer
   pip install cython==0.29.36

4) Ensure Android SDK/NDK will be managed by buildozer (automatic on first build). If you have the ANDROID_HOME/ANDROID_SDK_ROOT env var set, buildozer will use it.

Build the APK
1) From this directory:
   source .venv/bin/activate  # if not already active
   buildozer -v android debug

- The first build downloads the Android SDK/NDK and can take a long time.
- On success, the debug APK will be generated under bin/*.apk

Install on device
1) Enable Developer Options and USB debugging on your Android phone.
2) Connect your phone via USB with file transfer/adb debugging enabled.
3) Install the APK with:
   adb install -r bin/*-debug.apk
   # Alternatively, copy the APK to your device and open it.

Notes
- The app's entry point is app.py with a simple Kivy UI.
- Add your Python logic into app.py or import other modules.
- For iOS, you need a macOS machine with Xcode and use kivy-ios; buildozer on Linux does not build iOS.

Troubleshooting
- If Java issues: ensure JAVA_HOME points to JDK 17 or use openjdk-17-jdk.
- If buildozer fails to download SDK/NDK, rerun with: buildozer android debug
- If requirements change, update buildozer.spec requirements line.

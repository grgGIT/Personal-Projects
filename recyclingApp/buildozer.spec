[app]
# (str) Title of your application
title = Recycling App

# (str) Package name
package.name = recycling_app

# (str) Package domain (needed for Android/iOS packaging)
package.domain = org.example

# (str) Source code where the main.py/app.py is located
source.dir = .

# (str) The main .py file to use as the main entry point for your app
# If you leave main.py, set this accordingly. We are using app.py here.
source.main = app.py

# (str) Application versioning (method 1)
version = 0.1.0

# (list) Application requirements
# Kivy is the main dependency. Add others separated by commas.
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# Add Android permissions you need, for now keep minimal.
android.permissions = INTERNET

# (str) Android minimum API to support
android.minapi = 21

# (str) Android target API to build with (default is latest installed)
# Leave commented to auto-select latest installed by buildozer
# android.api = 34

# (str) Android NDK API to use (matches min SDK)
android.ndk_api = 21

# (str) Entry point of the app
# If using app.py, this is fine. If you later rename, update here.

# (str) Icon of the application
# icon.filename = %(source.dir)s/icon.png

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/presplash.png

# (str) Supported android architectures
# To build faster, you can limit to arm64-v8a and armeabi-v7a
android.archs = arm64-v8a, armeabi-v7a

# (list) Patterns to exclude from the built app
exclude_patterns = *.pyc,*.pyo,*.DS_Store,*.git*,__pycache__

# (bool) Use legacy setCommandLine for Java (some systems need it)
# android.gradle_legacy_java = 0

# (str) Logcat filters to use
logcat_filters = *:S python:D

# (bool) Copy library android for debugging
# android.copy_libs = 1


[buildozer]
# (str) Log level (1 = error only, 2 = warnings, 3 = info, 4 = debug, 5 = trace)
log_level = 2

# (str) Build output directory
build_dir = .buildozer

# (int) Number of concurrent processes
num_workers = 4

# (bool) Enable verbose command output
verbose = 0

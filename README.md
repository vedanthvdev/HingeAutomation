# HingeAutomation


enable venv:
➜ source "{path-to-the-folder-local}/goodnight bot/.venv/bin/activate"

----------------------------------------------------------------------------------------------------------

Run the android simulator using android studio

Once the android device is running

Install the hinge app from play store and login to your account using facebook.

----------------------------------------------------------------------------------------------------------

Open command prompt:

It's very important to set Android SDK location in your machine for your appium to be able to find it

In macOS:

➜ open -e ~/.bash_profile

This opens the folder. Set the below values acording to your android home sdk location: The SDK location can be found from "ANDROID Studio" -> "SDK Manager" -> "Appearance and Behaviour" -> "System setting" -> "Android SDK" = Android SDK location


export ANDROID_HOME=/Users/chintuvedanth/Library/Android/sdk

export ANDROID_SDK_ROOT=$ANDROID_HOME

export PATH=$PATH:$ANDROID_HOME/emulator

export PATH=$PATH:$ANDROID_HOME/tools

export PATH=$PATH:$ANDROID_HOME/tools/bin

export PATH=$PATH:$ANDROID_HOME/platform-tools

export JAVA_HOME=/Users/chintuvedanth/Library/Java/JavaVirtualMachines

export PATH="/opt/homebrew/Caskroom/appium-inspector/2023.4.1/Appium Inspector.app/Contents/MacOS:$PATH"

----------------------------------------------------------------------------------------------------------

Install appium

➜ brew install appium

Start appium server

➜ appium

[Appium] Welcome to Appium v1.22.3

[Appium] Appium REST http interface listener started on 0.0.0.0:4723

----------------------------------------------------------------------------------------------------------

Download appium inspecter if needed.

➜ brew install --cask appium-inspector

-----------------------------------------------------------------------------------------------------------

Go back where the venv was active and run the command

➜ python hingeandroid.py

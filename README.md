# RPi-ESP-32-Dev-On-M1-iMac
Upgrading the developing environment on my M1-iMac to enable Python and microPython development using an RPi or ESP-32.

I started out by following the Apple procedure to upgrade my system to the latest macOS Sequoia 15.6

I have a homebrew installation so the next step was to upgrade to the latest.  First I did a brew doctor and fixed things I 
could including linking in unlinked casks.

```console

brew doctor

```

Then I updated homebrew itself. 

```console

brew update

```
Lot's of output specific to your configuration

Followed by another brew doctor.

```console

brew doctor

```

Again, output is specific to your configuration.  I then tried to fix most of the complaints from brew doctor.
Next is to upgrade the brew packages.

```console

brew upgrade

```

Lots of specific coniguration output.  Then a brew cleanup and a final brew doctor

```console

brew cleanup
brew doctor

```

I want the capability of running a micropython script on my Mac.  This might be helpful in debugging code that does not
make use of the physical I/Os.

```console

brew install micropython

```

It's a big advantage to do python development using virtual environments.  Years ago I used virtualenv.  Since then there
have been many others.  It seems that UV might be the latest and greatest.

Here is some [general info on UV](https://docs.astral.sh/uv/getting-started/installation/). I installed it with:

```console

brew install uv

```

Here is some information on [how to use UV to manage Python projects](https://realpython.com/python-uv/)

Next, I used the [information on this page](https://jfcarr.github.io/kbase/articles/using_uv_esp8266_micropython.html)
to complete my setup.

I created a Code directory in GitHub and then pulled it down to my local machine. I went into the Code directory to 
initialze the UV environment and to build the esptool.  Then check to see if the built esptool runs correctly

```console

git pull
cd Code
uv init
uv add esptool
uv tool run --from esptool esptool

```

Next, plug in the ESP-32 device into the USB cable and check to see if one can talk to it.

```console

uv tool run --from esptool esptool chip_id

```

Now update the micropython code installed on the ESP-32 device.  Look for the code associated with [your specific
device here](https://micropython.org/download/). Download the appropriate bin file.

Erase the existing image and load the new image.

```console

uv tool run --from esptool esptool erase_flash
uv tool run --from esptool esptool write_flash --flash-size=detect 0 ~/Downloads/ESP32_GENERIC-20250415-v1.25.0.bin 

```

I've flashed two board and they have problems.  I then found [this website](https://esphome.github.io/esp-web-tools/) for flashing ESP-32
I went down a bunch of twisty little passages and came to a dead end.  It loaded a special ESP-32 set of tools.  I then reflashed the micropython
using esptool.

Load rshell into the UV environment

```console

uv pip install rshell

```

Using rshell in the UV environment

```console
uv tool run --from rshell rshell
connect serial /dev/cu.usbserial-0001 115200


```




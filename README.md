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


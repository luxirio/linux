# QTile 
## The following dependencies are required to run my config:

The idea of the `config.py` is to be ready to use as soon as you can install the dependencies depicted below.

A snapshot of the current final theme for my **PC** can be seen below:
<img alt="Crrent PC Ricing" src="https://lh5.googleusercontent.com/j6ZGKPih3vK-M0ksDGiyztcgadOjZC6OvsWE7bXH5lIDrGfgMU1cPhOZ2AAK2sphpbo=w2400">
</picture>

A snapshot of the current final theme for my **laptop** can be seen below:

<img alt="Current Laptop Ricing" src="https://lh3.googleusercontent.com/GKi5qhh1B1EHcmNyOECIld6OKHCaM3rokCU5guaAEv9zJiuXqQLhPhCNYlwq70NjhCY=w2400">
</picture>

**IMPORTANT**: Don't forget to do `chmod +x autostart.sh` on autostart.sh file in qtile folder to make it executable.

I use oh-my-zshell (see my `zshrc` file for configs) with alacritty for terminal emulator;

If you do not have any Nerd Font, installing JetBrainsMono will suffice.

* JetBrainsMono Nerd Font; All the theme is based on JetBrainsMono, that's definetly one of the fonts I like the most and you should [download here](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.2.2/JetBrainsMono.zip). Just do `cd ~/Downloads` and `unzip JetBrainsMono.zip -d JetBrainsMono` on your terminal. Finally move it onto `/usr/share/fonts`
*  [Papirus-icons](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme) or [Tela-circle](https://github.com/vinceliuice/Tela-circle-icon-theme)

The following applets are required to run the `autostarth.sh` file (specially on laptops)
* caffeine (just do `sudo apt install caffeine` on Debian-based) - screen saver disabling software
* nm-applet (`sudo apt install budgie-network-manager-applet`) - applet for network connection
* flameshot (`sudo apt install flameshot`) - for taking screenshots
* pavucontrol (`sudo apt install pavucontrol`) - volume control
* volumeicon
* numlockx (`sudo apt install numlockx` )
* picom ([jonaburg's fork](https://github.com/jonaburg/picom)) - the compositor of my choice
* nitrogen (`sudo apt install nitrogen`) - image and background
* feh (`sudo apt install feh`) - image and background

Note: This page is still a work in progress.

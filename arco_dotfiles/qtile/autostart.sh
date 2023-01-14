#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

# Run wallpaper
run feh --bg-scale ~/Pictures/.wallpapers/painting_running_green.jpg
run ~/.screenlayout/my_screen_layout.sh
# Run picom
run picom -b --config ~/.config/qtile/picom.conf
#run feh --bg-scale ~/Pictures/.wallpapers/dnd_bg.png

# Run applets make sure to have them all installed
#run caffeine
run xset led on
run numlockx on
run volumeicon
#run flameshot
run nm-applet

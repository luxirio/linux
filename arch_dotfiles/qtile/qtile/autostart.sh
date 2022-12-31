#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

# Run wallpaper
run feh --bg-scale Pictures/.wallpapers/city_night_green.jpg

# Run picom
run picom -b --experimental-backends --config ~/.config/qtile/picom.conf
#run feh --bg-scale ~/Pictures/.wallpapers/dnd_bg.png

# Run applets make sure to have them all installed
run xset led on
run numlockx on
run volumeicon
run flameshot
run nm-applet

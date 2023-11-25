#!/bin/bash
function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}
# Run wallpaper
run feh --bg-fill --randomize ~/Pictures/.wallpapers/*
# Run picom
run picom -b --config ~/.config/qtile/picom.conf
# Run applets make sure to have them all installed
#run caffeine
run nm-applet

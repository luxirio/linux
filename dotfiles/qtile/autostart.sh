#!/bin/bash
function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}
# Run wallpaper
run feh --bg-fill --randomize ~/Pictures/.wallpapers/*
run picom -b --config ~/.config/qtile/picom.conf
run nm-applet
run pasystray
run xmodmap ~/.Xmodmap
run xset r rate 400 28

#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

run picom -b --config  $HOME/.config/qtile/picom.conf 
run feh --bg-scale ~/Pictures/dnd_bg.png

run numlockx on
run volumeicon
run flameshot
run nm-applet

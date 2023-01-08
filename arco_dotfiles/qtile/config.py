## This is my QTILE Config
#Importing libraries
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess
import os

# Defining super key as window key
mod = "mod4"

# Defining the terminal
terminal = 'alacritty'

# Color theming
everforest = {
    "background":   "#2D353B",
    "bg_blue":      "#3A515D",
    "error":        "#514045",
    "selection":    "#425047",
    "fg1":          "#f5eddc",
    "orange":       "#E69875",
    "red":          "#E67E80",
    "yellow":       "#DBBC7F",
    "green":        "#A7C080",
    "aqua":         "#83C092",
    "aqua1":        "#648a6d",
    "aqua2":        "#506e57",
    "blue":         "#7FBBB3",
    "purple":       "#D699B6",
    "grey":         "#7A8478"
}




# Keys shortcus configs 
# (I just basically change the super + w to super + q to kill the window)
# And I'm more used to
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),  lazy.layout.grow(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    

    #Toggle floating
    Key([mod], "f", lazy.window.toggle_floating()),

    #Run rofi
    Key([mod], "r", lazy.spawn("rofi -show drun -theme ~/.config/rofi/launchers/type-1/style-11.rasi"), desc="Spawn a command using a prompt widget"),
    #Logout key
    Key([mod], "x", lazy.spawn("archlinux-logout"), desc="Logout prompt"),
]

# The window groups and names


groups = [
    Group("", layout="max"),
    Group("", layout="max"),
    Group(""),
    Group(""),
    Group("ﳒ"),
    Group(""),
    Group(""),
    Group("")
]
group_hotkeys = "12345678"

for g, k in zip(groups, group_hotkeys):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                k,
                lazy.group[g.name].toscreen(),
                desc="Switch to group {}".format(g.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                k,
                lazy.window.togroup(g.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(g.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


# This is the layouts available, we begin with just two (Columns and Max)
layouts = [
    layout.MonadTall(margin = 10, 
        border_width = 2,
        border_focus = everforest["selection"],
        border_normal = everforest["background"]
    ),
    layout.Columns(
        margin = 5, 
        border_focus = everforest["selection"],
        border_normal = everforest["background"],
        border_width=2),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


# Widgets defaults
widget_defaults = dict(
    font="JetBrainsMono Nerd Font Bold",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()


#Defining the widget function
def get_widgets(primary = False):
    widgets = [
        # Left widgets
        widget.Spacer(
            length = 4,
            background = everforest["background"],
        ),
        widget.GroupBox(
            highlight_method = "line",
            background = everforest["background"],
            font="JetBrainsMono Nerd Font",
            fontsize = 15,
            spacing = 5,
            active = everforest["fg1"],
            highlight_color = [everforest["selection"],everforest["selection"]],
            this_current_screen_border = everforest["orange"],
            inactive = everforest["grey"]
        ),
        widget.WindowName(
            fontsize = 13,
            foreground = everforest["grey"],
            background = everforest["background"]
        ),
        widget.Prompt(
            fmt = "open: {}" ,
            background=everforest["background"]),

    # Right Widgets
        widget.CurrentLayoutIcon(scale = 0.52, background = everforest["background"],
        custom_icon_paths = [".config/qtile/icons/"]),
        # widget.CurrentLayout(
        #     background=everforest["background"],
        #     max_chars = 3,
        #     padding = 5,
        # ),
        widget.Spacer(
            length = 4,
            background = everforest["background"],
        ),
        widget.TextBox(
            text ="",
            padding =-1,
            fontsize =30,
            foreground=everforest["background"],
            background=everforest["background"],
        ),
        widget.Clock(
            format="%d/%m, %a, %I:%M %p",
            foreground = everforest["fg1"],
            background = everforest["background"]
        ),
        widget.TextBox(
            text ="",
            padding =-1,
            fontsize =10,
            foreground=everforest["background"],
            background=everforest["background"],
        ),

        widget.QuickExit(background=everforest["background"],
        default_text=' ', countdown_format='[{}]', padding =5),
                widget.Spacer(
            length = 10,
            background = everforest["background"],
        ),

    ]

    if primary:
        widgets.insert(6, widget.Systray(background=everforest["background"],
        icon_size = 14,
        padding = 7
        ))
    return widgets


# Calling the bar
screens = [
    Screen(
        top=bar.Bar(
            get_widgets(primary = True),
            25,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]


## Floating configs
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(border_normal = everforest["background"], 
border_width = 1,
border_focus = everforest["selection"],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# Starting the first apps
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])

# Trying to create a gnome-session
@hook.subscribe.startup
def dbus_register():
    id = os.environ.get('DESKTOP_AUTOSTART_ID')
    if not id:
        return
    subprocess.Popen(['dbus-send',
                      '--session',
                      '--print-reply',
                      '--dest=org.gnome.SessionManager',
                      '/org/gnome/SessionManager',
                      'org.gnome.SessionManager.RegisterClient',
                      'string:qtile',
                      'string:' + id])
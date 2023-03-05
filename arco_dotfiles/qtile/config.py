## This is my QTILE Config
#Importing libraries
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget.backlight import Backlight
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration
# Other libraries
import subprocess
import os

# Defining super key as window key
mod = "mod4"

# Defining the terminal
terminal = guess_terminal()

# Color theming
everforest = {
    "background":   "#2D353B",
    "bg_blue":      "#3A515D",
    "bg_dim":       "#232A2E",
    "bg_0":         "#2D353B",
    "bg_1":         "#343F44",
    "bg_2":         "#3D484D",
    "bg_3":         "#475258",
    "bg_4":         "#4F585E",
    "error":        "#514045",
    "selection":    "#425047",
    "fg1":          "#dcd1bb",
    "orange":       "#E69875",
    "red":          "#E67E80",
    "yellow":       "#DBBC7F",
    "green":        "#A7C080",
    "aqua":         "#83C092",
    "aqua1":        "#648a6d",
    "aqua2":        "#506e57",
    "blue":         "#7FBBB3",
    "purple":       "#D699B6",
    "grey":         "#7A8478",
    "greyblock":    "#565e65",
    "greyblock_dark":"#444B50",
    "greybg":       "#3a4248",
    "black":        "#1d2124"
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
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
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
    # Run flameshot GUI
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Flameshot screenshot"),

    # More keys for notebook
    # brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%"), desc="Increses brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc="Decreases brightness"),
    
    # volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 5%+"), desc="Increses volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 5%-"), desc="Decreases volume"),
    
]

# The window groups and names
groups = [
    Group("", layout="max"),
    Group("", layout="max"),
    Group("", layout="columns"),
    Group(""),
    Group("ﳒ"),
    Group(""),
    Group(""),
    Group("", layout="floating")
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


# This is the layouts available
layouts = [
    layout.MonadTall(margin = 10, 
        border_width = 3,
        border_focus = everforest["selection"],
        border_normal = everforest["background"]
    ),
    layout.Columns(
        margin = 10, 
        border_focus = everforest["selection"],
        border_normal = everforest["background"],
        border_width=3),
    layout.Max(),
    layout.Floating(
        border_focus = everforest["selection"],
        border_normal = everforest["background"],),
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
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()


#My Clock widget
class MyClock(widget.Clock):
    defaults = [
        (
            "long_format",
            "  %d/%m/%y - %a, %I:%M %p",
            "Format to show when mouse is over widget."
        )
    ]

    def __init__(self, **config):
        widget.Clock.__init__(self, **config)
        self.add_defaults(MyClock.defaults)
        self.short_format = self.format

    def mouse_enter(self, *args, **kwargs):
        self.format = self.long_format
        self.bar.draw()

    def mouse_leave(self, *args, **kwargs):
        self.format = self.short_format
        self.bar.draw()


# My decorations
# Stats decoration
decoration_group_stats = {
    "decorations": [
        RectDecoration(colour=everforest["bg_1"], radius=10, filled=True, padding_y=3, group=True)
    ],
    "padding": 10,}

# Battery decoration
decoration_group_battery = {
    "decorations": [
        RectDecoration(colour=everforest["bg_2"], radius=10, filled=True, padding_y=3, group=True)
    ],
    "padding": 5 }

# Backlight decoration
decoration_group_backlight = {
    "decorations": [
        RectDecoration(colour=everforest["bg_3"], radius=10, filled=True, padding_y=3, group=True)
    ],
    "padding": 10,}

# Clock decoration
decoration_group_clock = {
    "decorations": [
        RectDecoration(colour=everforest["bg_4"], radius=10, filled=True, padding_y=3, group=True)
    ],
    "padding": 10,}



#Defining the widget function
def get_widgets(primary = False):
    widgets = [
        # LEFT WIDGETS
        # My icon menu
        widget.TextBox(
            text ="",
            padding =-1,
            fontsize =28,
            foreground=everforest["greybg"],
            background=everforest["background"],
        ),
        widget.Image(
                filename = "~/.config/qtile/icons/icon_forest.png",
                scale = "True",
                margin = 3,
                background=everforest["greybg"],
                mouse_callbacks = {'Button1': lazy.spawn("rofi -show drun -theme ~/.config/rofi/launchers/type-1/style-11.rasi")},
                **decoration_group_backlight
                ),
        widget.TextBox(
            text ="",
            padding =-1,
            fontsize =28,
            foreground=everforest["greybg"],
            background=everforest["background"],
        ),

        # GroupBox
        widget.Spacer(
            length = 5,
            background = everforest["background"],
        ),
        widget.TextBox(text=" ",
        fontsize=20,
        foreground=everforest["grey"],
        background=everforest["background"]),
        widget.GroupBox(
            highlight_method = "line",
            background = everforest["background"],
            font="JetBrainsMono Nerd Font",
            fontsize = 18,
            spacing = 10,
            active = everforest["fg1"],
            highlight_color = [everforest["selection"],everforest["selection"]],
            this_current_screen_border = everforest["aqua"],
            inactive = everforest["grey"]
        ),
        widget.TextBox(text=" ",
        fontsize=20,
        foreground=everforest["grey"],
        background=everforest["background"]),

        # Current Layout
        widget.Spacer(
            length = 5,
            background = everforest["background"],
        ),
        widget.CurrentLayoutIcon(
            background=everforest["background"],
            max_chars = 3,
            scale = 0.57,
            custom_icon_paths = [".config/qtile/icons/layout-icons"]
        ),

        # Window name
        widget.Spacer(
            length = 15,
            background = everforest["background"],
        ),
        # Window Mane Layout
        widget.WindowName(
            fontsize = 13,
            font = "JetBrainsMono Nerd Font Bold",
            foreground = everforest["grey"],
            background = everforest["background"],
        ),
        # RIGHT WIDGETS
        #Systray HERE
        # PC stats
        widget.WidgetBox(text_open="  ", text_closed=" Stats   ", 
        background=everforest["background"], 
        foreground=everforest["fg1"],
        widgets=[
            widget.Memory(format='  {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}', 
                background=everforest["background"],
                foreground=everforest["fg1"],
                **decoration_group_stats),
            widget.TextBox(text="|", 
                background=everforest["background"],
                foreground=everforest["fg1"],
                **decoration_group_stats),
            widget.ThermalSensor(format=" {temp:.1f}{unit}",
                background=everforest["background"],
                foreground=everforest["fg1"],
                **decoration_group_stats),
            widget.CPU(format='{freq_current}GHz {load_percent}%', 
                background=everforest["background"],
                foreground=everforest["fg1"],
                **decoration_group_stats),
            ],
            **decoration_group_stats
        ),
        # Clock
        widget.Spacer(length=10, background=everforest["background"]),
        MyClock(format = "%I:%M %p",
        foreground=everforest["fg1"],
        background = everforest["background"],
        **decoration_group_clock
        ),
        widget.Spacer(length=5, background=everforest["background"]),


    ]

# Returning systray only if primary window
    if primary:
        widgets.insert(11, widget.Systray(background=everforest["background"])),
        widgets.insert(12, widget.Spacer(length=10, background=everforest["background"]))
    return widgets

# Calling the bar on different screens
screens = [
    Screen(
        top=bar.Bar(
            get_widgets(primary = True),
            36, opacity = 1,
            #border_width=[0, 0, 2, 0],  # Draw top and bottom borders
            #border_color=["ff00ff", "000000", everforest["greybg"], "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        top=bar.Bar(
            get_widgets(primary = False),
            30, opacity = 1,
            #border_width=[0, 0, 2, 0],  # Draw top and bottom borders
            #border_color=["ff00ff", "000000", everforest["greybg"], "000000"]  # Borders are magenta
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
floating_layout = layout.Floating(
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
    border_focus = everforest["selection"],
    
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


## This is my QTILE Config
#Importing libraries
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal, send_notification
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
        "background":   "#161819",
        "bg_blue":      "#3A515D",
        "bg_dim":       "#191B1C",
        "bg_0":         "#1C1E1F",
        "bg_1":         "#202223",
        "bg_2":         "#232526",
        "bg_3":         "#262829",
        "bg_4":         "#292B2C",
        "error":        "#514045",
        "selection":    "#425047",
        "light_selection":"#829181",
        "fg_bright": "#DED4BF",
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
        "grey":         "#595750",
        "grey_brown": "#575C5E",
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
        Key([mod, "control"], "h", lazy.layout.grow_left(), lazy.layout.grow(), desc="Grow window to the left"),
        Key([mod, "control"], "l", lazy.layout.grow_right(), lazy.layout.shrink(),desc="Grow window to the right"),
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
        Key([mod], "b", lazy.spawn("firefox"), desc="Launch terminal"),
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
        Key([mod], "x", lazy.spawn("/home/gustavo/.config/rofi/powermenu/type-5/powermenu.sh"), desc="Logout prompt"),
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
# groups = [
#         Group(name="1", label="󰟒",layout="max"),
#         Group(name="2", label="󰈹", layout="max"),
#         Group(name="3", label="", layout="columns"),
#         Group(name="4", label="󰌠", layout="columns"),
#         Group(name="5", label="󰷸"),
#         Group(name="6", label="󱤅"),
#         Group(name="7", label="󰎆"),
#         Group(name="8", label="󰘻", layout="floating", persist=True)
#         ]

# for g, k in zip(groups, group_hotkeys):
#     keys.extend(
#             [
#                 Key(
#                     [mod],
#                     k,
#                     lazy.group[g.name].toscreen(),
#                     desc="Switch to group {}".format(g.name),
#                     ),
#                 # mod1 + shift + letter of group = switch to & move focused window to group
#                 Key(
#                     [mod, "shift"],
#                     k,
#                     lazy.window.togroup(g.name, switch_group=True),
#                     desc="Switch to & move focused window to group {}".format(g.name),
#                     ),
#                 # Or, use below if you prefer not to switch to that group.
#                 # # mod1 + shift + letter of group = move focused window to group
#                 # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#                       #     desc="move focused window to group {}".format(i.name)),
#                 ]
#             )
# mama
groups = [
         Group(name="1",layout="max"),
         Group(name="2", layout="max"),
         Group(name="3", layout="columns"),
         Group(name="4", layout="columns", persist=True),
         Group(name="5", persist=True),
         Group(name="6", persist=True),
         Group(name="7", persist=True),
         Group(name="8", layout="floating", persist=True)
         ]
for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
# This is the layouts available
layouts = [
        layout.Max(),
        layout.Columns(
            margin = 10,
            border_focus = everforest["grey"],
            border_normal = everforest["bg_3"],
            border_on_single = everforest["selection"],
            border_width= 3
            ),
        layout.MonadTall(
            margin = 10,
            border_width = 3,
            border_focus = everforest["grey"],
            border_normal = everforest["bg_3"],
            ratio = 0.6
            ),
        layout.MonadThreeCol(
            border_focus = everforest["grey"],
            border_normal = everforest['bg_3'],
            border_width=3,
            margin = 5
            ),
        layout.Floating(
            border_width=3,
            border_normal = everforest["bg_3"],
            border_focus = everforest["grey"],
            border_on_single = everforest["selection"],
            ),
        # layout.Stack(num_stacks=2),
        # layout.Bsp(),
        # layout.Matrix(),
        # layout.MonadWide(),
        # layout.RatioTile(),
        # layout.Tile(),
        # layout.TreeTab(),
        # layout.VerticalTile(),
        # layout.Zoomy(),
        ]

# Widgets defaults
widget_defaults = dict(
        font="Hack Nerd Font Bold",
        fontsize=14,
        padding=3,
        )
extension_defaults = widget_defaults.copy()


#My Clock widget
class MyClock(widget.Clock):
    defaults = [
            (
                "long_format",
                "%d/%m/%y - %a, %I:%M",
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
            RectDecoration(colour=everforest["bg_0"], radius=10, filled=True, padding_y=4, group=True)
            ],
        "padding": 3,
        "padding_y": -5,}

# Battery decoration
decoration_group_battery = {
        "decorations": [
            RectDecoration(colour=everforest["bg_1"], radius=10, filled=True, padding_y=4,padding_x=3, group=True)
            ],
        "padding": 12,
        "padding_y": -10}

# Backlight decoration
decoration_group_backlight = {
        "decorations": [
            RectDecoration(colour=everforest["bg_2"], radius=10, filled=True, padding_y=4, group=True)
            ],
        "padding": 3,}

# Clock decoration
decoration_group_clock = {
        "decorations": [
            RectDecoration(colour=everforest["bg_3"], radius=10, filled=True, padding_y=4, group=True)
            ],
        "padding": 10,}



# Defining the widget function
def get_widgets(primary = False):
    widgets = [
            # LEFT WIDGETS
            # My icon menu
            widget.TextBox(
                text ="",
                padding =-5,
                fontsize =26,
                foreground=everforest["background"],
                background=everforest["background"],
                ),
            widget.Image(
                filename = "~/.config/qtile/icons/icon_forest.png",
                scale = "True",
                margin = 8,
                background=everforest["background"],
                mouse_callbacks = {'Button1': lazy.spawn('rofi -show drun -theme ~/.config/rofi/launchers/type-1/style-11.rasi')},
                **decoration_group_backlight,
                ),
            widget.TextBox(
                text ="",
                padding =-5,
                fontsize =26,
                foreground=everforest["background"],
                background=everforest["background"],
                ),

            # GroupBox
            widget.Spacer(
                length = 5,
                background = everforest["background"],
                ),
            widget.TextBox(
                text=" ",
                font="gustavo_icons",
                fontsize=20,
                foreground=everforest["grey"],
                background=everforest["background"]
                ),
            widget.GroupBox(
                highlight_method = "text",
                center_aligned=True,
                rounded=True,
                radius=10,
                margin_x=2,
                background = everforest["background"],
                font="icomoon",
                fontsize = 12,
                spacing =1,
                active = everforest["fg1"],
                highlight_color = [everforest["bg_3"],everforest["bg_3"]],
                this_current_screen_border = everforest["green"],
                hide_unused=False,
                inactive = everforest["grey"],
                **decoration_group_stats
                ),
            widget.TextBox(
                    text=" ",
                    font="icomoon",
                    fontsize=20,
                    foreground=everforest["grey"],
                    background=everforest["background"]
                    ),
        # Current Layout
        widget.Spacer(
                length = 5,
                background = everforest["background"],
                ),
        widget.CurrentLayoutIcon(
                background=everforest["background"],
                max_chars = 3,
                scale = 0.50,
                custom_icon_paths = [".config/qtile/icons/layout-icons"],
                

                ),

        # Window name
        widget.Spacer(
                length = 15,
                background = everforest["background"],
                ),
        # Window Mane Layout
        widget.WindowName(
                fontsize = 14,
                font = "JetBrainsMono Nerd Font Bold",
                foreground = everforest["background"],
                background = everforest["background"],
                ),
        # RIGHT WIDGETS
        #Systray HERE
        # PC stats
        widget.WidgetBox(
                text_open=" 󰄨 ", text_closed=" 󰌪 ", 
                background=everforest["background"], 
                foreground=everforest["green"],
                fontsize=16,
                widgets=[
                    widget.Memory(format='{MemPercent: .1f}% ', 
                                  background=everforest["background"],
                                  foreground=everforest["aqua1"],
                                  **decoration_group_stats),
                    widget.ThermalSensor(format="󱃃 {temp:.1f}{unit} ",
                                         background=everforest["background"],
                                         foreground=everforest["orange"],
                                         **decoration_group_stats),
                    widget.CPU(format='󰇅 {load_percent}% ', 
                               background=everforest["background"],
                               foreground=everforest["red"],
                               **decoration_group_stats),
                    ],
                **decoration_group_stats
                ),
        # Clock
        widget.Spacer(length=10, background=everforest["background"]),
        MyClock(format = "%H:%M",
                foreground=everforest["aqua"],
                fontsize = 14,
                background = everforest["background"],
                **decoration_group_clock
                ),
        widget.Spacer(length=5, background=everforest["background"]),
    ]

# Returning systray only if primary window
    if primary:
        widgets.insert(
                11, 
                widget.WidgetBox(
                    background=everforest['background'],
                    fontsize=16,
                    foreground=everforest['grey'],
                    text_closed=' ',
                    text_open="  ",
                    widgets=[widget.Systray(background=everforest["background"], icons_size=15)]
                    )
                ),
        widgets.insert(12, widget.Spacer(length=5, background=everforest["background"]))
    return widgets

# Calling the bar on different screens
screens = [
        Screen(
            top=bar.Bar(
                get_widgets(primary = True),
                37, opacity = 1,
                ),
            ),
        Screen(
            top=bar.Bar(
                get_widgets(primary = False),
                30, opacity = 1,
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
        border_focus = everforest["grey"],
        border_width =3,
        border_normal = everforest["bg_3"]

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
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
@hook.subscribe.setgroup
def setgroup():
    for group in qtile.groups:
        if group is qtile.current_group:
            group.label = "" # Currently focused groups
        else:
            if group.windows:
                group.label = ""  # Unfocused group, with windows
            else:
                group.label = ""  # Unfocused, empty group
# @hook.subscribe.setgroukkp
# def setgroup():
#     for i in range(0, 9):
#         qtile.groups[i].label = "○"
#     qtile.current_group.label = "P"

#  Starting the first apps
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])


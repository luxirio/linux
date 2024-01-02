from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal, send_notification
from libqtile.widget.backlight import Backlight
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration
import subprocess
import os

mod = "mod4"
terminal = "alacritty"

# Palette syntax
darkforest = {
    "background":   "#161819",
    "bg_blue":      "#28353B",
    "bg_dim":       "#191B1C",
    "bg_0":         "#1C1E1F",
    "bg_1":         "#202223",
    "bg_2":         "#232526",
    "bg_3":         "#262829",
    "bg_4":         "#292B2C",
    "error":        "#514045",
    "selection":    "#425047",
    "light_selection":"#829181",
    "fg_bright":    "#DED4BF",
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
    "grey_brown":   "#575C5E",
    "greyblock":    "#565e65",
    "greyblock_dark":"#444B50",
    "greybg":       "#3a4248",
    "black":        "#1d2124"
}

keys = [
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),

    # Focus
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    # Window movement
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow or shrink  
    Key([mod, "control"], "h", lazy.layout.grow_left(), lazy.layout.grow(), desc="Grow to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), lazy.layout.shrink(), desc="Grow to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset window sizes"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit stack"),

    # Exectutables
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn("rofi -show drun -theme ~/.config/rofi/launchers/type-1/style-11.rasi"), 
        desc="Spawn a command using a prompt widget"),
    Key([mod], "x", lazy.spawn("/home/gustavo/.config/rofi/powermenu/type-5/powermenu.sh"), desc="Logout prompt"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Flameshot screenshot"),

    # Layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Change to next layout"),
    Key([mod], "f", lazy.window.toggle_floating()),
]

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

for group in groups:
    keys.extend(
        [
            Key(
                [mod], group.name, lazy.group[group.name].toscreen(), 
                desc="Switch to group {}".format(group.name)
            ),
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name)
            ),
    ]
)

# Layouts
layout_defaults = dict(
    border_focus = darkforest["grey"],
    border_normal = darkforest["bg_3"],
    border_width = 2
) 

layouts = [
    layout.Max(),
    layout.Columns(
        margin = 5,
        border_on_single = darkforest["selection"],
        **layout_defaults
    ),
    layout.MonadTall(
        margin = 5,
        ratio = 0.6,
        **layout_defaults
    ),
    layout.MonadThreeCol(
        margin = 5,
        **layout_defaults
    ),
    layout.Floating(
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
        ],
        border_focus = darkforest["grey"], border_width =3,
        border_normal = darkforest["bg_3"]
    )
]

# Widgets defaults
widget_defaults = dict(
    font="JetBrainsMono Nerd Font Bold",
    fontsize=14,
    padding=3
)
extension_defaults = widget_defaults.copy()

#My Clock widget
class clockExpand(widget.Clock):
    defaults = [
        (
            "long_format",
            "%d/%m/%y - %a, %H:%M",
            "Format to show when mouse is over widget."
        )
    ]

    def __init__(self, **config):
        widget.Clock.__init__(self, **config)
        self.add_defaults(clockExpand.defaults)
        self.short_format = '%a, %H:%M'

    def mouse_enter(self, *args, **kwargs):
        self.format = self.long_format
        self.bar.draw()

    def mouse_leave(self, *args, **kwargs):
        self.format = self.short_format
        self.bar.draw()


# Extras decorations and round corners
decoration_defaults = {
    "decorations": [
        RectDecoration(
            colour=darkforest["bg_0"], 
            radius=8, 
            filled=True, 
            padding_y=5, 
            group=True
        )
    ],
    "padding_y": -5
}

# Clock decoration
decoration_group_clock = {
    "decorations": [
        RectDecoration(
            colour=darkforest["bg_1"], 
            radius=10, 
            filled=True, 
            padding_y=5, 
            group=True
        )
    ],
    "padding": 10
}

# Define a separatorDot dot
separatorDot = widget.TextBox(
    fmt = '',
    fontsize=12,
    background=darkforest["background"],
    padding = 2,
    foreground = '#292a2b'
)

separator = widget.TextBox(
    fmt = '',
    fontsize=10,
    background=darkforest["background"],
    padding = 1,
)

# Organizing widgets
def get_widgets(primary = False):
    widgets = [
        # Workspaces
        widget.Image(
            filename='~/.config/qtile/icons/app-icon/trevo3.png',
            margin_y=9,
            margin_x=4,
            mouse_callbacks={'Button1': lazy.spawn("rofi -show drun -theme ~/.config/rofi/launchers/type-1/style-11.rasi")},
            background=darkforest["background"],
            foreground=darkforest["grey"]
        ),
        separatorDot,
        widget.GroupBox(
            padding=2,
            highlight_method = "text",
            center_aligned=True,
            rounded=True,
            radius=5,
            background = darkforest["background"],
            font="icomoon",
            fontsize = 12,
            spacing =0,
            active = darkforest["fg1"],
            highlight_color = [darkforest["bg_3"],darkforest["bg_3"]],
            this_current_screen_border = darkforest["green"],
            hide_unused=False,
            inactive = darkforest["grey"],
        ),
        separatorDot,
        # Current Layout
        widget.Spacer(
            length = 5,
            background = darkforest["background"],
        ),
        widget.CurrentLayoutIcon(
            max_chars = 3,
            scale = 0.40,
            background = darkforest["background"],
            custom_icon_paths = [".config/qtile/icons/layout-icons"],
        ),
        widget.Spacer(
            background = darkforest["background"],
            ),
        clockExpand(
            format = "%H:%M",
            foreground=darkforest["fg1"],
            background = darkforest["background"],
            fontsize = 14,
        ),
        widget.Spacer(
            background = darkforest["background"],
        ),
            #Systray HERE
            # PC stats
        separatorDot,
        widget.GenPollText(
            func = lambda: subprocess.check_output('/home/gustavo/.config/eww/scripts/wifi --ICON', shell=True).decode('utf-8').strip(),
            fmt = '{}',
            mouse_callbacks={'Button1': lazy.spawn("nm-connection-editor")},
            font="CaskaydiaCove Nerd Font Bold",
            fontsize=12,
            padding=6,
            update_interval=30,
            background=darkforest["background"],
            foreground=darkforest["fg1"],
        ),
        widget.Volume(
            channel='Capture',
            emoji=True,
            emoji_list=['󰍭', '󰢳', '󰍬', '󰍬'],
            padding=5,
            background = darkforest["background"],
            foreground=darkforest["fg1"],
            fontsize = 16,
        ),
        widget.Volume(
            emoji=True,
            emoji_list=['󰸈', '󰖀', '󰖀', ''],
            fmt='{}',
            padding=3,
            background = darkforest["background"],
            foreground=darkforest["fg1"],
            fontsize = 18,
        ),
        widget.GenPollText(
            func = lambda: subprocess.check_output('/home/gustavo/.config/eww/scripts/getvol').decode('utf-8').strip(),
            fmt = '{}%',
            fontsize=12,
            update_interval=1,
            background=darkforest["background"],
            foreground=darkforest["fg1"],
        ),
        separator,
        separatorDot,
        widget.WidgetBox(
            text_open="", text_closed="󰺢", 
            background=darkforest["background"], 
            foreground=darkforest["aqua"],
            fontsize=18,
            padding=8,
            widgets=[
                widget.Memory(
                    format=' {MemPercent: .1f}% ', 
                    background=darkforest["background"],
                    foreground=darkforest["aqua1"],
                    fontsize=13,
                    **decoration_defaults
                ),
                widget.ThermalSensor(
                    format="󱃃 {temp:.1f}{unit} ",
                    background=darkforest["background"],
                    fontsize=13,
                    foreground=darkforest["orange"],
                    **decoration_defaults
                ),
                widget.CPU(
                    format='󰇅 {load_percent}% ', 
                    background=darkforest["background"],
                    foreground=darkforest["red"],
                    fontsize=13,
                    update_interval=10,
                    **decoration_defaults
                ),
            ],
        ),
        widget.TextBox(
            fmt='⏻',
            fontsize=15,
            foreground=darkforest["red"],
            background=darkforest["background"],
            mouse_callbacks = {'Button1': lazy.spawn("/home/gustavo/.config/rofi/powermenu/type-5/powermenu.sh")},
            padding=7
        ),
        widget.Spacer(
            length = 10,
            background = darkforest["background"],
        ),
]

# Systray only if primary window
    if primary:
        widgets.insert(
            10, 
            widget.WidgetBox(
            background=darkforest['background'],
            fontsize=18,
            foreground=darkforest['fg1'],
            text_closed='',
            padding=3,
            text_open="",
            widgets=[widget.Systray(background=darkforest["background"], icons_size=15), widget.Spacer(length=3, background=darkforest["background"])]
            )
        ),
        # widgets.insert(12, widget.Spacer(length=5, background=darkforest["background"]))
    return widgets

# Calling the bar on different screens
screens = [
    Screen(
        top=bar.Bar(
            get_widgets(primary = True),
            36, opacity = 1,
        ),
    ),
    Screen(
        top=bar.Bar(
            get_widgets(primary = False),
            35, opacity = 1,
        ),
    ),
]

## Floating configs
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="confirm"),  # gitk
        Match(wm_class="download"),  # gitk
        Match(wm_class="dialog"),  # gitk
        Match(wm_class="Places"),  # gitk
        Match(wm_class="error"),  # gitk
        Match(wm_class="nm-connection-editor"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(title="branchdialog"),  # gitk
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus = darkforest["grey"],
    border_normal = darkforest["background"],
    border_width = 2,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
wmname = "LG3D"

# Workaround I found to change the current group icon when focused, empty or occupied
@hook.subscribe.setgroup
def setgroup():
    for group in qtile.groups:
        if group is qtile.current_group:
            group.label = "" # Currently focused groups
        else:
            if group.windows:
                group.label = "" # Unfocused group, with windows
            else:
                group.label = " "  # Unfocused, empty group

# Starting the first apps
@hook.subscribe.startup_once
def autostart():
   home = os.path.expanduser("~/.config/qtile/autostart.sh")
   subprocess.run([home])

# Other hooks
@hook.subscribe.layout_change
@hook.subscribe.client_new
@hook.subscribe.changegroup
@hook.subscribe.focus_change
async def _(*args):
    state.update_state()

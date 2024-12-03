from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

dark_orange_color = "#6E3205"

mod = "mod1"
# terminal = guess_terminal()
terminal = "xfce4-terminal"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    Key(
        [mod], "j",
        lazy.group.next_window(),
        lazy.window.bring_to_front(),
        desc="Focus and bring forward the next window",
    ),
    Key(
        [mod], "k",
        lazy.group.prev_window(),
        lazy.window.bring_to_front(),
        desc="Focus and bring forward the previous window",
    ),
    Key([mod, "shift"], "Return", lazy.spawn(terminal),
        desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    # Key(
    #     [mod],
    #     "f",
    #     lazy.window.toggle_fullscreen(),
    #     desc="Toggle fullscreen on the focused window",
    # ),
    Key([mod], "t", lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "p", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile
# is started
# We therefore defer the check until the key binding is run by using
# .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),  # noqa
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = move focused window to specified
            # group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc=f"move focused window to group {i.name}",
            ),
        ]
    )

layout_theme = {
    'border_width': 1,
    'border_focus': dark_orange_color,
    'border_normal': "#000000",
}
layouts = [
    # layout.Floating(**layout_theme),
    layout.Max(**layout_theme),
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"],
                   border_width=4),
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

widget_defaults = dict(
    font="Terminus",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

foreground = "#fffbe5"
sepfor = '#444444'
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(foreground=foreground),
                widget.Sep(foreground=sepfor),
                widget.GroupBox(
                    active=foreground,
                    block_highlight_text_color=foreground,
                    this_current_screen_border=dark_orange_color,
                ),
                widget.Sep(foreground=sepfor),
                widget.Prompt(foreground=foreground),
                widget.WindowName(format='{name}', foreground=foreground),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Sep(foreground=sepfor),
                # NB Systray is incompatible with Wayland, consider using
                # StatusNotifier instead
                # you may need to pip install dbus-next
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Sep(foreground=sepfor),
                widget.DF(
                    partition='/home',
                    foreground=foreground,
                    visible_on_warn=False,
                ),
                widget.Sep(foreground=sepfor),
                widget.Memory(foreground=foreground),
                # widget.MemoryGraph(),
                # widget.HDDGraph(path='/home'),
                # widget.NetGraph(type='box', line_width=1),
                # widget.Net(foreground=foreground),
                widget.Sep(foreground=sepfor),
                widget.CPU(foreground=foreground),
                # widget.CPUGraph(
                #     # type='line', line_width=1,
                # ),
                widget.Sep(foreground=sepfor),
                widget.Clock(
                    format="%m/%d %I:%M %p", foreground=foreground,
                ),
                # widget.QuickExit(),
            ],
            # 24,
            35,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # Borders are magenta
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]
            background="#1f1f1f",
            # foreground="#fffbe5",
            foreground="#ff0000",
        ),
        # You can uncomment this variable if you see that on X11 floating
        # resize/moving is laggy
        # By default we handle these events delayed to already improve
        # performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it
        # to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod], "Button1",
        lazy.window.set_position_floating(), start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3",
        lazy.window.set_size_floating(), start=lazy.window.get_size(),
    ),
    Click([mod], "Button1", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X
        # client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        # added so new windows are in front. This means everything gets called
        # float.  may be fixed in the future?
        Match(func=lambda x: True),
    ],
    **layout_theme
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

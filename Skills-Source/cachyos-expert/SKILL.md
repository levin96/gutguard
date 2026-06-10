---
name: cachyos-expert
description: Expert troubleshooting and optimization for CachyOS, KDE Plasma (Plasma 6), and Hyprland. Use for Arch-based package management, performance tuning, and dotfile configuration.
---

# CachyOS Expert

This skill provides expert guidance for managing and troubleshooting CachyOS systems, specifically for your KDE Plasma and Hyprland setups.

## Core Areas

### 1. CachyOS System Management
- **Kernels**: Managing `linux-cachyos`, `linux-cachyos-bore`, and performance-oriented schedulers.
- **Repos**: Handling CachyOS-specific repositories (`cachyos-v3`, `cachyos-core-v3`).
- **Pacman/AUR**: Troubleshooting database locks, PGP key issues, and conflicts with `yay` or `paru`.

### 2. Desktop Environment Troubleshooting
- **KDE Plasma (Plasma 6)**: KWin rules, Wayland vs. X11 issues, and desktop portal configurations.
- **Hyprland**: Dotfile management (`hyprland.conf`), Waybar, Hyprpaper, and swaync.
- **Screen Sharing**: Pipewire and Wireplumber troubleshooting for Wayland environments.

### 3. Performance Tuning
- **GAMEMODE**: Ensuring `gamemoded` and performance profiles are active.
- **Latency**: Optimizing system responsiveness for high-refresh-rate displays.

## Common Workflows

### System Update Failures
1.  Check `/var/lib/pacman/db.lck`.
2.  Refresh mirrors: `sudo cachyos-rate-mirrors`.
3.  Check for manual interventions on [Arch News](https://archlinux.org/news/) or CachyOS forums.

### Wayland/Hyprland Display Issues
1.  Verify `xdg-desktop-portal-hyprland` is running.
2.  Check Hyprland logs: `hyprctl instances` then `cat /tmp/hypr/$instance/hyprland.log`.
3.  Verify GPU drivers (`nvidia-dkms` or `mesa`).

## Useful Scripts
- `scripts/sysinfo.sh`: Gathers critical hardware and software version info for troubleshooting.

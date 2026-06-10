---
name: homelab-architect
description: Architectural guidance for building and managing a homelab. Covers networking (reverse proxies, VPNs), containerization (Docker, Podman), and self-hosting services (Nextcloud, Home Assistant).
---

# Homelab Architect

This skill provides expert advice for planning, deploying, and maintaining a self-hosted homelab environment.

## Design Philosophy
- **Reliability**: Backups, UPS, and uptime monitoring.
- **Security**: SSH hardening, reverse proxies, and VLAN isolation.
- **Efficiency**: Containerization over VMs when possible.

## Core Infrastructure

### 1. Networking
- **Reverse Proxy**: Setting up Nginx Proxy Manager, Caddy, or Traefik.
- **Remote Access**: Tailscale, WireGuard, and Cloudflare Tunnels.
- **DNS**: Pi-hole, AdGuard Home, and local DNS overrides.

### 2. Containerization
- **Docker/Podman**: Best practices for `docker-compose.yml`, volumes, and networking.
- **Monitoring**: Prometheus, Grafana, and Uptime Kuma.
- **Management**: Portainer or Dockge for visual orchestration.

### 3. Self-Hosted Services
- **Storage**: TrueNAS, Unraid, and ZFS datasets.
- **Automation**: Home Assistant and Zigbee2MQTT.
- **Media**: Jellyfin, Plex, and the *arr suite (Radarr, Sonarr).

## Common Workflows

### Deploying a New Service
1.  Verify ports are available.
2.  Define a Docker Compose file.
3.  Set up reverse proxy and SSL (Let's Encrypt).
4.  Configure internal DNS.

### Backup Strategy (3-2-1)
1.  3 copies of data (Live, Local Backup, Offsite).
2.  2 different media types.
3.  1 copy offsite.

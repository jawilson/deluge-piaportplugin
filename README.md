# deluge-piaportplugin

This is a simple plugin for [Deluge](https://www.deluge-torrent.org/) that's meant to be used with [Gluetun](https://github.com/qdm12/gluetun).

Getting VPN port forwarding set up when using containers can be a pain since the port number is dynamic. This plugin automatically updates the incoming port for Deluge based on the current forwarded port.

## Usage

1. Download a recent version from [releases](https://github.com/jawilson/deluge-piaportplugin/releases).
2. Add to Deluge by going to Preferences -> Plugins -> Install.
3. Create a file called `forwarded_port` containing a port number and mount it under `/pia` in the Deluge container (so full path should be `/pia/forwarded_port`).

	When using Docker Compose, this can be accomplished with:

	```yaml
	vpn:
	   image: qmcgaw/gluetun:latest
	   ...
	   environment:
	     ...
	     PORT_FORWARDING: 'on'
	     PORT_FORWARDING_STATUS_FILE: "/gluetun/forwarded_port"
	   volumes:
	     - ./gluetun:/gluetun

	deluge:
	    image: ghcr.io/linuxserver/deluge:latest
	    ...
	    volumes:
	      ...
	      - ./gluetun:/pia:ro
	```

4. Make sure you're using a VPN region that supports port forwarding. Here's [a list for PIA](https://www.privateinternetaccess.com/pages/client-support/#portforward).


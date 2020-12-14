# ZTP Config Push and Upgrade

Unlike examples 1 and 2 where switch configuration is served directly to the switch (statically generated in example1 and dinamically generated in example2), this example serves instead the provided bash script (upgandconfig.sh) to the switch (same script to all switches). So the switch downloads the script and executes it resulting in the switch getting its configuration and upgrading/downgrading EOS to the desired version. 

The point here is that the downloaded script runs in the switch.

In this example the flow is:
1. Switches in ZTP mode make DHCP requests
2. DHCP server running the provided configuration (dhcp.conf.lab3) serves the same Bootfilename URL to all switches pointing to the provided script (upgandconfig.sh)
3. The switch downloads the script and executes it. Please, note that is the switch itself who executes the downloaded script, so script execution takes place in the switch and not in the host serving the script. The script itself is just served by the nginx webserver running the provided nginx.conf configuration
4. The downloaded script contains `#!/bin/bash` shebang so it will be interpreted with /bin/bash. The script leverages `FastCli` to run EOS commands from inside the bash script to get switch's current version and switch's SystemMac
5. By calling the exact same URL that generates the dynamic switch configs detailed in Example2 (and thus passing the SystemMAC obtained in previous step in the curl request) the switch gets its config from the dynconfig Python Flask program and writes it to its startup-config
6. The switch compares the switch's current version against the desired one. If different, the switch downloads the desired EOS version from the given URL writing it to flash: and with a given name. Finally it configures the switch to boot system flash from it

This is how the switch downloads the upgandconfig.sh script served by nginx
![script image](https://github.com/aristaiberia/automation101/blob/main/day1_ztp/example3_config_push_and_upgrade/images/script.png)

The command `/bin/FastCli -p 15 -c "copy $TARGET_URL flash:$TARGET_FILENAME"` in the script makes the switch download the desired EOS version (if different than current). Truncated output as it is a large response with EOS swi image.
![swi image](https://github.com/aristaiberia/automation101/blob/main/day1_ztp/example3_config_push_and_upgrade/images/swi.png)

Due to `/bin/curl -o "/mnt/flash/startup-config" -H "X-Arista-SystemMAC: $SYSTEMMAC" $CONFIG_URL` command in the script this is how the switch downloads it's configuration. Note that the script does not need to pass the rest of X-Arista-* http headers. Example2 shows how the config is dynamically generated.
![config image](https://github.com/aristaiberia/automation101/blob/main/day1_ztp/example3_config_push_and_upgrade/images/config.png)

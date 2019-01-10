#!/bin/bash
for ((;;)); do
    printf "Copying at "
    date
    rm -rf /tmp/Usage
    cp -r /Library/Application\ Support/JAMF/Usage /tmp/
    chown -R boesene /tmp/Usage
    chmod -R u=rwX,go=rX /tmp/Usage
    cp -rp /tmp/Usage ~boesene/src/jamfanalysis/
    sleep 200
done

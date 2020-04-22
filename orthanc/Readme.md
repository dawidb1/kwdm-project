# Orthanc server

## Quick Start

Copy config.json folder with Orhanc installed

Open this folder in CMD

Run `Orhanc.exe config.json`

Download http://nginx.org/en/download.html , version for windows 	nginx/Windows-1.17.10  
Unpack it
Replace nginx.conf in folder /conf (with file from this repo)
Open cmd in nginx folder, type start nginx
Open browser and go to localhost, if there is text: 'Welcome to nginx!' everything is working fine
http://localhost/orthanc is the address of our orthanc server

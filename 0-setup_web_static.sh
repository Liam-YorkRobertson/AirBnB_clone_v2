#!/usr/bin/env bash
# Setup a web servers for the deployment of web_static.
sudo apt-get -y update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Test</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart

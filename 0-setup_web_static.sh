#!/usr/bin/env bash
# preparing a web server for the deployment of web_static.
if ! dpkg -l | grep -q nginx; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate symbolic link
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
config_content="location /hbnb_static {
    alias /data/web_static/current/;
    index index.html;
}"

# Check if the configuration content is already in the file
if ! grep -q "$config_content" "$config_file"; then
    sudo sed -i "/location \/ {/a $config_content" "$config_file"
fi

# Restart Nginx
sudo service nginx restart

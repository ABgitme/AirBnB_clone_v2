#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.
# Install nginx if not already installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get install -y nginx
fi
sudo ufw allow 'Nginx HTTP'
# Create necessary folders if they don't exist
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/{releases/test/,shared/}
sudo touch /data/web_static/releases/test/index.html
# Create a fake HTML file for testing
sudo echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Remove existing symbolic link and create new one
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership of /data folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart nginx
sudo service nginx restart


# Setting up the web server with puppet
exec { 'Nginx setup':
command => 'sudo apt-get -y update;
sudo apt-get -y install nginx;
mkdir -p /data/web_static/shared/;
mkdir -p /data/web_static/releases/test/;
echo "Holberton" > /data/web_static/releases/test/index.html;
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current;
sudo chown -R ubuntu: /data/;
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /usr/share/nginx/html;
    index  index.html index.htm;
    location /hbnb_static {
    	alias /data/web_static/current;
    	index  index.html index.htm;
    }

    location /redirect_me {
        return 301 http://youtube.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /usr/share/nginx/html;
      internal;
    }
}" > /etc/nginx/sites-available/default;
sudo service nginx restart;
',
provider   => 'shell',
}

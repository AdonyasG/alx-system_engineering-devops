# Installs a Nginx server
exec {'install':
provider => shell,
command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee s/usr/share/nginx/html/index.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/AdonyasG permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}

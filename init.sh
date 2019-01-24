  git clone https://Shadowrise:Zona4567@github.com/Shadowrise/web.git /home/box/web
  sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
  sudo rm -rf /etc/nginx/sites-enabled/default
  sudo /etc/init.d/nginx restart
  sudo cd /home/box/web/ask
  sudo python manage.py runserver 0.0.0.0:80000 

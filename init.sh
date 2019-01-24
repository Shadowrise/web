  sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
  sudo rm -rf /etc/nginx/sites-enabled/default
  sudo /etc/init.d/nginx restart
  sudo python /home/box/web/ask/manage.py runserver 0.0.0.0:8000

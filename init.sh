  sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
  sudo rm -rf /etc/nginx/sites-enabled/default
  sudo /etc/init.d/nginx restart
  sudo /etc/init.d/mysql restart
  sudo mysql -u root < /home/box/web/init.sql
  #sudo python /home/box/web/ask/manage.py runserver 0.0.0.0:8000
  sudo python /home/box/web/ask/manage.py makemigrations
  sudo python /home/box/web/ask/manage.py migrate

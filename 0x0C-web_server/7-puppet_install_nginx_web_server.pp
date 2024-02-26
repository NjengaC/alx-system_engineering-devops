# Manifest gets updates, install and configure Nginx as rquired

package { 'nginx':
  ensure => 'installed'
}

file { 'var/www/html/index.html':
  path => '/var/www/html/index.html',
  content => 'Hello World!',
}

exec { 'ufw':
  command => "sudo ufw allow 'Nginx HTTP'",
  provider => 'shell'
}

exec { 'redirection':
  command  => "sudo sed -i '/listen 80 default_server/a rewrite ^/redirect_me /var/www/html/index.html permanent;' /etc/nginx/sites-available/default",
  provider => 'shell'
}

exec { '404':
  command => 'echo "Ceci n\'est pas une page"',
  provider => 'shell'
}

file_line { 'add_custom_error_page':
  path  => '/etc/nginx/sites-available/default',
  line  => '        error_page 404 /custom_404.html;',
  after => 'index index.html index.htm index.nginx-debian.html;',
  match => '^index.nginx-debian.html;$'
}

exec { 'restart nginx':
  command  => 'sudo service nginx restart',
  provider => 'shell'
}

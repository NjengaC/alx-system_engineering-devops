# Manifest automates Fixing Apache returning a 500 error

exec { 'fix-wordpress':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => 'shell'
}

#Creating a file in /tmp
file { 'school':
  path    => '/tmp/school',
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  mode    => '0744'
  }

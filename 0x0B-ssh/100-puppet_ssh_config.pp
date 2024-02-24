#Manifest setup client SSH config file ...without a password
file { '/home/cyrus/.ssh/config':
  ensure  => file,
  mode    => '0600',
  content => "\
Host ubuntu
    HostName ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no\n",
}

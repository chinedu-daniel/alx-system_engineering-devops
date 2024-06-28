# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'fix-for-nginx':
  command     => 'sudo sed -i "s/^ULIMIT.*/ULIMIT=4096/" /etc/default/nginx',
  path        => ['/bin', '/usr/bin'],
  logoutput   => true,
  refreshonly => true,
}

# Restart Nginx
exec { 'nginx-restart':
  command     => 'sudo systemctl restart nginx.service',
  path        => ['/bin', '/usr/bin'],
  logoutput   => true,
  refreshonly => true,
  subscribe   => Exec['fix-for-nginx'],
}


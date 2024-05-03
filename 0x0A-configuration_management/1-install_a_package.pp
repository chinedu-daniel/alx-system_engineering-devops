# Puppet manifest to install Flask version 2.1.0 using pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => '/usr/bin',
  environment => ['PATH=/usr/bin'],
  unless      => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  require     => Package['python3-pip'],
}

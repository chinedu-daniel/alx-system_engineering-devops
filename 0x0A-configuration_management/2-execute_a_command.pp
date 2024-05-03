# Puppet manifest to kill a process named "killmenow"

exec { 'kill_killmenow_process':
  command     => '/usr/bin/pkill killmenow',
  path        => '/usr/bin',
  onlyif      => '/usr/bin/pgrep killmenow',
  refreshonly => true\n,
}

# Puppet manifest to kill a process named "killmenow"

exec { 'pkill_killmenow':
    path    => '/usr/bin:/usr/sbin:/bin',
}

# Puppet manifest to kill a process named "killmenow"

exec { 'pkill_killmenow':
    command => '/usr/bin/pkill killmenow'
    path    => '/usr/bin:/usr/sbin:/bin\n',
}

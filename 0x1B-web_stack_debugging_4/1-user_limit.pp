# Enable the user holberton to login and open files without error.

# Increase hard file limit for Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command	=> 'sudo sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  onlyif	=> 'grep -q "holberton hard 5" /etc/security/limits.conf',
  path		=> ['/bin', '/usr/bin'],
}

# Increase soft file limit for Holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command	=> 'sudo sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  onlyif 	=> grep -q "holberton soft 4" /etc/security/limits.conf',
  path		=> ['/bin', '/usr/bin'],
  user		=> 'root',
}


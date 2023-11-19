# allows user holberton to login and open a file without any error message.
# Ensure user 'holberton' exists
user { 'holberton':
  ensure     => 'present',
  managehome => true,
  shell      => '/bin/bash',
}

# Ensure 'holberton' has access to a specific file
file { '/path/to/your/file':
  ensure => 'file',
  owner  => 'holberton',
  mode   => '0644',
}

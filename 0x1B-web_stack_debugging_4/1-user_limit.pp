# allows user holberton to login and open a file without any error message.
exec { 'set_file_limit':
    command => 'ulimit -n 65535',
    path    => ['/bin', '/usr/bin'],
    user    => 'holberton',
    environment => 'HOME=/home/holberton',
    onlyif  => 'test $(ulimit -n) -lt 65535',
}

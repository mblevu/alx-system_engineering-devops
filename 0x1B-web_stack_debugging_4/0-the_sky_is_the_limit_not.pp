# fixing request issue on server
# Install Apache
package { 'apache2':
    ensure => 'installed',
}

# Configure Apache
file { '/etc/apache2/mods-available/mpm_prefork.conf':
    ensure  => 'file',
    content => "StartServers             5\n" +
                          "MinSpareServers          5\n" +
                          "MaxSpareServers          10\n" +
                          "MaxRequestWorkers        100\n" +
                          "MaxConnectionsPerChild   0\n",
    notify  => Service['apache2'],
}

# Enable and start Apache service
service { 'apache2':
    ensure    => 'running',
    enable    => true,
    subscribe => File['/etc/apache2/mods-available/mpm_prefork.conf'],
}

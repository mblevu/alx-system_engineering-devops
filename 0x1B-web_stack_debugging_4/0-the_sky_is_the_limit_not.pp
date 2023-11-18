# fixing request issue on server
# Install Apache
package { 'apache2':
    ensure => 'installed',
}

# Configure Apache
file { '/etc/apache2/mods-available/mpm_prefork.conf':
    ensure  => 'file',
    content => "StartServers             5
                MinSpareServers          5
                MaxSpareServers          10
                MaxRequestWorkers        100
                MaxConnectionsPerChild   0",
    notify  => Service['apache2'],
}

# Enable and start Apache service
service { 'apache2':
    ensure    => 'running',
    enable    => true,
    subscribe => File['/etc/apache2/mods-available/mpm_prefork.conf'],
}

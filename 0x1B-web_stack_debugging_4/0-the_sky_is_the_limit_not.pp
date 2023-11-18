# fixing request issue on server
# Install Apache
package { 'apache2':
    ensure => 'installed',
}

# Ensure the directory exists
file { '/etc/apache2/mods-available':
    ensure => 'directory',
}

# Configure Apache
file { '/etc/apache2/mods-available/mpm_prefork.conf':
    ensure  => 'file',
    content => "StartServers             5
                MinSpareServers          5
                MaxSpareServers          10
                MaxRequestWorkers        100
                MaxConnectionsPerChild   0",
    require => File['/etc/apache2/mods-available'],
    notify  => Service['apache2'],
}

# Enable and start Apache service
service { 'apache2':
    ensure    => 'running',
    require   => File['/etc/apache2/mods-available/mpm_prefork.conf'],
}

exec { 'killmenow_process':
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true,
}

# Notify to run the exec resource immediately
notify { 'killmenow_process':
  require => Exec['killmenow_process'],
}

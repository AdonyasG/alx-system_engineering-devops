# kills a process named killmenow
exec { 'pkill -f':
    command => '/usr/bin/pkill -f killmenow'
}

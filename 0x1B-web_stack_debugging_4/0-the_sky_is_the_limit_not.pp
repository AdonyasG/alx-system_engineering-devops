# this puppet manifest fixes too many open files error
exec { '/etc/default/nginx':
  command => "/bin/echo ULIMIT='-n 5000' > /etc/default/nginx && /usr/bin/sudo\
  service nginx restart"
}

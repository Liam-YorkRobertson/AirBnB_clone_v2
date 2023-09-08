# script that sets up your web servers for the deployment of web_static

file { '/data':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

file { '/data/web_static':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => '<html>
    <head>
    </head>
    <body>
      Test
    </body>
  </html>',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'root',
  group  => 'root',
}

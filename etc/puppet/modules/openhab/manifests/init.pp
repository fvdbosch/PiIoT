class openhab {

  include apt
  include openhab::configuration

  apt::key { 'openhab':
    key_source => 'https://bintray.com/user/downloadSubjectPublicKey?username=openhab',
  } ->

  apt::source { 'openhab':
    location     => 'http://dl.bintray.com/openhab/apt-repo',
    release      => 'stable',
    repos        => 'main',
    include_src  => false,
  } ->

  package { 'openhab-runtime':
    ensure  => 'installed',
  } ~>

  service { 'openhab':
    ensure => 'running',
    enable => true,
  }

}

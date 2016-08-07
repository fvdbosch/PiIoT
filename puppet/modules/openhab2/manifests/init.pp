class openhab2 {

  include apt
  include openhab2::configuration
  include openhab2::mqtt

  apt::key { 'openhab':
    key_source => 'https://bintray.com/user/downloadSubjectPublicKey?username=openhab',
  }

  apt::source { 'openhab':
    location     => 'http://dl.bintray.com/openhab/apt-repo2',
    release      => '2.0.0.b3',
    repos        => 'main',
    include_src  => false,
  } ->

  package { 'openhab2-offline':
    ensure  => 'installed',
  } ~>

  service { 'openhab2':
    ensure => 'running',
    enable => true,
  }

}

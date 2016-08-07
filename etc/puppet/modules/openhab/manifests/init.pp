class openhab (
  $version = 2,
) {

  include apt
  include openhab::configuration

  apt::key { 'openhab':
    key_source => 'https://bintray.com/user/downloadSubjectPublicKey?username=openhab',
  }

  if $version == 2 {
    apt::source { 'openhab':
      location     => 'http://dl.bintray.com/openhab/apt-repo2',
      release      => '2.0.0.b3',
      repos        => 'main',
      include_src  => false,
    } ->

    package { 'openhab2-offline':
      ensure  => 'installed',
    }
  }

  else {
    apt::source { 'openhab':
      location     => 'http://dl.bintray.com/openhab/apt-repo',
      release      => 'stable',
      repos        => 'main',
      include_src  => false,
    } ->

    package { 'openhab-runtime':
      ensure  => 'installed',
    }
  }

  service { 'openhab':
    ensure => 'running',
    enable => true,
  }

}

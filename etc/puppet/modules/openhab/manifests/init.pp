class openhab {

  include apt

  apt::key { 'openhab':
    key_source => 'https://bintray.com/user/downloadSubjectPublicKey?username=openhab',
  }

  apt::source { 'openhab':
    location     => 'http://dl.bintray.com/openhab/apt-repo',
    release      => 'stable',
    repos        => 'main',
    include_src  => false,
  }

  package {
    'openhab-runtime':
      ensure => 'installed';
    'openhab-addon-binding-enocean':
      ensure => 'installed',
      require => Package['openhab-runtime'];
    'openhab-addon-binding-hue':
      ensure => 'installed',
      require => Package['openhab-runtime'];
    'openhab-addon-persistence-mysql':
      ensure => 'installed',
      require => Package['openhab-runtime'];
  }

  File {
    ensure  => 'present',
    require => Package['openhab-runtime'],
  }

  file {
    '/etc/openhab/configurations/openhab.cfg':
      source => 'puppet:///modules/openhab/config';
    '/etc/openhab/configurations/sitemaps/openhab.sitemap':
      source  => 'puppet:///modules/openhab/sitemap';
    '/etc/openhab/configurations/items/openhab.items':
      source  => 'puppet:///modules/openhab/items';
    '/etc/openhab/configurations/rules/openhab.rules':
      source  => 'puppet:///modules/openhab/rules';
    '/etc/openhab/configurations/transform/openhab.transform':
      source  => 'puppet:///modules/openhab/transform';
    '/etc/openhab/configurations/persistence/openhab.persistence':
      source  => 'puppet:///modules/openhab/persistence';
  }
}
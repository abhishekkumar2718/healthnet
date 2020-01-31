VAGRANTFILE_API_VERSION = 2
VAGRANT_BOX = 'generic/ubuntu1804'
VM_NAME = 'healthnet'
VM_USER = 'vagrant'
HOST_USER = 'abhishek'
HOME = '/home/' + VM_USER
GUEST_PATH = HOME + '/' + 'healthnet'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = VAGRANT_BOX
  config.vm.hostname = VM_NAME

  config.vm.provider 'virtualbox' do |v|
    v.name = VM_NAME
    v.memory = 4*1024
  end

  config.vm.network 'forwarded_port', guest: 8000, host: 8000
  config.vm.synced_folder '.', GUEST_PATH

  config.vm.provision 'shell', inline: <<~SHELL
  apt-get -y update
  DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade

  apt-get -y install python3-pip
  pip3 install --user pipenv
  cd #{GUEST_PATH}
  pipenv install django
  SHELL
end

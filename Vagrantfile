# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.hostname = "vagrant-school-dairy"
    config.vm.network "private_network", ip: "192.168.160.10"

    config.vm.provider "virtualbox" do |v|
        v.memory = 500
        v.cpus = 1
    end

end

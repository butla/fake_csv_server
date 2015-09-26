# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
sudo apt-get update
sudo apt-get install -y python3-pip
sudo pip3 install -r /vagrant/requirements.txt
python3 /vagrant/fake_csv_server/app.py &
SCRIPT

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.network "forwarded_port", guest: 9090, host: 9090

  config.vm.provision "shell", inline: $script

  config.vm.provider "virtualbox" do |v|
    v.memory = 1536
    v.cpus = 2
  end
end

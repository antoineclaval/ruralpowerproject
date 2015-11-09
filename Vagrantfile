$setup = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get update
SCRIPT

$dependencies = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql libpq-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-dev libjpeg-dev zlib1g-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-virtualenv virtualenvwrapper
SCRIPT

Vagrant.configure('2') do |config|

    config.vm.box = 'precise64'
    config.vm.box_url = "http://files.vagrantup.com/" + config.vm.box + ".box"

    #config.ssh.forward_agent = true
    # Forward the dev server port
    #config.vm.network : forwarded_port, guest:8000, guest_ip:"127.0.0.1", host:4210 , host_ip:"127.0.0.1"
    #config.vm.network :forwarded_port, host: 4567, guest: 8000
    #config.vm.network :forwarded_port, host: 5434, guest: 5433

    config.vm.network "private_network", ip: "192.168.50.4"

    config.vm.provision "shell", inline: "echo well, hi!"
    config.vm.provision "shell", inline: $setup
    config.vm.provision "shell", inline: $dependencies
end

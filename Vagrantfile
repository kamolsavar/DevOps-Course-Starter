# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.network "forwarded_port", guest: 5000, host: 8080
  # config.vm.network "forwarded_port", guest: 5000, host: 5000 
  

  config.vm.provider "virtualbox" do |vb|
      # Display the VirtualBox GUI when booting the machine
      vb.memory = "2048"
      vb.cpus = 4
    end
  
  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    sudo apt-get update;
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git python-openssl
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
    echo 'eval "$(pyenv init --path)"' >> ~/.profile
    source ~/.profile
    CFLAGS=-I/usr/include/openssl \
    LDFLAGS=-L/usr/lib64 \
    pyenv install -v 3.5.1
    pyenv global 3.5.1
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
  SHELL
  
  config.trigger.after :up do |trigger|
    trigger.name = "Launching App"
    trigger.info = "Running the TODO app setup script"
    trigger.run_remote = {privileged: false, inline: "
    # # Install dependencies and launch
    cd /vagrant 
    poetry install
    # poetry run flask run
    nohup poetry run flask run --host 0.0.0.0 > logs.txt 2>&1 &
    "}
  end
end

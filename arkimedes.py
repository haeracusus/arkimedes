import os
#xfce, xarchiver, yay, firefox, neovim, htop, neofetch [!!ABSOLUTELY NECESSARY FOR EVERY INSTALL!!], vlc, pipewire over fartaudio, gvfs, fish shell fastest mirrors
os.system('sudo pacman -S reflector')
os.system('sudo reflector --verbose --sort rate -l 15 -p https --save /etc/pacman.d/mirrorlist')
os.system('sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si && cd')
os.system('sudo pacman -S xfce4 xfce4-goodies xarchiver fish unzip unrar firefox neovim gvfs pipewire pipewire-pulse pipewire-alsa pipewire-jack wireplumber lightdm lightdm-gtk-greeter gvfs')
os.system('systemctl enable lightdm && chsh -s $(which fish)')

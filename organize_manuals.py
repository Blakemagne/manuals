#!/usr/bin/env python3
"""
Intelligent Manual Organizer - Categorize manuals into logical directories
"""

import os
import shutil
from pathlib import Path

# Manual categorization based on functionality
MANUAL_CATEGORIES = {
    'system': {
        'description': 'System Administration & Core Tools',
        'commands': [
            'systemctl', 'systemd', 'service', 'chkconfig', 'init',
            'mount', 'umount', 'fdisk', 'lsblk', 'df', 'du', 'free',
            'ps', 'top', 'htop', 'kill', 'killall', 'pkill', 'pgrep',
            'crontab', 'at', 'batch', 'jobs', 'nohup', 'disown',
            'sudo', 'su', 'passwd', 'chpasswd', 'usermod', 'useradd', 'userdel',
            'chmod', 'chown', 'chgrp', 'umask', 'setfacl', 'getfacl',
            'sysctl', 'ulimit', 'lsof', 'netstat', 'ss', 'iotop', 'iostat',
            'chroot', 'jail', 'systemd-nspawn',
            'dmesg', 'journalctl', 'logger', 'rsyslog', 'syslog',
            'who', 'w', 'last', 'lastlog', 'finger', 'id', 'groups',
            'uptime', 'uname', 'hostname', 'hostnamectl', 'date', 'timedatectl',
            'sync', 'fsck', 'e2fsck', 'tune2fs', 'dumpe2fs', 'resize2fs',
            'parted', 'gparted', 'mkfs', 'mke2fs', 'mkswap', 'swapon', 'swapoff',
            'modprobe', 'lsmod', 'rmmod', 'insmod', 'depmod',
            'systemd-analyze', 'systemd-cgls', 'systemd-cgtop'
        ]
    },
    'files': {
        'description': 'File Operations & Text Processing',
        'commands': [
            'ls', 'find', 'locate', 'which', 'whereis', 'file', 'stat', 'lstat',
            'cp', 'mv', 'rm', 'rmdir', 'mkdir', 'touch', 'ln', 'link', 'unlink',
            'cat', 'less', 'more', 'head', 'tail', 'tee', 'nl', 'pr',
            'grep', 'egrep', 'fgrep', 'rg', 'ripgrep', 'ag', 'ack', 'zgrep',
            'sed', 'awk', 'gawk', 'mawk', 'cut', 'sort', 'uniq', 'wc', 'tr', 'rev',
            'diff', 'patch', 'cmp', 'comm', 'join', 'split', 'csplit',
            'fold', 'fmt', 'expand', 'unexpand', 'column', 'paste',
            'strings', 'od', 'hexdump', 'xxd', 'base64', 'uuencode', 'uudecode',
            'iconv', 'dos2unix', 'unix2dos', 'recode',
            'basename', 'dirname', 'readlink', 'realpath', 'pathchk',
            'shred', 'wipe', 'srm', 'dd', 'ddrescue',
            'rsync', 'scp', 'sftp', 'rcp', 'ftp', 'lftp'
        ]
    },
    'editors': {
        'description': 'Text Editors & IDEs',
        'commands': [
            'vi', 'vim', 'nvim', 'nano', 'emacs', 'ed', 'ex',
            'code', 'atom', 'sublime', 'gedit', 'kate'
        ]
    },
    'network': {
        'description': 'Network Tools & Communication',
        'commands': [
            'ssh', 'ssh-keygen', 'ssh-agent', 'ssh-add', 'ssh-copy-id',
            'telnet', 'nc', 'netcat', 'socat',
            'curl', 'wget', 'lynx', 'w3m',
            'ping', 'traceroute', 'mtr', 'nslookup', 'dig', 'host',
            'iptables', 'ufw', 'firewall-cmd',
            'tcpdump', 'wireshark', 'tshark', 'nmap',
            'mail', 'mutt', 'sendmail', 'postfix'
        ]
    },
    'development': {
        'description': 'Programming & Development Tools',
        'commands': [
            'gcc', 'g++', 'clang', 'make', 'cmake', 'autoconf', 'automake',
            'git', 'svn', 'hg', 'bzr', 'cvs',
            'python', 'python3', 'pip', 'pip3', 'virtualenv', 'conda',
            'node', 'npm', 'yarn', 'nvm',
            'ruby', 'gem', 'rbenv', 'rvm',
            'java', 'javac', 'jar', 'maven', 'gradle',
            'go', 'cargo', 'rustc',
            'docker', 'docker-compose', 'podman',
            'vagrant', 'ansible', 'terraform',
            'gdb', 'lldb', 'strace', 'ltrace', 'valgrind'
        ]
    },
    'shell': {
        'description': 'Shell & Terminal Tools',
        'commands': [
            'bash', 'sh', 'zsh', 'fish', 'csh', 'tcsh', 'ksh',
            'tmux', 'screen', 'byobu',
            'history', 'fc', 'alias', 'unalias', 'which',
            'export', 'env', 'printenv', 'set', 'unset',
            'cd', 'pwd', 'pushd', 'popd', 'dirs',
            'echo', 'printf', 'read', 'test', 'expr',
            'xargs', 'parallel'
        ]
    },
    'archive': {
        'description': 'Compression & Archive Tools',
        'commands': [
            'tar', 'gtar', 'star', 'pax', 'cpio',
            'gzip', 'gunzip', 'zcat', 'zless', 'zgrep', 'gzexe',
            'bzip2', 'bunzip2', 'bzcat', 'bzless', 'bzgrep',
            'xz', 'unxz', 'xzcat', 'xzless', 'xzgrep', 'lzma', 'unlzma',
            'zip', 'unzip', 'zipinfo', 'zipgrep', 'zipnote', 'zipsplit',
            'rar', 'unrar', '7z', '7za', '7zr',
            'compress', 'uncompress', 'zcat', 'pack', 'unpack',
            'ar', 'ranlib', 'nm', 'objdump', 'objcopy', 'strip'
        ]
    },
    'media': {
        'description': 'Media & Graphics Tools',
        'commands': [
            'ffmpeg', 'ffplay', 'ffprobe', 'mencoder', 'mplayer', 'vlc',
            'imagemagick', 'convert', 'identify', 'mogrify', 'montage', 'composite',
            'gimp', 'inkscape', 'blender', 'gthumb', 'eog', 'feh', 'gpicview',
            'sox', 'aplay', 'arecord', 'pulseaudio', 'alsamixer', 'amixer',
            'audacity', 'lame', 'flac', 'oggenc', 'mpg123', 'ogg123'
        ]
    },
    'documentation': {
        'description': 'Documentation & Help Systems',
        'commands': [
            'man', 'info', 'apropos', 'whatis', 'makewhatis', 'catman',
            'help', 'pinfo', 'tkinfo', 'xman', 'yelp',
            'texi2dvi', 'texi2pdf', 'makeinfo', 'install-info',
            'groff', 'nroff', 'troff', 'tbl', 'eqn', 'pic', 'refer',
            'pandoc', 'asciidoc', 'a2x', 'rst2html', 'markdown'
        ]
    },
    'security': {
        'description': 'Security & Encryption Tools',
        'commands': [
            'gpg', 'gpg2', 'pgp', 'openssl', 'ssh-keygen', 'ssh-agent', 'ssh-add',
            'chage', 'pwck', 'grpck', 'newgrp', 'sg', 'gpasswd',
            'selinux', 'sestatus', 'setsebool', 'getsebool', 'semanage',
            'apparmor', 'aa-status', 'aa-enforce', 'aa-complain',
            'iptables', 'ip6tables', 'ufw', 'firewall-cmd', 'nftables',
            'fail2ban', 'denyhosts', 'logwatch', 'tripwire', 'aide',
            'lynis', 'rkhunter', 'chkrootkit', 'clamav', 'freshclam'
        ]
    },
    'database': {
        'description': 'Database Tools',
        'commands': [
            'mysql', 'mysqldump', 'mysqladmin', 'mysqlcheck', 'mysqlimport',
            'postgresql', 'psql', 'pg_dump', 'pg_restore', 'createdb', 'dropdb',
            'sqlite3', 'sqlite', 'redis-cli', 'redis-server',
            'mongo', 'mongod', 'mongodump', 'mongorestore',
            'influxdb', 'influx', 'grafana', 'prometheus'
        ]
    },
    'monitoring': {
        'description': 'System Monitoring & Performance',
        'commands': [
            'htop', 'atop', 'iotop', 'iftop', 'nethogs', 'nload',
            'vmstat', 'iostat', 'mpstat', 'sar', 'pidstat',
            'strace', 'ltrace', 'ftrace', 'perf', 'systemtap',
            'tcpdump', 'wireshark', 'tshark', 'ngrep', 'tcpflow',
            'nagios', 'icinga', 'zabbix', 'munin', 'cacti',
            'collectd', 'statsd', 'ganglia', 'mrtg'
        ]
    },
    'virtualization': {
        'description': 'Virtualization & Containers',
        'commands': [
            'docker', 'docker-compose', 'podman', 'buildah', 'skopeo',
            'kubernetes', 'kubectl', 'helm', 'minikube', 'kind',
            'vagrant', 'packer', 'terraform', 'ansible', 'puppet', 'chef',
            'lxc', 'lxd', 'systemd-nspawn', 'chroot', 'unshare',
            'qemu', 'kvm', 'virt-manager', 'virsh', 'vbox', 'vmware',
            'xen', 'xl', 'xm', 'xentop'
        ]
    },
    'package': {
        'description': 'Package Management',
        'commands': [
            'apt', 'apt-get', 'apt-cache', 'aptitude', 'dpkg', 'dpkg-query',
            'yum', 'dnf', 'rpm', 'rpm2cpio', 'rpmquery', 'rpmverify',
            'zypper', 'pacman', 'makepkg', 'yay', 'paru',
            'emerge', 'ebuild', 'equery', 'eix', 'layman',
            'pkg', 'pkg_add', 'pkg_delete', 'pkg_info',
            'brew', 'port', 'nix', 'guix', 'snap', 'flatpak', 'appimage'
        ]
    }
}

def categorize_manual(filename):
    """Determine which category a manual belongs to"""
    # Extract command name from filename
    if filename.startswith('sexy_'):
        command = filename[5:]  # Remove 'sexy_' prefix
    else:
        command = filename
    
    # Remove file extension
    command = command.replace('.html', '').replace('.md', '')
    
    # Check each category
    for category, data in MANUAL_CATEGORIES.items():
        if command in data['commands']:
            return category
    
    # Default category for uncategorized manuals
    return 'misc'

def create_category_index(category, commands, description):
    """Create an index page for a category"""
    content = f"""# {description}

> *{description} documentation*

## Available Manuals

"""
    
    for cmd in sorted(commands):
        title = cmd.upper()
        content += f"- [📚 {title}](./{cmd}.html) - {cmd} manual\n"
    
    content += f"""

---

[🏠 Back to Home](../index.html)

*Part of the Sexy Shell Manuals collection*
"""
    
    return content

def organize_manuals():
    """Organize all markdown files in public/content/ into categorized directories"""
    content_dir = Path("public/content")
    if not content_dir.exists():
        print("❌ Error: public/content/ directory not found!")
        return
    
    print("📁 Organizing manuals into categories...")
    
    # Track which files go where
    categorized_files = {}
    category_commands = {cat: [] for cat in MANUAL_CATEGORIES.keys()}
    category_commands['misc'] = []
    
    # Categorize all markdown files
    for md_file in content_dir.glob("*.md"):
        if md_file.name == "index.md":
            continue
            
        category = categorize_manual(md_file.name)
        if category not in categorized_files:
            categorized_files[category] = []
        categorized_files[category].append(md_file)
        
        # Track command name for index
        if md_file.name.startswith('sexy_'):
            cmd_name = md_file.name[5:].replace('.md', '')
        else:
            cmd_name = md_file.name.replace('.md', '')
        category_commands[category].append(cmd_name)
    
    # Create category directories and organize files
    for category, files in categorized_files.items():
        category_dir = content_dir / category
        category_dir.mkdir(exist_ok=True)
        
        print(f"📂 Creating {category}/ with {len(files)} manuals")
        
        # Move files to category directory
        for file in files:
            new_path = category_dir / file.name
            shutil.move(str(file), str(new_path))
        
        # Create category index
        if category in MANUAL_CATEGORIES:
            description = MANUAL_CATEGORIES[category]['description']
        else:
            description = "Miscellaneous Tools"
            
        index_content = create_category_index(category, category_commands[category], description)
        
        # Write category index as markdown first
        index_md = category_dir / "index.md"
        with open(index_md, 'w') as f:
            f.write(index_content)
    
    # Update main index to link to categories
    update_main_index(categorized_files)
    
    print("✅ Organization complete!")
    print(f"📊 Created {len(categorized_files)} categories")
    
    return categorized_files

def update_main_index(categorized_files):
    """Update the main index to link to category directories"""
    main_index_md = Path("public/content/index.md")
    
    if not main_index_md.exists():
        print("⚠️  Warning: main index.md not found, skipping update")
        return
    
    # Create new organized index content with simple markdown
    content = """# Sexy Shell Manuals

Beautiful, readable documentation for command-line tools organized by category.

Making shell documentation sexy, one manual at a time.

## Browse by Category

"""
    
    # Add category links (simple markdown that works with the parser)
    for category, files in sorted(categorized_files.items()):
        if category in MANUAL_CATEGORIES:
            description = MANUAL_CATEGORIES[category]['description']
            icon = {
                'system': '⚙️',
                'files': '📁', 
                'editors': '✏️',
                'network': '🌐',
                'development': '💻',
                'shell': '🐚',
                'archive': '📦',
                'media': '🎬',
                'documentation': '📖',
                'security': '🔒',
                'database': '🗄️',
                'monitoring': '📊',
                'virtualization': '🐳',
                'package': '📦'
            }.get(category, '📚')
        else:
            description = "Miscellaneous Tools"
            icon = '📚'
            
        content += f"### {icon} [{description}](./{category}/index.html)\n"
        content += f"*{len(files)} manuals available*\n\n"
    
    content += f"""---

**📋 {sum(len(files) for files in categorized_files.values())} manuals available!**

## About This Project

Transform boring Unix/Linux manual pages into beautiful, readable documentation with enhanced formatting, better navigation, and modern styling.

## How It Works

We take traditional manual pages and make them sexy:

1. **Steal** a manual page using fip/fop
2. **Format** to enhanced markdown with our sexy formatter  
3. **Generate** beautiful HTML with our static site generator
4. **Organize** into logical categories for easy browsing

No more ugly, hard-to-navigate shell manuals!

## Features

- 🎨 **Vercel-inspired design** - Modern, clean interface
- 🌙 **Dark theme optimized** for readability
- 📱 **Mobile-responsive** - Beautiful on any device
- ⚡ **Fast, lightweight** pages
- 🔗 **Smart cross-references** - Manual links that actually work
- 🏠 **Easy navigation** - Home button on every page
- 📁 **Intelligent categorization** by functionality

---

*This site was generated from markdown using a custom static site generator.*
"""
    
    # Write updated index
    with open(main_index_md, 'w') as f:
        f.write(content)
    
    print("✅ Updated main index with category links")

def main():
    """Run the organization process"""
    organize_manuals()
    
    print("\n🔄 Next steps:")
    print("1. cd public && python3 src/main.py  # Regenerate HTML with categories")
    print("2. git add docs/ && git commit -m 'Organize manuals by category'")

if __name__ == "__main__":
    main()
#wsl 每次启动后  ifconfig的ip都会变化  window每次都要做一次端口映射172.25.83.93
netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=22 connectaddress=172.25.83.93 connectport=22


#wsl 每次启动后  ifconfig的ip都会变化  window每次都要做一次端口映射172.25.83.93
#!/usr/bin/bash
# 为 win 设置 wsl host
# win hosts 文件路径
win_hosts_path="/mnt/c/Windows/System32/drivers/etc/hosts"
# 为 wsl2 设置的域名
wsl_domain="wzq.com"
# 获取 wsl2 的 ip
wsl_ip=$(ifconfig eth0 | grep -w inet | awk '{print $2}')
# 判断是否已存在 wsl2 的域名，如果存在则修改，否则追加
if grep -wq "$wsl_domain" $win_hosts_path
then
    # 此处因为权限问题没有直接用 sed 修改 hosts 文件
        win_hosts=$(sed -s "s/.* $wsl_domain/$wsl_ip $wsl_domain/g" $win_hosts_path)
        echo "$win_hosts" > $win_hosts_path
    else
        echo "$wsl_ip $wsl_domain" >> $win_hosts_path
fisudo service ssh --full-restart

Host wzq.com
  HostName wzq.com
  User wzq
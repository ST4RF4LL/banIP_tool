#banIP_Tool
# Description
今天看到搭酸酸乳的vps有24W+的登录失败次数，我寻思着vultr自动生成的密码我自己都记不住,理论上应该是爆破不出来的  
但是出于**尊重一下**的想法，决定把这几个沙雕IP给ban了，网上找了一下方法，搞了一下但是又有一点嫌麻烦，决定自己写一个自动化脚本。

# Details
暂时先实现一下基本的功能，实现一个半自动化。
## 原理
从lastb中获取IP并进行处理，再写入`/etc/hosts.deny`.
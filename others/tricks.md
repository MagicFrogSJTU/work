macOS 关闭滚动加速
```
# 关闭滚轮加速度（线性滚动）
defaults write -g com.apple.scrollwheel.scaling -float 1.0
defaults write -g com.apple.scrollwheel.acceleration -float 0

# 重启系统偏好进程（不用重启电脑）
killall cfprefsd
```
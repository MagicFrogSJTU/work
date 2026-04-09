
网络服务器禁止生成.DS_store
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true
killall Finder
```


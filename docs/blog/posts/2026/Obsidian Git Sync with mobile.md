---
date: 2026-10-27
---
* Obsidian: enable community plugins, add the Git ("by Vinzent") community plugin and configure it
* `echo .obsidian/ >> .gitignore` (a more finegrained exclude might be possible here, to have some of your settings in sync, but I am too busy for testing that at the moment)
* on your desktop system, copy the whole repository workspace and change the remote from ssh to https
* create a fine grained personal github token to access the repo
* create a zip from that copy and transfer it to your mobile
* on your mobile, unzip, open that vault in obsidian, configure the git community plugin - it will ask for your token
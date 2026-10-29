---
date: 
  created: 2026-10-25
  updated: 2026-10-28
categories:
  - misc
---

Read here how to:

* mobile usage of obsidian-git plugin using a token
* mobile git repo sync with a separate GitSync app (Andoird and iOS)

<!-- more -->

## mobile usage of obsidian-git plugin
* **ATTENTION!** The Git Plugin is unstable on mobile devices. If your workflow breaks, look [here](https://github.com/Vinzent03/obsidian-git#mobile-support-experimental) for mentioned alternatives, for example [GitSync](https://github.com/ViscousPot/GitSync) App for Android ans iOS.
* Obsidian: enable community plugins, add the Git ("by Vinzent") community plugin and configure it
* `echo .obsidian/ >> .gitignore` (a more finegrained exclude might be possible here, to have some of your settings in sync, but I am too busy for testing that at the moment)
* on your desktop system, copy the whole repository workspace and change the remote from ssh to https
* create a fine grained personal github token to access the repo
* create a zip from that copy and transfer it to your mobile
* on your mobile, unzip, open that vault in obsidian, configure the git community plugin - it will ask for your token

## mobile sync with GitSync app
* sync on opening and closing the obsidian app
* add the entry `**/.obsidian/community-plugins.json` to `.git/info/exclude` on Mobile (via the GitSync App)
* this way you can sync all plugin settings, you only have to enable and disable the plugins on your mobile
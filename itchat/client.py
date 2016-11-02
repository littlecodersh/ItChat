



<!DOCTYPE html>
<html lang="en" class=" is-copy-enabled emoji-size-boost is-u2f-enabled">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-9ad495a7b5d4473ee5031bc7b3e2d60090320bca47a10a6fa472132f678b6160.css" integrity="sha256-mtSVp7XURz7lAxvHs+LWAJAyC8pHoQpvpHITL2eLYWA=" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-3ca4d5a0760c7ca10f98748867f95c64b034bd809a90302ab1caf3adf1b7845c.css" integrity="sha256-PKTVoHYMfKEPmHSIZ/lcZLA0vYCakDAqscrzrfG3hFw=" media="all" rel="stylesheet" />
    
    
    
    

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=device-width">
    
    <title>ItChat/client.py at master · littlecodersh/ItChat</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="/apple-touch-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="/apple-touch-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="/apple-touch-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="/apple-touch-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon-180x180.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="https://avatars3.githubusercontent.com/u/13028340?v=3&amp;s=400" name="twitter:image:src" /><meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="littlecodersh/ItChat" name="twitter:title" /><meta content="ItChat - A complete and graceful API for Wechat. 微信个人号接口（支持文件、图片上下载）、微信机器人及命令行微信。三十行即可自定义个人号机器人。" name="twitter:description" />
      <meta content="https://avatars3.githubusercontent.com/u/13028340?v=3&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="littlecodersh/ItChat" property="og:title" /><meta content="https://github.com/littlecodersh/ItChat" property="og:url" /><meta content="ItChat - A complete and graceful API for Wechat. 微信个人号接口（支持文件、图片上下载）、微信机器人及命令行微信。三十行即可自定义个人号机器人。" property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/MTE4MTgxMTQ6MGZjZGE3YTA0OTcxZjZmZGE4YTBlYTEyZTc5Y2M5Mjc6NjM5NDEyMzFlNjdjMGZjZWU5ZGI1MDY3NDUxY2E4MmRkZjc3NzQ0MWFhNjFkOTUzMGNiMjdkMmYzM2NhOGZkZQ==--6d692fbd08c6cfd492ae93cbfd1523f8ad2daa78">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">
    <meta name="request-id" content="68C7A510:74D4:7D017A1:581A02A8" data-pjax-transient>

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="68C7A510:74D4:7D017A1:581A02A8" name="octolytics-dimension-request_id" /><meta content="11818114" name="octolytics-actor-id" /><meta content="WhaleChen" name="octolytics-actor-login" /><meta content="686d42c4322d6dfa67d1105bfd1b485a0eedcd3f6fa615a06bf8cc97e1e435e0" name="octolytics-actor-hash" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />



  <meta class="js-ga-set" name="dimension1" content="Logged In">



        <meta name="hostname" content="github.com">
    <meta name="user-login" content="WhaleChen">

        <meta name="expected-hostname" content="github.com">
      <meta name="js-proxy-site-detection-payload" content="MDJjZjIxNTg5MThkM2I5ZjdhNTQzMDEwOGNmYjQ4YzgzM2Q4MGRhYjA5NTRkMjhhMjNlOThhZTcwY2M3NzU0Nnx7InJlbW90ZV9hZGRyZXNzIjoiMTA0LjE5OS4xNjUuMTYiLCJyZXF1ZXN0X2lkIjoiNjhDN0E1MTA6NzRENDo3RDAxN0ExOjU4MUEwMkE4IiwidGltZXN0YW1wIjoxNDc4MDk5NjI0LCJob3N0IjoiZ2l0aHViLmNvbSJ9">


      <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

    <meta name="html-safe-nonce" content="f8d282aaecc9bd00e5d7021985c2b32f5e73d685">
    <meta content="c0d08379c02b12c504ebed58d592a52b4ddd3f26" name="form-nonce" />

    <meta http-equiv="x-pjax-version" content="f983b7972fc2383d0fabea2ac9a3088f">
    

      
  <meta name="description" content="ItChat - A complete and graceful API for Wechat. 微信个人号接口（支持文件、图片上下载）、微信机器人及命令行微信。三十行即可自定义个人号机器人。">
  <meta name="go-import" content="github.com/littlecodersh/ItChat git https://github.com/littlecodersh/ItChat.git">

  <meta content="13028340" name="octolytics-dimension-user_id" /><meta content="littlecodersh" name="octolytics-dimension-user_login" /><meta content="49935814" name="octolytics-dimension-repository_id" /><meta content="littlecodersh/ItChat" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="49935814" name="octolytics-dimension-repository_network_root_id" /><meta content="littlecodersh/ItChat" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/littlecodersh/ItChat/commits/master.atom" rel="alternate" title="Recent Commits to ItChat:master" type="application/atom+xml">


      <link rel="canonical" href="https://github.com/littlecodersh/ItChat/blob/master/itchat/client.py" data-pjax-transient>
  </head>


  <body class="logged-in  env-production macintosh vis-public page-blob">
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>

    
    
    



        <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg aria-hidden="true" class="octicon octicon-mark-github" height="28" version="1.1" viewBox="0 0 16 16" width="28"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>


        <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/littlecodersh/ItChat/search" class="js-site-search-form" data-scoped-search-url="/littlecodersh/ItChat/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
      <div class="header-search-scope">This repository</div>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
    </label>
</form></div>


      <ul class="header-nav float-left" role="navigation">
        <li class="header-nav-item">
          <a href="/pulls" aria-label="Pull requests you created" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
            Pull requests
</a>        </li>
        <li class="header-nav-item">
          <a href="/issues" aria-label="Issues you created" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
            Issues
</a>        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com/" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
      </ul>

    
<ul class="header-nav user-nav float-right" id="user-links">
  <li class="header-nav-item">
    
    <a href="/notifications" aria-label="You have unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s js-socket-channel js-notification-indicator" data-channel="tenant:1:notification-changed:11818114" data-ga-click="Header, go to notifications, icon:unread" data-hotkey="g n">
        <span class="mail-status unread"></span>
        <svg aria-hidden="true" class="octicon octicon-bell" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"></path></svg>
</a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link tooltipped tooltipped-s js-menu-target" href="/new"
       aria-label="Create new…"
       data-ga-click="Header, create new, icon:add">
      <svg aria-hidden="true" class="octicon octicon-plus float-left" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 9H7v5H5V9H0V7h5V2h2v5h5z"></path></svg>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="littlecodersh/ItChat">This repository</span>
  </div>
    <a class="dropdown-item" href="/littlecodersh/ItChat/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </div>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name tooltipped tooltipped-sw js-menu-target" href="/WhaleChen"
       aria-label="View profile and more"
       data-ga-click="Header, show menu, icon:avatar">
      <img alt="@WhaleChen" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/11818114?v=3&amp;s=40" width="20" />
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <div class="dropdown-menu dropdown-menu-sw">
        <div class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">WhaleChen</strong>
        </div>

        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/WhaleChen" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a>
        <a class="dropdown-item" href="/WhaleChen?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a>
        <a class="dropdown-item" href="/explore" data-ga-click="Header, go to explore, text:explore">
          Explore
        </a>
          <a class="dropdown-item" href="/integrations" data-ga-click="Header, go to integrations, text:integrations">
            Integrations
          </a>
        <a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a>

        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a>

        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/logout" class="logout-form" data-form-nonce="c0d08379c02b12c504ebed58d592a52b4ddd3f26" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="RlGKydIAYZgwCxce93jG1gVbIWegKY88b12QwOwoK7nSvGEmOrKwd69bomKD+Nzo9mpZelaBX6nze4qlngUq1w==" /></div>
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </li>
</ul>


    
  </div>
</div>


      


    <div id="start-of-content" class="accessibility-aid"></div>

      <div id="js-flash-container">
</div>


    <div role="main">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
      
<div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
  <div class="container repohead-details-container">

    

<ul class="pagehead-actions">

  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-form-nonce="c0d08379c02b12c504ebed58d592a52b4ddd3f26" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="RpC4BOTOqlVwEUcCLNKmqA1LEU86+u/WsXfRfiVzxlE3baNRYXv7tjG5yIy5gGy8q6JWrJXwN6swRd5UcoyXyw==" /></div>      <input class="form-control" id="repository_id" name="repository_id" type="hidden" value="49935814" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/littlecodersh/ItChat/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
              <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
              Watch
            </span>
          </a>
          <a class="social-count js-social-count"
            href="/littlecodersh/ItChat/watchers"
            aria-label="94 users are watching this repository">
            94
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
                  <div class="select-menu-item-text">
                    <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
                  <div class="select-menu-item-text">
                    <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
                      Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
                  <div class="select-menu-item-text">
                    <input id="do_ignore" name="do" type="radio" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-mute" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"></path></svg>
                      Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container on">

    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/littlecodersh/ItChat/unstar" class="starred" data-form-nonce="c0d08379c02b12c504ebed58d592a52b4ddd3f26" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="wyyqCod/1C79cbk5Dfg4u4DP6shp5K54unH7LT/SOzpy/tFOVUJuWrwqtOiN50tvZRDIulNey5vEbUYfWIdb4g==" /></div>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar littlecodersh/ItChat"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"></path></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/littlecodersh/ItChat/stargazers"
           aria-label="977 users starred this repository">
          977
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/littlecodersh/ItChat/star" class="unstarred" data-form-nonce="c0d08379c02b12c504ebed58d592a52b4ddd3f26" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Nw5h1YKjXpP5CrThkmIBzLDmrHcj3Fq7amyrRnvA7eIXtrUq3/wGyJEmD2NUQE4jNi8t6ChjLlH7oSEWX5JJXw==" /></div>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star littlecodersh/ItChat"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"></path></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/littlecodersh/ItChat/stargazers"
           aria-label="977 users starred this repository">
          977
        </a>
</form>  </div>

  </li>

  <li>
          <a href="#fork-destination-box" class="btn btn-sm btn-with-count"
              title="Fork your own copy of littlecodersh/ItChat to your account"
              aria-label="Fork your own copy of littlecodersh/ItChat to your account"
              rel="facebox"
              data-ga-click="Repository, show fork modal, action:blob#show; text:Fork">
              <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
            Fork
          </a>

          <div id="fork-destination-box" style="display: none;">
            <h2 class="facebox-header" data-facebox-id="facebox-header">Where should we fork this repository?</h2>
            <include-fragment src=""
                class="js-fork-select-fragment fork-select-fragment"
                data-url="/littlecodersh/ItChat/fork?fragment=1">
              <img alt="Loading" height="64" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-128.gif" width="64" />
            </include-fragment>
          </div>

    <a href="/littlecodersh/ItChat/network" class="social-count"
       aria-label="309 users are forked this repository">
      309
    </a>
  </li>
</ul>

    <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"></path></svg>
  <span class="author" itemprop="author"><a href="/littlecodersh" class="url fn" rel="author">littlecodersh</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/littlecodersh/ItChat" data-pjax="#js-repo-pjax-container">ItChat</a></strong>

</h1>

  </div>
  <div class="container">
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/littlecodersh/ItChat" aria-selected="true" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /littlecodersh/ItChat" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"></path></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/littlecodersh/ItChat/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /littlecodersh/ItChat/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
        <span itemprop="name">Issues</span>
        <span class="counter">3</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/littlecodersh/ItChat/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /littlecodersh/ItChat/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
      <span itemprop="name">Pull requests</span>
      <span class="counter">2</span>
      <meta itemprop="position" content="3">
</a>  </span>

  <a href="/littlecodersh/ItChat/projects" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /littlecodersh/ItChat/projects">
    <svg class="octicon" aria-hidden="true" version="1.1" width="15" height="16" viewBox="0 0 15 16">
      <path d="M1 15h13V1H1v14zM15 1v14a1 1 0 0 1-1 1H1a1 1 0 0 1-1-1V1a1 1 0 0 1 1-1h13a1 1 0 0 1 1 1zm-4.41 11h1.82c.59 0 .59-.41.59-1V3c0-.59 0-1-.59-1h-1.82C10 2 10 2.41 10 3v8c0 .59 0 1 .59 1zm-4-2h1.82C9 10 9 9.59 9 9V3c0-.59 0-1-.59-1H6.59C6 2 6 2.41 6 3v6c0 .59 0 1 .59 1zM2 13V3c0-.59 0-1 .59-1h1.82C5 2 5 2.41 5 3v10c0 .59 0 1-.59 1H2.59C2 14 2 13.59 2 13z"></path>
    </svg>
    Projects
    <span class="counter">0</span>
</a>
    <a href="/littlecodersh/ItChat/wiki" class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /littlecodersh/ItChat/wiki">
      <svg aria-hidden="true" class="octicon octicon-book" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"></path></svg>
      Wiki
</a>

  <a href="/littlecodersh/ItChat/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /littlecodersh/ItChat/pulse">
    <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"></path></svg>
    Pulse
</a>
  <a href="/littlecodersh/ItChat/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /littlecodersh/ItChat/graphs">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"></path></svg>
    Graphs
</a>

</nav>

  </div>
</div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    

<a href="/littlecodersh/ItChat/blob/432d5dc3f0fba90cb20b2bd6723d5f6a1dcbdc06/itchat/client.py" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:9f12eee4db7e517de1dfb6231c967709 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/littlecodersh/ItChat/blob/master/itchat/client.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/littlecodersh/ItChat/blob/robot/itchat/client.py"
               data-name="robot"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                robot
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="BtnGroup float-right">
    <a href="/littlecodersh/ItChat/find/master"
          class="js-pjax-capture-input btn btn-sm BtnGroup-item"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/littlecodersh/ItChat"><span>ItChat</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a href="/littlecodersh/ItChat/tree/master/itchat"><span>itchat</span></a></span><span class="separator">/</span><strong class="final-path">client.py</strong>
  </div>
</div>


  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/littlecodersh/ItChat/commit/432d5dc3f0fba90cb20b2bd6723d5f6a1dcbdc06" data-pjax>
          432d5dc
        </a>
        <relative-time datetime="2016-11-02T09:01:59Z">Nov 2, 2016</relative-time>
      </span>
      <div>
        <img alt="@littlecodersh" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/13028340?v=3&amp;s=40" width="20" />
        <a href="/littlecodersh" class="user-mention" rel="author">littlecodersh</a>
          <a href="/littlecodersh/ItChat/commit/432d5dc3f0fba90cb20b2bd6723d5f6a1dcbdc06" class="message" data-pjax="true" title="Fix missing messages of rapid sending">Fix missing messages of rapid sending</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>3</strong>
         contributors
      </button>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="littlecodersh" href="/littlecodersh/ItChat/commits/master/itchat/client.py?author=littlecodersh"><img alt="@littlecodersh" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/13028340?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="tempdban" href="/littlecodersh/ItChat/commits/master/itchat/client.py?author=tempdban"><img alt="@tempdban" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/4144536?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="cc2cc" href="/littlecodersh/ItChat/commits/master/itchat/client.py?author=cc2cc"><img alt="@cc2cc" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/10631200?v=3&amp;s=40" width="20" /> </a>


    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@littlecodersh" height="24" src="https://avatars3.githubusercontent.com/u/13028340?v=3&amp;s=48" width="24" />
            <a href="/littlecodersh">littlecodersh</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@tempdban" height="24" src="https://avatars1.githubusercontent.com/u/4144536?v=3&amp;s=48" width="24" />
            <a href="/tempdban">tempdban</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@cc2cc" height="24" src="https://avatars0.githubusercontent.com/u/10631200?v=3&amp;s=48" width="24" />
            <a href="/cc2cc">cc2cc</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/littlecodersh/ItChat/raw/master/itchat/client.py" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/littlecodersh/ItChat/blame/master/itchat/client.py" class="btn btn-sm js-update-url-with-hash BtnGroup-item">Blame</a>
      <a href="/littlecodersh/ItChat/commits/master/itchat/client.py" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>

        <a class="btn-octicon tooltipped tooltipped-nw"
           href="https://mac.github.com"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:mac">
            <svg aria-hidden="true" class="octicon octicon-device-desktop" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"></path></svg>
        </a>

        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/littlecodersh/ItChat/edit/master/itchat/client.py" class="inline-form js-update-url-with-hash" data-form-nonce="c0d08379c02b12c504ebed58d592a52b4ddd3f26" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="h4oIkn70nF6B3TknveUzD8roo05k86/Az3JGKa78sXq16W5UyjkabGr05YCPy5dHzDe4+hqcKCdEFwnnoInVzw==" /></div>
          <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
            aria-label="Edit the file in your fork of this project" data-hotkey="e" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"></path></svg>
          </button>
</form>        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/littlecodersh/ItChat/delete/master/itchat/client.py" class="inline-form" data-form-nonce="c0d08379c02b12c504ebed58d592a52b4ddd3f26" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="q/0sPd/TBUNGK7Fz5teP9BemUn0y8QgBvshjtA5Lxnkw2B5UGBiDM5z6AJqyD28oBEIAHrcTQQUAEPrdXgSULg==" /></div>
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Delete the file in your fork of this project" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"></path></svg>
          </button>
</form>  </div>

  <div class="file-info">
      767 lines (759 sloc)
      <span class="file-info-divider"></span>
    38.2 KB
  </div>
</div>

  

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#coding=utf8</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> os, sys, time, re, io</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> threading, subprocess</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> json, xml.dom.minidom, mimetypes</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> copy, pickle, random</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> traceback</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> requests</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> . <span class="pl-k">import</span> config, storage, out, tools</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">BASE_URL</span> <span class="pl-k">=</span> config.<span class="pl-c1">BASE_URL</span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">QR_DIR</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>QR.jpg<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">client</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.storageClass <span class="pl-k">=</span> storage.Storage()</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.memberList <span class="pl-k">=</span> <span class="pl-v">self</span>.storageClass.memberList</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.mpList <span class="pl-k">=</span> <span class="pl-v">self</span>.storageClass.mpList</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.chatroomList <span class="pl-k">=</span> <span class="pl-v">self</span>.storageClass.chatroomList</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.msgList <span class="pl-k">=</span> <span class="pl-v">self</span>.storageClass.msgList</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.loginInfo <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.s <span class="pl-k">=</span> requests.Session()</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.uuid <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.debug <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">dump_login_status</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">fileDir</span>):</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">with</span> <span class="pl-c1">open</span>(fileDir, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f: f.write(<span class="pl-s"><span class="pl-pds">&#39;</span>DELETE THIS<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">            os.remove(fileDir)</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">raise</span> <span class="pl-c1">Exception</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Incorrect fileDir<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">        status <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>loginInfo<span class="pl-pds">&#39;</span></span> : <span class="pl-v">self</span>.loginInfo,</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>cookies<span class="pl-pds">&#39;</span></span>   : <span class="pl-v">self</span>.s.cookies.get_dict(),</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>storage<span class="pl-pds">&#39;</span></span>   : <span class="pl-v">self</span>.storageClass.dumps()}</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-c1">open</span>(fileDir, <span class="pl-s"><span class="pl-pds">&#39;</span>wb<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f:</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">            pickle.dump(status, f)</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">load_login_status</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">fileDir</span>):</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">with</span> <span class="pl-c1">open</span>(fileDir, <span class="pl-s"><span class="pl-pds">&#39;</span>rb<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f:</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">                j <span class="pl-k">=</span> pickle.load(f)</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">Exception</span> <span class="pl-k">as</span> e:</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.loginInfo <span class="pl-k">=</span> j[<span class="pl-s"><span class="pl-pds">&#39;</span>loginInfo<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.s.cookies <span class="pl-k">=</span> requests.utils.cookiejar_from_dict(j[<span class="pl-s"><span class="pl-pds">&#39;</span>cookies<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.storageClass.loads(j[<span class="pl-s"><span class="pl-pds">&#39;</span>storage<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">        msgList, contactList <span class="pl-k">=</span> <span class="pl-v">self</span>.__get_msg()</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (msgList <span class="pl-k">or</span> contactList) <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.s.cookies.clear()</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">del</span> <span class="pl-v">self</span>.chatroomList[:]</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># other info will be automatically cleared</span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> contactList: <span class="pl-v">self</span>.__update_chatrooms(contactList)</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> msgList:</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">                msgList <span class="pl-k">=</span> <span class="pl-v">self</span>.__produce_msg(msgList)</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> msg <span class="pl-k">in</span> msgList: <span class="pl-v">self</span>.msgList.insert(<span class="pl-c1">0</span>, msg)</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">            out.print_line(<span class="pl-s"><span class="pl-pds">&#39;</span>Login successfully as <span class="pl-c1">%s</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span><span class="pl-v">self</span>.storageClass.nickName, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.start_receiving()</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">auto_login</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">enableCmdQR</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">picDir</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-en">open_QR</span>():</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> get_count <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">10</span>):</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">                out.print_line(<span class="pl-s"><span class="pl-pds">&#39;</span>Getting uuid<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">while</span> <span class="pl-k">not</span> <span class="pl-v">self</span>.get_QRuuid(): time.sleep(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">                out.print_line(<span class="pl-s"><span class="pl-pds">&#39;</span>Getting QR Code<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-v">self</span>.get_QR(<span class="pl-v">enableCmdQR</span><span class="pl-k">=</span>enableCmdQR, <span class="pl-v">picDir</span><span class="pl-k">=</span>picDir): <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> <span class="pl-c1">9</span> <span class="pl-k">&lt;=</span> get_count:</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">                    out.print_line(<span class="pl-s"><span class="pl-pds">&#39;</span>Failed to get QR Code, please restart the program<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">                    sys.exit()</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">            out.print_line(<span class="pl-s"><span class="pl-pds">&#39;</span>Please scan the QR Code<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">        open_QR()</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">while</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">            status <span class="pl-k">=</span> <span class="pl-v">self</span>.check_login(<span class="pl-v">picDir</span><span class="pl-k">=</span>picDir)</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> status <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>200<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> status <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>201<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">                out.print_line(<span class="pl-s"><span class="pl-pds">&#39;</span>Please press confirm<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> status <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>408<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">                out.print_line(<span class="pl-s"><span class="pl-pds">&#39;</span>Reloading QR Code<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">                open_QR()</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.web_init()</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.show_mobile_login()</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">        tools.clear_screen()</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.get_contact(<span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">        out.print_line(<span class="pl-s"><span class="pl-pds">&#39;</span>Login successfully as <span class="pl-c1">%s</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span><span class="pl-v">self</span>.storageClass.nickName, <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.start_receiving()</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_QRuuid</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/jslogin<span class="pl-pds">&#39;</span></span><span class="pl-k">%</span><span class="pl-c1">BASE_URL</span></td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">        payloads <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>appid<span class="pl-pds">&#39;</span></span> : <span class="pl-s"><span class="pl-pds">&#39;</span>wx782c26e4c19acffb<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>fun<span class="pl-pds">&#39;</span></span>   : <span class="pl-s"><span class="pl-pds">&#39;</span>new<span class="pl-pds">&#39;</span></span>, }</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.get(url, <span class="pl-v">params</span> <span class="pl-k">=</span> payloads)</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">        regx <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span>window<span class="pl-c1">.</span>QRLogin<span class="pl-c1">.</span>code = (<span class="pl-c1">\d</span><span class="pl-k">+</span>); window<span class="pl-c1">.</span>QRLogin<span class="pl-c1">.</span>uuid = &quot;(<span class="pl-c1">\S</span><span class="pl-k">+?</span>)&quot;;<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">        data <span class="pl-k">=</span> re.search(regx, r.text)</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> data <span class="pl-k">and</span> data.group(<span class="pl-c1">1</span>) <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>200<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.uuid <span class="pl-k">=</span> data.group(<span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-v">self</span>.uuid</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_QR</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">uuid</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">enableCmdQR</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">picDir</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> uuid <span class="pl-k">==</span> <span class="pl-c1">None</span>: uuid <span class="pl-k">=</span> <span class="pl-v">self</span>.uuid</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">            url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/qrcode/<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span>(<span class="pl-c1">BASE_URL</span>, uuid)</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">            r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.get(url, <span class="pl-v">stream</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">            picDir <span class="pl-k">=</span> picDir <span class="pl-k">or</span> <span class="pl-c1">QR_DIR</span></td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">with</span> <span class="pl-c1">open</span>(picDir, <span class="pl-s"><span class="pl-pds">&#39;</span>wb<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f: f.write(r.content)</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> enableCmdQR:</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">            tools.print_cmd_qr(picDir, <span class="pl-v">enableCmdQR</span> <span class="pl-k">=</span> enableCmdQR)</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">            tools.print_qr(picDir)</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_login</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">uuid</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">picDir</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> uuid <span class="pl-k">is</span> <span class="pl-c1">None</span>: uuid <span class="pl-k">=</span> <span class="pl-v">self</span>.uuid</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/cgi-bin/mmwebwx-bin/login<span class="pl-pds">&#39;</span></span><span class="pl-k">%</span><span class="pl-c1">BASE_URL</span></td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">        payloads <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>tip=1&amp;uuid=<span class="pl-c1">%s</span>&amp;_=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span>(uuid, <span class="pl-c1">int</span>(time.time()))</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.get(url, <span class="pl-v">params</span> <span class="pl-k">=</span> payloads)</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">        regx <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span>window<span class="pl-c1">.</span>code=(<span class="pl-c1">\d</span><span class="pl-k">+</span>)<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">        data <span class="pl-k">=</span> re.search(regx, r.text)</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> data <span class="pl-k">and</span> data.group(<span class="pl-c1">1</span>) <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>200<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">            os.remove(picDir <span class="pl-k">or</span> <span class="pl-c1">QR_DIR</span>)</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">            regx <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span>window<span class="pl-c1">.</span>redirect_uri=&quot;(<span class="pl-c1">\S</span><span class="pl-k">+</span>)&quot;;<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> re.search(regx, r.text).group(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">            r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.get(<span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], <span class="pl-v">allow_redirects</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>][:<span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>].rfind(<span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span>)]</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> indexUrl, detailedUrl <span class="pl-k">in</span> (</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">                    (<span class="pl-s"><span class="pl-pds">&quot;</span>wx2.qq.com<span class="pl-pds">&quot;</span></span>      , (<span class="pl-s"><span class="pl-pds">&quot;</span>file.wx2.qq.com<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>webpush.wx2.qq.com<span class="pl-pds">&quot;</span></span>)),</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">                    (<span class="pl-s"><span class="pl-pds">&quot;</span>wx8.qq.com<span class="pl-pds">&quot;</span></span>      , (<span class="pl-s"><span class="pl-pds">&quot;</span>file.wx8.qq.com<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>webpush.wx8.qq.com<span class="pl-pds">&quot;</span></span>)),</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">                    (<span class="pl-s"><span class="pl-pds">&quot;</span>qq.com<span class="pl-pds">&quot;</span></span>          , (<span class="pl-s"><span class="pl-pds">&quot;</span>file.wx.qq.com<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>webpush.wx.qq.com<span class="pl-pds">&quot;</span></span>)),</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">                    (<span class="pl-s"><span class="pl-pds">&quot;</span>web2.wechat.com<span class="pl-pds">&quot;</span></span> , (<span class="pl-s"><span class="pl-pds">&quot;</span>file.web2.wechat.com<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>webpush.web2.wechat.com<span class="pl-pds">&quot;</span></span>)),</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">                    (<span class="pl-s"><span class="pl-pds">&quot;</span>wechat.com<span class="pl-pds">&quot;</span></span>      , (<span class="pl-s"><span class="pl-pds">&quot;</span>file.web.wechat.com<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>webpush.web.wechat.com<span class="pl-pds">&quot;</span></span>))):</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">                fileUrl, syncUrl <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>https://<span class="pl-c1">%s</span>/cgi-bin/mmwebwx-bin<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> url <span class="pl-k">for</span> url <span class="pl-k">in</span> detailedUrl]</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> indexUrl <span class="pl-k">in</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>fileUrl<span class="pl-pds">&#39;</span></span>], <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>syncUrl<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> \</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">                        fileUrl, syncUrl</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>fileUrl<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>syncUrl<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>deviceid<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>e<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">repr</span>(random.random())[<span class="pl-c1">2</span>:<span class="pl-c1">17</span>]</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">int</span>(time.time() <span class="pl-k">*</span> <span class="pl-c1">1000</span>)</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> node <span class="pl-k">in</span> xml.dom.minidom.parseString(r.text).documentElement.childNodes:</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> node.nodeName <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>skey<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>skey<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>Skey<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> node.childNodes[<span class="pl-c1">0</span>].data</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> node.nodeName <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>wxsid<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>wxsid<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>Sid<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> node.childNodes[<span class="pl-c1">0</span>].data</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> node.nodeName <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>wxuin<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>wxuin<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>Uin<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> node.childNodes[<span class="pl-c1">0</span>].data</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> node.nodeName <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>pass_ticket<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>pass_ticket<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>DeviceID<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> node.childNodes[<span class="pl-c1">0</span>].data</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&#39;</span>200<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> data <span class="pl-k">and</span> data.group(<span class="pl-c1">1</span>) <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>201<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&#39;</span>201<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> data <span class="pl-k">and</span> data.group(<span class="pl-c1">1</span>) <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>408<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&#39;</span>408<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&#39;</span>0<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">web_init</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxinit?r=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (<span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], <span class="pl-c1">int</span>(time.time()))</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">        payloads <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>], }</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> { <span class="pl-s"><span class="pl-pds">&#39;</span>ContentType<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json; charset=UTF-8<span class="pl-pds">&#39;</span></span> }</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.post(url, <span class="pl-v">data</span> <span class="pl-k">=</span> json.dumps(payloads), <span class="pl-v">headers</span> <span class="pl-k">=</span> headers)</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">        dic <span class="pl-k">=</span> json.loads(r.content.decode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf-8<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>replace<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">        tools.emoji_formatter(dic[<span class="pl-s"><span class="pl-pds">&#39;</span>User<span class="pl-pds">&#39;</span></span>], <span class="pl-s"><span class="pl-pds">&#39;</span>NickName<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>User<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> tools.struct_friend_info(dic[<span class="pl-s"><span class="pl-pds">&#39;</span>User<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>SyncKey<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> dic[<span class="pl-s"><span class="pl-pds">&#39;</span>SyncKey<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>synckey<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>|<span class="pl-pds">&#39;</span></span>.join([<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>_<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (item[<span class="pl-s"><span class="pl-pds">&#39;</span>Key<span class="pl-pds">&#39;</span></span>], item[<span class="pl-s"><span class="pl-pds">&#39;</span>Val<span class="pl-pds">&#39;</span></span>]) <span class="pl-k">for</span> item <span class="pl-k">in</span> dic[<span class="pl-s"><span class="pl-pds">&#39;</span>SyncKey<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>List<span class="pl-pds">&#39;</span></span>]])</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.storageClass.userName <span class="pl-k">=</span> dic[<span class="pl-s"><span class="pl-pds">&#39;</span>User<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.storageClass.nickName <span class="pl-k">=</span> dic[<span class="pl-s"><span class="pl-pds">&#39;</span>User<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>NickName<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> dic[<span class="pl-s"><span class="pl-pds">&#39;</span>User<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">update_chatroom</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">userName</span>, <span class="pl-smi">detailedMember</span><span class="pl-k">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxbatchgetcontact?type=ex&amp;r=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (<span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], <span class="pl-c1">int</span>(time.time()))</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> { <span class="pl-s"><span class="pl-pds">&#39;</span>ContentType<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json; charset=UTF-8<span class="pl-pds">&#39;</span></span> }</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">        payloads <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>Count<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">1</span>,</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>List<span class="pl-pds">&#39;</span></span>: [{</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>: userName,</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>ChatRoomId<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>, }], }</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">        j <span class="pl-k">=</span> json.loads(<span class="pl-v">self</span>.s.post(url, <span class="pl-v">data</span> <span class="pl-k">=</span> json.dumps(payloads), <span class="pl-v">headers</span> <span class="pl-k">=</span> headers</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">                ).content.decode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf8<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>replace<span class="pl-pds">&#39;</span></span>))[<span class="pl-s"><span class="pl-pds">&#39;</span>ContactList<span class="pl-pds">&#39;</span></span>][<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> detailedMember:</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">def</span> <span class="pl-en">get_detailed_member_info</span>(<span class="pl-smi">encryChatroomId</span>, <span class="pl-smi">memberList</span>):</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">                url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxbatchgetcontact?type=ex&amp;r=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (<span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], <span class="pl-c1">int</span>(time.time()))</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">                headers <span class="pl-k">=</span> { <span class="pl-s"><span class="pl-pds">&#39;</span>ContentType<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json; charset=UTF-8<span class="pl-pds">&#39;</span></span> }</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">                payloads <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Count<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">len</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>MemberList<span class="pl-pds">&#39;</span></span>]),</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>List<span class="pl-pds">&#39;</span></span>: [{<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>: member[<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>], <span class="pl-s"><span class="pl-pds">&#39;</span>EncryChatRoomId<span class="pl-pds">&#39;</span></span>: j[<span class="pl-s"><span class="pl-pds">&#39;</span>EncryChatRoomId<span class="pl-pds">&#39;</span></span>]} \</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">for</span> member <span class="pl-k">in</span> memberList],</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">                    }</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> json.loads(<span class="pl-v">self</span>.s.post(url, <span class="pl-v">data</span> <span class="pl-k">=</span> json.dumps(payloads), <span class="pl-v">headers</span> <span class="pl-k">=</span> headers</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">                        ).content.decode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf8<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>replace<span class="pl-pds">&#39;</span></span>))[<span class="pl-s"><span class="pl-pds">&#39;</span>ContactList<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">MAX_GET_NUMBER</span> <span class="pl-k">=</span> <span class="pl-c1">50</span></td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">            totalMemberList <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">len</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>MemberList<span class="pl-pds">&#39;</span></span>]) <span class="pl-k">/</span> <span class="pl-c1">MAX_GET_NUMBER</span> <span class="pl-k">+</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">                memberList <span class="pl-k">=</span> j[<span class="pl-s"><span class="pl-pds">&#39;</span>MemberList<span class="pl-pds">&#39;</span></span>][i<span class="pl-k">*</span><span class="pl-c1">MAX_GET_NUMBER</span>: (i<span class="pl-k">+</span><span class="pl-c1">1</span>)<span class="pl-k">*</span><span class="pl-c1">MAX_GET_NUMBER</span>]</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">                totalMemberList <span class="pl-k">+=</span> get_detailed_member_info(j[<span class="pl-s"><span class="pl-pds">&#39;</span>EncryChatRoomId<span class="pl-pds">&#39;</span></span>], memberList)</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">            j[<span class="pl-s"><span class="pl-pds">&#39;</span>MemberList<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> totalMemberList</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.__update_chatrooms([j])</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-v">self</span>.storageClass.search_chatrooms(<span class="pl-v">userName</span><span class="pl-k">=</span>j[<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_contact</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">update</span><span class="pl-k">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">1</span> <span class="pl-k">&lt;</span> <span class="pl-c1">len</span>(<span class="pl-v">self</span>.memberList) <span class="pl-k">and</span> <span class="pl-k">not</span> update: <span class="pl-k">return</span> copy.deepcopy(<span class="pl-v">self</span>.memberList)</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxgetcontact?r=<span class="pl-c1">%s</span>&amp;seq=0&amp;skey=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (<span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">int</span>(time.time()), <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>skey<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> { <span class="pl-s"><span class="pl-pds">&#39;</span>ContentType<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json; charset=UTF-8<span class="pl-pds">&#39;</span></span> }</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.get(url, <span class="pl-v">headers</span><span class="pl-k">=</span>headers)</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">        tempList <span class="pl-k">=</span> json.loads(r.content.decode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf-8<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>replace<span class="pl-pds">&#39;</span></span>))[<span class="pl-s"><span class="pl-pds">&#39;</span>MemberList<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">del</span> <span class="pl-v">self</span>.memberList[:]</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">del</span> <span class="pl-v">self</span>.mpList[:]</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">        chatroomList <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># chatroomList will not be cleared because:</span></td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># when initializing, it&#39;s cleared once</span></td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># when updating, there&#39;s not need for clearing</span></td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.memberList.append(<span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>User<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> m <span class="pl-k">in</span> tempList:</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">            tools.emoji_formatter(m, <span class="pl-s"><span class="pl-pds">&#39;</span>NickName<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>Sex<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.memberList.append(m)</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> <span class="pl-k">not</span> (<span class="pl-c1">any</span>([<span class="pl-c1">str</span>(n) <span class="pl-k">in</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>] <span class="pl-k">for</span> n <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">10</span>)]) <span class="pl-k">and</span></td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">any</span>([<span class="pl-c1">chr</span>(n) <span class="pl-k">in</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>] <span class="pl-k">for</span> n <span class="pl-k">in</span> (</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">list</span>(<span class="pl-c1">range</span>(<span class="pl-c1">ord</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span>), <span class="pl-c1">ord</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>z<span class="pl-pds">&#39;</span></span>) <span class="pl-k">+</span> <span class="pl-c1">1</span>)) <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">list</span>(<span class="pl-c1">range</span>(<span class="pl-c1">ord</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>A<span class="pl-pds">&#39;</span></span>), <span class="pl-c1">ord</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Z<span class="pl-pds">&#39;</span></span>) <span class="pl-k">+</span> <span class="pl-c1">1</span>)))])):</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">continue</span> <span class="pl-c"># userName have number and str</span></td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> <span class="pl-s"><span class="pl-pds">&#39;</span>@@<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">                m[<span class="pl-s"><span class="pl-pds">&#39;</span>isAdmin<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">None</span> <span class="pl-c"># this value will be set after update_chatroom</span></td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">                chatroomList.append(m)</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> <span class="pl-s"><span class="pl-pds">&#39;</span>@<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>VerifyFlag<span class="pl-pds">&#39;</span></span>] <span class="pl-k">&amp;</span> <span class="pl-c1">8</span> <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.memberList.append(m)</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.mpList.append(m)</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> chatroomList: <span class="pl-v">self</span>.__update_chatrooms(chatroomList)</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> copy.deepcopy(chatroomList)</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_friends</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">update</span><span class="pl-k">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> update: <span class="pl-v">self</span>.get_contact(<span class="pl-v">update</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> copy.deepcopy(<span class="pl-v">self</span>.memberList)</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_chatrooms</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">update</span><span class="pl-k">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span> get chatrooms</span></td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         * if update is set to True, this will only return chatrooms in contact</span></td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> update:</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-v">self</span>.get_contact(<span class="pl-v">update</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> copy.deepcopy(<span class="pl-v">self</span>.chatroomList)</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_mps</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">update</span><span class="pl-k">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> update: <span class="pl-v">self</span>.get_contact(<span class="pl-v">update</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> copy.deepcopy(<span class="pl-v">self</span>.mpList)</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">show_mobile_login</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxstatusnotify?lang=zh_CN&amp;pass_ticket=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span>(<span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>],<span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>pass_ticket<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">        payloads <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>Code<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">3</span>,</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>FromUserName<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.storageClass.userName,</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>ToUserName<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.storageClass.userName,</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>ClientMsgId<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">int</span>(time.time()),</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">                }</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> { <span class="pl-s"><span class="pl-pds">&#39;</span>ContentType<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json; charset=UTF-8<span class="pl-pds">&#39;</span></span> }</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.post(url, <span class="pl-v">data</span> <span class="pl-k">=</span> json.dumps(payloads), <span class="pl-v">headers</span> <span class="pl-k">=</span> headers)</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">start_receiving</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-en">maintain_loop</span>():</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">            i <span class="pl-k">=</span> <span class="pl-v">self</span>.__sync_check()</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">            count <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">while</span> i <span class="pl-k">and</span> count <span class="pl-k">&lt;</span><span class="pl-c1">4</span>:</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> i <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>0<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">                        msgList, contactList <span class="pl-k">=</span> <span class="pl-v">self</span>.__get_msg()</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">if</span> contactList: <span class="pl-v">self</span>.__update_chatrooms(contactList)</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">if</span> msgList:</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">                            msgList <span class="pl-k">=</span> <span class="pl-v">self</span>.__produce_msg(msgList)</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">                            <span class="pl-k">for</span> msg <span class="pl-k">in</span> msgList: <span class="pl-v">self</span>.msgList.insert(<span class="pl-c1">0</span>, msg)</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">                    i <span class="pl-k">=</span> <span class="pl-v">self</span>.__sync_check()</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">                    count <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span> requests.exceptions.RequestException <span class="pl-k">as</span> e:</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">                    count <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> <span class="pl-v">self</span>.debug: traceback.print_exc()</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">                    time.sleep(count <span class="pl-k">*</span> <span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span> <span class="pl-c1">Exception</span> <span class="pl-k">as</span> e:</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">                    out.print_line(<span class="pl-c1">str</span>(e), <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> <span class="pl-v">self</span>.debug: traceback.print_exc()</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">            out.print_line(<span class="pl-s"><span class="pl-pds">&#39;</span>LOG OUT<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">        maintainThread <span class="pl-k">=</span> threading.Thread(<span class="pl-v">target</span> <span class="pl-k">=</span> maintain_loop)</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">        maintainThread.setDaemon(<span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">        maintainThread.start()</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">__sync_check</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/synccheck<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-v">self</span>.loginInfo.get(<span class="pl-s"><span class="pl-pds">&#39;</span>syncUrl<span class="pl-pds">&#39;</span></span>, <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">        params <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>r<span class="pl-pds">&#39;</span></span>        : <span class="pl-c1">int</span>(time.time() <span class="pl-k">*</span> <span class="pl-c1">1000</span>),</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>skey<span class="pl-pds">&#39;</span></span>     : <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>skey<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>sid<span class="pl-pds">&#39;</span></span>      : <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>wxsid<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>uin<span class="pl-pds">&#39;</span></span>      : <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>wxuin<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>deviceid<span class="pl-pds">&#39;</span></span> : <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>deviceid<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>synckey<span class="pl-pds">&#39;</span></span>  : <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>synckey<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>_<span class="pl-pds">&#39;</span></span>        : <span class="pl-c1">int</span>(time.time() <span class="pl-k">*</span> <span class="pl-c1">1000</span>),}</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.get(url, <span class="pl-v">params</span><span class="pl-k">=</span>params)</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">        regx <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span>window<span class="pl-c1">.</span>synccheck={retcode:&quot;(<span class="pl-c1">\d</span><span class="pl-k">+</span>)&quot;,selector:&quot;(<span class="pl-c1">\d</span><span class="pl-k">+</span>)&quot;}<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">        pm <span class="pl-k">=</span> re.search(regx, r.text)</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> pm <span class="pl-k">is</span> <span class="pl-c1">None</span> <span class="pl-k">or</span> pm.group(<span class="pl-c1">1</span>) <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>0<span class="pl-pds">&#39;</span></span> : <span class="pl-k">return</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> pm.group(<span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">__get_msg</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxsync?sid=<span class="pl-c1">%s</span>&amp;skey=<span class="pl-c1">%s</span>&amp;pass_ticket=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span>(</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>wxsid<span class="pl-pds">&#39;</span></span>], <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>skey<span class="pl-pds">&#39;</span></span>],<span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>pass_ticket<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">        payloads <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>SyncKey<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>SyncKey<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>rr<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">int</span>(time.time()), }</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> { <span class="pl-s"><span class="pl-pds">&#39;</span>ContentType<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json; charset=UTF-8<span class="pl-pds">&#39;</span></span> }</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.post(url, <span class="pl-v">data</span> <span class="pl-k">=</span> json.dumps(payloads), <span class="pl-v">headers</span> <span class="pl-k">=</span> headers)</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">        dic <span class="pl-k">=</span> json.loads(r.content.decode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf-8<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>replace<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> dic[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseResponse<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>Ret<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> <span class="pl-c1">0</span>: <span class="pl-k">return</span> <span class="pl-c1">None</span>, <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>SyncKey<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> dic[<span class="pl-s"><span class="pl-pds">&#39;</span>SyncKey<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>synckey<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>|<span class="pl-pds">&#39;</span></span>.join([<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>_<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (item[<span class="pl-s"><span class="pl-pds">&#39;</span>Key<span class="pl-pds">&#39;</span></span>], item[<span class="pl-s"><span class="pl-pds">&#39;</span>Val<span class="pl-pds">&#39;</span></span>]) <span class="pl-k">for</span> item <span class="pl-k">in</span> dic[<span class="pl-s"><span class="pl-pds">&#39;</span>SyncKey<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>List<span class="pl-pds">&#39;</span></span>]])</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> dic[<span class="pl-s"><span class="pl-pds">&#39;</span>AddMsgList<span class="pl-pds">&#39;</span></span>], dic[<span class="pl-s"><span class="pl-pds">&#39;</span>ModContactList<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">__update_chatrooms</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">l</span>):</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">        oldUsernameList <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> chatroom <span class="pl-k">in</span> l:</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># format NickName &amp; DisplayName &amp; self keys</span></td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">            tools.emoji_formatter(chatroom, <span class="pl-s"><span class="pl-pds">&#39;</span>NickName<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> member <span class="pl-k">in</span> chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>MemberList<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-v">self</span>.storageClass.userName <span class="pl-k">==</span> member[<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">                    chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>self<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> member</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">                tools.emoji_formatter(member, <span class="pl-s"><span class="pl-pds">&#39;</span>NickName<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">                tools.emoji_formatter(member, <span class="pl-s"><span class="pl-pds">&#39;</span>DisplayName<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># get useful information from old version of this chatroom</span></td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">            oldChatroom <span class="pl-k">=</span> tools.search_dict_list(</td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.chatroomList, <span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>, chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> oldChatroom <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">                memberList, oldMemberList <span class="pl-k">=</span> \</td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">                    chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>MemberList<span class="pl-pds">&#39;</span></span>], oldChatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>MemberList<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"># update member list</span></td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> memberList:</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">for</span> member <span class="pl-k">in</span> memberList:</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">                        oldMember <span class="pl-k">=</span> tools.search_dict_list(</td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">                            oldMemberList, <span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>, member[<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">if</span> oldMember <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">                            <span class="pl-k">for</span> k <span class="pl-k">in</span> oldMember:</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">                                member[k] <span class="pl-k">=</span> member[k] <span class="pl-k">or</span> oldMember[k]</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">                    chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>MemberList<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> oldMemberList</td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"># update other info</span></td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> k <span class="pl-k">in</span> oldChatroom:</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">                    chatroom[k] <span class="pl-k">=</span> chatroom.get(k) <span class="pl-k">or</span> oldChatroom[k]</td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"># ready for deletion</span></td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">                oldUsernameList.append(oldChatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># update OwnerUin</span></td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> chatroom.get(<span class="pl-s"><span class="pl-pds">&#39;</span>ChatRoomOwner<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">                chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>OwnerUin<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> tools.search_dict_list(</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">                    chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>MemberList<span class="pl-pds">&#39;</span></span>], <span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>, chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>ChatRoomOwner<span class="pl-pds">&#39;</span></span>])[<span class="pl-s"><span class="pl-pds">&#39;</span>Uin<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># update isAdmin</span></td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>OwnerUin<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> chatroom <span class="pl-k">and</span> chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>OwnerUin<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">                chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>isAdmin<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> \</td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">                    chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>OwnerUin<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">int</span>(<span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>wxuin<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">                chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>isAdmin<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># delete old chatrooms</span></td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">        oldIndexList <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i, chatroom <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(<span class="pl-v">self</span>.chatroomList):</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>] <span class="pl-k">in</span> oldUsernameList:</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">                oldIndexList.append(i)</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">        oldIndexList.sort(<span class="pl-v">reverse</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i <span class="pl-k">in</span> oldIndexList: <span class="pl-k">del</span> <span class="pl-v">self</span>.chatroomList[i]</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># add new chatrooms</span></td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> chatroom <span class="pl-k">in</span> l:</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.chatroomList.append(chatroom)</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">__get_download_fn</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">url</span>, <span class="pl-smi">msgId</span>):</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-en">download_fn</span>(<span class="pl-smi">downloadDir</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">            params <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>: msgId,</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>skey<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>skey<span class="pl-pds">&#39;</span></span>],}</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">            r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.get(url, <span class="pl-v">params</span><span class="pl-k">=</span>params, <span class="pl-v">stream</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">            tempStorage <span class="pl-k">=</span> io.BytesIO()</td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> block <span class="pl-k">in</span> r.iter_content(<span class="pl-c1">1024</span>):</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">                tempStorage.write(block)</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> downloadDir <span class="pl-k">is</span> <span class="pl-c1">None</span>: <span class="pl-k">return</span> tempStorage.getvalue()</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">with</span> <span class="pl-c1">open</span>(downloadDir, <span class="pl-s"><span class="pl-pds">&#39;</span>wb<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f: f.write(tempStorage.getvalue())</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> download_fn</td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">__produce_msg</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">l</span>):</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">        rl <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">        srl <span class="pl-k">=</span> [<span class="pl-c1">40</span>, <span class="pl-c1">43</span>, <span class="pl-c1">50</span>, <span class="pl-c1">52</span>, <span class="pl-c1">53</span>, <span class="pl-c1">9999</span>]</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># 40 msg, 43 videochat, 50 VOIPMSG, 52 voipnotifymsg, 53 webwxvoipnotifymsg, 9999 sysnotice</span></td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> m <span class="pl-k">in</span> l:</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>@@<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>FromUserName<span class="pl-pds">&#39;</span></span>] <span class="pl-k">or</span> <span class="pl-s"><span class="pl-pds">&#39;</span>@@<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>ToUserName<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.__produce_group_chat(m)</td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">                tools.msg_formatter(m, <span class="pl-s"><span class="pl-pds">&#39;</span>Content<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">1</span>: <span class="pl-c"># words</span></td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>Url<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">                    regx <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span>(<span class="pl-c1">.</span><span class="pl-k">+?</span><span class="pl-cce">\(</span><span class="pl-c1">.</span><span class="pl-k">+?</span><span class="pl-cce">\)</span>)<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">                    data <span class="pl-k">=</span> re.search(regx, m[<span class="pl-s"><span class="pl-pds">&#39;</span>Content<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">                    data <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Map<span class="pl-pds">&#39;</span></span> <span class="pl-k">if</span> data <span class="pl-k">is</span> <span class="pl-c1">None</span> <span class="pl-k">else</span> data.group(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">                    msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Map<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: data,}</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">                    msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: m[<span class="pl-s"><span class="pl-pds">&#39;</span>Content<span class="pl-pds">&#39;</span></span>],}</td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">3</span> <span class="pl-k">or</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">47</span>: <span class="pl-c"># picture</span></td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">                download_fn <span class="pl-k">=</span> <span class="pl-v">self</span>.__get_download_fn(</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxgetmsgimg<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], m[<span class="pl-s"><span class="pl-pds">&#39;</span>NewMsgId<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">                msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>     : <span class="pl-s"><span class="pl-pds">&#39;</span>Picture<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>FileName<span class="pl-pds">&#39;</span></span> : <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>.<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span>(time.strftime(<span class="pl-s"><span class="pl-pds">&#39;</span>%y%m<span class="pl-c1">%d</span>-%H%M%S<span class="pl-pds">&#39;</span></span>, time.localtime()),</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>png<span class="pl-pds">&#39;</span></span> <span class="pl-k">if</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">3</span> <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>gif<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>     : download_fn, }</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">34</span>: <span class="pl-c"># voice</span></td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line">                download_fn <span class="pl-k">=</span> <span class="pl-v">self</span>.__get_download_fn(</td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxgetvoice<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], m[<span class="pl-s"><span class="pl-pds">&#39;</span>NewMsgId<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line">                msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Recording<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>FileName<span class="pl-pds">&#39;</span></span> : <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>.mp4<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> time.strftime(<span class="pl-s"><span class="pl-pds">&#39;</span>%y%m<span class="pl-c1">%d</span>-%H%M%S<span class="pl-pds">&#39;</span></span>, time.localtime()),</td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: download_fn,}</td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">37</span>: <span class="pl-c"># friends</span></td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">                msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Friends<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: {</td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>status<span class="pl-pds">&#39;</span></span>        : m[<span class="pl-s"><span class="pl-pds">&#39;</span>Status<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>userName<span class="pl-pds">&#39;</span></span>      : m[<span class="pl-s"><span class="pl-pds">&#39;</span>RecommendInfo<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>ticket<span class="pl-pds">&#39;</span></span>        : m[<span class="pl-s"><span class="pl-pds">&#39;</span>Ticket<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>userInfo<span class="pl-pds">&#39;</span></span> : m[<span class="pl-s"><span class="pl-pds">&#39;</span>RecommendInfo<span class="pl-pds">&#39;</span></span>], }, }</td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">42</span>: <span class="pl-c"># name card</span></td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">                msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Card<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: m[<span class="pl-s"><span class="pl-pds">&#39;</span>RecommendInfo<span class="pl-pds">&#39;</span></span>], }</td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">49</span>: <span class="pl-c"># sharing</span></td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>AppMsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">6</span>:</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">                    msg <span class="pl-k">=</span> m</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line">                    cookiesList <span class="pl-k">=</span> {name:data <span class="pl-k">for</span> name,data <span class="pl-k">in</span> <span class="pl-v">self</span>.s.cookies.items()}</td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">def</span> <span class="pl-en">download_atta</span>(<span class="pl-smi">attaDir</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line">                        url <span class="pl-k">=</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>fileUrl<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/webwxgetmedia<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line">                        params <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&#39;</span>sender<span class="pl-pds">&#39;</span></span>: msg[<span class="pl-s"><span class="pl-pds">&#39;</span>FromUserName<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&#39;</span>mediaid<span class="pl-pds">&#39;</span></span>: msg[<span class="pl-s"><span class="pl-pds">&#39;</span>MediaId<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&#39;</span>filename<span class="pl-pds">&#39;</span></span>: msg[<span class="pl-s"><span class="pl-pds">&#39;</span>FileName<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&#39;</span>fromuser<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>wxuin<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&#39;</span>pass_ticket<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>undefined<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&#39;</span>webwx_data_ticket<span class="pl-pds">&#39;</span></span>: cookiesList[<span class="pl-s"><span class="pl-pds">&#39;</span>webwx_data_ticket<span class="pl-pds">&#39;</span></span>],}</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line">                        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.get(url, <span class="pl-v">params</span><span class="pl-k">=</span>params, <span class="pl-v">stream</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">                        tempStorage <span class="pl-k">=</span> io.BytesIO()</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">for</span> block <span class="pl-k">in</span> r.iter_content(<span class="pl-c1">1024</span>):</td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line">                            tempStorage.write(block)</td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">if</span> attaDir <span class="pl-k">is</span> <span class="pl-c1">None</span>: <span class="pl-k">return</span> tempStorage.getvalue()</td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">with</span> <span class="pl-c1">open</span>(attaDir, <span class="pl-s"><span class="pl-pds">&#39;</span>wb<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f: f.write(tempStorage.getvalue())</td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line">                    msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Attachment<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: download_atta, }</td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>AppMsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">17</span>:</td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line">                    msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Note<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: m[<span class="pl-s"><span class="pl-pds">&#39;</span>FileName<span class="pl-pds">&#39;</span></span>], }</td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>AppMsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">2000</span>:</td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line">                    regx <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span><span class="pl-cce">\[</span>CDATA<span class="pl-cce">\[</span>(<span class="pl-c1">.</span><span class="pl-k">+?</span>)<span class="pl-cce">\]</span><span class="pl-c1">[</span><span class="pl-c1">\s\S</span><span class="pl-c1">]</span><span class="pl-k">+?</span><span class="pl-cce">\[</span>CDATA<span class="pl-cce">\[</span>(<span class="pl-c1">.</span><span class="pl-k">+?</span>)<span class="pl-cce">\]</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line">                    data <span class="pl-k">=</span> re.search(regx, m[<span class="pl-s"><span class="pl-pds">&#39;</span>Content<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> data:</td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line">                        data <span class="pl-k">=</span> data.group(<span class="pl-c1">2</span>).split(<span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>。<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line">                        data <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>You may found detailed info in Content key.<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line">                    msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Note<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: data, }</td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line">                    msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Sharing<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: m[<span class="pl-s"><span class="pl-pds">&#39;</span>FileName<span class="pl-pds">&#39;</span></span>], }</td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">51</span>: <span class="pl-c"># phone init</span></td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line">                msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Init<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: m[<span class="pl-s"><span class="pl-pds">&#39;</span>ToUserName<span class="pl-pds">&#39;</span></span>], }</td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">62</span>: <span class="pl-c"># tiny video</span></td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line">                msgId <span class="pl-k">=</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgId<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">def</span> <span class="pl-en">download_video</span>(<span class="pl-smi">videoDir</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line">                    url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxgetvideo<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line">                    params <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>: msgId,</td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&#39;</span>skey<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>skey<span class="pl-pds">&#39;</span></span>],}</td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line">                    headers <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>Range<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>bytes=0-<span class="pl-pds">&#39;</span></span>}</td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line">                    r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.get(url, <span class="pl-v">params</span><span class="pl-k">=</span>params, <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">stream</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line">                    tempStorage <span class="pl-k">=</span> io.BytesIO()</td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">for</span> block <span class="pl-k">in</span> r.iter_content(<span class="pl-c1">1024</span>):</td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line">                        tempStorage.write(block)</td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> videoDir <span class="pl-k">is</span> <span class="pl-c1">None</span>: <span class="pl-k">return</span> tempStorage.getvalue()</td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">with</span> <span class="pl-c1">open</span>(videoDir, <span class="pl-s"><span class="pl-pds">&#39;</span>wb<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f: f.write(tempStorage.getvalue())</td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line">                msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Video<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>FileName<span class="pl-pds">&#39;</span></span> : <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>.mp4<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> time.strftime(<span class="pl-s"><span class="pl-pds">&#39;</span>%y%m<span class="pl-c1">%d</span>-%H%M%S<span class="pl-pds">&#39;</span></span>, time.localtime()),</td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: download_video, }</td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">10000</span>:</td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line">                msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Note<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: m[<span class="pl-s"><span class="pl-pds">&#39;</span>Content<span class="pl-pds">&#39;</span></span>],}</td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">10002</span>:</td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line">                regx <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span><span class="pl-cce">\[</span>CDATA<span class="pl-cce">\[</span>(<span class="pl-c1">.</span><span class="pl-k">+?</span>)<span class="pl-cce">\]\]</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line">                data <span class="pl-k">=</span> re.search(regx, m[<span class="pl-s"><span class="pl-pds">&#39;</span>Content<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line">                data <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>System message<span class="pl-pds">&#39;</span></span> <span class="pl-k">if</span> data <span class="pl-k">is</span> <span class="pl-c1">None</span> <span class="pl-k">else</span> data.group(<span class="pl-c1">1</span>).replace(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line">                msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Note<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: data, }</td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">in</span> srl:</td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line">                msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Useless<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>UselessMsg<span class="pl-pds">&#39;</span></span>, }</td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line">                out.print_line(<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType Unknown: <span class="pl-c1">%s</span><span class="pl-cce">\n</span><span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span>(m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>], <span class="pl-c1">str</span>(m)), <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line">                srl.append(m[<span class="pl-s"><span class="pl-pds">&#39;</span>MsgType<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line">                msg <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Useless<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Text<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>UselessMsg<span class="pl-pds">&#39;</span></span>, }</td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line">            m <span class="pl-k">=</span> <span class="pl-c1">dict</span>(m, <span class="pl-k">**</span>msg)</td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line">            rl.append(m)</td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> rl</td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">__produce_group_chat</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">msg</span>):</td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> re.match(<span class="pl-s"><span class="pl-pds">&#39;</span>(@[0-9a-z]*?):&lt;br/&gt;(.*)$<span class="pl-pds">&#39;</span></span>, msg[<span class="pl-s"><span class="pl-pds">&#39;</span>Content<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> r: <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line">        actualUserName, content <span class="pl-k">=</span> r.groups()</td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line">        chatroom <span class="pl-k">=</span> <span class="pl-v">self</span>.storageClass.search_chatrooms(<span class="pl-v">userName</span><span class="pl-k">=</span>msg[<span class="pl-s"><span class="pl-pds">&#39;</span>FromUserName<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line">        member <span class="pl-k">=</span> tools.search_dict_list((chatroom <span class="pl-k">or</span> {}).get(</td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>MemberList<span class="pl-pds">&#39;</span></span>) <span class="pl-k">or</span> [], <span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>, actualUserName)</td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> member <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line">            chatroom <span class="pl-k">=</span> <span class="pl-v">self</span>.update_chatroom(msg[<span class="pl-s"><span class="pl-pds">&#39;</span>FromUserName<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line">            member <span class="pl-k">=</span> tools.search_dict_list((chatroom <span class="pl-k">or</span> {}).get(</td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>MemberList<span class="pl-pds">&#39;</span></span>) <span class="pl-k">or</span> [], <span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>, actualUserName)</td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line">        msg[<span class="pl-s"><span class="pl-pds">&#39;</span>ActualUserName<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> actualUserName</td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line">        msg[<span class="pl-s"><span class="pl-pds">&#39;</span>ActualNickName<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> member[<span class="pl-s"><span class="pl-pds">&#39;</span>DisplayName<span class="pl-pds">&#39;</span></span>] <span class="pl-k">or</span> member[<span class="pl-s"><span class="pl-pds">&#39;</span>NickName<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line">        msg[<span class="pl-s"><span class="pl-pds">&#39;</span>Content<span class="pl-pds">&#39;</span></span>]        <span class="pl-k">=</span> content</td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line">        tools.msg_formatter(msg, <span class="pl-s"><span class="pl-pds">&#39;</span>Content<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line">        atFlag <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>@<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> (chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>self<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>DisplayName<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">or</span> <span class="pl-v">self</span>.storageClass.nickName)</td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line">        msg[<span class="pl-s"><span class="pl-pds">&#39;</span>isAt<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> (</td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line">            (atFlag <span class="pl-k">+</span> (<span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span><span class="pl-cce">\u2005</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">if</span> <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span><span class="pl-cce">\u2005</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> msg[<span class="pl-s"><span class="pl-pds">&#39;</span>Content<span class="pl-pds">&#39;</span></span>] <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">in</span> msg[<span class="pl-s"><span class="pl-pds">&#39;</span>Content<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">or</span></td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line">            msg[<span class="pl-s"><span class="pl-pds">&#39;</span>Content<span class="pl-pds">&#39;</span></span>].endswith(atFlag))</td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">send_raw_msg</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">msgType</span>, <span class="pl-smi">content</span>, <span class="pl-smi">toUserName</span>):</td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxsendmsg<span class="pl-pds">&#39;</span></span><span class="pl-k">%</span><span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line">        payloads <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>Msg<span class="pl-pds">&#39;</span></span>: {</td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: msgType,</td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>Content<span class="pl-pds">&#39;</span></span>: content,</td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>FromUserName<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.storageClass.userName,</td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>ToUserName<span class="pl-pds">&#39;</span></span>: (toUserName <span class="pl-k">if</span> toUserName <span class="pl-k">else</span> <span class="pl-v">self</span>.storageClass.userName),</td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>LocalID<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>ClientMsgId<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code blob-code-inner js-file-line">                }, }</td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> { <span class="pl-s"><span class="pl-pds">&#39;</span>ContentType<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json; charset=UTF-8<span class="pl-pds">&#39;</span></span> }</td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.post(url, <span class="pl-v">data</span><span class="pl-k">=</span>json.dumps(payloads, <span class="pl-v">ensure_ascii</span><span class="pl-k">=</span><span class="pl-c1">False</span>).encode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf8<span class="pl-pds">&#39;</span></span>), <span class="pl-v">headers</span><span class="pl-k">=</span>headers)</td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> r.json()</td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">send_msg</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">msg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Test Message<span class="pl-pds">&#39;</span></span>, <span class="pl-smi">toUserName</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.send_raw_msg(<span class="pl-c1">1</span>, msg, toUserName)</td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> r[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseResponse<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>Ret<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">__upload_file</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">fileDir</span>, <span class="pl-smi">isPicture</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>, <span class="pl-smi">isVideo</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> tools.check_file(fileDir): <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-v">self</span>.loginInfo.get(<span class="pl-s"><span class="pl-pds">&#39;</span>fileUrl<span class="pl-pds">&#39;</span></span>, <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>]) <span class="pl-k">+</span> \</td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>/webwxuploadmedia?f=json<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># save it on server</span></td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code blob-code-inner js-file-line">        fileSize <span class="pl-k">=</span> <span class="pl-c1">str</span>(os.path.getsize(fileDir))</td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code blob-code-inner js-file-line">        cookiesList <span class="pl-k">=</span> {name:data <span class="pl-k">for</span> name,data <span class="pl-k">in</span> <span class="pl-v">self</span>.s.cookies.items()}</td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code blob-code-inner js-file-line">        fileType <span class="pl-k">=</span> mimetypes.guess_type(fileDir)[<span class="pl-c1">0</span>] <span class="pl-k">or</span> <span class="pl-s"><span class="pl-pds">&#39;</span>application/octet-stream<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code blob-code-inner js-file-line">        files <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span>: (<span class="pl-c1">None</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>WU_FILE_0<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>: (<span class="pl-c1">None</span>, os.path.basename(fileDir)),</td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>type<span class="pl-pds">&#39;</span></span>: (<span class="pl-c1">None</span>, fileType),</td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>lastModifiedDate<span class="pl-pds">&#39;</span></span>: (<span class="pl-c1">None</span>, time.strftime(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%a</span> %b <span class="pl-c1">%d</span> %Y %H:%M:%S GMT+0800 (CST)<span class="pl-pds">&#39;</span></span>)),</td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>size<span class="pl-pds">&#39;</span></span>: (<span class="pl-c1">None</span>, fileSize),</td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>mediatype<span class="pl-pds">&#39;</span></span>: (<span class="pl-c1">None</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>pic<span class="pl-pds">&#39;</span></span> <span class="pl-k">if</span> isPicture <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>video<span class="pl-pds">&#39;</span></span> <span class="pl-k">if</span> isVideo <span class="pl-k">else</span><span class="pl-s"><span class="pl-pds">&#39;</span>doc<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>uploadmediarequest<span class="pl-pds">&#39;</span></span>: (<span class="pl-c1">None</span>, json.dumps({</td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>ClientMediaId<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">int</span>(time.time()),</td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>TotalLen<span class="pl-pds">&#39;</span></span>: fileSize,</td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>StartPos<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">0</span>,</td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>DataLen<span class="pl-pds">&#39;</span></span>: fileSize,</td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>MediaType<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">4</span>, }, <span class="pl-v">separators</span> <span class="pl-k">=</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>:<span class="pl-pds">&#39;</span></span>))),</td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>webwx_data_ticket<span class="pl-pds">&#39;</span></span>: (<span class="pl-c1">None</span>, cookiesList[<span class="pl-s"><span class="pl-pds">&#39;</span>webwx_data_ticket<span class="pl-pds">&#39;</span></span>]),</td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>pass_ticket<span class="pl-pds">&#39;</span></span>: (<span class="pl-c1">None</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>undefined<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L579" class="blob-num js-line-number" data-line-number="579"></td>
        <td id="LC579" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>filename<span class="pl-pds">&#39;</span></span> : (os.path.basename(fileDir), <span class="pl-c1">open</span>(fileDir, <span class="pl-s"><span class="pl-pds">&#39;</span>rb<span class="pl-pds">&#39;</span></span>), fileType), }</td>
      </tr>
      <tr>
        <td id="L580" class="blob-num js-line-number" data-line-number="580"></td>
        <td id="LC580" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> { <span class="pl-s"><span class="pl-pds">&#39;</span>User-Agent<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36<span class="pl-pds">&#39;</span></span>, }</td>
      </tr>
      <tr>
        <td id="L581" class="blob-num js-line-number" data-line-number="581"></td>
        <td id="LC581" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.post(url, <span class="pl-v">files</span> <span class="pl-k">=</span> files, <span class="pl-v">headers</span> <span class="pl-k">=</span> headers)</td>
      </tr>
      <tr>
        <td id="L582" class="blob-num js-line-number" data-line-number="582"></td>
        <td id="LC582" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> json.loads(r.text)[<span class="pl-s"><span class="pl-pds">&#39;</span>MediaId<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L583" class="blob-num js-line-number" data-line-number="583"></td>
        <td id="LC583" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">send_file</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">fileDir</span>, <span class="pl-smi">toUserName</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L584" class="blob-num js-line-number" data-line-number="584"></td>
        <td id="LC584" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> toUserName <span class="pl-k">is</span> <span class="pl-c1">None</span>: toUserName <span class="pl-k">=</span> <span class="pl-v">self</span>.storageClass.userName</td>
      </tr>
      <tr>
        <td id="L585" class="blob-num js-line-number" data-line-number="585"></td>
        <td id="LC585" class="blob-code blob-code-inner js-file-line">        mediaId <span class="pl-k">=</span> <span class="pl-v">self</span>.__upload_file(fileDir)</td>
      </tr>
      <tr>
        <td id="L586" class="blob-num js-line-number" data-line-number="586"></td>
        <td id="LC586" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> mediaId <span class="pl-k">is</span> <span class="pl-c1">None</span>: <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L587" class="blob-num js-line-number" data-line-number="587"></td>
        <td id="LC587" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxsendappmsg?fun=async&amp;f=json<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L588" class="blob-num js-line-number" data-line-number="588"></td>
        <td id="LC588" class="blob-code blob-code-inner js-file-line">        data <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L589" class="blob-num js-line-number" data-line-number="589"></td>
        <td id="LC589" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L590" class="blob-num js-line-number" data-line-number="590"></td>
        <td id="LC590" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>Msg<span class="pl-pds">&#39;</span></span>: {</td>
      </tr>
      <tr>
        <td id="L591" class="blob-num js-line-number" data-line-number="591"></td>
        <td id="LC591" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">6</span>,</td>
      </tr>
      <tr>
        <td id="L592" class="blob-num js-line-number" data-line-number="592"></td>
        <td id="LC592" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>Content<span class="pl-pds">&#39;</span></span>: (<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;appmsg appid=&#39;wxeb7ec651dd0aefa9&#39; sdkver=&#39;&#39;&gt;&lt;title&gt;<span class="pl-c1">%s</span>&lt;/title&gt;<span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>os.path.basename(fileDir) <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L593" class="blob-num js-line-number" data-line-number="593"></td>
        <td id="LC593" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&quot;</span>&lt;des&gt;&lt;/des&gt;&lt;action&gt;&lt;/action&gt;&lt;type&gt;6&lt;/type&gt;&lt;content&gt;&lt;/content&gt;&lt;url&gt;&lt;/url&gt;&lt;lowurl&gt;&lt;/lowurl&gt;<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L594" class="blob-num js-line-number" data-line-number="594"></td>
        <td id="LC594" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&quot;</span>&lt;appattach&gt;&lt;totallen&gt;<span class="pl-c1">%s</span>&lt;/totallen&gt;&lt;attachid&gt;<span class="pl-c1">%s</span>&lt;/attachid&gt;<span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">str</span>(os.path.getsize(fileDir)), mediaId) <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L595" class="blob-num js-line-number" data-line-number="595"></td>
        <td id="LC595" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&quot;</span>&lt;fileext&gt;<span class="pl-c1">%s</span>&lt;/fileext&gt;&lt;/appattach&gt;&lt;extinfo&gt;&lt;/extinfo&gt;&lt;/appmsg&gt;<span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>os.path.splitext(fileDir)[<span class="pl-c1">1</span>].replace(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)),</td>
      </tr>
      <tr>
        <td id="L596" class="blob-num js-line-number" data-line-number="596"></td>
        <td id="LC596" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>FromUserName<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.storageClass.userName,</td>
      </tr>
      <tr>
        <td id="L597" class="blob-num js-line-number" data-line-number="597"></td>
        <td id="LC597" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>ToUserName<span class="pl-pds">&#39;</span></span>: toUserName,</td>
      </tr>
      <tr>
        <td id="L598" class="blob-num js-line-number" data-line-number="598"></td>
        <td id="LC598" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>LocalID<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L599" class="blob-num js-line-number" data-line-number="599"></td>
        <td id="LC599" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>ClientMsgId<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>], }, }</td>
      </tr>
      <tr>
        <td id="L600" class="blob-num js-line-number" data-line-number="600"></td>
        <td id="LC600" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L601" class="blob-num js-line-number" data-line-number="601"></td>
        <td id="LC601" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L602" class="blob-num js-line-number" data-line-number="602"></td>
        <td id="LC602" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>User-Agent<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L603" class="blob-num js-line-number" data-line-number="603"></td>
        <td id="LC603" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>Content-Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json;charset=UTF-8<span class="pl-pds">&#39;</span></span>, }</td>
      </tr>
      <tr>
        <td id="L604" class="blob-num js-line-number" data-line-number="604"></td>
        <td id="LC604" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.post(url, <span class="pl-v">data</span><span class="pl-k">=</span>json.dumps(data, <span class="pl-v">ensure_ascii</span><span class="pl-k">=</span><span class="pl-c1">False</span>).encode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf8<span class="pl-pds">&#39;</span></span>), <span class="pl-v">headers</span><span class="pl-k">=</span>headers)</td>
      </tr>
      <tr>
        <td id="L605" class="blob-num js-line-number" data-line-number="605"></td>
        <td id="LC605" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L606" class="blob-num js-line-number" data-line-number="606"></td>
        <td id="LC606" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">send_image</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">fileDir</span>, <span class="pl-smi">toUserName</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L607" class="blob-num js-line-number" data-line-number="607"></td>
        <td id="LC607" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> toUserName <span class="pl-k">is</span> <span class="pl-c1">None</span>: toUserName <span class="pl-k">=</span> <span class="pl-v">self</span>.storageClass.userName</td>
      </tr>
      <tr>
        <td id="L608" class="blob-num js-line-number" data-line-number="608"></td>
        <td id="LC608" class="blob-code blob-code-inner js-file-line">        mediaId <span class="pl-k">=</span> <span class="pl-v">self</span>.__upload_file(fileDir, <span class="pl-v">isPicture</span><span class="pl-k">=</span><span class="pl-k">not</span> fileDir[<span class="pl-k">-</span><span class="pl-c1">4</span>:] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.gif<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L609" class="blob-num js-line-number" data-line-number="609"></td>
        <td id="LC609" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> mediaId <span class="pl-k">is</span> <span class="pl-c1">None</span>: <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L610" class="blob-num js-line-number" data-line-number="610"></td>
        <td id="LC610" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxsendmsgimg?fun=async&amp;f=json<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L611" class="blob-num js-line-number" data-line-number="611"></td>
        <td id="LC611" class="blob-code blob-code-inner js-file-line">        data <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L612" class="blob-num js-line-number" data-line-number="612"></td>
        <td id="LC612" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L613" class="blob-num js-line-number" data-line-number="613"></td>
        <td id="LC613" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>Msg<span class="pl-pds">&#39;</span></span>: {</td>
      </tr>
      <tr>
        <td id="L614" class="blob-num js-line-number" data-line-number="614"></td>
        <td id="LC614" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">3</span>,</td>
      </tr>
      <tr>
        <td id="L615" class="blob-num js-line-number" data-line-number="615"></td>
        <td id="LC615" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>MediaId<span class="pl-pds">&#39;</span></span>: mediaId,</td>
      </tr>
      <tr>
        <td id="L616" class="blob-num js-line-number" data-line-number="616"></td>
        <td id="LC616" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>FromUserName<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.storageClass.userName,</td>
      </tr>
      <tr>
        <td id="L617" class="blob-num js-line-number" data-line-number="617"></td>
        <td id="LC617" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>ToUserName<span class="pl-pds">&#39;</span></span>: toUserName,</td>
      </tr>
      <tr>
        <td id="L618" class="blob-num js-line-number" data-line-number="618"></td>
        <td id="LC618" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>LocalID<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L619" class="blob-num js-line-number" data-line-number="619"></td>
        <td id="LC619" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>ClientMsgId<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>], }, }</td>
      </tr>
      <tr>
        <td id="L620" class="blob-num js-line-number" data-line-number="620"></td>
        <td id="LC620" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L621" class="blob-num js-line-number" data-line-number="621"></td>
        <td id="LC621" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> fileDir[<span class="pl-k">-</span><span class="pl-c1">4</span>:] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.gif<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L622" class="blob-num js-line-number" data-line-number="622"></td>
        <td id="LC622" class="blob-code blob-code-inner js-file-line">            url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxsendemoticon?fun=sys<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L623" class="blob-num js-line-number" data-line-number="623"></td>
        <td id="LC623" class="blob-code blob-code-inner js-file-line">            data[<span class="pl-s"><span class="pl-pds">&#39;</span>Msg<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">47</span></td>
      </tr>
      <tr>
        <td id="L624" class="blob-num js-line-number" data-line-number="624"></td>
        <td id="LC624" class="blob-code blob-code-inner js-file-line">            data[<span class="pl-s"><span class="pl-pds">&#39;</span>Msg<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>EmojiFlag<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">2</span></td>
      </tr>
      <tr>
        <td id="L625" class="blob-num js-line-number" data-line-number="625"></td>
        <td id="LC625" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L626" class="blob-num js-line-number" data-line-number="626"></td>
        <td id="LC626" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>User-Agent<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L627" class="blob-num js-line-number" data-line-number="627"></td>
        <td id="LC627" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>Content-Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json;charset=UTF-8<span class="pl-pds">&#39;</span></span>, }</td>
      </tr>
      <tr>
        <td id="L628" class="blob-num js-line-number" data-line-number="628"></td>
        <td id="LC628" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.post(url, <span class="pl-v">data</span><span class="pl-k">=</span>json.dumps(data, <span class="pl-v">ensure_ascii</span><span class="pl-k">=</span><span class="pl-c1">False</span>).encode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf8<span class="pl-pds">&#39;</span></span>), <span class="pl-v">headers</span><span class="pl-k">=</span>headers)</td>
      </tr>
      <tr>
        <td id="L629" class="blob-num js-line-number" data-line-number="629"></td>
        <td id="LC629" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L630" class="blob-num js-line-number" data-line-number="630"></td>
        <td id="LC630" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">send_video</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">fileDir</span>, <span class="pl-smi">toUserName</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L631" class="blob-num js-line-number" data-line-number="631"></td>
        <td id="LC631" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> toUserName <span class="pl-k">is</span> <span class="pl-c1">None</span>: toUserName <span class="pl-k">=</span> <span class="pl-v">self</span>.storageClass.userName</td>
      </tr>
      <tr>
        <td id="L632" class="blob-num js-line-number" data-line-number="632"></td>
        <td id="LC632" class="blob-code blob-code-inner js-file-line">        mediaId <span class="pl-k">=</span> <span class="pl-v">self</span>.__upload_file(fileDir, <span class="pl-v">isVideo</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L633" class="blob-num js-line-number" data-line-number="633"></td>
        <td id="LC633" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> mediaId <span class="pl-k">is</span> <span class="pl-c1">None</span>: <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L634" class="blob-num js-line-number" data-line-number="634"></td>
        <td id="LC634" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxsendvideomsg?fun=async&amp;f=json&amp;pass_ticket=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (</td>
      </tr>
      <tr>
        <td id="L635" class="blob-num js-line-number" data-line-number="635"></td>
        <td id="LC635" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>pass_ticket<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L636" class="blob-num js-line-number" data-line-number="636"></td>
        <td id="LC636" class="blob-code blob-code-inner js-file-line">        payloads <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L637" class="blob-num js-line-number" data-line-number="637"></td>
        <td id="LC637" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L638" class="blob-num js-line-number" data-line-number="638"></td>
        <td id="LC638" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>Msg<span class="pl-pds">&#39;</span></span>: {</td>
      </tr>
      <tr>
        <td id="L639" class="blob-num js-line-number" data-line-number="639"></td>
        <td id="LC639" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>         : <span class="pl-c1">43</span>,</td>
      </tr>
      <tr>
        <td id="L640" class="blob-num js-line-number" data-line-number="640"></td>
        <td id="LC640" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>MediaId<span class="pl-pds">&#39;</span></span>      : mediaId,</td>
      </tr>
      <tr>
        <td id="L641" class="blob-num js-line-number" data-line-number="641"></td>
        <td id="LC641" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>FromUserName<span class="pl-pds">&#39;</span></span> : <span class="pl-v">self</span>.storageClass.userName,</td>
      </tr>
      <tr>
        <td id="L642" class="blob-num js-line-number" data-line-number="642"></td>
        <td id="LC642" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>ToUserName<span class="pl-pds">&#39;</span></span>   : toUserName,</td>
      </tr>
      <tr>
        <td id="L643" class="blob-num js-line-number" data-line-number="643"></td>
        <td id="LC643" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>LocalID<span class="pl-pds">&#39;</span></span>      : <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L644" class="blob-num js-line-number" data-line-number="644"></td>
        <td id="LC644" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>ClientMsgId<span class="pl-pds">&#39;</span></span>  : <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>], },</td>
      </tr>
      <tr>
        <td id="L645" class="blob-num js-line-number" data-line-number="645"></td>
        <td id="LC645" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>Scene<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">0</span>, }</td>
      </tr>
      <tr>
        <td id="L646" class="blob-num js-line-number" data-line-number="646"></td>
        <td id="LC646" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>msgid<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L647" class="blob-num js-line-number" data-line-number="647"></td>
        <td id="LC647" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L648" class="blob-num js-line-number" data-line-number="648"></td>
        <td id="LC648" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>User-Agent<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L649" class="blob-num js-line-number" data-line-number="649"></td>
        <td id="LC649" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>Content-Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json;charset=UTF-8<span class="pl-pds">&#39;</span></span>, }</td>
      </tr>
      <tr>
        <td id="L650" class="blob-num js-line-number" data-line-number="650"></td>
        <td id="LC650" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.post(url, <span class="pl-v">data</span><span class="pl-k">=</span>json.dumps(data, <span class="pl-v">ensure_ascii</span><span class="pl-k">=</span><span class="pl-c1">False</span>).encode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf8<span class="pl-pds">&#39;</span></span>), <span class="pl-v">headers</span><span class="pl-k">=</span>headers)</td>
      </tr>
      <tr>
        <td id="L651" class="blob-num js-line-number" data-line-number="651"></td>
        <td id="LC651" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L652" class="blob-num js-line-number" data-line-number="652"></td>
        <td id="LC652" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">set_alias</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">userName</span>, <span class="pl-smi">alias</span>):</td>
      </tr>
      <tr>
        <td id="L653" class="blob-num js-line-number" data-line-number="653"></td>
        <td id="LC653" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxoplog?lang=<span class="pl-c1">%s</span>&amp;pass_ticket=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span>(</td>
      </tr>
      <tr>
        <td id="L654" class="blob-num js-line-number" data-line-number="654"></td>
        <td id="LC654" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], <span class="pl-s"><span class="pl-pds">&#39;</span>zh_CN<span class="pl-pds">&#39;</span></span>, <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>pass_ticket<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L655" class="blob-num js-line-number" data-line-number="655"></td>
        <td id="LC655" class="blob-code blob-code-inner js-file-line">        data <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L656" class="blob-num js-line-number" data-line-number="656"></td>
        <td id="LC656" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>    : userName,</td>
      </tr>
      <tr>
        <td id="L657" class="blob-num js-line-number" data-line-number="657"></td>
        <td id="LC657" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>CmdId<span class="pl-pds">&#39;</span></span>       : <span class="pl-c1">2</span>,</td>
      </tr>
      <tr>
        <td id="L658" class="blob-num js-line-number" data-line-number="658"></td>
        <td id="LC658" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>RemarkName<span class="pl-pds">&#39;</span></span>  : alias,</td>
      </tr>
      <tr>
        <td id="L659" class="blob-num js-line-number" data-line-number="659"></td>
        <td id="LC659" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span> : <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>], }</td>
      </tr>
      <tr>
        <td id="L660" class="blob-num js-line-number" data-line-number="660"></td>
        <td id="LC660" class="blob-code blob-code-inner js-file-line">        j <span class="pl-k">=</span> <span class="pl-v">self</span>.s.post(url, json.dumps(data, <span class="pl-v">ensure_ascii</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>).encode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf8<span class="pl-pds">&#39;</span></span>)).json()</td>
      </tr>
      <tr>
        <td id="L661" class="blob-num js-line-number" data-line-number="661"></td>
        <td id="LC661" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> j[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseResponse<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>Ret<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L662" class="blob-num js-line-number" data-line-number="662"></td>
        <td id="LC662" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">add_friend</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">userName</span>, <span class="pl-smi">status</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-smi">ticket</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>, <span class="pl-smi">userInfo</span><span class="pl-k">=</span>{}):</td>
      </tr>
      <tr>
        <td id="L663" class="blob-num js-line-number" data-line-number="663"></td>
        <td id="LC663" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span> Add a friend or accept a friend</span></td>
      </tr>
      <tr>
        <td id="L664" class="blob-num js-line-number" data-line-number="664"></td>
        <td id="LC664" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            * for adding status should be 2</span></td>
      </tr>
      <tr>
        <td id="L665" class="blob-num js-line-number" data-line-number="665"></td>
        <td id="LC665" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            * for accepting status should be 3 <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L666" class="blob-num js-line-number" data-line-number="666"></td>
        <td id="LC666" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxverifyuser?r=<span class="pl-c1">%s</span>&amp;pass_ticket=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span>(<span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], <span class="pl-c1">int</span>(time.time()), <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>pass_ticket<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L667" class="blob-num js-line-number" data-line-number="667"></td>
        <td id="LC667" class="blob-code blob-code-inner js-file-line">        payloads <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L668" class="blob-num js-line-number" data-line-number="668"></td>
        <td id="LC668" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L669" class="blob-num js-line-number" data-line-number="669"></td>
        <td id="LC669" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>Opcode<span class="pl-pds">&#39;</span></span>: status, <span class="pl-c"># 3</span></td>
      </tr>
      <tr>
        <td id="L670" class="blob-num js-line-number" data-line-number="670"></td>
        <td id="LC670" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>VerifyUserListSize<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">1</span>,</td>
      </tr>
      <tr>
        <td id="L671" class="blob-num js-line-number" data-line-number="671"></td>
        <td id="LC671" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>VerifyUserList<span class="pl-pds">&#39;</span></span>: [{</td>
      </tr>
      <tr>
        <td id="L672" class="blob-num js-line-number" data-line-number="672"></td>
        <td id="LC672" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>Value<span class="pl-pds">&#39;</span></span>: userName,</td>
      </tr>
      <tr>
        <td id="L673" class="blob-num js-line-number" data-line-number="673"></td>
        <td id="LC673" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>VerifyUserTicket<span class="pl-pds">&#39;</span></span>: ticket, }], <span class="pl-c"># &#39;&#39;</span></td>
      </tr>
      <tr>
        <td id="L674" class="blob-num js-line-number" data-line-number="674"></td>
        <td id="LC674" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>VerifyContent<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L675" class="blob-num js-line-number" data-line-number="675"></td>
        <td id="LC675" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>SceneListCount<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">1</span>,</td>
      </tr>
      <tr>
        <td id="L676" class="blob-num js-line-number" data-line-number="676"></td>
        <td id="LC676" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>SceneList<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">33</span>, <span class="pl-c"># [33]</span></td>
      </tr>
      <tr>
        <td id="L677" class="blob-num js-line-number" data-line-number="677"></td>
        <td id="LC677" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>skey<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>skey<span class="pl-pds">&#39;</span></span>], }</td>
      </tr>
      <tr>
        <td id="L678" class="blob-num js-line-number" data-line-number="678"></td>
        <td id="LC678" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> { <span class="pl-s"><span class="pl-pds">&#39;</span>ContentType<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json; charset=UTF-8<span class="pl-pds">&#39;</span></span> }</td>
      </tr>
      <tr>
        <td id="L679" class="blob-num js-line-number" data-line-number="679"></td>
        <td id="LC679" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.post(url, <span class="pl-v">data</span> <span class="pl-k">=</span> json.dumps(payloads), <span class="pl-v">headers</span> <span class="pl-k">=</span> headers)</td>
      </tr>
      <tr>
        <td id="L680" class="blob-num js-line-number" data-line-number="680"></td>
        <td id="LC680" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> userInfo: <span class="pl-c"># add user to storage</span></td>
      </tr>
      <tr>
        <td id="L681" class="blob-num js-line-number" data-line-number="681"></td>
        <td id="LC681" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.memberList.append(tools.struct_friend_info(userInfo))</td>
      </tr>
      <tr>
        <td id="L682" class="blob-num js-line-number" data-line-number="682"></td>
        <td id="LC682" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> r.json()</td>
      </tr>
      <tr>
        <td id="L683" class="blob-num js-line-number" data-line-number="683"></td>
        <td id="LC683" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_head_img</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">userName</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">chatroomUserName</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">picDir</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L684" class="blob-num js-line-number" data-line-number="684"></td>
        <td id="LC684" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span> get head image</span></td>
      </tr>
      <tr>
        <td id="L685" class="blob-num js-line-number" data-line-number="685"></td>
        <td id="LC685" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         * if you want to get chatroom header: only set chatroomUserName</span></td>
      </tr>
      <tr>
        <td id="L686" class="blob-num js-line-number" data-line-number="686"></td>
        <td id="LC686" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         * if you want to get friend header: only set userName</span></td>
      </tr>
      <tr>
        <td id="L687" class="blob-num js-line-number" data-line-number="687"></td>
        <td id="LC687" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         * if you want to get chatroom member header: set both</span></td>
      </tr>
      <tr>
        <td id="L688" class="blob-num js-line-number" data-line-number="688"></td>
        <td id="LC688" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L689" class="blob-num js-line-number" data-line-number="689"></td>
        <td id="LC689" class="blob-code blob-code-inner js-file-line">        params <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L690" class="blob-num js-line-number" data-line-number="690"></td>
        <td id="LC690" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>userName<span class="pl-pds">&#39;</span></span>: userName <span class="pl-k">or</span> chatroomUserName,</td>
      </tr>
      <tr>
        <td id="L691" class="blob-num js-line-number" data-line-number="691"></td>
        <td id="LC691" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>skey<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>skey<span class="pl-pds">&#39;</span></span>], }</td>
      </tr>
      <tr>
        <td id="L692" class="blob-num js-line-number" data-line-number="692"></td>
        <td id="LC692" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxgeticon<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L693" class="blob-num js-line-number" data-line-number="693"></td>
        <td id="LC693" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> chatroomUserName <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L694" class="blob-num js-line-number" data-line-number="694"></td>
        <td id="LC694" class="blob-code blob-code-inner js-file-line">            infoDict <span class="pl-k">=</span> <span class="pl-v">self</span>.storageClass.search_friends(<span class="pl-v">userName</span><span class="pl-k">=</span>userName)</td>
      </tr>
      <tr>
        <td id="L695" class="blob-num js-line-number" data-line-number="695"></td>
        <td id="LC695" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> infoDict <span class="pl-k">is</span> <span class="pl-c1">None</span>: <span class="pl-k">return</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L696" class="blob-num js-line-number" data-line-number="696"></td>
        <td id="LC696" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L697" class="blob-num js-line-number" data-line-number="697"></td>
        <td id="LC697" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> userName <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L698" class="blob-num js-line-number" data-line-number="698"></td>
        <td id="LC698" class="blob-code blob-code-inner js-file-line">                url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxgetheadimg<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L699" class="blob-num js-line-number" data-line-number="699"></td>
        <td id="LC699" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L700" class="blob-num js-line-number" data-line-number="700"></td>
        <td id="LC700" class="blob-code blob-code-inner js-file-line">                chatroom <span class="pl-k">=</span> <span class="pl-v">self</span>.storageClass.search_chatrooms(<span class="pl-v">userName</span><span class="pl-k">=</span>chatroomUserName)</td>
      </tr>
      <tr>
        <td id="L701" class="blob-num js-line-number" data-line-number="701"></td>
        <td id="LC701" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> chatroomUserName <span class="pl-k">is</span> <span class="pl-c1">None</span>: <span class="pl-k">return</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L702" class="blob-num js-line-number" data-line-number="702"></td>
        <td id="LC702" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>EncryChatRoomId<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L703" class="blob-num js-line-number" data-line-number="703"></td>
        <td id="LC703" class="blob-code blob-code-inner js-file-line">                    chatroom <span class="pl-k">=</span> <span class="pl-v">self</span>.update_chatroom(chatroomUserName)</td>
      </tr>
      <tr>
        <td id="L704" class="blob-num js-line-number" data-line-number="704"></td>
        <td id="LC704" class="blob-code blob-code-inner js-file-line">                params[<span class="pl-s"><span class="pl-pds">&#39;</span>chatroomid<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>EncryChatRoomId<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L705" class="blob-num js-line-number" data-line-number="705"></td>
        <td id="LC705" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.get(url, <span class="pl-v">params</span><span class="pl-k">=</span>params, <span class="pl-v">stream</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L706" class="blob-num js-line-number" data-line-number="706"></td>
        <td id="LC706" class="blob-code blob-code-inner js-file-line">        tempStorage <span class="pl-k">=</span> io.BytesIO()</td>
      </tr>
      <tr>
        <td id="L707" class="blob-num js-line-number" data-line-number="707"></td>
        <td id="LC707" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> block <span class="pl-k">in</span> r.iter_content(<span class="pl-c1">1024</span>):</td>
      </tr>
      <tr>
        <td id="L708" class="blob-num js-line-number" data-line-number="708"></td>
        <td id="LC708" class="blob-code blob-code-inner js-file-line">            tempStorage.write(block)</td>
      </tr>
      <tr>
        <td id="L709" class="blob-num js-line-number" data-line-number="709"></td>
        <td id="LC709" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> picDir <span class="pl-k">is</span> <span class="pl-c1">None</span>: <span class="pl-k">return</span> tempStorage.getvalue()</td>
      </tr>
      <tr>
        <td id="L710" class="blob-num js-line-number" data-line-number="710"></td>
        <td id="LC710" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-c1">open</span>(picDir, <span class="pl-s"><span class="pl-pds">&#39;</span>wb<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f: f.write(tempStorage.getvalue())</td>
      </tr>
      <tr>
        <td id="L711" class="blob-num js-line-number" data-line-number="711"></td>
        <td id="LC711" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">create_chatroom</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">memberList</span>, <span class="pl-smi">topic</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L712" class="blob-num js-line-number" data-line-number="712"></td>
        <td id="LC712" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> (<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxcreatechatroom?pass_ticket=<span class="pl-c1">%s</span>&amp;r=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span>(</td>
      </tr>
      <tr>
        <td id="L713" class="blob-num js-line-number" data-line-number="713"></td>
        <td id="LC713" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>pass_ticket<span class="pl-pds">&#39;</span></span>], <span class="pl-c1">int</span>(time.time())))</td>
      </tr>
      <tr>
        <td id="L714" class="blob-num js-line-number" data-line-number="714"></td>
        <td id="LC714" class="blob-code blob-code-inner js-file-line">        data <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L715" class="blob-num js-line-number" data-line-number="715"></td>
        <td id="LC715" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L716" class="blob-num js-line-number" data-line-number="716"></td>
        <td id="LC716" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>MemberCount<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">len</span>(memberList),</td>
      </tr>
      <tr>
        <td id="L717" class="blob-num js-line-number" data-line-number="717"></td>
        <td id="LC717" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>MemberList<span class="pl-pds">&#39;</span></span>: [{<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>: member[<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>]} <span class="pl-k">for</span> member <span class="pl-k">in</span> memberList],</td>
      </tr>
      <tr>
        <td id="L718" class="blob-num js-line-number" data-line-number="718"></td>
        <td id="LC718" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>Topic<span class="pl-pds">&#39;</span></span>: topic, }</td>
      </tr>
      <tr>
        <td id="L719" class="blob-num js-line-number" data-line-number="719"></td>
        <td id="LC719" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>content-type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json; charset=UTF-8<span class="pl-pds">&#39;</span></span>}</td>
      </tr>
      <tr>
        <td id="L720" class="blob-num js-line-number" data-line-number="720"></td>
        <td id="LC720" class="blob-code blob-code-inner js-file-line">        r <span class="pl-k">=</span> <span class="pl-v">self</span>.s.post(url, <span class="pl-v">data</span><span class="pl-k">=</span>json.dumps(data, <span class="pl-v">ensure_ascii</span><span class="pl-k">=</span><span class="pl-c1">False</span>).encode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf8<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>ignore<span class="pl-pds">&#39;</span></span>),<span class="pl-v">headers</span><span class="pl-k">=</span>headers)</td>
      </tr>
      <tr>
        <td id="L721" class="blob-num js-line-number" data-line-number="721"></td>
        <td id="LC721" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> r.json()</td>
      </tr>
      <tr>
        <td id="L722" class="blob-num js-line-number" data-line-number="722"></td>
        <td id="LC722" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">set_chatroom_name</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">chatroomUserName</span>, <span class="pl-smi">name</span>):</td>
      </tr>
      <tr>
        <td id="L723" class="blob-num js-line-number" data-line-number="723"></td>
        <td id="LC723" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> (<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxupdatechatroom?fun=modtopic&amp;pass_ticket=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span>(</td>
      </tr>
      <tr>
        <td id="L724" class="blob-num js-line-number" data-line-number="724"></td>
        <td id="LC724" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>pass_ticket<span class="pl-pds">&#39;</span></span>]))</td>
      </tr>
      <tr>
        <td id="L725" class="blob-num js-line-number" data-line-number="725"></td>
        <td id="LC725" class="blob-code blob-code-inner js-file-line">        data <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L726" class="blob-num js-line-number" data-line-number="726"></td>
        <td id="LC726" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L727" class="blob-num js-line-number" data-line-number="727"></td>
        <td id="LC727" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>ChatRoomName<span class="pl-pds">&#39;</span></span>: chatroomUserName,</td>
      </tr>
      <tr>
        <td id="L728" class="blob-num js-line-number" data-line-number="728"></td>
        <td id="LC728" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>NewTopic<span class="pl-pds">&#39;</span></span>: name, }</td>
      </tr>
      <tr>
        <td id="L729" class="blob-num js-line-number" data-line-number="729"></td>
        <td id="LC729" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>content-type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json; charset=UTF-8<span class="pl-pds">&#39;</span></span>}</td>
      </tr>
      <tr>
        <td id="L730" class="blob-num js-line-number" data-line-number="730"></td>
        <td id="LC730" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-v">self</span>.s.post(url, <span class="pl-v">data</span><span class="pl-k">=</span>json.dumps(data, <span class="pl-v">ensure_ascii</span><span class="pl-k">=</span><span class="pl-c1">False</span>).encode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf8<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>ignore<span class="pl-pds">&#39;</span></span>), <span class="pl-v">headers</span><span class="pl-k">=</span>headers).json()</td>
      </tr>
      <tr>
        <td id="L731" class="blob-num js-line-number" data-line-number="731"></td>
        <td id="LC731" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">delete_member_from_chatroom</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">chatroomUserName</span>, <span class="pl-smi">memberList</span>):</td>
      </tr>
      <tr>
        <td id="L732" class="blob-num js-line-number" data-line-number="732"></td>
        <td id="LC732" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> (<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxupdatechatroom?fun=delmember&amp;pass_ticket=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span>(</td>
      </tr>
      <tr>
        <td id="L733" class="blob-num js-line-number" data-line-number="733"></td>
        <td id="LC733" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>pass_ticket<span class="pl-pds">&#39;</span></span>]))</td>
      </tr>
      <tr>
        <td id="L734" class="blob-num js-line-number" data-line-number="734"></td>
        <td id="LC734" class="blob-code blob-code-inner js-file-line">        params <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L735" class="blob-num js-line-number" data-line-number="735"></td>
        <td id="LC735" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>: <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L736" class="blob-num js-line-number" data-line-number="736"></td>
        <td id="LC736" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>ChatRoomName<span class="pl-pds">&#39;</span></span>: chatroomUserName,</td>
      </tr>
      <tr>
        <td id="L737" class="blob-num js-line-number" data-line-number="737"></td>
        <td id="LC737" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>DelMemberList<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>.join([member[<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>] <span class="pl-k">for</span> member <span class="pl-k">in</span> memberList]), }</td>
      </tr>
      <tr>
        <td id="L738" class="blob-num js-line-number" data-line-number="738"></td>
        <td id="LC738" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>content-type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json; charset=UTF-8<span class="pl-pds">&#39;</span></span>}</td>
      </tr>
      <tr>
        <td id="L739" class="blob-num js-line-number" data-line-number="739"></td>
        <td id="LC739" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-v">self</span>.s.post(url, <span class="pl-v">data</span><span class="pl-k">=</span>json.dumps(params),<span class="pl-v">headers</span><span class="pl-k">=</span>headers).json()</td>
      </tr>
      <tr>
        <td id="L740" class="blob-num js-line-number" data-line-number="740"></td>
        <td id="LC740" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">add_member_into_chatroom</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">chatroomUserName</span>, <span class="pl-smi">memberList</span>,</td>
      </tr>
      <tr>
        <td id="L741" class="blob-num js-line-number" data-line-number="741"></td>
        <td id="LC741" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">useInvitation</span><span class="pl-k">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L742" class="blob-num js-line-number" data-line-number="742"></td>
        <td id="LC742" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span> add or invite member into chatroom</span></td>
      </tr>
      <tr>
        <td id="L743" class="blob-num js-line-number" data-line-number="743"></td>
        <td id="LC743" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         * there are two ways to get members into chatroom: invite or directly add</span></td>
      </tr>
      <tr>
        <td id="L744" class="blob-num js-line-number" data-line-number="744"></td>
        <td id="LC744" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         * but for chatrooms with more than 40 users, you can only use invite</span></td>
      </tr>
      <tr>
        <td id="L745" class="blob-num js-line-number" data-line-number="745"></td>
        <td id="LC745" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         * but don&#39;t worry we will auto-force userInvitation for you when necessary</span></td>
      </tr>
      <tr>
        <td id="L746" class="blob-num js-line-number" data-line-number="746"></td>
        <td id="LC746" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L747" class="blob-num js-line-number" data-line-number="747"></td>
        <td id="LC747" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> useInvitation:</td>
      </tr>
      <tr>
        <td id="L748" class="blob-num js-line-number" data-line-number="748"></td>
        <td id="LC748" class="blob-code blob-code-inner js-file-line">            chatroom <span class="pl-k">=</span> <span class="pl-v">self</span>.storageClass.search_chatrooms(<span class="pl-v">userName</span><span class="pl-k">=</span>chatroomUserName)</td>
      </tr>
      <tr>
        <td id="L749" class="blob-num js-line-number" data-line-number="749"></td>
        <td id="LC749" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> chatroom: chatroom <span class="pl-k">=</span> <span class="pl-v">self</span>.update_chatroom(chatroomUserName)</td>
      </tr>
      <tr>
        <td id="L750" class="blob-num js-line-number" data-line-number="750"></td>
        <td id="LC750" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(chatroom[<span class="pl-s"><span class="pl-pds">&#39;</span>MemberList<span class="pl-pds">&#39;</span></span>]) <span class="pl-k">&gt;</span> <span class="pl-c1">40</span>: useInvitation <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L751" class="blob-num js-line-number" data-line-number="751"></td>
        <td id="LC751" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> useInvitation:</td>
      </tr>
      <tr>
        <td id="L752" class="blob-num js-line-number" data-line-number="752"></td>
        <td id="LC752" class="blob-code blob-code-inner js-file-line">            fun, memberKeyName <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>invitemember<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>InviteMemberList<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L753" class="blob-num js-line-number" data-line-number="753"></td>
        <td id="LC753" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L754" class="blob-num js-line-number" data-line-number="754"></td>
        <td id="LC754" class="blob-code blob-code-inner js-file-line">            fun, memberKeyName <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>addmember<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>AddMsgList<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L755" class="blob-num js-line-number" data-line-number="755"></td>
        <td id="LC755" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> (<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/webwxupdatechatroom?fun=<span class="pl-c1">%s</span>&amp;pass_ticket=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span>(</td>
      </tr>
      <tr>
        <td id="L756" class="blob-num js-line-number" data-line-number="756"></td>
        <td id="LC756" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], fun, <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>pass_ticket<span class="pl-pds">&#39;</span></span>]))</td>
      </tr>
      <tr>
        <td id="L757" class="blob-num js-line-number" data-line-number="757"></td>
        <td id="LC757" class="blob-code blob-code-inner js-file-line">        params <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L758" class="blob-num js-line-number" data-line-number="758"></td>
        <td id="LC758" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>  : <span class="pl-v">self</span>.loginInfo[<span class="pl-s"><span class="pl-pds">&#39;</span>BaseRequest<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L759" class="blob-num js-line-number" data-line-number="759"></td>
        <td id="LC759" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>ChatRoomName<span class="pl-pds">&#39;</span></span> : chatroomUserName,</td>
      </tr>
      <tr>
        <td id="L760" class="blob-num js-line-number" data-line-number="760"></td>
        <td id="LC760" class="blob-code blob-code-inner js-file-line">            memberKeyName  : <span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>.join([member[<span class="pl-s"><span class="pl-pds">&#39;</span>UserName<span class="pl-pds">&#39;</span></span>] <span class="pl-k">for</span> member <span class="pl-k">in</span> memberList]), }</td>
      </tr>
      <tr>
        <td id="L761" class="blob-num js-line-number" data-line-number="761"></td>
        <td id="LC761" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>content-type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json; charset=UTF-8<span class="pl-pds">&#39;</span></span>}</td>
      </tr>
      <tr>
        <td id="L762" class="blob-num js-line-number" data-line-number="762"></td>
        <td id="LC762" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-v">self</span>.s.post(url, <span class="pl-v">data</span><span class="pl-k">=</span>json.dumps(params),<span class="pl-v">headers</span><span class="pl-k">=</span>headers).json()</td>
      </tr>
      <tr>
        <td id="L763" class="blob-num js-line-number" data-line-number="763"></td>
        <td id="LC763" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L764" class="blob-num js-line-number" data-line-number="764"></td>
        <td id="LC764" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>__main__<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L765" class="blob-num js-line-number" data-line-number="765"></td>
        <td id="LC765" class="blob-code blob-code-inner js-file-line">    wcc <span class="pl-k">=</span> WeChatClient()</td>
      </tr>
      <tr>
        <td id="L766" class="blob-num js-line-number" data-line-number="766"></td>
        <td id="LC766" class="blob-code blob-code-inner js-file-line">    wcc.login()</td>
      </tr>
</table>

  </div>

</div>

<button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
<div id="jump-to-line" style="display:none">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>


    </div>
  </div>

    </div>

        <div class="container site-footer-container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links float-right">
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2016 <span title="0.12891s from github-fe139-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



    

    <div id="ajax-error-message" class="ajax-error-message flash flash-error">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"></path></svg>
      <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
        <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
      </button>
      You can't perform that action at this time.
    </div>


      
      <script crossorigin="anonymous" integrity="sha256-NbnFQdNBMJuTCxx5D6GyejDHxEzhDH+CQokOPYPIrb0=" src="https://assets-cdn.github.com/assets/frameworks-35b9c541d341309b930b1c790fa1b27a30c7c44ce10c7f8242890e3d83c8adbd.js"></script>
      <script async="async" crossorigin="anonymous" integrity="sha256-KUc5sZMEhV0sUHfPRpDx7Im856pzqIhZt23B8iMWo9g=" src="https://assets-cdn.github.com/assets/github-294739b19304855d2c5077cf4690f1ec89bce7aa73a88859b76dc1f22316a3d8.js"></script>
      
      
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"></path></svg>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
    <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
    </button>
  </div>
</div>

  </body>
</html>


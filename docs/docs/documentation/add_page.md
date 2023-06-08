---
layout: page
show_sidebar: false
menubar: menu
title: Adding a Page
permalink: /add-page/
---

Adding a documentation page is very simple. All pages a written in markdown
which is then converted into HTML when the site is published. To create a documentation
page:

1) create a new markdown file (file with .md extension) in the `docs/documentation` directory by copying the
`page_template.md` file.

2) Once you have created the page there are just a couple of small items to modify:
   - First enter a title for you page in the `title` line of the header 
   - Then add a string to act as the reference for the page in the `permalink` line.

3) Now you can begin adding your documentation in markdown. You can reference the
markdown syntax [on this site](https://www.markdownguide.org). 

4) Once your page is complete it can be added to the menu bar by modifying the `_data/menu.yml` file. In the `Product Documentation`
section under items, add a list item for your page. 
   - The name parameter will be the display name for the page in the navigation
   - The link parameter should match the permalink you set in your page's header.

5) Commit and push the updates to GitHub and the site will be rebuilt automatically incorporating the changes.


If you want to prevew the site as you add your content follow [this guide](https://docs.github.com/en/enterprise-server@3.6/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll) to run it locally.
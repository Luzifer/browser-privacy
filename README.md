# Luzifer / browser-privacy

This repository contains a list of filter rules for uBlock Origin (AdBlock Plus is missing support for some of the rules) to enhance the browsing privacy and replace Ghostery, Privacy Badger and other similar extensions.

**The filter rules are set up for my personal browsing behaviour and you will be missing rules for your own behaviour.**

The setup is done following the suggested "medium" hard method for dynamic filter rules. The reason for using static filters instead of dynamic rules is quite simple: The author is [refusing to make dynamic rules loadable from a remote source](https://github.com/uBlockOrigin/uBlock-issues/issues/66) which is required for me as I'm using multiple browser profiles and therefore cannot use the "cloud sync" method suggested by him.

The method used here is derived from this video: [How to use uBlock Origin advanced user mode tutorial 2018](https://www.youtube.com/watch?v=2lisQQmWQkY):

- Block every third-party script and frame
- Allow some stuff globally to unbreak most of the internet
- Add specific allow-rules for websites I'm using still being broken by the previous rules

Together with a whole list of other filter lists this achieves a quite good coverage for blocking crap out of my browsing experience.

---

In case you really want to use this filter list for yourself:

- Clone this repo and modify the `filters.txt`
- OR subscribe to this list and add your own rules to your `My Filters` tab in uBlock Origin:
    ```
    https://raw.githubusercontent.com/Luzifer/browser-privacy/master/filters.txt
    ```

I most likely will not incorporate pull-requests or other additions to my list as this list is optimized for me.

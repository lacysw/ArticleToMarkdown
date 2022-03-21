# ArticleGrabber

Retrieves the body of online articles posted on supported platforms; returns content as a Markdown string. Preserves links, lists, etc.

> Why?

Users are more likely to read content if they don't have to visit a third-party service to do so. This script is intended for automated use, such as part of Reddit or Discord bots. Further, web scraping in this fashion is effective as a means of archiving information and bypassing hostile web design choices (e.g. paywalls and advertisements).

## Dependencies:

 - `requests`
 - `tldextract`
 - `markdownify`
 - `datetime`
 - `bs4`

## Usage

In your project:

```python
import get_article

...

reuters_article_text = get_article("https://www.reuters.com/markets/asia/japans-jan-consumer-inflation-rises-slower-pace-2022-02-17/")
```

## Supported Sites

Because every website displays information differently, to ensure maximum accuracy, a list of allowed sites is enforced. I manually create formatting functions on a site-by-site basis. *Please feel free to contribute to the project; I will merge all PRs for new website support.*

Currently, this project supports pulling text from the following websites:

 - `reuters.com`

More will be added soon.
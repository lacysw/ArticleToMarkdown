# ArticleToMarkdown

Retrieves the body of online articles posted on supported platforms; returns content as a Markdown string. Preserves links, lists, etc.

> Why?

Users are more likely to read content if they don't have to visit a third-party service to do so. This script is intended for automated use, such as part of Reddit or Discord bots. Further, web scraping in this fashion is effective as a means of archiving information and bypassing hostile web design choices (e.g. paywalls and advertisements).

## Dependencies:

 - `requests`
 - `tldextract`
 - `markdownify`
 - `datetime`
 - `bs4`

## Example Usage

In your project:

```python
import get_article

reuters_article_text = get_article("https://www.reuters.com/markets/asia/japans-jan-consumer-inflation-rises-slower-pace-2022-02-17/")
print(reuters_article_text)
```

**NOTE: the following article is included as an example from Reuters and is not my work.**

```
dev ~/projects/ArticleGrabber $ ./example.py
# Reuters: Japan's consumer prices rise in January, but at slower pace

> TOKYO, Feb 18 (Reuters) - Japan's core consumer prices rose for a fifth straight month in January but at a slower pace than in the previous month, boosting the likelihood the country's central bank will lag behind other economies in raising interest rates.
>
> Consumer inflation is expected to pick up in the coming months due to surging energy prices, while last year's mobile phone fee cuts are also set to fall out of calculations and will no longer be a drag on prices.
>
> The core consumer price index (CPI), which excludes volatile fresh food prices but includes fuel costs, increased 0.2% in January from a year earlier, government data showed on Friday.
>
> That was weaker than the median forecast for a 0.3% gain in a Reuters poll and a 0.5% rise in the previous two months.
>
> "Consumer inflation will pick up from next month onward on higher food and energy prices," said Taro Saito, executive research fellow at NLI Research Institute.
>
> "It may jump to more than 1.5% in one go in April once the impact of mobile phone fee cuts comes to an end."
>
> The price data will be among factors the Bank of Japan will scrutinise at its next policy meeting, which is scheduled for the middle of next month.
>
> The core CPI has posted a year-on-year increase every month since September. January's increase marked the slowest year-on-year rise in three months.
>
> Accommodation prices rose just 0.6% from a year earlier to grow at the weakest rate since June 2021 after a domestic travel campaign in late 2020 came to an end.
>
> Cellphone fee cuts pushed down the CPI by about 1.5 percentage points last month.
>
> The tepid overall rate of increase shows price rises in the world's third-largest economy have remained extremely modest compared with much sharper gains in other advanced economies as sluggish wage growth discourages firms from hiking prices much.
>
> The small gain reinforced expectations the Bank of Japan (BOJ) will maintain its ultra-loose monetary policy for the time being to achieve its 2% inflation target.
>
> Saito said any sharper rises in consumer prices in coming months were unlikely to prod the central bank to tighten monetary policy but could open the door for fresh government stimulus.
>
> That could include expanding a subsidy scheme to mitigate a steep increase in gasoline and other fuel prices or, eventually, additional cash handouts for households, he said.
>
> Overall energy prices soared 17.9% from a year earlier in January, posting their biggest rise in more than forty years, in part due to surging electricity bills and fuel costs.
>
> The BOJ has stuck to massive monetary stimulus as it seeks to have inflation reach its target, despite some worries about the side-effect of a weakening yen.
>
> Our Standards: [The Thomson Reuters Trust Principles.](https://www.thomsonreuters.com/en/about-us/trust-principles.html)

---

*Retrieved from [https://www.reuters.com/markets/asia/japans-jan-consumer-inflation-rises-slower-pace-2022-02-17/](https://www.reuters.com/markets/asia/japans-jan-consumer-inflation-rises-slower-pace-2022-02-17/) on 2022/03/21 at 10:23:12 UTC*.
```
## Supported Sites

Because every website displays information differently, to ensure maximum accuracy, a list of allowed sites is enforced. I manually create formatting functions on a site-by-site basis. *Please feel free to contribute to the project; I will merge all PRs for new website support.*

Currently, this project supports pulling text from the following websites:

 - `reuters.com`

More will be added soon.

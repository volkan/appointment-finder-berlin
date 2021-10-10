rm -rf /scrapyfile
mkdir /scrapyfile
cp -R /scraper /scrapyfile
cd /scrapyfile/scraper

scrapy crawl $1
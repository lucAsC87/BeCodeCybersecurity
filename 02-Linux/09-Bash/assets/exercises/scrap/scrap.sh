#!/bin/bash

curl -s 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops' \
| pup 'div.card json{}' \
| jq -r '
  .[]
  | .children[0].children[1].children[2].text as $desc
  | .children[0].children[1].children[0].children[0].text as $price
  | ($desc | capture("^(?<name>[^,]+),\\s*(?<rest>.+)$")) as $m
  | "\($m.name) | \($m.rest) | \($price)"
' \
| sed 's/&#34;/"/g'

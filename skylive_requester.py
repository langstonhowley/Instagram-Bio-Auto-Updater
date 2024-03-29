#    Copyright 2020 Langston Howley

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from bs4 import BeautifulSoup
import urllib.request


def planet_location(planet="Mars"):
    SKY_LIVE_URL = "https://theskylive.com/"
    sky_live_page = urllib.request.urlopen(SKY_LIVE_URL)
    soup = BeautifulSoup(sky_live_page, "html.parser")

    table_row = soup.find_all(title=planet)[0].find_parent("tr")
    table_data = []
    for data in table_row.find_all("td"):
        table_data.append(data.text.strip())

    return table_data


if __name__ == "__main__":
    planet_location()

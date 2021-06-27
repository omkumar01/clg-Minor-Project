import requests
from bs4 import BeautifulSoup


class Bot:        

    def headerCount(self, page):
        headcount = {}
        h1Tag = page.find_all("h1")
        count = 0
        for items in h1Tag:
            count += 1
        headcount["h1count"] = count

        h2Tag = page.find_all("h2")
        count = 0
        for items in h2Tag:
            count += 1
        headcount["h2count"] = count

        h3Tag = page.find_all("h3")
        count = 0
        for items in h3Tag:
            count += 1
        headcount["h3count"] = count

        h4Tag = page.find_all("h4")
        count = 0
        for items in h4Tag:
            count += 1
        headcount["h4count"] = count

        h5Tag = page.find_all("h5")
        count = 0
        for items in h5Tag:
            count += 1
        headcount["h5count"] = count

        return headcount


    def titleText(self, page):
        if page.find("title"):
            return page.find("title").get_text()
        else:
            return "no title tag found"


    def metaTags(self, page):
        meta_data = {}
        if page.find_all("meta"):
            tags = page.find_all("meta")
            for tag in tags:
                name = tag.get("name")
                prop = tag.get("property")
                if name == "viewport":
                    meta_data["viewport"] = tag.get("content")
                if name == "keywords":
                    meta_data["keywards"] = tag.get("content")
                if name == "description":
                    meta_data["description"] = tag.get("content")
                if name == "robots":
                    meta_data["robots"] = tag.get("content")
                if name == "twitter:card":
                    meta_data["twitter:card"] = tag.get("content")
                if name == "twitter:title":
                    meta_data["twitter:title"] = tag.get("content")
                if name == "twitter:description":
                    meta_data["twitter:description"] = tag.get("content")
                if name == "twitter:image":
                    meta_data["twitter:image"] = tag.get("content")

                if prop == "og:type":
                    meta_data["og:type"] = tag.get("content")
                if prop == "og:image":
                    meta_data["og:image"] = tag.get("content")
                if prop == "og:url":
                    meta_data["og:url"] = tag.get("content")
                if prop == "og:title":
                    meta_data["og:title"] = tag.get("content")
                if prop == "og:description":
                    meta_data["og:description"] = tag.get("content")

                if tag.get("charset"):
                    meta_data["charset"] = tag.get("charset")

            return meta_data

        else:
            return 0


    def checkSchema(self, page):
        if page.find_all("script"):
            scriptsTags = page.find_all("script")
            for scriptsTag in scriptsTags:
                if scriptsTag.get("type") == "application/ld+json":
                    return True

        else:
            return False


    def getLang(self, page):
        lang_info = {}
        if page.find("html"):
            tag = page.find("html")
            if tag.get("lang") == None:
                lang_info["lang_exist"] = False
                lang_info["content"] = "no language attribute"
                return lang_info
            else:
                lang_info["lang_exist"] = True
                lang_info["content"] = tag.get("lang")
                return lang_info


    def imgAlt(self, page):
        img_data = {}
        imgcount = 0
        img_alt_found = 0
        img_alt_not_found = 0
        if page.find_all("img"):
            img = page.find_all("img")

            for i in img:
                imgcount += 1
                if i.get("alt") == None:
                    img_alt_not_found += 1
                else:
                    img_alt_found += 1

            img_data["imgcount"] = imgcount
            img_data["img_alt_found"] = img_alt_found
            img_data["img_alt_not_found"] = img_alt_not_found
            return img_data
        else:
            img_data["imgcount"] = imgcount
            img_data["img_alt_found"] = img_alt_found
            img_data["img_alt_not_found"] = img_alt_not_found
            return img_data


def onPage(url):  
    html = requests.get(url)
    page = BeautifulSoup(html.content, "html.parser")
    dict = {}
    obj = Bot()
    dict.update(obj.headerCount(page))
    dict['page_title'] = obj.titleText(page)
    dict.update(obj.metaTags(page))
    dict['schema_exist'] = obj.checkSchema(page)
    dict.update(obj.getLang(page))
    dict.update(obj.imgAlt(page))
    return dict

if __name__ == '__main__':
    onPage("https://heapoftech.live")
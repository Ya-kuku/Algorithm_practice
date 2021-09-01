import re
def solution(word, pages):
    urlToIdx = {}
    urlToScore = {}
    exlinkToUrl = {}
    word = word.lower()
    for idx, page in enumerate(pages):
        # print(page)
        # \S = 숫자, 문자, 특수문자 모두 포함(공백 제외)
        #() = 추출한 부분의 그룹핑
        # 정확하게는 <meta[^>]*content="https://([\S]*)"/> 까지가 맞음
        page = page.lower()
        url = re.search(r'<meta[^>]*content="https://([\S]*)"',page).group(1)

        urlToIdx[url.lower()] = idx
        cnt = 0
        # 포함된 단어 찾기
        for f in re.findall(r'[a-z]+',page):
            if f == word:
                cnt += 1
        tmp_link = set()
        # 포함된 링크 찾기
        for e in re.findall(r'<a href="https://[\S]*"',page):
            tmp_link.add(re.search(r'"https://([\S]*)"',e).group(1))
        tmp_link = list(tmp_link)
        urlToScore[url] = []
        urlToScore[url].append(cnt)
        urlToScore[url].append(len(tmp_link))

        for link in tmp_link:
            if link not in exlinkToUrl:
                exlinkToUrl[link] = []
            exlinkToUrl[link].append(url)

    answer = []
    for k,v in urlToScore.items():
        score = v[0]
        # print(k)
        if k in exlinkToUrl:
            for u in exlinkToUrl[k]:
                score += urlToScore[u][0] / urlToScore[u][1]
        answer.append([score,urlToIdx[k]])
    # print(answer)
    answer.sort(key=lambda data:(-data[0],data[1]))

    return answer[0][1]

solution('Muzi',["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])
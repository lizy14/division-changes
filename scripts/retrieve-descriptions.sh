# Install html2text
# pip3 install html2text

# Download description HTML pages from 1999 to 2022
for i in $(seq 1999 2022); do
    curl http://xzqh.mca.gov.cn/description?dcpid=$i > $i.html;
done

# Convert HTMLs to txt
for i in $(seq 1999 2022); do
    echo $i;
    cat $i.html | iconv --from-code=gbk --to-code=utf8 | html2text > $i.txt;
done

# Download description HTML pages from 1949 to 2006
curl https://www.gov.cn/test/2007-03/23/content_558707.htm > 1949年.html
curl https://www.gov.cn/test/2007-03/23/content_558725.htm > 1950年.html
curl https://www.gov.cn/test/2007-03/23/content_558757.htm > 1951年.html
curl https://www.gov.cn/test/2007-03/23/content_558770.htm > 1952年.html
curl https://www.gov.cn/test/2007-03/23/content_558783.htm > 1953年.html
curl https://www.gov.cn/test/2007-03/23/content_558796.htm > 1954年.html
curl https://www.gov.cn/test/2007-03/23/content_558800.htm > 1955年.html
curl https://www.gov.cn/test/2007-03/23/content_558810.htm > 1956年.html
curl https://www.gov.cn/test/2007-03/23/content_558814.htm > 1957年.html
curl https://www.gov.cn/test/2007-03/23/content_558818.htm > 1958年.html
curl https://www.gov.cn/test/2007-03/23/content_558826.htm > 1959年.html
curl https://www.gov.cn/test/2007-03/23/content_558839.htm > 1960年.html
curl https://www.gov.cn/test/2007-03/23/content_558844.htm > 1961年.html
curl https://www.gov.cn/test/2007-03/23/content_558858.htm > 1962年.html
curl https://www.gov.cn/test/2007-03/23/content_558867.htm > 1963年.html
curl https://www.gov.cn/test/2007-03/23/content_558876.htm > 1964年.html
curl https://www.gov.cn/test/2007-03/23/content_558906.htm > 1965年.html
curl https://www.gov.cn/test/2007-03/23/content_558909.htm > 1966年.html
curl https://www.gov.cn/test/2007-03/23/content_558926.htm > 1967年.html
curl https://www.gov.cn/test/2007-03/23/content_558934.htm > 1968年.html
curl https://www.gov.cn/test/2007-03/23/content_558938.htm > 1969年.html
curl https://www.gov.cn/test/2007-03/23/content_558950.htm > 1970年.html
curl https://www.gov.cn/test/2007-03/23/content_559047.htm > 1971年.html
curl https://www.gov.cn/test/2007-03/23/content_559054.htm > 1972年.html
curl https://www.gov.cn/test/2007-03/23/content_559061.htm > 1973年.html
curl https://www.gov.cn/test/2007-03/23/content_559077.htm > 1974年.html
curl https://www.gov.cn/test/2007-03/23/content_559082.htm > 1975年.html
curl https://www.gov.cn/test/2007-03/23/content_559092.htm > 1976年.html
curl https://www.gov.cn/test/2007-03/23/content_559096.htm > 1977年.html
curl https://www.gov.cn/test/2007-03/23/content_559102.htm > 1978年.html
curl https://www.gov.cn/test/2007-03/23/content_559106.htm > 1979年.html
curl https://www.gov.cn/test/2007-03/23/content_559117.htm > 1980年.html
curl https://www.gov.cn/test/2007-03/23/content_559119.htm > 1981年.html
curl https://www.gov.cn/test/2007-03/23/content_559122.htm > 1982年.html
curl https://www.gov.cn/test/2007-03/23/content_559123.htm > 1983年.html
curl https://www.gov.cn/test/2007-03/23/content_559128.htm > 1984年.html
curl https://www.gov.cn/test/2007-03/23/content_559136.htm > 1985年.html
curl https://www.gov.cn/test/2007-03/23/content_559140.htm > 1986年.html
curl https://www.gov.cn/test/2007-03/23/content_559145.htm > 1987年.html
curl https://www.gov.cn/test/2007-03/23/content_559151.htm > 1988年.html
curl https://www.gov.cn/test/2007-03/23/content_559156.htm > 1989年.html
curl https://www.gov.cn/test/2007-03/23/content_559159.htm > 1990年.html
curl https://www.gov.cn/test/2007-03/23/content_559160.htm > 1991年.html
curl https://www.gov.cn/test/2007-03/23/content_559164.htm > 1992年.html
curl https://www.gov.cn/test/2007-03/23/content_559171.htm > 1993年.html
curl https://www.gov.cn/test/2007-03/23/content_559172.htm > 1994年.html
curl https://www.gov.cn/test/2007-03/23/content_559194.htm > 1995年.html
curl https://www.gov.cn/test/2007-03/23/content_559199.htm > 1996年.html
curl https://www.gov.cn/test/2007-03/23/content_559206.htm > 1997年.html
curl https://www.gov.cn/test/2007-03/23/content_559214.htm > 1998年.html
curl https://www.gov.cn/test/2007-03/23/content_559228.htm > 1999年.html
curl https://www.gov.cn/test/2007-03/23/content_559255.htm > 2000年.html
curl https://www.gov.cn/test/2007-03/23/content_559267.htm > 2001年.html
curl https://www.gov.cn/test/2007-03/23/content_559272.htm > 2002年.html
curl https://www.gov.cn/test/2007-03/23/content_559287.htm > 2003年.html
curl https://www.gov.cn/test/2007-03/23/content_559291.htm > 2004年.html
curl https://www.gov.cn/test/2007-03/23/content_559298.htm > 2005年.html
curl https://www.gov.cn/test/2007-03/23/content_559299.htm > 2006年.html

# Convert HTMLs to txt
for i in $(seq 1949 2006); do
    echo $i;
    cat $i年.html | html2text > $i年.txt;
done

dictionary = {
    0: '零',
    1: '壹',
    2: '贰',
    3: '叁',
    4: '肆',
    5: '伍',
    6: '陆',
    7: '柒',
    8: '捌',
    9: '玖'
}

bdict = {1: '', 2: '拾', 3: '佰', 4: '仟'}
cdict = {1: '元', 2: '万', 3: '亿', 4: '兆'}
flags = [0 for i in range(5)]


def 大写(num):
    # if num < 0:
    #     time.sleep(4)
    #     return
    resluts = ['' for i in range(5)]
    num = int(100 * num)
    zhengflag = False
    if num % 100 > 0:
        jf = num % 100
        if jf % 10 != 0:
            if jf // 10 != 0:
                resluts[-1] = "{0}角{1}分".format(dictionary[jf//10],
                                                dictionary[jf % 10])
            else:
                resluts[-1] = "零{0}分".format(dictionary[jf % 10])
        else:
            if jf // 10 != 0:
                resluts[-1] = '{0}角'.format(dictionary[jf//10])
    else:
        zhengflag = True
    num //= 100
    for i in range(1, len(flags)+1):
        pnum = str((num % 10000**i)//(10000**(i-1)))
        flags[i-1] = '0'*(4-len(pnum)) + pnum
    print(flags)
    for i in range(4):
        nowresult = []
        afterzero = True
        nownum = list(map(int, list(flags[i][::-1])))
        for j in range(4):
            if nownum[j] == 0:
                if afterzero:
                    nowresult.append('')
                else:
                    nowresult.append(dictionary[0])
                afterzero = True
            else:
                afterzero = False
                nowresult.append(dictionary[nownum[j]]+bdict[j + 1])
        nowresult = "".join(nowresult[::-1])
        if nowresult != "":
            nowresult += cdict[i+1]
        else:
            nowresult = ""
        resluts[-i-2] = nowresult
    resluts = "".join(resluts)
    point = 0
    while True:
        if resluts[point] == '零':
            point += 1
            continue
        break
    resluts = resluts[point:]
    if zhengflag:
        resluts = resluts + '整'
    return resluts


def find_dictrionary(ch):
    for i in dictionary.keys():
        if dictionary[i] == ch:
            return i


def 小写(str):
    result = 0
    if not "整" in str:
        jfres = 0
        jf = str[str.find("元")+1:]
        if "分" in str:
            jfres += find_dictrionary(str[str.find("分")-1])
        if "角" in str:
            jfres += find_dictrionary(str[str.find("角")-1])*10
        result += jfres/100
    splits = [0 for i in range(4)]
    splitsch = "元万亿兆"
    for i in range(len(splitsch)):
        splits[i] = str.find(splitsch[i])
    parts = ['' for i in range(4)]
    for i in range(len(splits)):
        if splits[i] != -1:
            pointA = splits[i]
            pointB = -1
            j = i + 1
            while j < len(splits):
                if splits[j] != -1:
                    pointB = splits[j]
                    break
                j += 1
            parts[i] = str[pointB+1:pointA]
    for i in range(len(parts)):
        splitch = "拾佰仟"
        partres = 0
        for j in range(len(splitch)):
            pos = parts[i].find(splitch[j])
            if pos != -1:
                partres += find_dictrionary(parts[i][pos-1])*10**(j+1)
        if (len(parts[i])-1) != parts[i].find("拾"):
            partres += find_dictrionary(parts[i][-1])

        result += partres * 10000**i

    return result
  
if __name__ == "__main__":
  print(大写(1145141919810.89))

import sys
from konlpy.tag import Twitter
from collections import Counter


def get_nouns(text, ntags=50):
    spliter = Twitter()
    nouns = spliter.nouns(text)
    count = Counter(nouns)

    return_list = []
    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)
    return nouns


def main(argv):
    if len(argv) != 4:
        print('python [모듈 이름] [텍스트 파일명.txt] [단어 개수] [결과파일명.txt]')
        return
    text_file_name = argv[1]
    noun_count = int(argv[2])
    output_file_name = argv[3]
    open_text_file = open(text_file_name, 'r')
    text = open_text_file.read()
    nouns = get_nouns(text, noun_count)
    open_text_file.close()
    open_output_file = open(output_file_name, 'w')
    for noun in nouns:
        if len(noun) > 1:
            open_output_file.write('{} '.format(noun))
    open_output_file.close()


if __name__ == '__main__':
    main(sys.argv)

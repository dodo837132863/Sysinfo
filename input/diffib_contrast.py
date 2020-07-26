import difflib
import  hashlib

def find_file_different(filename1, filename2, output_filename):
    with open(filename1) as f:
        content1 = f.readlines()
    with open(filename2) as f:
        content2 = f.readlines()


    hdiff = difflib.HtmlDiff()
    result = hdiff.make_file(content1, content2)
    with open(output_filename, 'w') as f:
        f.write(result)
        print("写入html文件[%s]成功" %(output_filename))

def test_fun1():
    filename1 = '/root/PycharmProjects/untitled/Sysinfo/input/nginx_backup_20200725.conf'
    filename2 = '/root/PycharmProjects/untitled/Sysinfo/input/nginx_backup_20200726.conf'
    output_filename = 'output/diff.html'
    find_file_different(filename1, filename2, output_filename)

def is_same_file(filename1, filename2):
    with open(filename1) as f:
        content1 = f.read()
        md1 = hashlib.md5()
        md1.update(content1.encode('utf-8'))
        hex_content1 = md1.hexdigest()
    with open(filename2) as f:
        content2 = f.read()
        md1 = hashlib.md5(content2.encode('utf-8'))
        hex_content2 = md1.hexdigest()
    return  hex_content1 == hex_content2




from git import Repo

url = ""

repo = Repo(sourceDir) #sourceDir�������Ŀ��·���������޸ĸ��������Ŀ�����Է��ĵ��á�

#��ȡmaster���°汾��hexshaֵ
head = repo.head
master = head.reference
log = master.log()
newhexsha = (log[-1].newhexsha)
print(newhexsha)

if repo.is_dirty(): #�Ƿ��޸Ĺ�
    for v in repo.untracked_files: #untracked�ļ��б�
        print(v) #�ַ�����·��

index = repo.index
    for v in index.diff(None): #�����޸�δ�ύ�б�
       print(v.b_path) ##�����ļ�·��
       print(v. change_type) ###�޸����ͣ�����"m"��ʾmodified��
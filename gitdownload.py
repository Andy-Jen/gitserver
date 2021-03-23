from git import Repo

url = ""

repo = Repo(sourceDir) #sourceDir是你的项目的路径，不会修改覆盖你的项目，可以放心调用。

#获取master最新版本的hexsha值
head = repo.head
master = head.reference
log = master.log()
newhexsha = (log[-1].newhexsha)
print(newhexsha)

if repo.is_dirty(): #是否修改过
    for v in repo.untracked_files: #untracked文件列表
        print(v) #字符串，路径

index = repo.index
    for v in index.diff(None): #本地修改未提交列表
       print(v.b_path) ##本地文件路径
       print(v. change_type) ###修改类型，返回"m"表示modified。
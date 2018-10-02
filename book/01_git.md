### git 基础命令
```
# 克隆代码
> git clone https://github.com/defnngj/test_project

# 检查更新
> git status

# 添加修改的内容
> git add .        # 添加全部
> git add test.py  # 添加部分文件
> git add abc/     # 添加abc整个文件夹内容

# add 撤销
> git reset HEAD
> git reset HEAD test.py

# 提交更新(提交修改到本地仓库)
> git commit -m "xxxx"

# 同步到远程的master分支
> git push origin master

# 从远程master分支拉取最新代码到本地
> git pull origin master


```

### 分支操作
```
# 查看全部分支（远程和本地的）
> git branch -a

# 创建分支
> git branch dev

# 切换分支
> git checkout dev

# 合并分支(把dev分支合并到当前分支)
> git merge dev

```

### github客户端
github for desktop：
https://desktop.github.com/
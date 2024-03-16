## 搭配
本解答需要運作在 https://github.com/4-learn/devops-flask-demo-site 中

## 流程

#### 將 flask.yml  requirements.txt 兩個檔案，複製到 https://github.com/4-learn/devops-flask-demo-site 中:
```bash=
$ rm ../../../../devops-flask-demo-site/.github/workflows/*
$ /devops/github-action/workshop/flask$ cp flask.yml  requirements.txt  ../../../../devops-flask-demo-site/.github/workflows/
```

#### 到 https://github.com/4-learn/devops-flask-demo-site 進行 push
```bash=
$ cd ../../../../devops-flask-demo-site/
$ ls .github/workflows/
flask.yml  requirements.txt
ubuntu@slave1:~/workspace/devops-flask-demo-site$ git add . ; git commit -m "workshop: flask" ; git push
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
Enumerating objects: 14, done.
Counting objects: 100% (12/12), done.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (8/8), 979 bytes | 326.00 KiB/s, done.
Total 8 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/4-learn/devops-flask-demo-site
   20130f4..805945f  master -> master
```

## GitHub
- [Reference GitHub Action Job](https://github.com/4-learn/devops-flask-demo-site/actions/runs/8308120346/job/22738010089)
![image](https://github.com/yillkid/ntc-devops/assets/185872/19d09906-04d4-4752-ba01-db90dda3bb59)
![image](https://github.com/yillkid/ntc-devops/assets/185872/21da6be7-545a-47d2-98e4-2dedf2ca5e1d)

## 搭配
本解答需要運作在 https://github.com/4-learn/devops-flask-demo-site 中

## 流程

#### 將檔案複製到 https://github.com/4-learn/devops-flask-demo-site 中:
```bash=
$ rm -rf ../../../../devops-flask-demo-site/.github/workflows/*
$ /devops/github-action/workshop/CD$ cp -rf Dockerfile requirements.txt server.py tests ../../../../devops-flask-demo-site/
$ /devops/github-action/workshop/CD$ cp docker.yml flask.yml ../../../../devops-flask-demo-site/.github/workflows/
```

#### 到 https://github.com/4-learn/devops-flask-demo-site 進行 push
```bash=
$ cd ../../../../devops-flask-demo-site/
$ ls
Dockerfile  README.md  examples  requirements.txt  server.py  tests
$ ls .github/workflows/
docker.yml  flask.yml
$ git add . ; git commit -m "workshop: CD" ; git push
```

## GitHub
![image](https://github.com/4-learn/devops/assets/185872/cb744b60-6c11-4529-a1d7-aad9937a87e2)
![image](https://github.com/4-learn/devops/assets/185872/e4a6d1d0-3c74-4f0b-b122-fdc7bdb603a0)


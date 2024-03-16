## 搭配
本解答需要運作在 https://github.com/4-learn/devops-flask-demo-site 中

## 流程

#### 將檔案複製到 https://github.com/4-learn/devops-flask-demo-site 中:
```bash=
$ rm -rf ../../../../devops-flask-demo-site/.github/workflows/*
$ $ cp -rf check_element.py  ../../../../devops-flask-demo-site/
$ $ cp -rf check_website.yml ../../../../devops-flask-demo-site/.github/workflows/
```

## GitHub Action
- [push event log](https://github.com/4-learn/devops-flask-demo-site/actions/runs/8309011499)
- [cron log](https://github.com/4-learn/devops-flask-demo-site/actions/runs/8309064950)


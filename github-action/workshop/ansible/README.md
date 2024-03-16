## 搭配
本解答需要運作在 https://github.com/4-learn/devops-flask-demo-site 中

## 流程

#### 將檔案複製到 https://github.com/4-learn/devops-flask-demo-site 中:
```bash=
$ rm -rf ../../../../devops-flask-demo-site/.github/workflows/*
$ $ cp -rf check_status.yml ../../../../devops-flask-demo-site/
$ $ cp -rf check_connectivity.yml ../../../../devops-flask-demo-site/.github/workflows/
```

## GitHub Action
- [push event log](https://github.com/4-learn/devops-flask-demo-site/actions/runs/8308819737/job/22739466160)
- [cron log](https://github.com/4-learn/devops-flask-demo-site/actions/runs/8308827908)

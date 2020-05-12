# 测试 Docker .env 文件的环境变量载入

> Docker version 19.03.8

## load dotenv

### `FROM python:3.7` 测试通过

```bash
docker build -t testloadenv .
docker run -d -v /docker-env:/app -p 8080:80 testloadenv

curl http://0.0.0.0:8080
```

### `FROM ubuntu` 测试通过

```bash
docker build -f UbuntuDockerfile.dockerfile -t utestloadenv .
docker run -d -v /docker-env:/app -p 8080:80 utestloadenv

curl http://0.0.0.0:8080
```

## `doccker --env-file` 命令 测试通过

```bash
docker build -f UseEnvDockerfile.dockerfile -t useenvcmd .
docker run -d --env-file .env -v /docker-env:/app -p 8080:80 useenvcmd

curl http://0.0.0.0:8080
```

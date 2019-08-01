# 程序入口

from app import create_app

app = create_app("app.config")

if __name__ == "__main__":
  app.run()
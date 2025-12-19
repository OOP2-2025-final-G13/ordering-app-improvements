# 注文アプリ改

注文管理を効率化するためのWebアプリケーションです。ユーザー、製品、注文、統計、レビューの管理・編集が可能です。

---

## 目次
- [概要](#概要)
- [主な機能](#主な機能)
- [セットアップ](#セットアップ)
- [使い方](#使い方)
- [技術スタック](#技術スタック)
- [ディレクトリ構成](#ディレクトリ構成)

---

## 概要
本アプリケーションは、注文・ユーザー・製品・統計・レビューの管理を一元化し、業務効率化を支援します。直感的なUIで各項目の追加・編集が可能です。

## 主な機能
- ユーザー管理（追加・編集）
- 製品管理（追加・編集）
- 注文管理（追加・編集）
- 統計表示（売上確認）
- レビュー管理（追加・編集）

## セットアップ
### 必要条件
- Python 3.13 以上
- pip

### 必要パッケージ

```bash
pip install Flask==3.0.3 peewee==3.17.7
```

## 使い方
1. リポジトリをクローン
	```bash
	git clone https://github.com/OOP2-2025-final-G13/ordering-app-improvements.git
	cd ordering-app-improvements
	```
2. 必要パッケージをインストール
	```bash
	pip install Flask==3.0.3 peewee==3.17.7
	```
3. アプリケーションを起動
	```bash
	python app.py
	```
4. ブラウザでアクセス
	- [http://localhost:8080](http://localhost:8080)

## 技術スタック
- Python (Flask)
- Peewee (ORM)
- HTML/CSS (Jinja2テンプレート)

## ディレクトリ構成
```
ordering-app-improvements/
├── app.py
├── models/
├── routes/
├── static/
├── templates/
└── README.md
```

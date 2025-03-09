# Gitarist Music Bot

[![Stars](https://img.shields.io/github/stars/isagzbyk46/gitaristmusic?style=flat-square&color=yellow)](https://github.com/isagzbyk46/gitaristmusic/stargazers)
[![Forks](https://img.shields.io/github/forks/isagzbyk46/gitaristmusic?style=flat-square&color=orange)](https://github.com/isagzbyk46/gitaristmusic/fork)

[![Telegram](https://img.shields.io/badge/-Support-grey?style=for-the-badge&logo=Telegram&logoColor=white&labelColor=8E2DE2)](https://t.me/YOUR_SUPPORT_GROUP)
[![Telegram](https://img.shields.io/badge/-Updates-grey?style=for-the-badge&logo=Telegram&logoColor=white&labelColor=8E2DE2)](https://t.me/YOUR_UPDATE_CHANNEL)

## 🎵 Gitarist Music Bot
Gitarist Music Bot, Telegram gruplarında YouTube'dan müzik çalabilen güçlü bir müzik botudur.

## 🚀 Heroku'ya Deploy Et
Aşağıdaki butona tıklayarak Heroku'ya hızlıca deploy edebilirsiniz:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/isagzbyk46/gitaristmusic)

## 🖥️ VPS Üzerine Kurulum
Eğer botu bir VPS sunucusunda çalıştırmak istiyorsanız aşağıdaki adımları takip edin:

1. **Sunucunuzu güncelleyin:**
   ```sh
   sudo apt-get update && sudo apt-get upgrade -y
   ```

2. **Gerekli paketleri yükleyin:**
   ```sh
   sudo apt-get install python3-pip ffmpeg -y
   ```

3. **Node.js yükleyin:**
   ```sh
   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   sudo apt-get install nodejs -y && npm i -g npm
   ```

4. **Repository'yi klonlayın ve içine girin:**
   ```sh
   git clone https://github.com/isagzbyk46/gitaristmusic.git && cd gitaristmusic
   ```

5. **Gerekli Python bağımlılıklarını yükleyin:**
   ```sh
   pip3 install -U -r requirements.txt
   ```

6. **Çevre değişkenlerini (`.env`) oluşturun ve düzenleyin:**
   ```sh
   cp .env.example .env
   nano .env
   ```
   `nano` veya başka bir düzenleyiciyle `.env` dosyanızı açıp, gerekli API anahtarlarını girin.

7. **Tmux veya Screen ile oturumu açık tutun:**
   ```sh
   sudo apt install tmux -y
   tmux
   ```

8. **Botu başlatın:**
   ```sh
   bash start.sh
   ```

## 📜 Gerekli Değişkenler
Botun çalışabilmesi için aşağıdaki ortam değişkenlerini (`.env` dosyanızda) ayarlamalısınız:
- `API_ID` - Telegram API ID
- `API_HASH` - Telegram API Hash
- `BOT_TOKEN` - Telegram bot tokeni
- `MONGO_URI` - MongoDB bağlantı adresi
- `SESSION_STRING` - Pyrogram oturum stringi
- `OWNER_ID` - Bot sahibinin Telegram ID'si

## 🔗 Bağlantılar
- **Destek Grubu:** [Telegram](https://t.me/YOUR_SUPPORT_GROUP)
- **Güncellemeler:** [Telegram](https://t.me/YOUR_UPDATE_CHANNEL)

## 📌 Lisans
Bu proje **GNU GPL-3.0** lisansı altında dağıtılmaktadır. Dilediğiniz gibi kullanabilir, paylaşabilir ve geliştirebilirsiniz.

---

💙 **Gitarist Music** ile Telegram gruplarınızda müziğin keyfini çıkarın!


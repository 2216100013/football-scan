#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
777 扫盘中心 - 自动推送脚本
运行方式: python3 auto_push.py
"""

import subprocess
import tempfile
import shutil
import os
import json
from datetime import datetime, timezone

# ====== 配置区 ======
GITHUB_TOKEN = "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"
REPO_URL = "https://github.com/2216100013/football-scan.git"
# ====================

def run(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ 失败: {cmd}\n{result.stderr}")
        return False
    print(f"✅ {cmd[:40]}...")
    return True

def get_data():
    return {
        "version": "1.1",
        "lastUpdated": datetime.now(timezone.utc).isoformat(),
        "source": "777扫盘中心",
        "matches": [
            {"id": "001", "time": "00:50", "league": "沙职", "home": "新未来SC", "away": "利雅得青年", "homeEmoji": "🟢", "awayEmoji": "⚪", "prediction": "让球负（利雅得+1不败）", "confidence": "⭐⭐⭐", "odds": "@1.85", "isHeart": False, "score": "2-1", "result": "push", "review": "主队2-1赢球，让球走盘。赛前看低主队，结果主场拿下。"},
            {"id": "002", "time": "01:00", "league": "瑞超", "home": "天狼星", "away": "厄格里特", "homeEmoji": "🔵", "awayEmoji": "⚫", "prediction": "让球平/让球负", "confidence": "⭐⭐⭐", "odds": "@1.90", "isHeart": False, "score": "2-0", "result": "push", "review": "天狼星2-0完胜，让球平刚好走盘。客队未能守住指数。"},
            {"id": "003", "time": "02:00", "league": "沙职", "home": "布赖代合作", "away": "吉达国民", "homeEmoji": "🟡", "awayEmoji": "🔴", "prediction": "负（吉达国民客胜）", "confidence": "⭐⭐⭐⭐", "odds": "@1.75", "isHeart": True, "score": "1-2", "result": "win", "review": "吉达国民客场2-1取胜，重心胆命中！实力占优兑现。"},
            {"id": "004", "time": "02:45", "league": "意甲", "home": "那不勒斯", "away": "博洛尼亚", "homeEmoji": "🔵", "awayEmoji": "🔴", "prediction": "胜（首选）/让球平", "confidence": "⭐⭐⭐⭐⭐", "odds": "@1.65", "isHeart": True, "score": "2-3", "result": "loss", "review": "那不勒斯主场翻车！博洛尼亚客场3-2爆冷，重心胆黑掉。"},
            {"id": "005", "time": "03:00", "league": "英超", "home": "热刺", "away": "利兹联", "homeEmoji": "⚪", "awayEmoji": "⚪", "prediction": "让球平/让球负", "confidence": "⭐⭐⭐", "odds": "@1.80", "isHeart": False, "score": "1-1", "result": "push", "review": "利兹联1-1逼平热刺，受让+1走水。判断客队能抢分，方向对但走盘。"},
            {"id": "006", "time": "03:00", "league": "英冠", "home": "米尔沃尔", "away": "赫尔城", "homeEmoji": "🔵", "awayEmoji": "🟠", "prediction": "让球胜/搏平", "confidence": "⭐⭐⭐", "odds": "@1.90", "isHeart": False, "score": "0-2", "result": "loss", "review": "米尔沃尔0-2完败，推荐黑掉。主场优势未兑现，进攻端哑火。"},
            {"id": "007", "time": "03:00", "league": "西甲", "home": "巴列卡诺", "away": "赫罗纳", "homeEmoji": "⚪", "awayEmoji": "🔴", "prediction": "平（首选）/让球胜", "confidence": "⭐⭐⭐", "odds": "@2.10", "isHeart": False, "score": "1-1", "result": "win", "review": "1-1平局命中！双方实力接近，巴列卡诺主场守平。"},
            {"id": "008", "time": "03:15", "league": "葡超", "home": "里奥阿维", "away": "葡萄牙体育", "homeEmoji": "🔴", "awayEmoji": "🟢", "prediction": "让球胜/搏平", "confidence": "⭐⭐⭐", "odds": "@1.85", "isHeart": False, "score": "1-4", "result": "loss", "review": "里奥阿维1-4惨败，让球负黑掉。Sporting客场火力全开，实力碾压。"},
            {"id": "011", "time": "01:00", "league": "西甲", "home": "塞尔塔", "away": "莱万特", "homeEmoji": "🔵", "awayEmoji": "🔵", "prediction": "BTTS Yes", "confidence": "⭐⭐⭐", "odds": "@1.75", "isHeart": True, "score": "-", "result": "pending", "review": "重心胆：塞尔塔中卫Starfelt缺阵，防线重组；莱万特保级拼命必反击。"},
            {"id": "012", "time": "02:00", "league": "西甲", "home": "贝蒂斯", "away": "埃尔切", "homeEmoji": "🟢", "awayEmoji": "⚪", "prediction": "BTTS Yes", "confidence": "⭐⭐", "odds": "@1.65", "isHeart": True, "score": "-", "result": "pending", "review": "重心胆：贝蒂斯Bartra缺阵+Natan疑，中卫真空；埃尔切降级队有反击能力。"}
        ]
    }

def main():
    work_dir = tempfile.mkdtemp(prefix="scan_")
    repo_dir = os.path.join(work_dir, "football-scan")
    auth_url = REPO_URL.replace("https://", f"https://{GITHUB_TOKEN}@")
    
    print("🚀 777 扫盘中心 - 自动推送")
    print("=" * 40)
    
    # 1. 克隆
    if not run(f"git clone --depth 1 {auth_url} {repo_dir}"):
        return
    
    # 2. 配置 git
    run("git config user.email '777@scan.bot'", cwd=repo_dir)
    run("git config user.name '777 Bot'", cwd=repo_dir)
    
    # 3. 写入数据
    data = get_data()
    with open(os.path.join(repo_dir, "data.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 4. 提交推送
    run("git add -A", cwd=repo_dir)
    run(f"git commit -m 'auto: 更新扫盘数据 {datetime.now(timezone.utc).strftime('%m-%d %H:%M')}'", cwd=repo_dir)
    run("git push origin main", cwd=repo_dir)
    
    print("✅ 推送成功！")
    print(f"🔗 https://2216100013.github.io/football-scan/")
    
    # 清理
    shutil.rmtree(work_dir)

if __name__ == "__main__":
    main()


# 🧠 XMRT Rewards Calculator
import json

def calculate_rewards(mined_xmr, hashrate):
    base_xmrt = mined_xmr * 1000
    bonus = hashrate * 0.05
    return round(base_xmrt + bonus, 2)

# Example usage
if __name__ == "__main__":
    stats = {"xmr": 0.0247, "hashrate": 1000}
    xmrt = calculate_rewards(stats["xmr"], stats["hashrate"])
    print(f"🏆 Earned: {xmrt} XMRT")

import os

def main():
    # Competition: The One-Line Laugh (make.fun)
    # Target: Exactly one sentence, max 200 chars, everyday truth + surprise twist
    line = "I downloaded a mindfulness app to cure my anxiety, and now my main source of anxiety is whether I remembered to complete my daily streak before midnight."
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()

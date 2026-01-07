import pandas as pd
import string
import os
import time  # <--- 1. 新增：引入时间控制模块
from deep_translator import GoogleTranslator

# ================= 配置区域 =================
white_list_path = '/Users/liruochen/Desktop/Oxford_3000_Word_List.txt'

# 你的文章 (建议多贴一点文本试试)
article_text = """
Greetings to all! Year after year, life opens a fresh chapter. As the new year begins, I extend my best wishes to you from Beijing!
The year 2025 marks the completion of China's 14th Five-Year Plan for economic and social development. Over the past five years, we have pressed ahead with enterprise and fortitude, and overcome many difficulties and challenges. We met the targets in the Plan and made solid advances on the new journey of Chinese modernization. Our economic output has crossed thresholds one after another, and it is expected to reach RMB 140 trillion yuan this year. Our economic strength, scientific and technological abilities, defense capabilities, and composite national strength all reached new heights. Clear waters and lush mountains have become a salient feature of our landscape. Our people enjoy a growing sense of gain, happiness and security. The past five years have been a truly remarkable journey, and our accomplishments have not come easily. Your unwavering hard work has made our nation thrive and prosper. I salute you all for your exceptional diligence and invaluable contributions.
This year is full of indelible memories. We solemnly commemorated the 80th anniversary of the victory of the Chinese People's War of Resistance Against Japanese Aggression and the World Anti-Fascist War, and established the Taiwan Recovery Day. These grand national events were majestic and powerful, and the glory of victory will shine through the pages of history. They are inspiring all the sons and daughters of the Chinese nation to remember history, honor fallen heroes, cherish peace, and create a better future. They are rallying a mighty force for the great rejuvenation of our nation.
We sought to energize high-quality development through innovation. We integrated science and technology deeply with industries, and made a stream of new innovations. Many large AI models have been competing in a race to the top, and breakthroughs have been achieved in the research and development of our own chips. All this has turned China into one of the economies with the fastest growing innovation capabilities. The Tianwen-2 probe began its star-chasing journey to explore asteroids and comets. Construction of the hydropower project at the lower reaches of the Yarlung Zangbo River started. China's first aircraft carrier equipped with an electromagnetic catapult system was officially commissioned. Humanoid robots did kung fu kicks, and drones performed spectacular light shows. Inventions and innovations have boosted new quality productive forces and added colorful dimensions to our lives.
We endeavored to nurture our spiritual home with cultural development. There was a surging public interest in cultural relics, museums, and intangible cultural heritage. A new Chinese cultural site was added to the World Heritage List. Cultural IPs such as Wukong and Nezha became global hits. The younger generation came to deem classic Chinese culture as the finest form of aesthetic expression. The cultural and tourism sectors thrived. The "super league" football games in our cities and villages attracted numerous fans. Ice and snow sports ignited people's passion for the winter season. Tradition is now embracing modernity, and the Chinese culture is shining in even greater splendor.
We joined hands to build a better life and enjoyed it together. I attended celebrations in Xizang and Xinjiang. From the snow-covered plateau to both sides of the Tianshan Mountains, people of various ethnic groups are united as one, like seeds of a pomegranate sticking together. With white khatas and passionate singing and dancing, they expressed their love of the motherland and the happiness they enjoy. No issue of the people is too small; we care for every leaf and tend every branch in the garden of people's well-being. Over the past year, the rights and interests of the workforce in new forms of employment have been better protected, facilities have been upgraded to bring more convenience to the elderly, and each family with childcare needs has received a subsidy of RMB 300 yuan per month. When the happy hum of daily life fills every home, the big family of our nation will go from strength to strength.
We continued to embrace the world with open arms. The Shanghai Cooperation Organization Summit in Tianjin and the Global Leaders' Meeting on Women were very successful; and island-wide special customs operations were launched in the Hainan Free Trade Port. To better address climate change, China announced new Nationally Determined Contributions. After announcing the three global initiatives on development, security, and civilization, I put forward the Global Governance Initiative to promote a more just and equitable global governance system. The world today is undergoing both changes and turbulence, and some regions are still engulfed in war. China always stands on the right side of history, and is ready to work with all countries to advance world peace and development and build a community with a shared future for humanity.
Not long ago, I attended the opening ceremony of the National Games, and I was glad to see Guangdong, Hong Kong and Macao coming together in unity and acting in unison. We should unswervingly implement the policy of One Country, Two Systems, and support Hong Kong and Macao in better integrating into the overall development of our country and maintaining long-term prosperity and stability. We Chinese on both sides of the Taiwan Strait share a bond of blood and kinship. The reunification of our motherland, a trend of the times, is unstoppable!
Only a strong Communist Party of China can make our country strong. We launched the study and education program on fully implementing the central Party leadership's eight-point decision on improving Party and government conduct. We exercised strict governance of the Party through credible measures, and promoted the Party's self-revolution to fight corruption and advance healthy governance. As a result, the conduct of our Party and government steadily improved. We must stay true to our original aspiration and founding mission, and pursue our goal with perseverance and dedication. We should continue to give a good answer to the question on how to maintain long-term governance put forth in a cave dwelling in Yan'an and prove ourselves worthy of the people's expectation in the new era.
The year 2026 marks the beginning of the 15th Five-Year Plan. A successful venture should start with a good plan and with clear goals set. We should focus on our goals and tasks, boost confidence, and build momentum to press ahead. We should take solid steps to promote high-quality development, further deepen reform and opening up across the board, deliver prosperity for all, and write a new chapter in the story of China's miracle.
The dream lofty, the journey long-bold strides will get us there. Let us charge ahead like horses with courage, vitality, and energy, fight for our dreams and our happiness, and turn our great vision into beautiful realities.
The sun of the new year will soon rise. May our great motherland stand in magnificence! May the fields across the country deliver good harvest! May our nation bathe in the glory of the morning! May you all enjoy life to the fullest, and achieve every success! May all your dreams come true!
"""
# ===========================================

print(f"正在读取简单词表...")

try:
    with open(white_list_path, 'r', encoding='utf-8') as f:
        easy_vocab = set(word.strip().lower() for word in f.readlines())
    print(f"成功加载简单词表，共 {len(easy_vocab)} 个单词。")
except FileNotFoundError:
    print(f"❌ 错误：找不到文件！")
    exit()

# 清洗与分词
translator_table = str.maketrans('', '', string.punctuation)
clean_text = article_text.translate(translator_table)
words = clean_text.lower().split()
normalized_words = words

# 过滤与提取生词
hard_words = []
seen = set()

print("正在筛选生词并查询释义...")
print("⚠️ 为了防止被谷歌屏蔽，程序会故意变慢（每秒查一个词），请耐心等待...")

translator = GoogleTranslator(source='auto', target='zh-CN')
data_list = []

for w in normalized_words:
    if w.isalpha() and w not in easy_vocab and w not in seen and len(w) > 2:
        seen.add(w)

        # <--- 2. 新增：每次循环强制休息 1 秒
        time.sleep(1)

        try:
            chinese_meaning = translator.translate(w)
            print(f"✅ 成功提取：{w} -> {chinese_meaning}")
        except Exception as e:
            # 如果第一次失败，休息 2 秒再试一次（重试机制）
            time.sleep(2)
            try:
                chinese_meaning = translator.translate(w)
                print(f"✅ 重试成功：{w} -> {chinese_meaning}")
            except:
                chinese_meaning = "翻译失败(网络拦截)"
                print(f"❌ 失败：{w}")

        data_list.append({
            '生词': w,
            '中文释义': chinese_meaning
        })

# 导出 Excel
if data_list:
    output_path = '/Users/liruochen/Desktop/My_Vocabulary_Book_Final.xlsx'  # 改个名防止覆盖
    df = pd.DataFrame(data_list)
    df.to_excel(output_path, index=False)
    print(f"\n🎉 完美！生词本已生成：{output_path}")
else:
    print("\n⚠️ 没有提取到生词。")
food_paragraph = "Plants as a food source are divided into  legumes, grains and nuts.[36] Where plants fall within these categories can vary, with botanically described fruits such as the tomato, squash, pepper and eggplant or seeds like peas commonly considered vegetables.[37] Food is a fruit if the part eaten is derived from the reproductive tissue, so seeds, nuts and grains are technically fruit.[38][39] From a culinary perspective, fruits are generally considered the remains of botanically described fruits after grains, nuts, seeds and fruits used as vegetables are removed.[40] Grains can be defined as seeds that humans eat or harvest, with cereal grains (oats, wheat, rice, corn, barley, rye, sorghum and millet) belonging to the Poaceae (grass) family[41] and pulses coming from the Fabaceae (legume) family.[42] Whole grains are foods that contain all the elements of the original seed (bran, germ, and endosperm).[43] Nuts are dry fruits, distinguishable by their woody shell.[40]"
cinema_paragraph = "The movies Shimha, Avatar, RRR, KGF, and Sholay are very popular among audiences. RRR and KGF are action-packed films with powerful characters and exciting stories. Sholay is a classic Indian movie loved by many generations. Avatar is famous for its amazing visual effects and science fiction world. People enjoy watching different types of movies for entertainment and relaxation."
food = ["tomato", "pea", "nut", "grain", "vegetable", "seed", "fruit"]
cinema = ["deewaar", "ganga jamuna", "sholay", "zeenat aman", "zanjeer", "parveen babi"]
message_text = food_paragraph.lower()
found_keywords = []
for word in food:
    count = message_text.count(word.lower())
    if count > 0:
        found_keywords.append((word, count))

if len(found_keywords) > 0:
    print("This message is related to Food")
    print("Matched words:", found_keywords)
else:
    print("This message is not clearly related to Food")

cinema_text = cinema_paragraph.lower()
found_word = []
for word in cinema:
    count = cinema_text.count(word.lower())
    if count > 0:
        found_word.append((word, count))

if len(found_word) > 0:
    print("This message is related to Cinema")
    print("Matched words:", found_word)
else:
    print("This message is not clearly related to Cinema")


import matplotlib.pyplot as plt

food_words = [item[0] for item in found_keywords]
food_counts = [item[1] for item in found_keywords]

cinema_words = [item[0] for item in found_word]
cinema_counts = [item[1] for item in found_word]

plt.figure(figsize=(10, 5))
plt.bar(food_words, food_counts, label="Food", alpha=0.7)
plt.bar(cinema_words, cinema_counts, label="Cinema", alpha=0.7)
plt.title("Keyword Frequency Comparison")
plt.xlabel("Keywords")
plt.ylabel("Count")
plt.legend()
plt.show()
